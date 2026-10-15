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


def test_slots_in_a_say_exactly_line_are_filled_from_the_profile(tmp_path):
    refs = make_refs(tmp_path)
    wf = refs / "workflows" / "01-enquiry.md"
    wf.write_text(wf.read_text(encoding="utf-8")
                  + chr(10) + '| R-59 | Voicemail: say exactly "Hello, this is <agent name> from <business name>. Please call us back at <phone>." |' + chr(10),
                  encoding="utf-8")
    full = PROFILE + "| Business phone | 080-5550-0121 |" + chr(10)
    slots = cfl.profile_slots(full)
    assert slots == {"business name": "Lakeview Hospital", "agent name": "Asha", "phone": "080-5550-0121"}
    line = "Hello, this is Asha from Lakeview Hospital. Please call us back at 080-5550-0121."
    ok = cfl.check("Hello there. I can't share that. " + line, refs, numbers=["01"], tools={"card_block_tool": False}, slots=slots)
    assert ok == []
    bad = cfl.check("Hello there. I can't share that.", refs, numbers=["01"], tools={"card_block_tool": False}, slots=slots)
    assert [q for _, q in bad] == [line]
    no_phone = cfl.profile_slots(PROFILE)
    assert "phone" not in no_phone
    skipped = cfl.check("Hello there. I can't share that.", refs, numbers=["01"], tools={"card_block_tool": False}, slots=no_phone)
    assert skipped == []  # a slot the profile does not give: the line is not required
    assert cfl.fill_slots("Call <phone>.", None) == "Call <phone>."


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
    assert "I can't share account details on this call." not in lines  # lookup tool on: the account-data line is not required
    off = [q for _, q in cfl.required_lines(refs, {"01", "02", "03"}, "inbound", cfl.with_defaults({"card_block_tool": False, "balance_lookup_tool": False}))]
    assert "I can't share account details on this call." in off
    assert "I'm sorry, I could not complete that. Our team will call you to confirm." in lines


