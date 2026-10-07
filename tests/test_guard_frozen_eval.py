import json
import subprocess
import sys
from pathlib import Path

import pytest

HOOK = Path(__file__).resolve().parent.parent / ".claude" / "hooks" / "guard_frozen_eval.py"


def run_hook(file_path):
    event = {"tool_name": "Edit", "tool_input": {"file_path": str(file_path)}}
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=json.dumps(event),
        capture_output=True,
        text=True,
    )


def write_eval(tmp_path, frozen):
    p = tmp_path / "evals" / "synthetic" / "eval.json"
    p.parent.mkdir(parents=True)
    p.write_text(json.dumps({"frozen": frozen}), encoding="utf-8")
    return p


def test_frozen_eval_blocked(tmp_path):
    r = run_hook(write_eval(tmp_path, True))
    assert r.returncode == 2
    assert "frozen" in r.stderr


def test_unfrozen_eval_allowed(tmp_path):
    assert run_hook(write_eval(tmp_path, False)).returncode == 0


def test_non_eval_path_allowed(tmp_path):
    p = tmp_path / "notes.json"
    p.write_text(json.dumps({"frozen": True}), encoding="utf-8")
    assert run_hook(p).returncode == 0


@pytest.mark.skipif(sys.platform != "win32", reason="backslash paths only resolve on Windows")
def test_windows_backslash_path_blocked(tmp_path):
    p = write_eval(tmp_path, True)
    path = str(p).replace("/", "\\")
    assert "\\" in path
    assert run_hook(path).returncode == 2
