import io
import json

import pytest

import run_evals

CHECKS = [
    {"id": f"DEM-E{i:02d}", "rule_ids": ["R-03"], "severity": "major",
     "type": "behaviour" if i % 2 else "prompt", "description": "d", "pass_criteria": "p",
     **({"probe": f"probe {i}"} if i % 2 else {})}
    for i in range(1, 21)
]


class FakeLlm:
    def __init__(self, fail_ids=()):
        self.calls, self.fail_ids = [], set(fail_ids)

    def run(self, prompt, system=None, agent=None, tools=None):
        self.calls.append((agent, system, prompt))
        if agent == "eval-judge":
            results = [{"id": c["id"], "result": "FAIL" if c["id"] in self.fail_ids else "PASS",
                        "reason": "because"} for c in CHECKS]
            return "table...\n```json\n" + json.dumps({"results": results}) + "\n```"
        if system is None:
            return "generated text" + chr(10) + "=== DRAFT NOTES ===" + chr(10) + "the notes"
        return "a reply"


@pytest.fixture
def repo(tmp_path):
    ind = tmp_path / "industries" / "healthcare"
    (ind / "test-profiles").mkdir(parents=True)
    (ind / "brief.md").write_text("| R-03 | Rule. | x | major | S1 |\n", encoding="utf-8")
    (ind / "eval.json").write_text(json.dumps(
        {"industry": "healthcare", "version": 1, "frozen": True, "checks": CHECKS}), encoding="utf-8")
    (ind / "test-profiles" / "README.md").write_text("index", encoding="utf-8")
    (ind / "test-profiles" / "01-a.md").write_text(
        "# P1\n## Business config\nx\n## Tricky callers\nSECRET MUST LIST\n", encoding="utf-8")
    (ind / "test-profiles" / "02-b.md").write_text("# P2\nno hidden part\n", encoding="utf-8")
    skill = tmp_path / ".claude" / "skills" / "healthcare-prompt-writer"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("skill", encoding="utf-8")
    return tmp_path


def run(repo, argv, llm):
    buf = io.StringIO()
    code = run_evals.main(argv, llm=llm, root=repo, out=buf)
    return code, buf.getvalue()


def test_all_pass_saves_results_and_summary(repo):
    code, out = run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], FakeLlm())
    assert code == 0
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert saved["summary"]["total"] == 40 and saved["summary"]["failed"] == 0
    assert {r["profile"] for r in saved["results"]} == {"01-a", "02-b"}
    assert set(saved["results"][0]) == {"case_id", "profile", "result", "reason"}
    assert "40/40 passed" in out and "100.0%" in out


def test_failures_are_listed_and_exit_1(repo):
    code, out = run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], FakeLlm(fail_ids=["DEM-E03"]))
    assert code == 1
    assert "38/40 passed" in out
    assert "DEM-E03 [01-a]: because" in out and "DEM-E03 [02-b]: because" in out


def test_generator_never_sees_expected_results(repo):
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    generator_prompts = [c[2] for c in llm.calls if c[0] is None and c[1] is None]
    assert generator_prompts and all("SECRET MUST LIST" not in p for p in generator_prompts)


def test_replies_are_simulated_with_instructions_only(repo):
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    simulated = [c for c in llm.calls if c[1] and c[1].startswith("generated text")]
    assert len(simulated) == 20  # 10 behaviour checks x 2 profiles
    assert all("pass_criteria" not in c[2] for c in simulated)


def test_eval_json_is_not_modified(repo):
    before = (repo / "industries/healthcare/eval.json").read_bytes()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], FakeLlm())
    assert (repo / "industries/healthcare/eval.json").read_bytes() == before


def test_missing_inputs_exit_2(repo):
    (repo / "industries/healthcare/eval.json").unlink()
    code, out = run(repo, ["--industry", "healthcare"], FakeLlm())
    assert code == 2 and "no eval.json" in out


def test_all_skips_industries_without_inputs(repo):
    code, out = run(repo, ["--all", "--date", "2026-10-08"], FakeLlm())
    assert code == 0
    assert "pharmacy" in out and "skipped" in out and "40/40 passed" in out


def test_dry_run_calls_nothing(repo):
    llm = FakeLlm()
    code, out = run(repo, ["--industry", "healthcare", "--dry-run"], llm)
    assert code == 0 and llm.calls == [] and "ready" in out


