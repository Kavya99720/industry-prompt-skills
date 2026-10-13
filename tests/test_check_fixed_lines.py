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


def make_must_refs(tmp_path):
    refs = make_refs(tmp_path)
    (refs / "core.md").write_text(
        (refs / "core.md").read_text(encoding="utf-8")
        + '| R-08 | Section 1 must include "Never claim to be human." |\n'
        + '| R-50 | Section 5 must include "If the patient\'s name was not clearly heard, ask again." |\n'
        + '| R-09 | Tool row for `card_block_tool`: must include "Card block is available." |\n', encoding="utf-8")
    return refs


def test_a_must_include_line_that_is_present_passes_whatever_the_case_or_punctuation(tmp_path):
    refs = make_must_refs(tmp_path)
    out = ("Hello there. I can't share that. NEVER CLAIM TO BE HUMAN, and if the patients name was not clearly heard - "
           "ask again; then carry on.")
    assert cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": False}) == []


def test_a_missing_must_include_line_is_flagged_with_its_source(tmp_path):
    refs = make_must_refs(tmp_path)
    out = "Hello there. I can't share that. Never claim to be human."
    missing = cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": False})
    assert missing == [("core.md", cfl.MUST_PREFIX + "If the patient's name was not clearly heard, ask again.")]
    on = [q for _, q in cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": True})]
    assert cfl.MUST_PREFIX + "Card block is available." in on


def test_must_include_lines_count_as_required_and_print_with_the_marker(tmp_path):
    refs = make_must_refs(tmp_path)
    bad = tmp_path / "bad.md"
    bad.write_text("Hello there. I can't share that.", encoding="utf-8")
    cmd = [sys.executable, str(SKILL_SCRIPT), str(bad), "--references", str(refs), "--workflows", "01", "--tool", "card_block_tool=off"]
    res = subprocess.run(cmd, capture_output=True, text=True)
    assert res.returncode == 1
    assert 'MISSING (from core.md): must include "Never claim to be human."' in res.stdout
    assert "fixed lines: 4 required, 2 missing" in res.stdout


def test_rows_without_the_marker_behave_as_before(tmp_path):
    refs = make_refs(tmp_path)
    out = "=== INSTRUCTIONS ===\nThank you for calling. Hello there.\nI can\u2019t share that.\n"
    assert cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": False}) == []
    assert cfl.required_text(refs, {"01"}, "inbound", cfl.with_defaults({})) == []
    missing = cfl.check("Thank you for calling.\n", refs, numbers=["01"], tools={"card_block_tool": False})
    assert [q for _, q in missing] == ["Hello there.", "I can't share that."]


def make_upload_refs(tmp_path):
    refs = make_refs(tmp_path)
    (refs / "workflows" / "01-enquiry.md").write_text(
        '| R-54a | [upload: whatsapp] If {{var.prescription_upload_method}} is whatsapp: say exactly "Is this number on WhatsApp?" |\n'
        '| R-54b | [upload: email] If {{var.prescription_upload_method}} is email: say exactly "Please tell me your email address." |\n'
        'Say exactly "I can\'t share that." then wait.\n', encoding="utf-8")
    return refs


def test_upload_branch_lines_are_required_only_for_the_chosen_method(tmp_path):
    refs = make_upload_refs(tmp_path)
    def need(method):
        tools = {"card_block_tool": False}
        if method:
            tools["prescription_upload_method"] = method
        return [q for _, q in cfl.required_lines(refs, {"01"}, "inbound", cfl.with_defaults(tools))]
    both = need(None)
    assert "Is this number on WhatsApp?" in both and "Please tell me your email address." in both
    wa = need("whatsapp")
    assert "Is this number on WhatsApp?" in wa and "Please tell me your email address." not in wa
    em = need("email")
    assert "Please tell me your email address." in em and "Is this number on WhatsApp?" not in em
    for none in ("in_store", "not_set"):
        got = need(none)
        assert "Is this number on WhatsApp?" not in got and "Please tell me your email address." not in got
        assert "I can't share that." in got


def test_the_upload_method_option_is_accepted_on_the_command_line(tmp_path):
    refs = make_upload_refs(tmp_path)
    out = tmp_path / "out.md"
    out.write_text("Hello there. I can't share that. Is this number on WhatsApp?", encoding="utf-8")
    base = [sys.executable, str(SKILL_SCRIPT), str(out), "--references", str(refs), "--workflows", "01",
            "--tool", "card_block_tool=off"]
    ok = subprocess.run(base + ["--tool", "prescription_upload_method=whatsapp"], capture_output=True, text=True)
    assert ok.returncode == 0 and "0 missing" in ok.stdout
    bad = subprocess.run(base + ["--tool", "prescription_upload_method=email"], capture_output=True, text=True)
    assert bad.returncode == 1 and "Please tell me your email address." in bad.stdout
    store = subprocess.run(base + ["--tool", "prescription_upload_method=in_store"], capture_output=True, text=True)
    assert store.returncode == 0
    wrong = subprocess.run(base + ["--tool", "prescription_upload_method=sms"], capture_output=True, text=True)
    assert wrong.returncode == 2


def test_rule_ids_inside_the_instructions_are_reported_but_not_in_the_notes(tmp_path):
    refs = make_refs(tmp_path)
    text = ("=== INSTRUCTIONS ===\nHello there. I can't share that.\nBOOK: say the R-41 line of section 5.\n"
            "## Prompt Variables\n\n=== DRAFT NOTES ===\n- Rule R-76 was applied; see S-37.\n")
    missing = cfl.check(text, refs, numbers=["01"], tools={"card_block_tool": False})
    assert missing == [("Instructions line 3", cfl.RULE_ID_PREFIX + "R-41 in: BOOK: say the R-41 line of section 5.")]
    clean = text.replace("the R-41 line", "the on-leave line")
    assert cfl.check(clean, refs, numbers=["01"], tools={"card_block_tool": False}) == []
    bad = tmp_path / "bad.md"
    bad.write_text(text, encoding="utf-8")
    res = subprocess.run([sys.executable, str(SKILL_SCRIPT), str(bad), "--references", str(refs), "--workflows", "01",
                          "--tool", "card_block_tool=off"], capture_output=True, text=True)
    assert res.returncode == 1 and "RULE ID in the Instructions (Instructions line 3)" in res.stdout


PROFILE = """| Item | Value |
|---|---|
| Business name | Lakeview Hospital |
| Assistant | Asha (female) |
| Business type | Hospital (the agent says "the hospital") |
| Direction | Inbound |
"""


def test_welcome_is_built_from_the_profile_values():
    assert cfl.welcome_from_profile(PROFILE) == "Thank you for calling Lakeview Hospital. This is Asha. How can I help you?"
    no_agent = PROFILE.replace("| Assistant | Asha (female) |", "| Assistant | NOT given |")
    assert cfl.welcome_from_profile(no_agent) == "Thank you for calling Lakeview Hospital. How can I help you?"
    no_name = PROFILE.replace("| Business name | Lakeview Hospital |", "| Business name | NOT given |")
    assert cfl.welcome_from_profile(no_name) == "Thank you for calling the hospital. This is Asha. How can I help you?"
    outbound = PROFILE.replace("| Direction | Inbound |", "| Direction | Outbound |")
    assert cfl.welcome_from_profile(outbound) == "Hello, this is Asha calling from Lakeview Hospital. Is this a good time to talk?"
    assert cfl.welcome_from_profile(outbound.replace("| Assistant | Asha (female) |", "| Assistant | not provided |")) == \
        "Hello, I am calling from Lakeview Hospital. Is this a good time to talk?"


def test_the_profile_welcome_is_required_word_for_word(tmp_path):
    refs = make_refs(tmp_path)
    profile = tmp_path / "profile.md"
    profile.write_text(PROFILE, encoding="utf-8")
    good = tmp_path / "good.md"
    good.write_text("=== INSTRUCTIONS ===\nThank you for calling Lakeview Hospital. This is Asha. How can I help you?\n"
                    "Hello there. I can't share that.\n", encoding="utf-8")
    bad = tmp_path / "bad.md"
    bad.write_text("=== INSTRUCTIONS ===\nThank you for calling Lakeview Hospital. How can I help you?\n"
                   "Hello there. I can't share that.\n", encoding="utf-8")
    cmd = [sys.executable, str(SKILL_SCRIPT), "--references", str(refs), "--workflows", "01", "--tool", "card_block_tool=off",
           "--profile", str(profile)]
    ok = subprocess.run(cmd[:2] + [str(good)] + cmd[2:], capture_output=True, text=True)
    assert ok.returncode == 0 and "0 missing" in ok.stdout
    res = subprocess.run(cmd[:2] + [str(bad)] + cmd[2:], capture_output=True, text=True)
    assert res.returncode == 1 and 'MISSING (from welcome (profile)): "Thank you for calling Lakeview Hospital. This is Asha.' in res.stdout


def test_a_package_offer_line_is_required_only_when_a_package_exists(tmp_path):
    refs = make_refs(tmp_path)
    core = refs / "core.md"
    core.write_text(core.read_text(encoding="utf-8")
                    + '| R-84 | Required only when a package or offer exists (package_offer). Section 1 must include "Offer it once." |' + chr(10),
                    encoding="utf-8")
    out = "Hello there. I can't share that."
    off = [q for _, q in cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": False})]
    assert cfl.MUST_PREFIX + "Offer it once." not in off
    on = [q for _, q in cfl.check(out, refs, numbers=["01"], tools={"card_block_tool": False, "package_offer": True})]
    assert cfl.MUST_PREFIX + "Offer it once." in on
    assert cfl.check(out + " Offer it once.", refs, numbers=["01"], tools={"card_block_tool": False, "package_offer": True}) == []


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
