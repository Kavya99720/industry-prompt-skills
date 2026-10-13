import io
import json

import pytest

import check_variables as cv

VARS = {
    "variables": [
        {"name": n, "source": "Fixed", "description": "d", "example": "e", "industries": ["all"]}
        for n in ("agent_name", "company_name", "roster", "business_phone", "minors_may_book_alone")
    ]
}


@pytest.fixture
def repo(tmp_path):
    (tmp_path / "docs" / "shared").mkdir(parents=True)
    (tmp_path / "docs" / "shared" / "variables.json").write_text(json.dumps(VARS), encoding="utf-8")
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "denylist.txt").write_text("# private\nAcme Hospital\nRavi Kumar\n", encoding="utf-8")
    (tmp_path / "outputs").mkdir()
    return tmp_path


def scan(repo, text, fix=False, name="p.md"):
    f = repo / "outputs" / name
    f.write_text(text, encoding="utf-8")
    out = io.StringIO()
    result = cv.run(repo, ["outputs"], repo / "docs/shared/variables.json",
                    repo / "scripts/denylist.txt", fix=fix, out=out)
    return result, f, out.getvalue()


def problems(issues):
    return [i.problem for i in issues]


def test_clean_text_passes(repo):
    (errors, warns, _, _), _, _ = scan(repo, "You are {{var.agent_name}}. Doctors: {{var.roster}}.\n")
    assert (errors, warns) == (0, 0)


def test_unknown_var_fails_with_suggestion(repo):
    (errors, _, _, issues), _, out = scan(repo, "Call {{var.business_phones}}.\n")
    assert errors == 1
    assert "unknown variable" in problems(issues)[0]
    assert "did you mean {{var.business_phone}}" in out


@pytest.mark.parametrize("bad", ["{{hospital_name}}", "{{persona_name}}", "{{doctors}}", "@company_name", "@agent_name"])
def test_wrong_styles_fail(repo, bad):
    (errors, _, _, issues), _, out = scan(repo, f"Hello {bad} here.\n")
    assert errors == 1
    assert "wrong variable style" in problems(issues)[0]
    assert "{{var." in out


def test_unknown_old_name_has_no_autofix_but_is_reported(repo):
    (errors, _, fixed, _), f, _ = scan(repo, "Use {{transfer_target}}.\n", fix=True)
    assert errors == 1 and fixed == 0
    assert "{{transfer_target}}" in f.read_text(encoding="utf-8")


def test_fix_rewrites_known_names(repo):
    text = "You are {{persona_name}} of {{hospital_name}}. See {{doctors}} or @agent_name. Flag {{minors_may_book_alone}}.\n"
    (errors, _, fixed, _), f, _ = scan(repo, text, fix=True)
    assert errors == 0 and fixed == 5
    assert f.read_text(encoding="utf-8") == (
        "You are {{var.agent_name}} of {{var.company_name}}. See {{var.roster}} or {{var.agent_name}}. "
        "Flag {{var.minors_may_book_alone}}.\n"
    )


def test_email_address_is_not_a_variable(repo):
    (errors, _, _, _), _, _ = scan(repo, "Write to help@company_name.example\n")
    assert errors == 0


def test_denylist_name_fails(repo):
    (errors, _, _, issues), _, _ = scan(repo, "Dr. ravi kumar sits on Monday.\n")
    assert errors == 1 and "denylist" in problems(issues)[0]


def test_denylist_matches_whole_words_only(repo):
    (errors, _, _, _), _, _ = scan(repo, "Acme Hospitality is fine.\n")
    assert errors == 0


@pytest.mark.parametrize("phone", ["9876543210", "98765 43210", "+91 9876543210"])
def test_phone_number_fails(repo, phone):
    (errors, _, _, issues), _, _ = scan(repo, f"Call {phone} now.\n")
    assert errors == 1 and "phone" in problems(issues)[0]


def test_emergency_numbers_are_not_phone_numbers(repo):
    (errors, _, _, _), _, _ = scan(repo, "Call 108 or 112, or 14416 for Tele-MANAS, or 1930.\n")
    assert errors == 0


def test_pin_code_address_fails(repo):
    (errors, _, _, issues), _, _ = scan(repo, "Main Road, Bengaluru 560001\n")
    assert errors == 1 and "PIN" in problems(issues)[0]


@pytest.mark.parametrize("line,warns", [
    ("Welcome message: Hello, this is {{var.agent_name}} from {{var.company_name}}.", 0),
    ("Closing: Thank you for calling {{var.company_name}}.", 0),
    ("If asked, say: I'm an AI assistant for {{var.company_name}}.", 0),
    ("Tell the caller that {{var.company_name}} has 50 beds.", 1),
])
def test_company_name_usage_warns(repo, line, warns):
    (errors, got, _, _), _, _ = scan(repo, line + "\n")
    assert errors == 0 and got == warns


