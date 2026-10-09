import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / ".claude" / "hooks" / "guard_industry_scope.py"
spec = importlib.util.spec_from_file_location("guard_industry_scope", HOOK)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


def make_root(tmp_path, locked=("healthcare", "pharmacy")):
    (tmp_path / ".claude").mkdir()
    (tmp_path / ".claude" / "locked-industries.json").write_text(json.dumps({"locked": list(locked)}), encoding="utf-8")
    return tmp_path


def event(path, agent=None):
    e = {"tool_name": "Write", "tool_input": {"file_path": str(path)}}
    if agent:
        e["agent_type"] = agent
        e["agent_id"] = "abc123"
    return e


def test_industry_agent_may_write_in_its_own_folders(tmp_path):
    root = make_root(tmp_path)
    assert guard.decide(event(root / "industries/banking/core.md", "banking-agent"), root) is None
    assert guard.decide(event(root / ".claude/skills/banking-prompt-writer/SKILL.md", "banking-agent"), root) is None


def test_industry_agent_is_blocked_everywhere_else(tmp_path):
    root = make_root(tmp_path)
    for target in ("industries/hr/core.md", ".claude/skills/hr-prompt-writer/SKILL.md", "docs/DECISIONS.md",
                   "scripts/run_evals.py", ".claude/agents/banking-agent.md", ".claude/locked-industries.json", "CLAUDE.md"):
        message = guard.decide(event(root / target, "banking-agent"), root)
        assert message and "banking agent may write only inside industries/banking/" in message, target


def test_main_session_is_never_blocked_by_the_scope_rule(tmp_path):
    root = make_root(tmp_path)
    for target in ("industries/hr/core.md", "docs/DECISIONS.md", "scripts/run_evals.py", ".claude/locked-industries.json"):
        assert guard.decide(event(root / target), root) is None


def test_other_kinds_of_agent_are_not_limited(tmp_path):
    root = make_root(tmp_path)
    assert guard.decide(event(root / "docs/DECISIONS.md", "general-purpose"), root) is None
    assert guard.decide(event(root / "docs/DECISIONS.md", "claude"), root) is None


def test_locked_industries_block_everyone_including_the_main_session(tmp_path):
    root = make_root(tmp_path)
    for target in ("industries/healthcare/core.md", "industries/pharmacy/workflows/02-order-prescription.md",
                   ".claude/skills/healthcare-prompt-writer/SKILL.md", ".claude/skills/pharmacy-prompt-writer/references/core.md"):
        for agent in (None, "healthcare-agent", "pharmacy-agent"):
            message = guard.decide(event(root / target, agent), root)
            assert message and "is locked" in message and "unlock" in message, (target, agent)


def test_unlocking_an_industry_allows_edits_again(tmp_path):
    root = make_root(tmp_path, locked=("healthcare",))
    assert guard.decide(event(root / "industries/pharmacy/core.md"), root) is None
    assert guard.decide(event(root / "industries/healthcare/core.md"), root)


def test_files_outside_the_repo_and_shared_files_are_allowed_for_the_main_session(tmp_path):
    root = make_root(tmp_path)
    assert guard.decide(event(tmp_path.parent / "elsewhere.md"), root) is None
    assert guard.decide(event(root / "docs/shared/baseline-rules.md"), root) is None


def test_hook_exit_codes_through_the_command_line(tmp_path):
    root = make_root(tmp_path)
    env_event = event(root / "industries/healthcare/core.md")
    env_event["cwd"] = str(root)
    blocked = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(env_event), capture_output=True, text=True,
                             env={"PATH": "", "CLAUDE_PROJECT_DIR": str(root)})
    assert blocked.returncode == 2 and "locked" in blocked.stderr
    allowed = event(root / "docs/x.md")
    allowed["cwd"] = str(root)
    ok = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(allowed), capture_output=True, text=True,
                        env={"PATH": "", "CLAUDE_PROJECT_DIR": str(root)})
    assert ok.returncode == 0
