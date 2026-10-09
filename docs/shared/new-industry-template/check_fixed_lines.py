#!/usr/bin/env python
"""Fixed-line self-check for a prompt-writer skill. Standard library only.

Every `say exactly "..."` line (and every fixed block, which is one quoted string) in references/core.md and the
selected workflows must appear verbatim in the skill's output. Run it on your own output before you finish:

  python check_fixed_lines.py OUTPUT.md --workflows 01 02 03 --tool card_block_tool=on --tool balance_lookup_tool=off

  OUTPUT.md        the whole output, starting with the === INSTRUCTIONS === marker (or only the Instructions part)
  --workflows      workflow numbers you selected (default: every written workflow of the output's direction;
                   a workflow whose file name contains "outbound" belongs to the outbound direction)
  --direction      inbound or outbound (default: outbound when the welcome says "calling from")
  --tool name=on|off
                   an optional config tool or setting. A line that only appears in rules mentioning one that is OFF is not
                   required. confirmation_channels is OFF unless you pass --tool confirmation_channels=on
  --references DIR the references folder (default: ../references next to this script)

Exit code 0: nothing missing. Exit code 1: lines are missing; each is printed. If lines are missing, add exactly those
lines (with their action) where their rule says, and run the check once more. Rewrite only once, then output.
Exit code 2: usage error.
"""
import argparse
import re
import sys
from pathlib import Path

SAY_EXACTLY = re.compile(r'say exactly(?: and only)?(?: this block\b[^"]{0,50})?\s*"([^"]+)"', re.I)


def norm(text):
    text = text.replace("`", "").replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    return " ".join(text.split())


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
    """confirmation_channels is OFF unless the client configured a channel: its lines are then required."""
    merged = {"confirmation_channels": False}
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
                mentioned = [t for t in tools if t in row]
                needed = (not mentioned) or any(tools[t] for t in mentioned)
                key = norm(q)
                if key not in found:
                    found[key] = [f.name, q, needed]
                elif needed:
                    found[key][2] = True
    return [(v[0], v[1]) for v in found.values() if v[2]]


def check(output_text, refs, numbers=(), direction=None, tools=None):
    tools = with_defaults(tools)
    head = output_text.split("\n", 12)
    if direction is None:
        direction = "outbound" if any("calling from" in l for l in head) else "inbound"
    body = norm(output_text)
    return [(src, q) for src, q in required_lines(Path(refs), set(numbers), direction, tools) if norm(q) not in body]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("output")
    ap.add_argument("--workflows", nargs="*", default=[])
    ap.add_argument("--direction", choices=("inbound", "outbound"))
    ap.add_argument("--tool", action="append", default=[], help="name=on|off")
    ap.add_argument("--references", default=str(Path(__file__).resolve().parent.parent / "references"))
    args = ap.parse_args(argv)
    path = Path(args.output)
    if not path.is_file():
        print(f"cannot read {path}", file=sys.stderr)
        return 2
    tools = {}
    for item in args.tool:
        name, _, state = item.partition("=")
        if state.lower() not in ("on", "off"):
            print(f"--tool needs name=on or name=off, got {item}", file=sys.stderr)
            return 2
        tools[name] = state.lower() == "on"
    missing = check(path.read_text(encoding="utf-8"), args.references, args.workflows, args.direction, tools)
    for src, q in missing:
        print(f'MISSING (from {src}): "{q}"')
    required = len(required_lines(Path(args.references), set(args.workflows),
                                  args.direction or ("outbound" if "calling from" in path.read_text(encoding="utf-8")[:900] else "inbound"), with_defaults(tools)))
    print(f"fixed lines: {required} required, {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