def test_ignore_marker_skips_a_line(repo):
    (errors, _, _, _), _, _ = scan(repo, "Never write {{hospital_name}}. check_variables: ignore\n")
    assert errors == 0


def test_missing_denylist_skips_client_check_but_not_phones(repo):
    (repo / "scripts" / "denylist.txt").unlink()
    (errors, _, _, _), _, out = scan(repo, "Acme Hospital 9876543210\n")
    assert errors == 1 and "denylist.txt not found" in out


def test_main_exit_codes(repo):
    (repo / "outputs" / "a.md").write_text("ok {{var.roster}}\n", encoding="utf-8")
    args = ["--root", str(repo), "--paths", "outputs"]
    assert cv.main(args) == 0
    (repo / "outputs" / "b.md").write_text("bad {{doctors}}\n", encoding="utf-8")
    assert cv.main(args) == 1
    assert cv.main(args + ["--fix"]) == 0


def test_real_repo_variables_json_is_well_formed():
    known = cv.load_variables(cv.ROOT / "docs" / "shared" / "variables.json")
    for required in ("agent_name", "agent_gender", "default_language", "business_hours", "business_phone",
                     "clinic_address", "company_name", "now_local", "roster",
                     "emergency_signs_extra", "minors_may_book_alone"):
        assert required in known


def test_results_folders_are_skipped(repo):
    res = repo / "industries" / "demo" / "results" / "2026-10-08"
    res.mkdir(parents=True)
    (res / "x.md").write_text("bad {{doctors}} 9876543210" + chr(10), encoding="utf-8")
    kept = repo / "industries" / "demo" / "brief.md"
    kept.write_text("bad {{doctors}}" + chr(10), encoding="utf-8")
    out = io.StringIO()
    errors, _, _, issues = cv.run(repo, ["industries"], repo / "docs/shared/variables.json",
                                  repo / "scripts/denylist.txt", out=out)
    assert errors == 1 and all("results" not in i.path for i in issues)


def test_sentence_tests_folders_are_skipped_but_a_named_file_is_still_checked(repo):
    st = repo / "industries" / "demo" / "sentence-tests"
    st.mkdir(parents=True)
    bad = st / "t.md"
    bad.write_text("bad {{doctors}} Dr. Ramesh Kumar 9876543210" + chr(10), encoding="utf-8")
    kept = repo / "industries" / "demo" / "brief.md"
    kept.write_text("bad {{doctors}}" + chr(10), encoding="utf-8")
    deep = repo / ".claude" / "skills" / "x-prompt-writer" / "sentence-tests"
    deep.mkdir(parents=True)
    (deep / "u.md").write_text("bad {{doctors}}" + chr(10), encoding="utf-8")
    out = io.StringIO()
    errors, _, _, issues = cv.run(repo, ["industries", ".claude/skills"], repo / "docs/shared/variables.json",
                                  repo / "scripts/denylist.txt", out=out)
    assert errors == 1 and all("sentence-tests" not in i.path for i in issues)
    out = io.StringIO()
    named, _, _, named_issues = cv.run(repo, ["industries/demo/sentence-tests/t.md"], repo / "docs/shared/variables.json",
                                       repo / "scripts/denylist.txt", out=out)
    assert named >= 1 and any("sentence-tests" in i.path for i in named_issues)


def make_inline_industry(repo, name="demo"):
    d = repo / "industries" / name
    d.mkdir(parents=True, exist_ok=True)
    (d / "variables.json").write_text(json.dumps({
        "inline_values": True,
        "variables": [{"name": n, "source": "Built in", "description": "d", "example": "e", "industries": [name]}
                      for n in ("now_local", "roster")]}), encoding="utf-8")
    (repo / "outputs" / name).mkdir(parents=True, exist_ok=True)
    return d


def run_on(repo, rel):
    out = io.StringIO()
    errors, warns, _, issues = cv.run(repo, [rel], repo / "docs/shared/variables.json", repo / "scripts/denylist.txt", out=out)
    return errors, issues


GOOD_OUTPUT = (
    "=== INSTRUCTIONS ===\n"
    "Thank you for calling Sunrise Clinic. This is Asha. How can I help you?\n"
    "The clinic is at 12 Park Road, Indiranagar, Bengaluru 560038 and the phone is 9876543210. Open 9 AM to 8 PM.\n"
    "Say Doctor <name> is available from <start> to <end>. Today is {{var.now_local}}.\n"
    "{{var.roster}}\n"
    "=== DRAFT NOTES ===\n"
    "- Ask the customer about <business name> and {{var.business_hours}}; call 9876543211.\n"
)


