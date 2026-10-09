#!/usr/bin/env python
"""Run one evaluation round per industry.

Usage:
  python scripts/run_evals.py --industry healthcare
  python scripts/run_evals.py --all
  python scripts/run_evals.py --industry healthcare --dry-run     check inputs, call nothing
  python scripts/run_evals.py --industry healthcare --profiles 01 03   run only these test profiles
  python scripts/run_evals.py --industry pharmacy --date <same date> --resume   continue a cut run: finished profiles are skipped
  python scripts/run_evals.py --industry pharmacy --profiles 01 02 --cases E04,E06   run and judge only these cases
                                      (a profile with none of them is skipped, with no generation)

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
(`claude -p`); the binary is found on PATH, then in ~/.local/bin; set CLAUDE_BIN to override. Standard library only.
Exit code: 0 all passed, 1 some failed, 2 an industry was missing inputs.
"""
import argparse
import concurrent.futures
import datetime
import json
import os
import re
import shutil
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
MAX_PARALLEL = 4  # never more than 4 claude processes at once
WORKERS = min(MAX_PARALLEL, int(os.environ.get("RUN_EVALS_WORKERS", str(MAX_PARALLEL))))
AUTH_RETRIES = int(os.environ.get("RUN_EVALS_AUTH_RETRIES", "3"))
AUTH_WAIT = int(os.environ.get("RUN_EVALS_AUTH_WAIT", "60"))
AUTH_ERROR = re.compile(r"oauth|authenticat|unauthori[sz]ed|\b401\b|token.{0,20}(expired|refresh|invalid)|please run /login|invalid.{0,20}credential|ENOTFOUND|EAI_AGAIN|ECONNRESET|ETIMEDOUT|can.t reach the API server|check your internet", re.I)
NOTES_MARKER = "=== DRAFT NOTES ==="
INSTRUCTIONS_MARKER = "=== INSTRUCTIONS ==="
COMMON_TOOLS = ("change_language", "transfer", "end_call", "send_confirmation")
# Platform tools per industry; an industry not listed gets only the common ones. Keep in step with each core.md tool table.
INDUSTRY_TOOLS = {
    "healthcare": ("booking", "reschedule", "change_language", "transfer", "end_call"),
    "pharmacy": ("check_stock", "place_order", "change_language", "transfer", "end_call"),
}
TOOLS_NOTE_TEMPLATE = (
    "\n\n---\nTest harness note (not part of your instructions): you have these tools: {tools}. "
    "In this text-only test you cannot call them. "
    "When you would call a tool, write [tool: <name>] inline at that point in your reply, for example "
    "[tool: end_call] or [tool: transfer], then carry on with what you say aloud. Never write a tool marker "
    "for a tool you would not call. "
    "Reply only with what the agent says aloud plus [tool: ...] markers. "
    "No commentary about the test, the prompt or the variables."
)


def tools_note(industry):
    return TOOLS_NOTE_TEMPLATE.format(tools=", ".join(INDUSTRY_TOOLS.get(industry, COMMON_TOOLS)))

HIDDEN_HEADINGS = ("## Tricky callers", "## Expected skill output", "## Expected word budget", "## Test values")


def find_claude(home=None):
    """The claude binary: CLAUDE_BIN, then PATH, then ~/.local/bin/claude(.exe). Falls back to the bare name."""
    override = os.environ.get("CLAUDE_BIN")
    if override:
        return override
    found = shutil.which("claude")
    if found:
        return found
    base = Path(home) if home else Path.home()
    for name in ("claude.exe", "claude"):
        candidate = base / ".local" / "bin" / name
        if candidate.is_file():
            return str(candidate)
    return "claude"


