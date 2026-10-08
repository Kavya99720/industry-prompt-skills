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
    simulated = [c for c in llm.calls if c[1] == "generated text"]
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
    probes = [c[2] for c in llm.calls if c[1] == "generated text"]
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