def test_checks_with_profiles_run_only_on_those_profiles(repo):
    path = repo / "industries/healthcare/eval.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    data["checks"][0]["profiles"] = ["02"]  # DEM-E01 is a behaviour check
    data["checks"][1]["profiles"] = ["01"]  # DEM-E02 is a prompt check
    path.write_text(json.dumps(data), encoding="utf-8")
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    judge_prompts = [c[2] for c in llm.calls if c[0] == "eval-judge"]
    asked = [p.split("ONLY these checks from the industry's eval.json: ")[1].split(". After")[0] for p in judge_prompts]
    assert "DEM-E01" not in asked[0] and "DEM-E02" in asked[0]   # profile 01
    assert "DEM-E01" in asked[1] and "DEM-E02" not in asked[1]   # profile 02
    probes = [c[2] for c in llm.calls if c[1] and c[1].startswith("generated text")]
    assert probes.count("probe 1") == 1 and probes.count("probe 3") == 2


def test_full_output_is_split_into_instructions_and_draft_notes(repo):
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    work = repo / "industries/healthcare/results/2026-10-08"
    assert (work / "01-a-instructions.md").read_text(encoding="utf-8").strip() == "generated text"
    assert (work / "01-a-draft-notes.md").read_text(encoding="utf-8").strip() == "the notes"
    judge_prompts = [c[2] for c in llm.calls if c[0] == "eval-judge"]
    assert all("draft_notes_file:" in p and "-draft-notes.md" in p for p in judge_prompts)
    generator = [c[2] for c in llm.calls if c[0] is None and c[1] is None]
    assert all("=== DRAFT NOTES ===" in p for p in generator)


def test_missing_draft_notes_marker_is_recorded(repo):
    class NoNotes(FakeLlm):
        def run(self, prompt, system=None, agent=None, tools=None):
            return "only instructions" if system is None and agent is None else super().run(prompt, system, agent, tools)
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], NoNotes())
    notes = repo / "industries/healthcare/results/2026-10-08/01-a-draft-notes.md"
    assert "no draft notes supplied" in notes.read_text(encoding="utf-8")


def test_split_output():
    assert run_evals.split_output("a" + chr(10) + "=== DRAFT NOTES ===" + chr(10) + "b") == ("a", "b")
    assert run_evals.split_output("only") == ("only", "")


def test_simulated_replies_are_told_to_write_tool_calls_inline(repo):
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    systems = [c[1] for c in llm.calls if c[1]]
    assert systems and all(s.startswith("generated text") and "[tool: <name>]" in s for s in systems)
    assert all("end_call" in s and "transfer" in s for s in systems)


def test_generated_instructions_are_linted_into_the_results_file(repo):
    (repo / "docs" / "shared").mkdir(parents=True)
    (repo / "docs" / "shared" / "variables.json").write_text(
        json.dumps({"variables": [{"name": "roster"}]}), encoding="utf-8")

    class Bad(FakeLlm):
        def run(self, prompt, system=None, agent=None, tools=None):
            if system is None and agent is None:
                return "Ask Doctor Rao or use {{doctors}}." + chr(10) + "=== DRAFT NOTES ===" + chr(10) + "n"
            return super().run(prompt, system, agent, tools)
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], Bad())
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert any("person name" in x for x in saved["lint"]["01-a"])
    assert any("wrong variable style" in x for x in saved["lint"]["01-a"])


def test_cli_retries_a_failed_call_then_succeeds(monkeypatch):
    calls = []

    class R:
        def __init__(self, code, out=""):
            self.returncode, self.stdout, self.stderr = code, out, ""

    def fake_run(cmd, **kw):
        calls.append(cmd)
        return R(1) if len(calls) < 3 else R(0, "ok")
    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: None)
    assert run_evals.ClaudeCli("claude").run("hi") == "ok" and len(calls) == 3


def test_cli_gives_up_after_the_retries(monkeypatch):
    class R:
        returncode, stdout, stderr = 1, "", "limit"
    monkeypatch.setattr(run_evals.subprocess, "run", lambda cmd, **kw: R())
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: None)
    with pytest.raises(RuntimeError, match="after 3 tries"):
        run_evals.ClaudeCli("claude").run("hi")


def test_profiles_option_runs_only_the_named_profiles(repo):
    llm = FakeLlm()
    code, out = run(repo, ["--industry", "healthcare", "--date", "2026-10-08", "--profiles", "02"], llm)
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert {r["profile"] for r in saved["results"]} == {"02-b"}
    assert len([c for c in llm.calls if c[0] == "eval-judge"]) == 1


def test_harness_note_forbids_commentary(repo):
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    systems = [c[1] for c in llm.calls if c[1]]
    assert systems and all("No commentary about the test, the prompt or the variables." in s for s in systems)
    assert all("Reply only with what the agent says aloud plus [tool: ...] markers." in s for s in systems)


