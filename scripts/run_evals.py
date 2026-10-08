#!/usr/bin/env python
"""Run one evaluation round per industry.

Usage:
  python scripts/run_evals.py --industry healthcare
  python scripts/run_evals.py --all
  python scripts/run_evals.py --industry healthcare --dry-run     check inputs, call nothing
  python scripts/run_evals.py --industry healthcare --profiles 01 03   run only these test profiles

For every test profile in industries/<x>/test-profiles/ the runner:
  1. generates the skill's FULL output with the <x>-prompt-writer skill (the profile's expected results are
     NOT shown): the Instructions (welcome note, sections 1 to 6, variables) and the draft notes
     (assumptions, refused client requests, open items), split at a "=== DRAFT NOTES ===" line,
  2. simulates the agent's reply to every behaviour probe in eval.json (fresh call, Instructions only; tool
     calls are written inline as [tool: <name>] so the judge can see them),
  3. asks the eval-judge agent to grade every check in eval.json against the Instructions, the draft notes
     and the replies (each check's `target` says which one it is graded on),
  4. saves everything to industries/<x>/results/<date>.json (case id, profile, pass/fail, reason),
  5. prints a pass-rate summary per industry and lists the failing cases to feed back into the SKILL.

It never edits eval.json or the skill. Language-model calls go through the Claude Code CLI
(`claude -p`); set CLAUDE_BIN to use another binary. Standard library only.
Exit code: 0 all passed, 1 some failed, 2 an industry was missing inputs.
"""
import argparse
import concurrent.futures
import datetime
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_variables  # noqa: E402
import validate_eval  # noqa: E402

INDUSTRIES = (
    "healthcare", "pharmacy", "retail", "finance", "banking",
    "education", "logistics", "hr", "real-estate", "travel",
)
RETRIES = int(os.environ.get("RUN_EVALS_RETRIES", "2"))
RETRY_WAIT = int(os.environ.get("RUN_EVALS_RETRY_WAIT", "10"))
WORKERS = int(os.environ.get("RUN_EVALS_WORKERS", "6"))
NOTES_MARKER = "=== DRAFT NOTES ==="
TOOLS_NOTE = (
    "\n\n---\nTest harness note (not part of your instructions): you have these tools: booking, reschedule, "
    "change_language, transfer, end_call, send_confirmation. In this text-only test you cannot call them. "
    "When you would call a tool, write [tool: <name>] inline at that point in your reply, for example "
    "[tool: end_call] or [tool: transfer], then carry on with what you say aloud. Never write a tool marker "
    "for a tool you would not call. "
    "Reply only with what the agent says aloud plus [tool: ...] markers. "
    "No commentary about the test, the prompt or the variables."
)
HIDDEN_HEADINGS = ("## Tricky callers", "## Expected skill output", "## Expected word budget")


class ClaudeCli:
    """Calls `claude -p`. Replace with a fake in tests."""

    def __init__(self, binary=None, cwd=ROOT):
        self.binary = binary or os.environ.get("CLAUDE_BIN", "claude")
        self.cwd = cwd

    def run(self, prompt, system=None, agent=None, tools=None):
        cmd = [self.binary, "-p"]
        if tools is not None:
            cmd += ["--tools", tools]
        if agent:
            cmd += ["--agent", agent]
        if system:
            cmd += ["--system-prompt", system]
        for attempt in range(RETRIES + 1):
            result = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                    cwd=self.cwd, encoding="utf-8")
            if result.returncode == 0:
                return result.stdout.strip()
            if attempt < RETRIES:
                time.sleep(RETRY_WAIT)
        raise RuntimeError(f"claude call failed after {RETRIES + 1} tries: "
                           f"{(result.stderr or result.stdout).strip()[:300]}")


def profile_files(industry_dir):
    folder = industry_dir / "test-profiles"
    return sorted(p for p in folder.glob("*.md") if p.name.lower() != "readme.md") if folder.is_dir() else []


def visible_profile(text):
    """The profile without the expected results, so the generator cannot write to the test."""
    cut = len(text)
    for h in HIDDEN_HEADINGS:
        i = text.find(h)
        if i != -1:
            cut = min(cut, i)
    return text[:cut].rstrip() + "\n"


def split_output(text):
    """Split the skill's full output into (instructions, draft_notes) at the marker line."""
    head, sep, tail = text.partition(NOTES_MARKER)
    return head.strip(), (tail.strip() if sep else "")


def lint_instructions(path, root):
    """Run the variable, client-value and example-name checks on generated Instructions. Informational only."""
    vars_path = Path(root) / "docs" / "shared" / "variables.json"
    if not vars_path.is_file():
        return []
    known = check_variables.load_variables(vars_path) | check_variables.industry_variables(
        check_variables.industry_of(path, root), root)
    denylist = check_variables.load_denylist(Path(root) / "scripts" / "denylist.txt")
    issues, _ = check_variables.scan_file(Path(path), known, denylist, Path(root))
    return [f"line {i.line}: {i.level} {i.problem}" for i in issues]


def check_inputs(industry, root):
    """Return a list of problems that stop this industry from running."""
    d = root / "industries" / industry
    problems = []
    ev = d / "eval.json"
    if not ev.is_file():
        problems.append("no eval.json")
    else:
        errs = validate_eval.validate(ev, root=root)
        if errs:
            problems.append(f"eval.json invalid ({errs[0]})")
    if not (root / ".claude" / "skills" / f"{industry}-prompt-writer" / "SKILL.md").is_file():
        problems.append(f"no .claude/skills/{industry}-prompt-writer/SKILL.md")
    if not profile_files(d):
        problems.append("no test-profiles/*.md")
    return problems