class ClaudeCli:
    """Calls `claude -p`. Replace with a fake in tests."""

    def __init__(self, binary=None, cwd=ROOT):
        self.binary = binary or find_claude()
        self.cwd = cwd

    def run(self, prompt, system=None, agent=None, tools=None):
        cmd = [self.binary, "-p"]
        if tools is not None:
            cmd += ["--tools", tools]
        if agent:
            cmd += ["--agent", agent]
        if system:
            cmd += ["--system-prompt", system]
        auth_tries = 0
        attempt = 0
        while True:
            result = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                                    cwd=self.cwd, encoding="utf-8")
            if result.returncode == 0:
                return result.stdout.strip()
            message = (result.stderr or "") + " " + (result.stdout or "")
            if AUTH_ERROR.search(message) and auth_tries < AUTH_RETRIES:
                auth_tries += 1  # an OAuth refresh problem or a network drop: wait a minute, then try again
                time.sleep(AUTH_WAIT)
                continue
            if attempt < RETRIES:
                attempt += 1
                time.sleep(RETRY_WAIT)
                continue
            raise RuntimeError(f"claude call failed after {attempt + 1} tries"
                               f"{f' and {auth_tries} auth waits' if auth_tries else ''}: "
                               f"{message.strip()[:300]}")


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


NOTES_RE = re.compile(r"^[ \t]*" + re.escape(NOTES_MARKER) + r"[ \t]*$", re.M)
INSTRUCTIONS_RE = re.compile(r"^[ \t]*" + re.escape(INSTRUCTIONS_MARKER) + r"[ \t]*$", re.M)


def split_output(text):
    """Split the skill's full output into (instructions, draft_notes) at the notes marker.
    The marker counts only when it is alone on its own line, so a preamble that mentions it cannot split the text."""
    m = NOTES_RE.search(text)
    if not m:
        return text.strip(), ""
    return text[:m.start()].strip(), text[m.end():].strip()


def split_marked(text):
    """Split the full output using both markers. Returns (instructions, draft_notes, outside_lines).
    With an INSTRUCTIONS marker (alone on its line), the Instructions are only what sits between the two markers and any
    text before the marker is returned as outside text. Without it, this is split_output and nothing counts as outside."""
    m = INSTRUCTIONS_RE.search(text)
    if not m:
        instructions, notes = split_output(text)
        return instructions, notes, []
    instructions, notes = split_output(text[m.end():])
    return instructions, notes, [l.strip() for l in text[:m.start()].splitlines() if l.strip()]


def case_selected(case_id, wanted):
    """True when no case filter is given, or the id equals a wanted token or ends with -TOKEN (E04 matches PHA-E04)."""
    if not wanted:
        return True
    cid = case_id.upper()
    return any(cid == w.upper() or cid.endswith("-" + w.upper()) for w in wanted)


SAY_EXACTLY = re.compile(r'say exactly(?: and only)?\s+"([^"]+)"', re.I)
WELCOME_LINE = re.compile(r'^- (Inbound|Outbound): "([^"]+)"', re.M)


def _norm(text):
    """Compare text without markdown ticks, curly quotes or line breaks."""
    text = text.replace("`", "").replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    return " ".join(text.split())


def profile_facts(profile_text):
    """Direction, selected workflow numbers and prescription upload method read from a test profile."""
    d = re.search(r"\|\s*Direction\s*\|\s*(\w+)", profile_text)
    direction = d.group(1).lower() if d else "inbound"
    sel = re.search(r"## Selected workflows\s+(.*?)(?=\n## |\Z)", profile_text, re.S)
    chosen = re.sub(r"[^.]*not selected[^.]*\.", "", sel.group(1)) if sel else ""
    numbers = sorted(set(re.findall(r"\b0[1-8]\b", chosen)))
    u = re.search(r"\|\s*Prescription upload\s*\|\s*(\w+)", profile_text)
    method = u.group(1).lower() if u and u.group(1).lower() in ("whatsapp", "email", "in_store") else "not set"
    confirmation = bool(re.search(r"confirmation_channels\W{0,6}=\s*(whatsapp|email)", profile_text, re.I)
                        or re.search(r"\|\s*Confirmation channels\s*\|\s*(whatsapp|email)", profile_text, re.I))
    return {"direction": direction, "workflows": numbers, "upload": method, "confirmation": confirmation}


VARIABLE_LABELS = {
    "prescription upload": "prescription_upload_method", "hours": "business_hours", "payment modes": "payment_modes",
    "delivery info": "delivery_info", "return policy": "return_policy", "store address": "store_address",
    "confirmation channels": "confirmation_channels",
}
CALL_CONTEXT = ("customer_name", "refill_details")
VAR_TOKEN = re.compile(r"\{\{var\.(\w+)\}\}")
# Industries whose simulated agent is told the profile's variable values, as the platform fills {{var.x}} on a real call.
VARIABLE_VALUE_INDUSTRIES = ("pharmacy",)