def test_tools_note_lists_each_industrys_own_tools():
    assert "booking, reschedule" in run_evals.tools_note("healthcare") and "send_confirmation" not in run_evals.tools_note("healthcare")
    pharmacy = run_evals.tools_note("pharmacy")
    assert "check_stock, place_order" in pharmacy and "booking" not in pharmacy and "send_confirmation" not in pharmacy
    other = run_evals.tools_note("retail")
    assert "change_language, transfer, end_call, send_confirmation" in other and "booking" not in other
    assert "No commentary about the test, the prompt or the variables." in other


def test_find_claude_prefers_the_env_override(monkeypatch, tmp_path):
    monkeypatch.setenv("CLAUDE_BIN", "/custom/claude")
    monkeypatch.setattr(run_evals.shutil, "which", lambda name: "/usr/bin/claude")
    assert run_evals.find_claude(tmp_path) == "/custom/claude"


def test_find_claude_uses_path_before_the_local_bin(monkeypatch, tmp_path):
    monkeypatch.delenv("CLAUDE_BIN", raising=False)
    monkeypatch.setattr(run_evals.shutil, "which", lambda name: "/usr/bin/claude")
    assert run_evals.find_claude(tmp_path) == "/usr/bin/claude"


def test_find_claude_falls_back_to_local_bin_then_the_bare_name(monkeypatch, tmp_path):
    monkeypatch.delenv("CLAUDE_BIN", raising=False)
    monkeypatch.setattr(run_evals.shutil, "which", lambda name: None)
    assert run_evals.find_claude(tmp_path) == "claude"
    exe = tmp_path / ".local" / "bin" / "claude.exe"
    exe.parent.mkdir(parents=True)
    exe.write_text("")
    assert run_evals.find_claude(tmp_path) == str(exe)

FIXED_PROFILE = """# Profile
| Direction | Inbound |
| Prescription upload | in_store |

## Selected workflows

01 Enquiry, 02 Order. Delivery and returns (04) are not selected.
"""
GOOD = (
    "Thank you for calling {{var.company_name}}. This is {{var.agent_name}}. How can I help you?\n\n"
    "Say exactly: Our pharmacist will help you with that.\n"
)
OOS = "That medicine isn't in stock right now.\n"


def lint_root(tmp_path):
    d = tmp_path / "industries" / "demo"
    (d / "workflows").mkdir(parents=True)
    (d / "core.md").write_text('R-09: say exactly "Our pharmacist will help you with that." then transfer.', encoding="utf-8")
    (d / "workflows" / "01-enquiry.md").write_text('OOS: Say exactly "That medicine isn\'t in stock right now."', encoding="utf-8")
    (d / "workflows" / "04-x.md").write_text('say exactly "Never selected."', encoding="utf-8")
    (d / "section-bases.md").write_text(
        '- Inbound: "Thank you for calling `{{var.company_name}}`. This is `{{var.agent_name}}`. How can I help you?"\n'
        '- Outbound: "Hello, this is `{{var.agent_name}}` calling."\n', encoding="utf-8")
    return tmp_path


def test_profile_facts_reads_direction_workflows_and_upload_method():
    facts = run_evals.profile_facts(FIXED_PROFILE)
    assert facts == {"direction": "inbound", "workflows": ["01", "02"], "upload": "in_store", "confirmation": False,
                     "inline_welcome": None}


def test_fixed_line_lint_reports_a_missing_line(tmp_path):
    root = lint_root(tmp_path)
    problems = run_evals.lint_fixed_and_config("demo", GOOD, FIXED_PROFILE, root)
    assert len(problems) == 1 and "isn't in stock" in problems[0]
    assert run_evals.lint_fixed_and_config("demo", GOOD + OOS.replace("'", "’"), FIXED_PROFILE, root) == []


def test_lint_requires_the_welcome_as_the_first_line(tmp_path):
    root = lint_root(tmp_path)
    problems = run_evals.lint_fixed_and_config("demo", "Here is the output.\n" + GOOD + OOS, FIXED_PROFILE, root)
    assert len(problems) == 1 and problems[0].startswith("welcome is not the first line")


def test_lint_flags_a_prescription_route_the_profile_does_not_enable(tmp_path):
    root = lint_root(tmp_path)
    text = GOOD + OOS + "For a prescription, send it by WhatsApp with the send tool.\n"
    problems = run_evals.lint_fixed_and_config("demo", text, FIXED_PROFILE, root)
    assert any("whatsapp" in p for p in problems) and any("send tool" in p for p in problems)
    assert run_evals.lint_fixed_and_config("demo", text, FIXED_PROFILE.replace("in_store", "whatsapp"), root) == []


