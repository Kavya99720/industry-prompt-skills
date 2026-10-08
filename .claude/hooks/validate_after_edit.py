#!/usr/bin/env python
"""PostToolUse hook (Edit|Write|MultiEdit).

- An edited industries/<industry>/eval.json is validated with scripts/validate_eval.py.
- Any edited .md/.json/.txt under .claude/skills, industries or outputs is checked with
  scripts/check_variables.py (wrong variable styles, unknown variables, client values).
Exit 2 sends the problems back to Claude.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

EVAL_RE = re.compile(r"(^|/)industries/[^/]+/eval\.json$")
ROOT = Path(__file__).resolve().parent.parent.parent
VALIDATOR = ROOT / "scripts" / "validate_eval.py"
VARIABLE_CHECKER = ROOT / "scripts" / "check_variables.py"
VARIABLE_SCOPE_RE = re.compile(r"(^|/)(\.claude/skills|industries|outputs)/.+\.(md|json|txt)$")


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    path = (event.get("tool_input") or {}).get("file_path")
    if not isinstance(path, str):
        return 0
    norm = path.replace("\\", "/")
    problems = []
    if EVAL_RE.search(norm):
        result = subprocess.run([sys.executable, str(VALIDATOR), path], capture_output=True, text=True)
        if result.returncode != 0:
            problems.append(result.stderr or result.stdout)
    if VARIABLE_SCOPE_RE.search(norm):
        result = subprocess.run(
            [sys.executable, str(VARIABLE_CHECKER), "--paths", path], capture_output=True, text=True
        )
        if result.returncode != 0:
            problems.append(result.stdout or result.stderr)
    if problems:
        print(chr(10).join(problems), file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