def test_values(profile_text):
    """Placeholder values from the profile's '## Test values' section: lines like '- <order_number> = 48213'."""
    sec = re.search(r"## Test values\s+(.*?)(?=\n## |\Z)", profile_text, re.S)
    found = re.findall(r"^- <(\w+)>\s*=\s*(.+?)\s*$", sec.group(1), re.M) if sec else []
    return dict(found)


def profile_variable_values(profile_text):
    """Variable values given in a test profile's config table, plus call context from its test values.
    A value the profile says is not provided becomes '(empty)'."""
    values = {}
    for label, cell in re.findall(r"^\|\s*([^|]+?)\s*\|\s*(.+?)\s*\|\s*$", profile_text, re.M):
        cell = cell.replace("`", "")
        token = VAR_TOKEN.search(cell)
        name = token.group(1) if token else VARIABLE_LABELS.get(label.lower())
        if not name or name in CALL_CONTEXT:
            continue
        if token and "=" in cell:
            value = cell.split("=", 1)[1].strip()
        elif token:
            value = cell.split("(", 1)[0].strip()
        else:
            value = cell
        if re.match(r"(not provided|not given)", value, re.I):
            value = "(empty)"
        elif value.lower() == "given":
            continue
        values[name] = value
    for name, value in test_values(profile_text).items():
        if name in CALL_CONTEXT:
            values[name] = value
    return values


def values_note(values):
    if not values:
        return ""
    lines = "\n".join(f"{name} = {value}" for name, value in sorted(values.items()))
    return ("\n\n---\nVariable values for this test (the platform has already filled in the {{var.x}} variables "
            "before the call, so use these values; a value of (empty) means the business gave none):\n" + lines)


def fill_placeholders(probe, values):
    """Replace <customer_name>, <order_number>, <address> and the like in a probe with the profile's test values."""
    return re.sub(r"<(\w+)>", lambda m: values.get(m.group(1), m.group(0)), probe)


def strip_before_welcome(instructions, welcome, window=6):
    """Drop stray lines (code fences, chatter) before the welcome line when the welcome is within the first lines.
    Returns (clean text, removed lines). If the welcome is not found, nothing is removed."""
    lines = instructions.splitlines()
    for i, line in enumerate(lines[:window]):
        if line.strip() and _norm(line) == _norm(welcome):
            removed = [l for l in lines[:i] if l.strip()]
            return "\n".join(lines[i:]).strip(), removed
    return instructions, []


# Workflows that hold outbound-only fixed lines (stop-calling, voicemail, wrong person); they count for outbound profiles only.
OUTBOUND_ONLY_WORKFLOWS = {"pharmacy": ("03",), "healthcare": ("04",)}


def fixed_lines(industry, facts, root=ROOT):
    """The quoted lines the sources mark 'say exactly' for this profile, plus the welcome for its direction.
    A rule row that mentions confirmation_channels (the confirmation flow) counts only when the profile sets a channel."""
    d = Path(root) / "industries" / industry
    files = [d / "core.md"]
    for n in facts["workflows"]:
        if n in OUTBOUND_ONLY_WORKFLOWS.get(industry, ()) and facts["direction"] != "outbound":
            continue
        files += sorted((d / "workflows").glob(f"{n}-*.md"))
    lines = []
    for f in files:
        if not f.is_file():
            continue
        for row in f.read_text(encoding="utf-8").splitlines():
            if "confirmation_channels" in row and not facts.get("confirmation"):
                continue
            for q in SAY_EXACTLY.findall(row):
                if q.strip() == "X":
                    continue  # the format example in R-71, not a real line
                if _norm(q) not in [_norm(x[1]) for x in lines]:
                    lines.append((f.name, q))
    bases = d / "section-bases.md"
    if bases.is_file():
        for kind, q in WELCOME_LINE.findall(bases.read_text(encoding="utf-8")):
            if kind.lower() == facts["direction"]:
                lines.append(("welcome", q))
    return lines