VALUES_PROFILE = """# Profile
| Item | Value |
|---|---|
| Direction | Inbound |
| Prescription upload | in_store (`{{var.prescription_upload_method}}`) |
| Hours | `{{var.business_hours}}` = 8 AM to 10 PM, every day |
| Delivery info | not provided |
| Return policy | NOT given |
| Call data | `{{var.customer_name}}` and `{{var.refill_details}}` (unconfirmed) |

## Test values

- <customer_name> = Test Person
- <order_number> = 48213
- <refill_details> = Medicine G due
"""


def test_profile_variable_values_reads_the_table_and_call_context():
    values = run_evals.profile_variable_values(VALUES_PROFILE)
    assert values == {"prescription_upload_method": "in_store", "business_hours": "8 AM to 10 PM, every day",
                      "delivery_info": "(empty)", "return_policy": "(empty)",
                      "customer_name": "Test Person", "refill_details": "Medicine G due"}
    note = run_evals.values_note(values)
    assert "prescription_upload_method = in_store" in note and "business_hours = 8 AM to 10 PM" in note


def test_probe_placeholders_are_replaced_by_test_values():
    values = run_evals.test_values(VALUES_PROFILE)
    probe = "My name is <customer_name>, order <order_number>, near <unknown>."
    assert run_evals.fill_placeholders(probe, values) == "My name is Test Person, order 48213, near <unknown>."
    assert "## Test values" in run_evals.HIDDEN_HEADINGS
    assert "Test Person" not in run_evals.visible_profile(VALUES_PROFILE)


def test_stray_text_before_the_welcome_is_stripped():
    welcome = "Hello, this is {{var.agent_name}}."
    text = "```\nNow assembling the output.\n\nHello, this is {{var.agent_name}}.\n\n## 1. Role\n"
    clean, removed = run_evals.strip_before_welcome(text, welcome)
    assert clean.startswith("Hello, this is") and removed == ["```", "Now assembling the output."]
    same, nothing = run_evals.strip_before_welcome("## 1. Role\n\nbody", welcome)
    assert same == "## 1. Role\n\nbody" and nothing == []
def test_run_industry_gives_the_agent_values_fills_probes_and_lints_stray_text(repo, monkeypatch):
    monkeypatch.setattr(run_evals, "VARIABLE_VALUE_INDUSTRIES", ("healthcare",))
    ind = repo / "industries" / "healthcare"
    (ind / "section-bases.md").write_text('- Inbound: "Hello, this is {{var.agent_name}}."\n', encoding="utf-8")
    (ind / "test-profiles" / "02-b.md").unlink()
    (ind / "test-profiles" / "01-a.md").write_text(VALUES_PROFILE, encoding="utf-8")
    checks = json.loads((ind / "eval.json").read_text(encoding="utf-8"))
    checks["checks"][0]["probe"] = "I am <customer_name>, order <order_number>."
    (ind / "eval.json").write_text(json.dumps(checks), encoding="utf-8")

    class Llm(FakeLlm):
        def run(self, prompt, system=None, agent=None, tools=None):
            if agent is None and system is None:
                self.calls.append((agent, system, prompt))
                return "```\nHello, this is {{var.agent_name}}.\n## 1. Role\n=== DRAFT NOTES ===\nnotes"
            return super().run(prompt, system=system, agent=agent, tools=tools)
    llm = Llm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    probes = [c for c in llm.calls if c[1] and "prescription_upload_method = in_store" in c[1]]
    assert probes and any(c[2] == "I am Test Person, order 48213." for c in probes)
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert any("stray text before the welcome" in m for m in saved["lint"]["01-a"])
    text = (repo / "industries/healthcare/results/2026-10-08/01-a-instructions.md").read_text(encoding="utf-8")
    assert text.startswith("Hello, this is")


def test_lint_ignores_the_format_example_and_variable_routes(tmp_path):
    root = lint_root(tmp_path)
    core = root / "industries" / "demo" / "core.md"
    core.write_text(core.read_text(encoding="utf-8") + '\nFormat: say exactly "X", then in the same reply transfer.', encoding="utf-8")
    text = GOOD + OOS + "If {{var.prescription_upload_method}} is whatsapp or email, send the upload instructions.\n"
    assert run_evals.lint_fixed_and_config("demo", text, FIXED_PROFILE, root) == []


def test_split_marked_reads_only_between_the_markers():
    text = "Here is the output:\n=== INSTRUCTIONS ===\nWelcome\n## 1\n=== DRAFT NOTES ===\nnotes\n"
    assert run_evals.split_marked(text) == ("Welcome\n## 1", "notes", ["Here is the output:"])
    assert run_evals.split_marked("a\n=== DRAFT NOTES ===\nb") == ("a", "b", [])


def test_case_selected_accepts_short_and_full_ids():
    assert run_evals.case_selected("PHA-E04", None)
    assert run_evals.case_selected("PHA-E04", ["E04"]) and run_evals.case_selected("PHA-E04", ["pha-e04"])
    assert not run_evals.case_selected("PHA-E14", ["E04"])


