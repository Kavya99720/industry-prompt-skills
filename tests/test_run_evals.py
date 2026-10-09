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
    assert "booking, reschedule" in run_evals.tools_note("healthcare")
    pharmacy = run_evals.tools_note("pharmacy")
    assert "check_stock, place_order" in pharmacy and "booking" not in pharmacy and "send_confirmation" not in pharmacy
    other = run_evals.tools_note("travel")
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
    assert facts == {"direction": "inbound", "workflows": ["01", "02"], "upload": "in_store"}


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
