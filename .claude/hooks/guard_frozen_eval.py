#!/usr/bin/env python
"""PreToolUse hook (Edit|Write|MultiEdit): block changes to a frozen industries/<industry>/eval.json."""
import json
import re
import sys
from pathlib import Path

MESSAGE = (
    "eval.json is frozen. Fix the industry skill instead. "
    "If the eval is genuinely wrong, ask the user and record it in docs/DECISIONS.md."
)
EVAL_RE = re.compile(r"(^|/)industries/[^/]+/eval\.json$")


def is_frozen(path):
    try:
        return json.loads(Path(path).read_text(encoding="utf-8")).get("frozen") is True
    except (OSError, ValueError, AttributeError):
        return False


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    path = (event.get("tool_input") or {}).get("file_path")
    if not isinstance(path, str):
        return 0
    if EVAL_RE.search(path.replace("\\", "/")) and is_frozen(path):
        print(MESSAGE, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