def test_cases_option_judges_only_those_cases_and_skips_other_profiles(repo):
    ind = repo / "industries" / "healthcare"
    data = json.loads((ind / "eval.json").read_text(encoding="utf-8"))
    data["checks"][2]["profiles"] = ["01"]
    (ind / "eval.json").write_text(json.dumps(data), encoding="utf-8")
    llm = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08", "--cases", "E03"], llm)
    judged = [c[2] for c in llm.calls if c[0] == "eval-judge"]
    assert len(judged) == 1 and "01-a" in judged[0] and "DEM-E03" in judged[0] and "DEM-E04" not in judged[0]
    generated = [c for c in llm.calls if c[0] is None and c[1] is None]
    assert len(generated) == 1


def test_stray_text_outside_the_markers_is_a_warning_not_an_error(repo):
    class Llm(FakeLlm):
        def run(self, prompt, system=None, agent=None, tools=None):
            if agent is None and system is None:
                self.calls.append((agent, system, prompt))
                return "chatter\n=== INSTRUCTIONS ===\nbody\n=== DRAFT NOTES ===\nnotes"
            return super().run(prompt, system=system, agent=agent, tools=tools)
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], Llm())
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert any(m.startswith("warning: text outside the markers") for m in saved["lint"]["01-a"])
    assert (repo / "industries/healthcare/results/2026-10-08/01-a-instructions.md").read_text(encoding="utf-8").startswith("body")


class _R:
    def __init__(self, code, out="", err=""):
        self.returncode, self.stdout, self.stderr = code, out, err


def test_auth_error_waits_60_seconds_and_retries_up_to_3_times(monkeypatch):
    waits, calls = [], []

    def fake_run(cmd, **kw):
        calls.append(cmd)
        return _R(1, err="OAuth token has expired") if len(calls) < 4 else _R(0, "ok")
    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: waits.append(s))
    assert run_evals.ClaudeCli("claude").run("hi") == "ok"
    assert waits == [60, 60, 60] and len(calls) == 4


def test_auth_error_gives_up_after_3_waits(monkeypatch):
    waits = []
    monkeypatch.setattr(run_evals.subprocess, "run", lambda cmd, **kw: _R(1, err="401 Unauthorized"))
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: waits.append(s))
    with pytest.raises(RuntimeError, match="3 auth waits"):
        run_evals.ClaudeCli("claude").run("hi")
    assert waits.count(60) == 3


def test_other_errors_do_not_wait_60_seconds(monkeypatch):
    waits = []
    monkeypatch.setattr(run_evals.subprocess, "run", lambda cmd, **kw: _R(1, err="some other failure"))
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: waits.append(s))
    with pytest.raises(RuntimeError):
        run_evals.ClaudeCli("claude").run("hi")
    assert 60 not in waits


def test_at_most_4_claude_processes_run_in_parallel(monkeypatch):
    assert run_evals.MAX_PARALLEL == 4 and run_evals.WORKERS <= 4


def _resume(repo, llm, extra=()):
    return run(repo, ["--industry", "healthcare", "--date", "2026-10-08", "--resume", *extra], llm)


def test_resume_skips_complete_profiles_and_judges_only_when_replies_exist(repo):
    first = FakeLlm()
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], first)
    work = repo / "industries/healthcare/results/2026-10-08"
    # profile 02-b is cut mid-way (no replies, no judgment); profile 01-a lost only its judgment
    (work / "02-b-replies.json").unlink()
    (work / "02-b-judgment.json").unlink()
    (work / "01-a-judgment.json").unlink()
    again = FakeLlm()
    code, out = _resume(repo, again)
    assert "resume 01-a: Instructions, notes and replies are complete, judging only" in out
    assert "resume 02-b: not complete, regenerating" in out
    generated = [c for c in again.calls if c[0] is None and c[1] is None]
    judged = [c for c in again.calls if c[0] == "eval-judge"]
    assert len(generated) == 1 and len(judged) == 2
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert saved["summary"]["total"] == 40


def test_resume_skips_a_fully_judged_profile_without_any_call(repo):
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], FakeLlm())
    again = FakeLlm()
    code, out = _resume(repo, again)
    assert again.calls == [] and out.count("complete, skipped") == 2 and "40/40 passed" in out


def test_resume_ignores_a_judgment_made_for_other_cases(repo):
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08", "--cases", "E03"], FakeLlm())
    again = FakeLlm()
    _resume(repo, again, extra=["--cases", "E05"])
    assert [c for c in again.calls if c[0] == "eval-judge"]