def test_a_fixed_block_written_as_say_exactly_this_block_is_required(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text('| R-07 | say exactly this block, in this order: "One. Two." then ask the name. |', encoding="utf-8")
    assert [q for _, q in cfl.check("nothing", refs)] == ["One. Two."]
    assert cfl.check("One.  Two.", refs) == []


def test_welcome_from_profile_banking_outbound_names_the_ai():
    outbound = PROFILE.replace("| Direction | Inbound |", "| Direction | Outbound |")
    assert cfl.welcome_from_profile(outbound, "banking") ==         "Hello, this is Asha, an AI assistant calling from Lakeview Hospital. Is this a good time to talk?"
    no_agent = outbound.replace("| Assistant | Asha (female) |", "| Assistant | not provided |")
    assert cfl.welcome_from_profile(no_agent, "banking") ==         "Hello, I am an AI assistant calling from Lakeview Hospital. Is this a good time to talk?"
    # other industries and inbound keep their forms
    assert cfl.welcome_from_profile(outbound, "pharmacy") ==         "Hello, this is Asha calling from Lakeview Hospital. Is this a good time to talk?"
    assert cfl.welcome_from_profile(PROFILE, "banking") ==         "Thank you for calling Lakeview Hospital. This is Asha. How can I help you?"


def test_a_lookup_off_line_is_required_only_when_the_lookup_tool_is_not_on(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text("", encoding="utf-8")
    (refs / "workflows" / "01-enquiry.md").write_text(
        '| R-41 | [balance_lookup_tool: off] When the tool is OFF say exactly "I can\'t share account details on this call." |\n'
        'ACCOUNT (lookup off): say exactly "I can\'t share account details on this call." then transfer.\n', encoding="utf-8")
    quote = "I can't share account details on this call."
    on = [q for _, q in cfl.check("nothing", refs, numbers=["01"], tools={"balance_lookup_tool": True})]
    off = [q for _, q in cfl.check("nothing", refs, numbers=["01"], tools={"balance_lookup_tool": False})]
    unset = [q for _, q in cfl.check("nothing", refs, numbers=["01"])]
    assert quote not in on
    assert quote in off and quote in unset


def test_confirmation_lines_follow_the_channels_the_client_gave(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text(
        '| R-19 | Flow (confirmation_channels): say exactly "Would you like a confirmation on WhatsApp or email?" '
        'then say exactly "Is this number on WhatsApp?" then say exactly "Please tell me your email address." '
        'then say exactly "Is there anything else I can help with?" |\n', encoding="utf-8")

    def need(channels):
        return {q for _, q in cfl.required_lines(refs, set(), "inbound", cfl.with_defaults(
            {"confirmation_channels": True, "channels": channels}))}
    both = need({"whatsapp", "email"})
    assert len(both) == 4
    wa = need({"whatsapp"})
    assert wa == {"Is this number on WhatsApp?", "Is there anything else I can help with?"}
    em = need({"email"})
    assert em == {"Please tell me your email address.", "Is there anything else I can help with?"}


def test_the_confirmation_channels_option_takes_whatsapp_email_or_both(tmp_path):
    out = tmp_path / "o.md"
    out.write_text("Hello", encoding="utf-8")
    refs = ROOT / ".claude" / "skills" / "banking-prompt-writer" / "references"
    for value in ("whatsapp", "email", "both"):
        r = subprocess.run([sys.executable, str(SKILL_SCRIPT), str(out), "--references", str(refs), "--workflows", "01", "02", "03",
                            "--tool", f"confirmation_channels={value}"], capture_output=True, text=True)
        assert r.returncode == 1 and "fixed lines:" in r.stdout


def test_profile_tools_reads_the_real_settings_of_each_banking_profile():
    def tools(n):
        f = next((ROOT / "industries" / "banking" / "test-profiles").glob(f"{n}-*.md"))
        return cfl.profile_tools(f.read_text(encoding="utf-8"))
    assert tools("01")["card_block_tool"] and tools("01")["balance_lookup_tool"] and tools("01")["channels"] == {"whatsapp", "email"}
    assert not tools("02")["card_block_tool"] and not tools("02")["balance_lookup_tool"] and tools("02")["channels"] == {"whatsapp"}
    assert not tools("03")["card_block_tool"] and not tools("03")["confirmation_channels"]
    assert tools("04")["card_block_tool"] and not tools("04")["balance_lookup_tool"]
    assert not tools("05")["card_block_tool"] and not tools("05")["balance_lookup_tool"]  # not stated: off by default


CYBER_BLOCK = "Please report this quickly on the cybercrime helpline, 1 9 3 0. Please stop. I never ask for that, and you should never share it with anyone."
PRINT_DECLINE = "I can't share that. I can help with your card or account, or connect you to our team."


def test_the_cybercrime_block_and_the_print_decline_are_required_on_every_banking_profile():
    refs = ROOT / ".claude" / "skills" / "banking-prompt-writer" / "references"
    profiles = sorted((ROOT / "industries" / "banking" / "test-profiles").glob("0*.md"))
    assert len(profiles) == 5
    for f in profiles:
        text = f.read_text(encoding="utf-8")
        direction = "outbound" if "| Direction | Outbound" in text else "inbound"
        tools = cfl.with_defaults(cfl.profile_tools(text))
        lines = [q for _, q in cfl.required_lines(refs, set(), direction, tools)]
        assert CYBER_BLOCK in lines, f.name
        assert PRINT_DECLINE in lines, f.name
        assert ("I'll connect you to our team." in lines) is (tools[cfl.TRANSFER_TARGET]), f.name
        # the block is a line of the s1-lines block of core.md, so every set carries it in section 1
        core = (refs / "core.md").read_text(encoding="utf-8")
        s1 = core.split("```s1-lines", 1)[1].split("```", 1)[0]
        assert CYBER_BLOCK in s1 and PRINT_DECLINE in s1


def test_banking_core_has_the_s5_lines_and_the_checker_requires_the_two_fixed_sentences():
    refs = ROOT / ".claude" / "skills" / "banking-prompt-writer" / "references"
    core = (refs / "core.md").read_text(encoding="utf-8")
    s5 = core.split("```s5-lines", 1)[1].split("```", 1)[0]
    stop = "Please stop. I never ask for that, and you should never share it with anyone."
    assert "Never transfer silently. Every transfer: say exactly \"I'll connect you to our team.\" then transfer." in s5
    assert "\"I'll connect you to our team.\" [tool: transfer]" in s5
    assert f'say exactly "{stop}"' in s5
    assert "The confirmation flow is never used after a failed action, in an emergency, on a transfer or on a voicemail." in s5
    lines = [q for _, q in cfl.required_lines(refs, set(), "inbound", cfl.with_defaults({}))]
    assert stop in lines and "I'll connect you to our team." in lines


def test_the_team_phrase_is_required_only_when_a_transfer_target_exists():
    refs = ROOT / ".claude" / "skills" / "banking-prompt-writer" / "references"
    phrase = "I'll connect you to our team."
    for name, expected in (("01", True), ("02", True), ("03", True), ("04", True), ("05", False)):
        f = next((ROOT / "industries" / "banking" / "test-profiles").glob(name + "-*.md"))
        text = f.read_text(encoding="utf-8")
        tools = cfl.with_defaults(cfl.profile_tools(text))
        assert tools[cfl.TRANSFER_TARGET] is expected, name
        direction = "outbound" if "| Direction | Outbound" in text else "inbound"
        lines = [q for _, q in cfl.required_lines(refs, set(), direction, tools)]
        assert (phrase in lines) is expected, name
    # no target known (other industries, no profile): still required
    assert phrase in [q for _, q in cfl.required_lines(refs, set(), "inbound", cfl.with_defaults({}))]


def test_real_estate_outbound_welcome_names_the_ai_and_adds_the_recording_line_only_when_recorded():
    base = PROFILE.replace("| Direction | Inbound |", "| Direction | Outbound |")
    ai = "Hello, this is Asha, an AI assistant calling from Lakeview Hospital. Is this a good time to talk?"
    assert cfl.welcome_from_profile(base, "real-estate") == ai
    rec = base + "\n| Calls recorded | yes |\n"
    named = "Hello, this is Asha, an AI assistant calling from Lakeview Hospital. "
    assert cfl.welcome_from_profile(rec, "real-estate") == (
        named + "This call may be recorded for quality purposes. Is this a good time to talk?")
    unnamed = rec.replace("| Assistant | Asha (female) |", "| Assistant | not given |")
    assert cfl.welcome_from_profile(unnamed, "real-estate") == (
        "Hello, I am an AI assistant calling from Lakeview Hospital. "
        "This call may be recorded for quality purposes. Is this a good time to talk?")
    no = base + "\n| Calls recorded | no |\n"
    assert cfl.welcome_from_profile(no, "real-estate") == ai
    assert "recorded" not in cfl.welcome_from_profile(rec, "banking")


def test_real_estate_tools_default_off_and_profile_can_turn_them_on():
    defaults = cfl.with_defaults({})
    assert (defaults["booking_tool"], defaults["send_link"], defaults["calls_recorded"]) == (False, False, False)
    tools = cfl.profile_tools("| Tools | booking_tool ON, send_link OFF, transfer |\n| Calls recorded | yes |\n")
    assert tools["booking_tool"] is True and tools["send_link"] is False and tools["calls_recorded"] is True
    assert cfl.profile_tools("| Tools | transfer |\n")["calls_recorded"] is False


def test_a_booking_off_line_is_required_by_default_and_a_booking_on_line_is_not(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text(
        '| R-01 | Needs `booking_tool`: say exactly "Booked line." |\n'
        '| R-02 | [booking_tool: off] say exactly "Callback line." |\n', encoding="utf-8")
    assert cfl.check("Callback line.", refs, numbers=[]) == []
    assert [q for _, q in cfl.check("Callback line.", refs, numbers=[], tools={"booking_tool": True})] == ["Booked line."]


def test_a_row_naming_several_settings_is_required_only_when_all_are_on(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text(
        '| R-01 | Link row (`send_link`, `confirmation_channels`): say exactly "Link line." |\n'
        '| R-02 | Single row (`send_link`): say exactly "Single line." |\n', encoding="utf-8")
    def needed(tools):
        return sorted(q for _, q in cfl.required_lines(refs, set(), "inbound", cfl.with_defaults(tools)))
    assert needed({"send_link": False, "confirmation_channels": True}) == []
    assert needed({"send_link": True, "confirmation_channels": False}) == ["Single line."]
    assert needed({"send_link": True, "confirmation_channels": True}) == ["Link line.", "Single line."]


def test_the_not_known_source_line_is_required_only_without_lead_source_wording(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    line = "I don't have that detail with me. Would you like us to stop calling you?"
    (refs / "core.md").write_text(f'SOURCE: otherwise say exactly "{line}" and wait.\n', encoding="utf-8")
    def needed(tools):
        return [q for _, q in cfl.required_lines(refs, set(), "outbound", cfl.with_defaults(tools))]
    assert needed({}) == [line]
    assert needed({"lead_source_wording": False}) == [line]
    assert needed({"lead_source_wording": True}) == []
    assert cfl.profile_tools("| Lead-source wording | the advice request form |")["lead_source_wording"] is True
    assert cfl.profile_tools("| Lead-source wording | not provided |")["lead_source_wording"] is False
    assert "lead_source_wording" not in cfl.profile_tools("| Tools | transfer |")


# ---- retail (DECISIONS 114) ----

RETAIL = ROOT / "industries" / "retail"


def test_retail_outbound_welcome_names_the_ai_and_adds_the_recording_line_only_when_recorded():
    base = PROFILE.replace("| Direction | Inbound |", "| Direction | Outbound |")
    named = "Hello, this is Asha, an AI assistant calling from Lakeview Hospital. "
    assert cfl.welcome_from_profile(base, "retail") == named + "Is this a good time to talk?"
    rec = base + "\n| Calls recorded | yes |\n"
    assert cfl.welcome_from_profile(rec, "retail") == named + "This call may be recorded for quality purposes. Is this a good time to talk?"
    unnamed = rec.replace("| Assistant | Asha (female) |", "| Assistant | not given |")
    assert cfl.welcome_from_profile(unnamed, "retail") == (
        "Hello, I am an AI assistant calling from Lakeview Hospital. "
        "This call may be recorded for quality purposes. Is this a good time to talk?")
    # other industries are unchanged: healthcare keeps its plain outbound welcome, banking never adds the recording line
    assert cfl.welcome_from_profile(rec, "healthcare") == "Hello, this is Asha calling from Lakeview Hospital. Is this a good time to talk?"
    assert "recorded" not in cfl.welcome_from_profile(rec, "banking")


def test_retail_settings_default_off_and_the_profile_reader_finds_them():
    defaults = cfl.with_defaults({})
    assert (defaults["order_lookup_tool"], defaults["stock_check_tool"]) == (False, False)
    tools = cfl.profile_tools("| Tools | order_lookup_tool ON, stock_check_tool OFF, send_link ON, transfer |\n"
                              "| Confirmation channels | whatsapp |\n| Contact-source wording | your recent order |\n")
    assert tools["order_lookup_tool"] is True and tools["stock_check_tool"] is False and tools["send_link"] is True
    assert tools["confirmation_channels"] is True and tools["channels"] == {"whatsapp"}
    assert tools["lead_source_wording"] is True
    assert cfl.profile_tools("| Contact-source wording | not given (the not-known line is used) |")["lead_source_wording"] is False


def retail_lines(profile_name, workflows, direction, extra=()):
    """The required lines the checker computes for a retail profile (no generation: the settings only)."""
    profile = RETAIL / "test-profiles" / profile_name
    text = profile.read_text(encoding="utf-8")
    tools = {}
    for key, value in cfl.profile_tools(text).items():
        tools.setdefault(key, value)
    tools.update(dict(extra))
    slots = cfl.profile_slots(text)
    return [q for _, q in cfl.required_lines(RETAIL, set(workflows), direction, cfl.with_defaults(tools), slots)]


def test_the_order_verification_lines_follow_the_lookup_tool_setting():
    off = "I am not able to look up order details on this call. I can arrange a callback for you."
    no_match = "I could not match those details, so I cannot share order information on this call. I can arrange a callback for you."
    lines_off = retail_lines("01-single-store-inbound.md", ["01", "03", "05", "06"], "inbound")
    assert off in lines_off and no_match not in lines_off
    lines_on = retail_lines("02-ecommerce-inbound-order-lookup.md", ["01", "02", "03", "05", "06"], "inbound")
    assert no_match in lines_on and off not in lines_on
    lines_electronics = retail_lines("03-electronics-service-inbound.md", ["01", "02", "03", "04", "05", "06"], "inbound")
    assert off in lines_electronics and no_match not in lines_electronics


def test_retail_outbound_only_lines_are_not_required_inbound_and_the_recording_line_follows_the_setting():
    inbound = retail_lines("02-ecommerce-inbound-order-lookup.md", ["01", "02", "03", "05", "06"], "inbound")
    wrong_person = "Sorry for the trouble. I can only speak with the person this call is for."
    assert wrong_person not in inbound
    recorded = "This call may be recorded for quality purposes."
    assert recorded in inbound  # profile 02: calls recorded yes
    outbound_no = retail_lines("05-outbound-feedback-no-assistant-name.md", ["07", "10"], "outbound")
    assert wrong_person in outbound_no and recorded not in outbound_no
    # profile 05 gives no contact-source wording, so the not-known line is required; profile 04 gives wording, so it is not
    not_known = "I don't have that detail with me. Would you like us to stop calling you?"
    assert not_known in outbound_no
    assert not_known not in retail_lines("04-outbound-order-update-with-name.md", ["07", "08"], "outbound")
    assert not_known not in retail_lines("06-outbound-abandoned-cart.md", ["07", "09"], "outbound")


def test_retail_link_and_confirmation_lines_follow_the_profile_channels():
    p06 = retail_lines("06-outbound-abandoned-cart.md", ["07", "09"], "outbound")
    assert "You will get the link on WhatsApp shortly." in p06
    assert "You will get the link on email shortly." not in p06
    assert "Would you like the link on WhatsApp or email?" not in p06
    p01 = retail_lines("01-single-store-inbound.md", ["01", "03", "05", "06"], "inbound")
    assert not any("You will get" in q for q in p01)  # no channel, no send link


def test_the_bank_line_carries_the_cybercrime_helpline_in_latin_digits():
    lines = retail_lines("01-single-store-inbound.md", ["01", "03", "05", "06"], "inbound")
    assert "Please contact your bank or card issuer right away, and report it on the cybercrime helpline, 1 9 3 0." in lines


# ---- education (DECISIONS 118) ----

EDUCATION = ROOT / "industries" / "education"


def education_lines(profile_name, workflows, direction, extra=()):
    """The required lines the checker computes for an education profile (no generation: the settings only)."""
    text = (EDUCATION / "test-profiles" / profile_name).read_text(encoding="utf-8")
    tools = {}
    for key, value in cfl.profile_tools(text).items():
        tools.setdefault(key, value)
    tools.update(dict(extra))
    slots = cfl.profile_slots(text)
    return [q for _, q in cfl.required_lines(EDUCATION, set(workflows), direction, cfl.with_defaults(tools), slots)]


def test_education_outbound_welcome_names_the_ai_and_adds_the_recording_line_only_when_recorded():
    base = PROFILE.replace("| Direction | Inbound |", "| Direction | Outbound |")
    named = "Hello, this is Asha, an AI assistant calling from Lakeview Hospital. "
    assert cfl.welcome_from_profile(base, "education") == named + "Is this a good time to talk?"
    rec = base + "\n| Calls recorded | yes |\n"
    assert cfl.welcome_from_profile(rec, "education") == named + "This call may be recorded for quality purposes. Is this a good time to talk?"
    unnamed = rec.replace("| Assistant | Asha (female) |", "| Assistant | not given |")
    assert cfl.welcome_from_profile(unnamed, "education") == (
        "Hello, I am an AI assistant calling from Lakeview Hospital. "
        "This call may be recorded for quality purposes. Is this a good time to talk?")
    inbound = PROFILE.replace("| Direction | Outbound |", "| Direction | Inbound |")
    assert cfl.welcome_from_profile(inbound, "education").startswith("Thank you for calling")


def test_education_settings_default_and_the_profile_reader_finds_them():
    defaults = cfl.with_defaults({})
    assert (defaults["booking_tool"], defaults["send_link"], defaults["calls_recorded"]) == (False, False, False)
    assert defaults["callback_setting"] is True
    tools = cfl.profile_tools("| Tools | change_language, transfer. booking_tool ON, send_link OFF, callback ON |\n"
                              "| Confirmation channels | whatsapp |\n| Calls recorded | yes |\n")
    assert tools["booking_tool"] is True and tools["send_link"] is False and tools["callback_setting"] is True
    assert tools["calls_recorded"] is True and tools["channels"] == {"whatsapp"}
    assert cfl.profile_tools("| Tools | transfer. callback OFF |")["callback_setting"] is False
    assert cfl.profile_tools("| Tools | transfer |")["callback_setting"] is True


def test_education_booking_and_callback_lines_follow_the_settings():
    failed = "I am sorry, that did not work. Our team will call you to confirm."
    callback_line = "Our team can call back during office hours."
    wrong_person = "Sorry for the trouble. I can only speak with the person this call is for."
    assert failed in education_lines("03-coaching-inbound-demo-booking.md", ["01", "02", "04", "05", "06"], "inbound")
    p05 = education_lines("05-outbound-fee-reminder-no-assistant-name.md", ["09", "11"], "outbound")
    assert wrong_person in p05 and callback_line in p05
    p05_off = education_lines("05-outbound-fee-reminder-no-assistant-name.md", ["09", "11"], "outbound", extra=[("callback_setting", False)])
    assert wrong_person in p05_off and callback_line not in p05_off
    assert wrong_person not in education_lines("01-school-inbound.md", ["01", "02", "03", "05", "06"], "inbound")


def test_education_recording_links_and_source_lines_follow_the_profile():
    recorded = "This call may be recorded for quality purposes."
    assert recorded in education_lines("02-college-inbound.md", ["01", "02", "03", "05", "06"], "inbound")
    assert recorded not in education_lines("01-school-inbound.md", ["01", "02", "03", "05", "06"], "inbound")
    p01 = education_lines("01-school-inbound.md", ["01", "02", "03", "05", "06"], "inbound")
    assert "Would you like the link on WhatsApp or email?" in p01
    p03 = education_lines("03-coaching-inbound-demo-booking.md", ["01", "02", "04", "05", "06"], "inbound")
    assert "You will get the link on WhatsApp shortly." in p03 and "You will get the link on email shortly." not in p03
    p02 = education_lines("02-college-inbound.md", ["01", "02", "03", "05", "06"], "inbound")
    assert not any("You will get" in q for q in p02)
    not_known = "I don't have that detail with me. Would you like us to stop calling you?"
    assert not_known in education_lines("05-outbound-fee-reminder-no-assistant-name.md", ["09", "11"], "outbound")
    assert not_known not in education_lines("04-edtech-outbound-counselling.md", ["09", "12"], "outbound")


def test_education_safety_lines_are_required_and_the_pickup_line_only_with_its_workflow():
    lines = education_lines("06-preschool-inbound-pickup.md", ["01", "02", "05", "06", "08"], "inbound")
    for needed in ("Call 1 1 2 right now.", "Childline: 1 0 9 8.", "Tele-MANAS: 1 4 4 1 6. Emergency: 1 0 8 or 1 1 2.",
                   "For privacy, I cannot share a student's details on this call.",
                   "I cannot confirm or change who may pick up a child on this call. I have noted your request for our staff.",
                   "Please contact your bank or card issuer right away, and report it on the cybercrime helpline, 1 9 3 0."):
        assert needed in lines
    pickup = "I cannot confirm or change who may pick up a child on this call. I have noted your request for our staff."
    assert pickup not in education_lines("01-school-inbound.md", ["01", "02", "03", "05", "06"], "inbound")


# ---- logistics (DECISIONS 124) ----

LOGISTICS = ROOT / "industries" / "logistics"


def logistics_lines(profile_name, workflows, direction):
    """The required lines the checker computes for a logistics profile (no generation: the settings only)."""
    text = (LOGISTICS / "test-profiles" / profile_name).read_text(encoding="utf-8")
    tools = dict(cfl.profile_tools(text))
    slots = cfl.profile_slots(text)
    return [q for _, q in cfl.required_lines(LOGISTICS, set(workflows), direction, cfl.with_defaults(tools), slots)]


def test_logistics_tools_default_off_and_the_profile_reader_finds_them():
    defaults = cfl.with_defaults({})
    for name in ("tracking_lookup_tool", "reschedule_tool", "pickup_request_tool", "address_change_tool"):
        assert defaults[name] is False
    tools = cfl.profile_tools("| Tools | tracking_lookup_tool ON, reschedule_tool ON, pickup_request_tool OFF, address_change_tool ON, transfer |")
    assert tools["tracking_lookup_tool"] and tools["reschedule_tool"] and tools["address_change_tool"]
    assert tools["pickup_request_tool"] is False and tools["booking_tool"] is False  # pickup_request_tool is not read as booking_tool


def test_logistics_outbound_welcome_names_the_ai_and_puts_the_recording_line_before_the_question():
    text = (LOGISTICS / "test-profiles" / "04-outbound-delivery-update-named-recorded.md").read_text(encoding="utf-8")
    assert cfl.welcome_from_profile(text, "logistics") == (
        "Hello, this is Nisha, an AI assistant calling from Quickdrop Parcel Test. "
        "This call may be recorded for quality purposes. Is this a good time to talk?")
    unnamed = (LOGISTICS / "test-profiles" / "05-outbound-pickup-cod-no-assistant-name.md").read_text(encoding="utf-8")
    assert cfl.welcome_from_profile(unnamed, "logistics") == "Hello, I am an AI assistant calling from Swift Lane Couriers Test. Is this a good time to talk?"


def test_the_shipment_verification_lines_follow_the_tracking_lookup_setting():
    off = "I am not able to look up shipment details on this call. I can arrange a callback for you."
    not_verified = "I could not verify those details, so I cannot share shipment information on this call. I can arrange a callback for you."
    lines_off = logistics_lines("01-courier-inbound-tools-off.md", ["01", "02", "03", "04", "05"], "inbound")
    assert off in lines_off and not_verified not in lines_off
    lines_on = logistics_lines("02-ecommerce-courier-inbound-lookup-on.md", ["01", "02", "03", "04", "05"], "inbound")
    assert not_verified in lines_on and off not in lines_on
    lines_freight = logistics_lines("03-freight-forwarder-inbound.md", ["06", "05", "04"], "inbound")
    assert not_verified in lines_freight and off not in lines_freight


def test_logistics_scam_block_stop_line_and_bank_line_are_always_required_inbound():
    for name, wfs in (("01-courier-inbound-tools-off.md", ["01", "02", "03", "04", "05"]), ("06-warehouse-inbound-client-requests-refused.md", ["06", "05"])):
        lines = logistics_lines(name, wfs, "inbound")
        for q in ("Please be careful. We never ask for a payment, an OTP or any details to release a parcel. Do not share them with anyone.",
                  "I cannot confirm whether that call was from us.",
                  "Please report this quickly on the cybercrime helpline, 1 9 3 0.",
                  "Please contact your bank or card issuer right away, and report it on the cybercrime helpline, 1 9 3 0.",
                  "Please do not share that. I do not need it on this call.",
                  "Tele-MANAS: 1 4 4 1 6. Emergency: 1 0 8 or 1 1 2.", "Call 1 1 2 right now.", "Our team will call you back."):
            assert q in lines, (name, q)


def test_logistics_team_phrase_is_not_required_without_a_transfer_target():
    team = "I'll connect you to our team."
    assert team not in logistics_lines("06-warehouse-inbound-client-requests-refused.md", ["06", "05"], "inbound")
    assert team in logistics_lines("01-courier-inbound-tools-off.md", ["01", "02", "03", "04", "05"], "inbound")


def test_logistics_outbound_only_lines_and_the_source_and_recording_settings():
    inbound = logistics_lines("01-courier-inbound-tools-off.md", ["01", "02", "03", "04", "05"], "inbound")
    wrong_person = "Sorry for the trouble. I can only speak with the person this call is for."
    assert wrong_person not in inbound
    recorded = "This call may be recorded for quality purposes."
    assert recorded not in inbound  # profile 01: calls recorded no
    assert recorded in logistics_lines("02-ecommerce-courier-inbound-lookup-on.md", ["01", "02", "03", "04", "05"], "inbound")
    not_known = "I don't have that detail with me. Would you like us to stop calling you?"
    out05 = logistics_lines("05-outbound-pickup-cod-no-assistant-name.md", ["07", "09"], "outbound")
    assert wrong_person in out05 and not_known in out05 and recorded not in out05
    assert not_known not in logistics_lines("04-outbound-delivery-update-named-recorded.md", ["07", "08"], "outbound")


def test_off_skips_a_rule_and_its_repeats_in_other_rows(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text('| R-01 | say exactly "Keep me." |\n', encoding="utf-8")
    (refs / "workflows" / "01-a.md").write_text(
        '| R-52 | On a cancel request say exactly "I have noted your request." |\n'
        'Step 3: say exactly "I have noted your request." then ask the day.\n', encoding="utf-8")
    out = "Keep me."
    assert [q for _, q in cfl.check(out, refs, numbers=["01"])] == ["I have noted your request."]
    assert cfl.check(out, refs, numbers=["01"], tools={cfl.SKIP_RULES: {"R-52"}}) == []
    assert cfl.main([str(tmp_path / "o.md"), "--references", str(refs), "--workflows", "01", "--off", "cancel,R-52"]) == 2  # no such file


def test_off_confirmation_skips_channel_lines_only_when_booking_is_off(tmp_path):
    refs = tmp_path / "references"
    (refs / "workflows").mkdir(parents=True)
    (refs / "core.md").write_text('| R-18 | Flow in {{var.confirmation_channels}}: say exactly "Is this number on WhatsApp?" |\n| R-01 | say exactly "Keep me." |\n', encoding="utf-8")
    out = tmp_path / "o.md"
    out.write_text("Keep me.", encoding="utf-8")
    assert cfl.main([str(out), "--references", str(refs), "--tool", "confirmation_channels=whatsapp"]) == 1
    assert cfl.main([str(out), "--references", str(refs), "--tool", "confirmation_channels=whatsapp", "--off", "confirmation"]) == 0
    assert cfl.main([str(out), "--references", str(refs), "--tool", "booking_tool=on", "--off", "confirmation"]) == 2
