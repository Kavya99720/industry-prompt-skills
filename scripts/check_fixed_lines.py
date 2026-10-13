#!/usr/bin/env python
"""Fixed-line check for generated Instructions. Standard library only. For the runner and CI only: a skill never runs
this during generation (it would need a tool approval, which cannot be given in a non-interactive run; DECISIONS 63).

Every `say exactly "..."` line (and every fixed block, which is one quoted string) in the skill's references/core.md and
the selected workflows must appear verbatim in the generated output. A line marked `must include "..."` (on any line of
core.md or a selected workflow file) is required text, not a spoken line: it must appear in the output as a normalized
match (case-insensitive, punctuation ignored), so a longer sentence that contains it passes:

  python scripts/check_fixed_lines.py OUTPUT.md --industry banking --workflows 01 02 03 --tool card_block_tool=on --tool balance_lookup_tool=off

  OUTPUT.md        the whole output, starting with the === INSTRUCTIONS === marker (or only the Instructions part)
  --workflows      workflow numbers you selected (default: every written workflow of the output's direction;
                   a workflow whose file name contains "outbound" belongs to the outbound direction)
  --direction      inbound or outbound (default: outbound when the welcome says "calling from")
  --tool name=on|off
                   an optional config tool or setting. A line that only appears in rules mentioning one that is OFF is not
                   required. confirmation_channels is OFF unless you pass --tool confirmation_channels=on
  --industry NAME  use .claude/skills/NAME-prompt-writer/references (default when --references is not given: banking)
  --references DIR the references folder, instead of --industry

  --tool prescription_upload_method=whatsapp|email|in_store|not_set
                   the prescription upload method the client chose. Rows marked [upload: whatsapp] or [upload: email] are
                   required only for the matching method (none for in_store or not_set). Without this option every marked
                   row is required, as before.

A rule ID such as "R-41" or "S-37" anywhere in the Instructions (the part before the === DRAFT NOTES === marker; the
whole text when there is no marker) is reported as a problem: rule IDs belong to the sources, never to the prompt.

  --profile FILE   a test profile (industries/<x>/test-profiles/NN-*.md) of an industry that prints its business facts
                   (inline_values). The expected welcome is built from the profile's Business name, Assistant and
                   Direction rows ("Thank you for calling <name>. This is <agent>. How can I help you?"; the "This is
                   <agent>." part is dropped when no assistant name is given; no business name gives the neutral
                   word of the Business type row) and must appear word for word.

Exit code 0: nothing missing. Exit code 1: lines are missing; each is printed.
Exit code 2: usage error.
"""
import argparse
import re
import sys
from pathlib import Path

SAY_EXACTLY = re.compile(r'say exactly(?: and only)?(?: this block\b[^"]{0,50})?\s*"([^"]+)"', re.I)
MUST_PREFIX = "must include: "
RULE_ID = re.compile(r"\b[RS]-\d+\b")
RULE_ID_PREFIX = "rule ID: "
NOTES_MARKER = "=== DRAFT NOTES ==="
UPLOAD_BRANCH = re.compile(r"\[upload:\s*(whatsapp|email)\]", re.I)
UPLOAD_TOOL = "prescription_upload_method"
UPLOAD_VALUES = ("whatsapp", "email", "in_store", "not_set")
MUST_INCLUDE = re.compile(r'must include\s*"([^"]+)"', re.I)


def norm(text):
    text = text.replace("`", "").replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    return " ".join(text.split())


def norm_text(text):
    """Case-insensitive, punctuation-free form used for must-include lines."""
    return " ".join(re.sub(r"[^\w\s]", "", norm(text).lower()).split())


def profile_value(profile_text, label):
    """The value cell of a `| label | value |` row of a test profile, or None."""
    m = re.search(r"^\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|\s*$", profile_text, re.M | re.I)
    return m.group(1).strip() if m else None


def welcome_from_profile(profile_text):
    """The welcome an inline-values Instructions set must start with, from a test profile's own values."""
    def given(v):
        return v is not None and not re.match(r"(not given|not provided|not stated|none)", v, re.I)
    biz = profile_value(profile_text, "Business name")
    if not given(biz):
        kind = profile_value(profile_text, "Business type") or ""
        m = re.search(r'says "([^"]+)"', kind)
        biz = m.group(1) if m else "our clinic"
    agent = profile_value(profile_text, "Assistant")
    agent = re.sub(r"\s*\([^)]*\)\s*$", "", agent).strip() if given(agent) else None
    direction = (profile_value(profile_text, "Direction") or "inbound").lower()
    if direction.startswith("out"):
        return (f"Hello, this is {agent} calling from {biz}. Is this a good time to talk?" if agent
                else f"Hello, I am calling from {biz}. Is this a good time to talk?")
    return (f"Thank you for calling {biz}. This is {agent}. How can I help you?" if agent
            else f"Thank you for calling {biz}. How can I help you?")


def workflow_files(refs, numbers, direction):
    wf = refs / "workflows"
    files = []
    if not wf.is_dir():
        return files
    for f in sorted(wf.glob("*.md")):
        if f.name.lower() == "readme.md":
            continue
        m = re.match(r"(\d+)-", f.name)
        if not m:
            continue
        if numbers:
            if m.group(1) not in numbers:
                continue
        elif ("outbound" in f.name.lower()) != (direction == "outbound"):
            continue
        if "Status: stub" in f.read_text(encoding="utf-8")[:600]:
            continue
        files.append(f)
    return files