def test_confirmation_lines_are_required_only_when_a_channel_is_set(tmp_path):
    root = lint_root(tmp_path)
    core = root / "industries" / "demo" / "core.md"
    core.write_text(core.read_text(encoding="utf-8")
                    + '\n| R-76 | Flow, only channels in {{var.confirmation_channels}}: ask once, say exactly "Would you like a confirmation?" |\n',
                    encoding="utf-8")
    text = GOOD + OOS
    assert run_evals.lint_fixed_and_config("demo", text, FIXED_PROFILE, root) == []
    enabled = FIXED_PROFILE + "\n- The hospital wants it (`{{var.confirmation_channels}}` = whatsapp, email).\n"
    problems = run_evals.lint_fixed_and_config("demo", text, enabled, root)
    assert len(problems) == 1 and "Would you like a confirmation?" in problems[0]
    assert run_evals.profile_facts(enabled)["confirmation"] is True


def test_languages_row_becomes_the_default_language_start_value():
    profile = ("| Item | Value |\n|---|---|\n| Direction | Inbound |\n"
               "| Languages | English start, switches to Hindi and Kannada expected |\n")
    assert run_evals.profile_variable_values(profile)["default_language"] == "English"
    assert run_evals.start_language("English start, Hindi expected") == "English"
    assert run_evals.start_language("Hindi start; callers speak Hindi") == "Hindi"
    assert run_evals.start_language("NOT given") == "(empty)"
    assert run_evals.start_language("not stated (English start)") == "(empty)"
    assert "default_language = English" in run_evals.values_note(run_evals.profile_variable_values(profile))


def test_the_runner_requires_only_the_upload_branch_the_profile_uses(tmp_path):
    root = lint_root(tmp_path)
    core = root / "industries" / "demo" / "core.md"
    core.write_text(core.read_text(encoding="utf-8")
                    + '\n| R-54a | [upload: whatsapp] say exactly "Is this number on WhatsApp?" |\n'
                    + '| R-54b | [upload: email] say exactly "Please tell me your email address." |\n', encoding="utf-8")
    base = FIXED_PROFILE
    def lines(upload):
        text = base.replace("| Prescription upload | in_store |", f"| Prescription upload | {upload} |")
        return [q for s, q in run_evals.fixed_lines("demo", run_evals.profile_facts(text), root)]
    assert "Is this number on WhatsApp?" in lines("whatsapp") and "Please tell me your email address." not in lines("whatsapp")
    assert "Please tell me your email address." in lines("email") and "Is this number on WhatsApp?" not in lines("email")
    for other in ("in_store", "not set"):
        got = lines(other)
        assert "Is this number on WhatsApp?" not in got and "Please tell me your email address." not in got


def test_an_inline_values_industry_takes_its_welcome_from_the_profile(tmp_path):
    root = lint_root(tmp_path)
    (root / "industries" / "demo" / "variables.json").write_text(
        json.dumps({"inline_values": True, "variables": []}), encoding="utf-8")
    profile = FIXED_PROFILE.replace("| Direction | Inbound |",
                                    "| Business name | Lakeview Hospital |\n| Assistant | Asha (female) |\n| Direction | Inbound |")
    welcome = "Thank you for calling Lakeview Hospital. This is Asha. How can I help you?"
    assert ("welcome", welcome) in run_evals.fixed_lines("demo", run_evals.profile_facts(profile), root)
    ok = welcome + "\n" + GOOD + OOS
    assert run_evals.lint_fixed_and_config("demo", ok, profile, root) == []
    wrong = "Thank you for calling Lakeview Hospital. How can I help you?\n" + GOOD + OOS
    problems = run_evals.lint_fixed_and_config("demo", wrong, profile, root)
    assert len(problems) == 1 and "welcome is not the first line, word for word" in problems[0]
    assert run_evals.profile_facts(FIXED_PROFILE)["inline_welcome"] is None  # a profile without business values keeps the old behaviour


def test_outbound_only_workflows_depend_on_the_industry():
    assert run_evals.OUTBOUND_ONLY_WORKFLOWS["pharmacy"] == ("03",)
    assert run_evals.OUTBOUND_ONLY_WORKFLOWS["healthcare"] == ("04",)


def test_network_drop_waits_60_seconds_and_retries(monkeypatch):
    waits, calls = [], []

    def fake_run(cmd, **kw):
        calls.append(cmd)
        return _R(1, err="API Error: Can't reach the API server, check your internet or DNS (ENOTFOUND)") if len(calls) < 3 else _R(0, "ok")
    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: waits.append(s))
    assert run_evals.ClaudeCli("claude").run("hi") == "ok" and waits == [60, 60]