def lint_fixed_and_config(industry, instructions, profile_text, root=ROOT):
    """Deterministic checks that need no model: every fixed line is in the Instructions word for word, the welcome is
    the first line, and a prescription route the profile does not enable is not offered. Returns a list of problems."""
    facts = profile_facts(profile_text)
    body = _norm(instructions)
    problems = []
    for source, q in fixed_lines(industry, facts, root):
        if source == "welcome":
            first = next((l for l in instructions.splitlines() if l.strip()), "")
            if _norm(first) != _norm(q):
                problems.append(f'welcome is not the first line, word for word: expected "{_norm(q)}", first line is "{first.strip()[:80]}"')
        elif _norm(q) not in body:
            problems.append(f'fixed line from {source} missing word for word: "{_norm(q)}"')
    allowed = {facts["upload"]} & {"whatsapp", "email"}
    for n, line in enumerate(instructions.splitlines(), 1):
        low = line.lower()
        if "prescription" not in low and "upload" not in low:
            continue
        if "prescription_upload_method" in low:
            continue  # the route is chosen by the variable on the real platform (R-40)
        for word in ("whatsapp", "email"):
            if word in low and word not in allowed:
                problems.append(f"line {n}: prescription route offers {word} but the profile upload method is {facts['upload']}")
        if not allowed and ("send tool" in low or "send_confirmation" in low):
            problems.append(f"line {n}: send tool used for prescriptions but the profile upload method is {facts['upload']}")
    return problems


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