def with_defaults(tools):
    """confirmation_channels is OFF unless the client configured a channel: its lines are then required.
    package_offer is OFF unless the business facts or the client name a package or offer (--tool package_offer=on)."""
    merged = {"confirmation_channels": False, "package_offer": False}
    merged.update(tools or {})
    return merged


def required_lines(refs, numbers, direction, tools):
    """Quotes that must be present, as a list of (source file name, quote)."""
    files = [refs / "core.md"] + workflow_files(refs, numbers, direction)
    found = {}
    for f in files:
        if not f.is_file():
            continue
        for row in f.read_text(encoding="utf-8").splitlines():
            for q in SAY_EXACTLY.findall(row):
                if q.strip() == "X":
                    continue  # the format example, not a real line
                mentioned = [t for t in tools if t in row and isinstance(tools[t], bool)]
                needed = (not mentioned) or any(tools[t] for t in mentioned)
                branch = UPLOAD_BRANCH.search(row)
                if branch and isinstance(tools.get(UPLOAD_TOOL), str):
                    needed = needed and tools[UPLOAD_TOOL] == branch.group(1).lower()
                key = norm(q)
                if key not in found:
                    found[key] = [f.name, q, needed]
                elif needed:
                    found[key][2] = True
    return [(v[0], v[1]) for v in found.values() if v[2]]


def required_text(refs, numbers, direction, tools):
    """Quotes marked must include, as a list of (source file name, quote)."""
    files = [refs / "core.md"] + workflow_files(refs, numbers, direction)
    found = {}
    for f in files:
        if not f.is_file():
            continue
        for row in f.read_text(encoding="utf-8").splitlines():
            for q in MUST_INCLUDE.findall(row):
                mentioned = [t for t in tools if t in row and isinstance(tools[t], bool)]
                needed = (not mentioned) or any(tools[t] for t in mentioned)
                key = norm_text(q)
                if key not in found:
                    found[key] = [f.name, q, needed]
                elif needed:
                    found[key][2] = True
    return [(v[0], v[1]) for v in found.values() if v[2]]


def check(output_text, refs, numbers=(), direction=None, tools=None, welcome=None):
    tools = with_defaults(tools)
    head = output_text.split("\n", 12)
    if direction is None:
        direction = "outbound" if any("calling from" in l for l in head) else "inbound"
    body = norm(output_text)
    missing = [(src, q) for src, q in required_lines(Path(refs), set(numbers), direction, tools) if norm(q) not in body]
    text = norm_text(output_text)
    missing += [(src, MUST_PREFIX + q) for src, q in required_text(Path(refs), set(numbers), direction, tools)
                if norm_text(q) not in text]
    if welcome and norm(welcome) not in body:
        missing.append(("welcome (profile)", welcome))
    missing += rule_id_problems(output_text)
    return missing


def rule_id_problems(output_text):
    """Rule IDs (R-12, S-37) inside the Instructions part of an output, as (where, RULE_ID_PREFIX + text) pairs."""
    instructions = output_text.split(NOTES_MARKER, 1)[0] if re.search(r"(?m)^" + re.escape(NOTES_MARKER) + r"\s*$", output_text) else output_text
    found = []
    for n, line in enumerate(instructions.splitlines(), 1):
        for m in RULE_ID.finditer(line):
            found.append((f"Instructions line {n}", RULE_ID_PREFIX + m.group(0) + " in: " + line.strip()[:70]))
    return found


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("output")
    ap.add_argument("--workflows", nargs="*", default=[])
    ap.add_argument("--direction", choices=("inbound", "outbound"))
    ap.add_argument("--tool", action="append", default=[], help="name=on|off")
    ap.add_argument("--industry", default="banking")
    ap.add_argument("--references")
    ap.add_argument("--profile")
    args = ap.parse_args(argv)
    if not args.references:
        args.references = str(Path(__file__).resolve().parent.parent / ".claude" / "skills" / f"{args.industry}-prompt-writer" / "references")
    path = Path(args.output)
    if not path.is_file():
        print(f"cannot read {path}", file=sys.stderr)
        return 2
    tools = {}
    for item in args.tool:
        name, _, state = item.partition("=")
        if name == UPLOAD_TOOL and state.lower() in UPLOAD_VALUES:
            tools[name] = state.lower()
            continue
        if state.lower() not in ("on", "off"):
            print(f"--tool needs name=on or name=off, got {item}", file=sys.stderr)
            return 2
        tools[name] = state.lower() == "on"
    welcome = welcome_from_profile(Path(args.profile).read_text(encoding="utf-8")) if args.profile else None
    missing = check(path.read_text(encoding="utf-8"), args.references, args.workflows, args.direction, tools, welcome)
    for src, q in missing:
        if q.startswith(RULE_ID_PREFIX):
            print(f"RULE ID in the Instructions ({src}): {q[len(RULE_ID_PREFIX):]}")
        elif q.startswith(MUST_PREFIX):
            print(f'MISSING (from {src}): must include "{q[len(MUST_PREFIX):]}"')
        else:
            print(f'MISSING (from {src}): "{q}"')
    direction = args.direction or ("outbound" if "calling from" in path.read_text(encoding="utf-8")[:900] else "inbound")
    required = (len(required_lines(Path(args.references), set(args.workflows), direction, with_defaults(tools)))
                + len(required_text(Path(args.references), set(args.workflows), direction, with_defaults(tools)))
                + (1 if welcome else 0))
    print(f"fixed lines: {required} required, {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