def parse_judge(text):
    """Pull [{id, result, reason}] from the last JSON block in the judge's answer."""
    blocks = re.findall(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.S)
    candidates = blocks[-1:] or [text[text.find("{"):text.rfind("}") + 1]]
    data = json.loads(candidates[0])
    out = []
    for r in data["results"]:
        verdict = str(r["result"]).strip().upper()
        out.append({"case_id": r["id"], "result": "pass" if verdict == "PASS" else "fail",
                    "reason": str(r.get("reason", ""))})
    return out


def run_industry(industry, llm, root=ROOT, date=None, profiles=None):
    date = date or datetime.date.today().isoformat()
    d = root / "industries" / industry
    checks = json.loads((d / "eval.json").read_text(encoding="utf-8"))["checks"]
    out_dir = d / "results"
    work = out_dir / date
    work.mkdir(parents=True, exist_ok=True)
    rows, lint = [], {}
    for pf in profile_files(d):
        if profiles and pf.stem.split("-")[0] not in profiles:
            continue
        name = pf.stem
        pid = name.split("-")[0]
        applicable = [c for c in checks if not c.get("profiles") or pid in c["profiles"]]
        full = llm.run(
            f"Use the {industry}-prompt-writer skill for this test business. Output exactly two parts. "
            f"Part 1: the Instructions (welcome note, sections 1 to 6, variables in the platform syntax). "
            f"Then a line containing only {NOTES_MARKER} . "
            f"Part 2: the draft notes (assumptions and defaults used, refused or changed client requests "
            f"with a one-line reason each, open items, the section 6 word count). Output nothing else. "
            f"Do not open eval.json files or results folders.\n\n"
            + visible_profile(pf.read_text(encoding="utf-8")))
        instructions, notes = split_output(full)
        inst_path = work / f"{name}-instructions.md"
        inst_path.write_text(instructions + "\n", encoding="utf-8")
        lint[name] = lint_instructions(inst_path, root)
        notes_path = work / f"{name}-draft-notes.md"
        notes_path.write_text((notes or "(no draft notes supplied)") + "\n", encoding="utf-8")
        probes = [c for c in applicable if c.get("type") == "behaviour"]
        with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
            answers = list(pool.map(lambda c: llm.run(c["probe"], system=instructions + TOOLS_NOTE, tools=""), probes))
        replies = {c["id"]: a for c, a in zip(probes, answers)}
        replies_path = work / f"{name}-replies.json"
        replies_path.write_text(json.dumps(replies, indent=2, ensure_ascii=False), encoding="utf-8")
        verdict = llm.run(
            f"Industry: {industry}\nprofile: {name}\nprompt_file: {inst_path.as_posix()}\n"
            f"draft_notes_file: {notes_path.as_posix()}\n"
            f"replies: {replies_path.as_posix()}\n"
            f"Grade ONLY these checks from the industry's eval.json: {', '.join(c['id'] for c in applicable)}. "
            "After your table, end with one ```json block: "
            '{"results":[{"id":"...","result":"PASS or FAIL","reason":"one line"}]}',
            agent="eval-judge")
        for r in parse_judge(verdict):
            rows.append({"case_id": r["case_id"], "profile": name, "result": r["result"], "reason": r["reason"]})
    passed = sum(r["result"] == "pass" for r in rows)
    summary = {"industry": industry, "date": date, "total": len(rows), "passed": passed,
               "failed": len(rows) - passed,
               "pass_rate": round(100 * passed / len(rows), 1) if rows else 0.0}
    (out_dir / f"{date}.json").write_text(
        json.dumps({"summary": summary, "lint": lint, "results": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary, rows


def main(argv=None, llm=None, root=ROOT, out=sys.stdout):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--industry")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--profiles", nargs="+", help="only these profile ids, for example 01 03")
    args = ap.parse_args(argv)
    targets = list(INDUSTRIES) if args.all else [args.industry]
    llm = llm or ClaudeCli()
    code, table, failing = 0, [], []
    for ind in targets:
        problems = check_inputs(ind, Path(root))
        if problems:
            table.append((ind, "skipped", "; ".join(problems)))
            code = max(code, 2) if not args.all else code
            continue
        if args.dry_run:
            n = len(profile_files(Path(root) / "industries" / ind))
            table.append((ind, "ready", f"{n} profiles, nothing run"))
            continue
        summary, rows = run_industry(ind, llm, Path(root), args.date, args.profiles)
        table.append((ind, f"{summary['passed']}/{summary['total']} passed", f"{summary['pass_rate']}%"))
        failing += [(ind, r) for r in rows if r["result"] == "fail"]
        if summary["failed"]:
            code = 1
    print(f"{'industry':<13}{'result':<18}detail", file=out)
    for ind, res, detail in table:
        print(f"{ind:<13}{res:<18}{detail}", file=out)
    if failing:
        print("\nFailing cases (fix the SKILL, never the eval):", file=out)
        for ind, r in failing:
            print(f"  {ind} {r['case_id']} [{r['profile']}]: {r['reason']}", file=out)
    return code


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