def load_judgment(path, wanted):
    """A saved per-profile judgment, or None when it is missing, unreadable or for different cases."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None
    if data.get("cases") != wanted or not isinstance(data.get("rows"), list):
        return None
    return data


def replies_complete(path, probes):
    """True when the saved replies file holds a reply for every probe."""
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return False
    return all(c["id"] in data and isinstance(data[c["id"]], str) for c in probes)


def run_industry(industry, llm, root=ROOT, date=None, profiles=None, out=None, cases=None, resume=False):
    out = out or sys.stdout
    date = date or datetime.date.today().isoformat()
    d = root / "industries" / industry
    checks = json.loads((d / "eval.json").read_text(encoding="utf-8"))["checks"]
    out_dir = d / "results"
    work = out_dir / date
    work.mkdir(parents=True, exist_ok=True)
    rows, lint, harness_errors = [], {}, []
    for pf in profile_files(d):
        if profiles and pf.stem.split("-")[0] not in profiles:
            continue
        name = pf.stem
        pid = name.split("-")[0]
        applicable = [c for c in checks if (not c.get("profiles") or pid in c["profiles"]) and case_selected(c["id"], cases)]
        if cases and not applicable:
            continue
        profile_text = pf.read_text(encoding="utf-8")
        inst_path = work / f"{name}-instructions.md"
        notes_path = work / f"{name}-draft-notes.md"
        replies_path = work / f"{name}-replies.json"
        lint_path = work / f"{name}-lint.json"
        judgment_path = work / f"{name}-judgment.json"
        wanted = [c["id"] for c in applicable]
        probes = [c for c in applicable if c.get("type") == "behaviour"]
        if resume:
            saved = load_judgment(judgment_path, wanted)
            if saved:
                rows += saved["rows"]
                lint[name] = saved.get("lint", [])
                print(f"resume {name}: complete, skipped", file=out)
                continue
        reuse = (resume and inst_path.is_file() and notes_path.is_file() and replies_complete(replies_path, probes))
        if reuse:
            print(f"resume {name}: Instructions, notes and replies are complete, judging only", file=out)
            try:
                lint[name] = json.loads(lint_path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                lint[name] = lint_instructions(inst_path, root)
        else:
            if resume:
                print(f"resume {name}: not complete, regenerating", file=out)
            full = llm.run(
                f"Use the {industry}-prompt-writer skill for this test business. Output exactly two parts. "
                f"Part 1: the Instructions (welcome note, sections 1 to 6, variables in the platform syntax); "
                f"if the skill's output format starts with a line containing only {INSTRUCTIONS_MARKER} , keep that line. "
                f"Then a line containing only {NOTES_MARKER} . "
                f"Part 2: the draft notes (assumptions and defaults used, refused or changed client requests "
                f"with a one-line reason each, open items, the section 6 word count). Output nothing else. "
                f"Do not open eval.json files or results folders.\n\n"
                + visible_profile(profile_text))
            instructions, notes, outside = split_marked(full)
            if not instructions.strip():
                message = (f"harness error: {name}: the Instructions part is empty after splitting the skill output "
                           f"(not a skill failure); profile stopped, nothing judged")
                print(message, file=out)
                harness_errors.append(message)
                (work / f"{name}-raw-output.md").write_text(full, encoding="utf-8")
                continue
            warnings = []
            if outside:
                warnings.append("warning: text outside the markers (ignored): " + " / ".join(o[:60] for o in outside))
            welcome = next((q for source, q in fixed_lines(industry, profile_facts(profile_text), root) if source == "welcome"), None)
            stray = []
            if welcome:
                instructions, removed = strip_before_welcome(instructions, welcome)
                if removed:
                    stray = ["fixed-line/config: stray text before the welcome (removed for judging): "
                             + " / ".join(r.strip()[:60] for r in removed)]
            inst_path.write_text(instructions + "\n", encoding="utf-8")
            lint[name] = lint_instructions(inst_path, root) + warnings + stray + [
                "fixed-line/config: " + p for p in lint_fixed_and_config(industry, instructions, profile_text, root)]
            lint_path.write_text(json.dumps(lint[name], indent=2, ensure_ascii=False), encoding="utf-8")
            notes_path.write_text((notes or "(no draft notes supplied)") + "\n", encoding="utf-8")
            filled = test_values(profile_text)
            note = values_note(profile_variable_values(profile_text)) if industry in VARIABLE_VALUE_INDUSTRIES else ""
            system = instructions + tools_note(industry) + note
            with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
                answers = list(pool.map(lambda c: llm.run(fill_placeholders(c["probe"], filled), system=system, tools=""), probes))
            replies = {c["id"]: a for c, a in zip(probes, answers)}
            replies_path.write_text(json.dumps(replies, indent=2, ensure_ascii=False), encoding="utf-8")
        for problem in lint[name]:
            print(f"lint {name}: {problem}", file=out)
        verdict = llm.run(
            f"Industry: {industry}\nprofile: {name}\nprompt_file: {inst_path.as_posix()}\n"
            f"draft_notes_file: {notes_path.as_posix()}\n"
            f"replies: {replies_path.as_posix()}\n"
            f"Grade ONLY these checks from the industry's eval.json: {', '.join(c['id'] for c in applicable)}. "
            "After your table, end with one ```json block: "
            '{"results":[{"id":"...","result":"PASS or FAIL","reason":"one line"}]}',
            agent="eval-judge")
        profile_rows = [{"case_id": r["case_id"], "profile": name, "result": r["result"], "reason": r["reason"]}
                        for r in parse_judge(verdict)]
        rows += profile_rows
        judgment_path.write_text(json.dumps({"cases": wanted, "rows": profile_rows, "lint": lint[name]},
                                            indent=2, ensure_ascii=False), encoding="utf-8")
    passed = sum(r["result"] == "pass" for r in rows)
    summary = {"industry": industry, "date": date, "total": len(rows), "passed": passed,
               "failed": len(rows) - passed,
               "pass_rate": round(100 * passed / len(rows), 1) if rows else 0.0,
               "harness_errors": harness_errors}
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
    ap.add_argument("--resume", action="store_true",
                    help="skip profiles already judged in this run folder; judge only a profile whose replies are complete; regenerate one cut mid-way")
    ap.add_argument("--cases", help="comma list of case ids to run and judge, for example E04,E06 (PHA-E04 also works)")
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
        summary, rows = run_industry(ind, llm, Path(root), args.date, args.profiles,
                                     cases=[c.strip() for c in args.cases.split(",") if c.strip()] if args.cases else None,
                                     resume=args.resume, out=out)
        table.append((ind, f"{summary['passed']}/{summary['total']} passed", f"{summary['pass_rate']}%"))
        failing += [(ind, r) for r in rows if r["result"] == "fail"]
        if summary["failed"]:
            code = 1
        if summary.get("harness_errors"):
            code = 2
            table[-1] = (table[-1][0], table[-1][1], table[-1][2] + f"  [{len(summary['harness_errors'])} harness error(s), see above]")
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
