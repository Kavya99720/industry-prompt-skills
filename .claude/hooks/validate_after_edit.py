#!/usr/bin/env python
"""PostToolUse hook (Edit|Write|MultiEdit): validate an edited evals/<industry>/eval.json."""
import json
import re
import subprocess
import sys
from pathlib import Path

EVAL_RE = re.compile(r"(^|/)evals/[^/]+/eval\.json$")
VALIDATOR = Path(__file__).resolve().parent.parent.parent / "scripts" / "validate_eval.py"


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    path = (event.get("tool_input") or {}).get("file_path")
    if not isinstance(path, str) or not EVAL_RE.search(path.replace("\\", "/")):
        return 0
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), path], capture_output=True, text=True
    )
    if result.returncode != 0:
        print(result.stderr or result.stdout, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