def test_markers_count_only_when_alone_on_their_own_line():
    text = ("I will separate the parts with === DRAFT NOTES === and start with === INSTRUCTIONS === below.\n"
            "=== INSTRUCTIONS ===\nWelcome\n## 1\n=== DRAFT NOTES ===\nnotes\n")
    instructions, notes, outside = run_evals.split_marked(text)
    assert instructions == "Welcome\n## 1" and notes == "notes" and len(outside) == 1 and "separate the parts" in outside[0]
    # without an INSTRUCTIONS marker, a mention inside a sentence does not split the text either
    text2 = "Plan: put === DRAFT NOTES === after the Instructions.\nWelcome\n## 1\n=== DRAFT NOTES ===\nnotes\n"
    instructions2, notes2 = run_evals.split_output(text2)
    assert instructions2.startswith("Plan:") and instructions2.endswith("## 1") and notes2 == "notes"
    assert run_evals.split_output("only a mention === DRAFT NOTES === here") == ("only a mention === DRAFT NOTES === here", "")


def test_empty_instructions_are_a_harness_error_and_stop_that_profile(repo):
    class Llm(FakeLlm):
        def run(self, prompt, system=None, agent=None, tools=None):
            if agent is None and system is None:
                self.calls.append((agent, system, prompt))
                if "P1" in prompt:
                    return "=== INSTRUCTIONS ===\n\n=== DRAFT NOTES ===\nnotes only"
                return "=== INSTRUCTIONS ===\nbody\n=== DRAFT NOTES ===\nnotes"
            return super().run(prompt, system=system, agent=agent, tools=tools)
    llm = Llm()
    code, out = run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], llm)
    assert code == 2 and "harness error: 01-a" in out
    judged = [c for c in llm.calls if c[0] == "eval-judge"]
    assert len(judged) == 1 and "02-b" in judged[0][2]
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert len(saved["summary"]["harness_errors"]) == 1 and {r["profile"] for r in saved["results"]} == {"02-b"}
    assert (repo / "industries/healthcare/results/2026-10-08/01-a-raw-output.md").is_file()


BANK_PROFILE = """| Tools | card_block_tool ON, balance_lookup_tool OFF, change_language, transfer, end_call |"""


def test_banking_tools_follow_the_profile_flags_and_have_no_send_tool():
    on = run_evals.tools_note("banking", BANK_PROFILE)
    assert "change_language, transfer, end_call, card_block_tool" in on and "balance_lookup_tool" not in on
    assert "send_confirmation" not in on
    both = run_evals.tools_note("banking", "card_block_tool ON, balance_lookup_tool ON")
    assert both.count("card_block_tool") == 1 and "balance_lookup_tool" in both
    off = run_evals.tools_note("banking", "card_block_tool OFF, balance_lookup_tool OFF")
    assert "card_block_tool" not in off and "balance_lookup_tool" not in off and "send_confirmation" not in off
    assert "card_block_tool" not in run_evals.tools_note("banking")


def test_banking_gets_variable_values_and_its_outbound_only_workflows():
    assert "banking" in run_evals.VARIABLE_VALUE_INDUSTRIES
    assert run_evals.OUTBOUND_ONLY_WORKFLOWS["banking"] == ("04", "05")



def test_self_check_statement_is_read_from_the_draft_notes():
    notes = "**Fixed-line self-check**\n- rewritten once (added: the failed-action line)\n**Word counts**\n- x"
    assert run_evals.self_check_statement(notes) == "rewritten once (added: the failed-action line)"
    assert run_evals.self_check_statement("**Fixed-line self-check:** passed the first time") == "passed the first time"
    assert run_evals.self_check_statement("nothing") == "not reported"
    assert run_evals.self_check_statement(None) == "not reported"


def test_each_kind_of_call_has_its_own_time_limit(monkeypatch):
    seen = []

    def fake_run(cmd, **kw):
        seen.append(kw.get("timeout"))
        return _R(0, "ok")
    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    cli = run_evals.ClaudeCli("claude")
    cli.run("make it")                                   # generation
    cli.run("probe", system="s", tools="")               # probe reply
    cli.run("grade", agent="eval-judge")                 # judge
    assert seen == [900, 600, 600] == [run_evals.TIMEOUTS["generation"], run_evals.TIMEOUTS["probe"], run_evals.TIMEOUTS["judge"]]


def test_a_timeout_is_logged_and_retried_like_any_failure(monkeypatch):
    calls, waits = [], []

    def fake_run(cmd, **kw):
        calls.append(kw["timeout"])
        if len(calls) < 3:
            raise run_evals.subprocess.TimeoutExpired(cmd, kw["timeout"])
        return _R(0, "fine")
    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: waits.append(s))
    cli = run_evals.ClaudeCli("claude")
    assert cli.run("hi", agent="eval-judge") == "fine"
    assert calls == [600, 600, 600] and waits == [run_evals.RETRY_WAIT] * 2
    assert [(e["kind"], e["attempt"], e["retried"]) for e in cli.timeout_log] == [("judge", 1, True), ("judge", 2, True)]