def test_generated_instructions_of_an_inline_industry_may_print_business_facts(repo):
    make_inline_industry(repo)
    (repo / "outputs" / "demo" / "t.md").write_text(GOOD_OUTPUT, encoding="utf-8")
    errors, issues = run_on(repo, "outputs/demo/t.md")
    assert errors == 0, [str(i) for i in issues]


def test_inline_industry_instructions_reject_other_variables_and_unresolved_slots(repo):
    make_inline_industry(repo)
    bad = GOOD_OUTPUT.replace("Open 9 AM to 8 PM.", "Open {{var.business_hours}}. Call <phone>. Welcome to <business name>.")
    (repo / "outputs" / "demo" / "t.md").write_text(bad, encoding="utf-8")
    errors, issues = run_on(repo, "outputs/demo/t.md")
    problems_ = problems(issues)
    assert errors == 3
    assert any("unknown variable {{var.business_hours}}" in p_ for p_ in problems_)
    assert any("unresolved placeholder <phone>" in p_ for p_ in problems_)
    assert any("unresolved placeholder <business name>" in p_ for p_ in problems_)


def test_inline_industry_still_checks_its_skill_sources_and_other_industries(repo):
    d = make_inline_industry(repo)
    (d / "core.md").write_text("Call 9876543210 and use {{var.agent_name}}.\n", encoding="utf-8")
    errors, issues = run_on(repo, "industries/demo/core.md")
    assert errors == 2 and any("phone number" in p_ for p_ in problems(issues)) and any("unknown variable" in p_ for p_ in problems(issues))
    other = repo / "industries" / "plain"
    other.mkdir()
    (repo / "outputs" / "plain").mkdir()
    (repo / "outputs" / "plain" / "t.md").write_text(GOOD_OUTPUT.replace("{{var.roster}}", "{{var.agent_name}}"), encoding="utf-8")
    errors, issues = run_on(repo, "outputs/plain/t.md")
    assert errors >= 1 and any("phone number" in p_ for p_ in problems(issues))


@pytest.mark.parametrize("line", ["Say Doctor Rao, is that right?", "Ask Dr. Shah first.", "Dr Kumar is in."])
def test_example_person_names_fail(repo, line):
    (errors, _, _, issues), _, _ = scan(repo, line + chr(10))
    assert errors == 1 and "person name" in problems(issues)[0]


@pytest.mark.parametrize("line", ["Say Doctor <name>, is that right?", "Doctor A sits on Monday.", "Doctor On leave: callback.",
                                  "Doctor status is shown.", "DOCTOR LIST: only these doctors exist.", "The doctor said so."])
def test_placeholders_and_status_words_are_not_person_names(repo, line):
    (errors, _, _, _), _, _ = scan(repo, line + chr(10))
    assert errors == 0


def test_person_names_allowed_in_test_profiles_and_eval_json(repo):
    ind = repo / "industries" / "demo"
    (ind / "test-profiles").mkdir(parents=True)
    (ind / "test-profiles" / "01-a.md").write_text("Doctor Rao sits Monday." + chr(10), encoding="utf-8")
    (ind / "eval.json").write_text('{"probe": "This is Doctor Test from the hospital."}', encoding="utf-8")
    (ind / "core.md").write_text("Say Doctor Rao." + chr(10), encoding="utf-8")
    out = io.StringIO()
    errors, _, _, issues = cv.run(repo, ["industries"], repo / "docs/shared/variables.json",
                                  repo / "scripts/denylist.txt", out=out)
    assert errors == 1 and issues[0].path.endswith("core.md")


def test_industry_custom_variables_are_valid_only_in_that_industry(repo):
    for slug in ("demo", "other"):
        (repo / "industries" / slug).mkdir(parents=True, exist_ok=True)
        (repo / "industries" / slug / "core.md").write_text("Use {{var.refund_window}} here." + chr(10), encoding="utf-8")
    (repo / "industries" / "demo" / "variables.json").write_text(
        json.dumps({"variables": [{"name": "refund_window"}]}), encoding="utf-8")
    out = io.StringIO()
    errors, _, _, issues = cv.run(repo, ["industries"], repo / "docs/shared/variables.json",
                                  repo / "scripts/denylist.txt", out=out)
    assert errors == 1 and issues[0].path == "industries/other/core.md"


def test_industry_variables_apply_to_the_skill_folder(repo):
    (repo / "industries" / "demo").mkdir(parents=True)
    (repo / "industries" / "demo" / "variables.json").write_text(
        json.dumps({"variables": [{"name": "refund_window"}]}), encoding="utf-8")
    skill = repo / ".claude" / "skills" / "demo-prompt-writer"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("Say {{var.refund_window}}." + chr(10), encoding="utf-8")
    out = io.StringIO()
    errors, _, _, _ = cv.run(repo, [".claude/skills"], repo / "docs/shared/variables.json",
                             repo / "scripts/denylist.txt", out=out)
    assert errors == 0
