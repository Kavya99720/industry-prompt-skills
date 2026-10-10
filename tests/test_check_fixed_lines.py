import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL_SCRIPT = ROOT / "scripts" / "check_fixed_lines.py"  # runner and CI only; no skill runs it
spec = importlib.util.spec_from_file_location("check_fixed_lines", SKILL_SCRIPT)
cfl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cfl)


def make_refs(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text(
        '| R-01 | Format: say exactly "X", then act. Say exactly "Hello there." then end_call. |\n'
        '| R-02 | Tool row for `card_block_tool`: say exactly "Your card is blocked." then transfer. |\n'
        '| R-03 | Flow in {{var.confirmation_channels}}: say exactly "Would you like a confirmation?" |\n', encoding="utf-8")
    (refs / "workflows" / "01-enquiry.md").write_text('Say exactly "I can\'t share that." then wait.', encoding="utf-8")
    (refs / "workflows" / "02-outbound-call.md").write_text('say exactly "Sorry for the trouble." then end_call', encoding="utf-8")
    (refs / "workflows" / "README.md").write_text('say exactly "Never required."', encoding="utf-8")
    return refs


def test_missing_lines_are_reported_and_present_ones_are_not(tmp_path):
    refs = make_refs(tmp_path)
    out = "=== INSTRUCTIONS ===\nThank you for calling. Hello there.\nI can’t share that.\n"
    missing = cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": False})
    assert missing == []
    missing = cfl.check("Thank you for calling.\n", refs, numbers=["01"], tools={"card_block_tool": False})
    assert [q for _, q in missing] == ["Hello there.", "I can't share that."]


def test_tool_lines_and_confirmation_lines_are_required_only_when_on(tmp_path):
    refs = make_refs(tmp_path)
    off = [q for _, q in cfl.check("Hello there. I can't share that.", refs, numbers=["01"], tools={"card_block_tool": False})]
    assert "Your card is blocked." not in off and "Would you like a confirmation?" not in off
    on = [q for _, q in cfl.check("Hello there. I can't share that.", refs, numbers=["01"],
                                  tools={"card_block_tool": True, "confirmation_channels": True})]
    assert "Your card is blocked." in on and "Would you like a confirmation?" in on


def test_direction_comes_from_the_welcome_or_the_workflow_file_name(tmp_path):
    refs = make_refs(tmp_path)
    inbound = [q for _, q in cfl.check("Thank you for calling.", refs)]
    outbound = [q for _, q in cfl.check("=== INSTRUCTIONS ===\nHello, this is A, an AI assistant calling from B.", refs)]
    assert "I can't share that." in inbound and "Sorry for the trouble." not in inbound
    assert "Sorry for the trouble." in outbound and "I can't share that." not in outbound
    assert "Never required." not in inbound + outbound


def test_the_command_line_exit_codes(tmp_path):
    refs = make_refs(tmp_path)
    good = tmp_path / "good.md"
    good.write_text("Hello there. I can't share that.", encoding="utf-8")
    bad = tmp_path / "bad.md"
    bad.write_text("Nothing here.", encoding="utf-8")
    cmd = [sys.executable, str(SKILL_SCRIPT), "--references", str(refs), "--workflows", "01", "--tool", "card_block_tool=off"]
    ok = subprocess.run(cmd[:2] + [str(good)] + cmd[2:], capture_output=True, text=True)
    assert ok.returncode == 0 and "0 missing" in ok.stdout
    fail = subprocess.run(cmd[:2] + [str(bad)] + cmd[2:], capture_output=True, text=True)
    assert fail.returncode == 1 and 'MISSING (from core.md): "Hello there."' in fail.stdout
    usage = subprocess.run(cmd[:2] + [str(tmp_path / "nope.md")] + cmd[2:], capture_output=True, text=True)
    assert usage.returncode == 2


def test_no_skill_or_template_runs_or_ships_the_script():
    assert not (ROOT / ".claude" / "skills" / "banking-prompt-writer" / "scripts").exists()
    assert not (ROOT / "docs" / "shared" / "new-industry-template" / "check_fixed_lines.py").exists()
    for rel in (".claude/skills/banking-prompt-writer/SKILL.md", "docs/shared/new-industry-template/skill.template.md"):
        text = (ROOT / rel).read_text(encoding="utf-8")
        assert "python .claude/skills" not in text and "check_fixed_lines.py <file>" not in text
        assert "run no command" in text.lower() or "no commands" in text.lower()


def test_the_banking_script_finds_the_fixed_blocks_in_the_real_references():
    refs = ROOT / ".claude" / "skills" / "banking-prompt-writer" / "references"
    lines = [q for _, q in cfl.required_lines(refs, {"01", "02", "03"}, "inbound", cfl.with_defaults({"card_block_tool": True, "balance_lookup_tool": True}))]
    assert "Please report this quickly on the cybercrime helpline, 1 9 3 0. Please stop. I never ask for that, and you should never share it with anyone." in lines
    assert "For your safety, please don't send any money right now. Please report this quickly on the cybercrime helpline, 1 9 3 0." in lines
    assert "I can't share account details on this call." in lines
    assert "I'm sorry, I could not complete that. Our team will call you to confirm." in lines


def test_a_fixed_block_written_as_say_exactly_this_block_is_required(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text('| R-07 | say exactly this block, in this order: "One. Two." then ask the name. |', encoding="utf-8")
    assert [q for _, q in cfl.check("nothing", refs)] == ["One. Two."]
    assert cfl.check("One.  Two.", refs) == []