def test_a_call_that_times_out_every_time_gives_up_with_a_clear_error(monkeypatch):
    def fake_run(cmd, **kw):
        raise run_evals.subprocess.TimeoutExpired(cmd, kw["timeout"])
    monkeypatch.setattr(run_evals.subprocess, "run", fake_run)
    monkeypatch.setattr(run_evals.time, "sleep", lambda s: None)
    cli = run_evals.ClaudeCli("claude")
    with pytest.raises(RuntimeError, match=r"\(generation\) timed out after 900 s on each of 3 tries"):
        cli.run("hi")
    assert len(cli.timeout_log) == 3 and cli.timeout_log[-1]["retried"] is False


def test_timeouts_are_saved_in_the_results_file(repo):
    class Llm(FakeLlm):
        timeout_log = [{"kind": "judge", "limit_seconds": 600, "attempt": 1, "retried": True, "at": "2026-10-10T08:00:00"}]
    run(repo, ["--industry", "healthcare", "--date", "2026-10-08"], Llm())
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert saved["timeouts"] == Llm.timeout_log
    run(repo, ["--industry", "healthcare", "--date", "2026-10-09"], FakeLlm())
    assert json.loads((repo / "industries/healthcare/results/2026-10-09.json").read_text(encoding="utf-8"))["timeouts"] == []


def _marker_skill(repo):
    skill = repo / ".claude" / "skills" / "healthcare-prompt-writer" / "SKILL.md"
    skill.write_text("Output starts with the line === INSTRUCTIONS === then the welcome.", encoding="utf-8")


GOOD_OUT = "=== INSTRUCTIONS ===\nWelcome\n\n## 1. Role & Identity\nbody\n=== DRAFT NOTES ===\nnotes"


def test_output_problem_needs_the_marker_line_and_a_first_section():
    f = run_evals.output_problem
    assert f(GOOD_OUT, "Welcome\n## 1. Role", True) is None
    assert f("anything", "", True) == "the Instructions part is empty after splitting"
    assert "no === INSTRUCTIONS ===" in f("Welcome\n## 1. Role\n=== DRAFT NOTES ===\nn", "Welcome\n## 1. Role", True)
    assert "I mention === INSTRUCTIONS === here" and "no === INSTRUCTIONS ===" in f("I mention === INSTRUCTIONS === here\n## 1. Role", "I mention === INSTRUCTIONS === here\n## 1. Role", True)
    assert 'no "## 1." section' in f("=== INSTRUCTIONS ===\nThis command needs your approval to run.", "This command needs your approval to run.", True)
    # a skill whose format has no marker is not held to it
    assert f("Welcome\n## 1. Role", "Welcome\n## 1. Role", False) is None
    assert f("just text", "just text", False) is None


class _BadThenGood(FakeLlm):
    def __init__(self, bad_times):
        super().__init__()
        self.bad_times, self.generated = bad_times, 0

    def run(self, prompt, system=None, agent=None, tools=None):
        if agent is None and system is None:
            self.calls.append((agent, system, prompt))
            self.generated += 1
            if self.generated <= self.bad_times:
                return "This command needs your approval to run. Could you approve it?"
            return GOOD_OUT
        return super().run(prompt, system=system, agent=agent, tools=tools)


def test_a_non_instructions_output_is_regenerated_once(repo):
    _marker_skill(repo)
    llm = _BadThenGood(bad_times=1)
    code, out = run(repo, ["--industry", "healthcare", "--date", "2026-10-08", "--profiles", "01"], llm)
    assert "harness error: 01-a" in out and "regenerating once" in out
    assert llm.generated == 2 and code == 0
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert len(saved["summary"]["harness_regenerations"]) == 1 and saved["summary"]["harness_errors"] == []
    assert {r["profile"] for r in saved["results"]} == {"01-a"}


def test_a_second_bad_output_stops_the_profile_as_a_harness_error(repo):
    _marker_skill(repo)
    llm = _BadThenGood(bad_times=2)
    code, out = run(repo, ["--industry", "healthcare", "--date", "2026-10-08", "--profiles", "01"], llm)
    assert code == 2 and "on both tries" in out
    assert llm.generated == 2 and not [c for c in llm.calls if c[0] == "eval-judge"]
    saved = json.loads((repo / "industries/healthcare/results/2026-10-08.json").read_text(encoding="utf-8"))
    assert len(saved["summary"]["harness_errors"]) == 1 and saved["results"] == []
    assert (repo / "industries/healthcare/results/2026-10-08/01-a-raw-output.md").is_file()

