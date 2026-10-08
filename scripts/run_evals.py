#!/usr/bin/env python
"""Run one evaluation round per industry.

Usage:
  python scripts/run_evals.py --industry healthcare
  python scripts/run_evals.py --all
  python scripts/run_evals.py --industry healthcare --dry-run     check inputs, call nothing

For every test profile in industries/<x>/test-profiles/ the runner:
  1. generates Instructions with the <x>-prompt-writer skill (the profile's expected results are NOT shown),
  2. simulates the agent's reply to every behaviour probe in eval.json (fresh call, Instructions only),
  3. asks the eval-judge agent to grade every check in eval.json against those Instructions and replies,
  4. saves everything to industries/<x>/results/<date>.json (case id, profile, pass/fail, reason),
  5. prints a pass-rate summary per industry and lists the failing cases to feed back into the SKILL.

It never edits eval.json or the skill. Language-model calls go through the Claude Code CLI
(`claude -p`); set CLAUDE_BIN to use another binary. Standard library only.
Exit code: 0 all passed, 1 some failed, 2 an industry was missing inputs.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_eval  # noqa: E402

INDUSTRIES = (
    "healthcare", "pharmacy", "retail", "finance", "banking",
    "education", "logistics", "hr", "real-estate", "travel",
)
HIDDEN_HEADINGS = ("## Tricky callers", "## Expected skill output", "## Expected word budget")


class ClaudeCli:
    """Calls `claude -p`. Replace with a fake in tests."""

    def __init__(self, binary=None, cwd=ROOT):
        self.binary = binary or os.environ.get("CLAUDE_BIN", "claude")
        self.cwd = cwd

    def run(self, prompt, system=None, agent=None):
        cmd = [self.binary, "-p"]
        if agent:
            cmd += ["--agent", agent]
        if system:
            cmd += ["--system-prompt", system]
        result = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                cwd=self.cwd, encoding="utf-8")
        if result.returncode != 0:
            raise RuntimeError(f"claude call failed: {result.stderr.strip()[:300]}")
        return result.stdout.strip()


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


def run_industry(industry, llm, root=ROOT, date=None):
    date = date or datetime.date.today().isoformat()
    d = root / "industries" / industry
    checks = json.loads((d / "eval.json").read_text(encoding="utf-8"))["checks"]
    out_dir = d / "results"
    work = out_dir / date
    work.mkdir(parents=True, exist_ok=True)
    rows = []
    for pf in profile_files(d):
        name = pf.stem
        instructions = llm.run(
            f"Use the {industry}-prompt-writer skill. Write the Instructions (welcome note, sections 1 to 6) "
            f"for this test business. Output only the Instructions.\n\n"
            + visible_profile(pf.read_text(encoding="utf-8")))
        inst_path = work / f"{name}-instructions.md"
        inst_path.write_text(instructions + "\n", encoding="utf-8")
        replies = {c["id"]: llm.run(c["probe"], system=instructions)
                   for c in checks if c.get("type") == "behaviour"}
        replies_path = work / f"{name}-replies.json"
        replies_path.write_text(json.dumps(replies, indent=2, ensure_ascii=False), encoding="utf-8")
        verdict = llm.run(
            f"Industry: {industry}\nprompt_file: {inst_path.as_posix()}\nreplies: {replies_path.as_posix()}\n"
            "Grade every check in the industry's eval.json. After your table, end with one ```json block: "
            '{"results":[{"id":"...","result":"PASS or FAIL","reason":"one line"}]}',
            agent="eval-judge")
        for r in parse_judge(verdict):
            rows.append({"case_id": r["case_id"], "profile": name, "result": r["result"], "reason": r["reason"]})
    passed = sum(r["result"] == "pass" for r in rows)
    summary = {"industry": industry, "date": date, "total": len(rows), "passed": passed,
               "failed": len(rows) - passed,
               "pass_rate": round(100 * passed / len(rows), 1) if rows else 0.0}
    (out_dir / f"{date}.json").write_text(
        json.dumps({"summary": summary, "results": rows}, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary, rows


def main(argv=None, llm=None, root=ROOT, out=sys.stdout):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--industry")
    g.add_argument("--all", action="store_true")
    ap.add_argument("--date")
    ap.add_argument("--dry-run", action="store_true")
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
        summary, rows = run_industry(ind, llm, Path(root), args.date)
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
    sys.exit(main())
