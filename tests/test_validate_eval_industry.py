import json

import pytest

import validate_eval

CORE = """# core
| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-01 | **Baseline B-02.** Never assume. | x | critical | S5 |
| R-02 | **Baseline B-06.** Ask again. | x | major | S5 |
| R-03 | Domain rule one. | x | critical | S1 |
| R-04 | Domain rule two. | x | major | S6 |
"""


def build(tmp_path, checks, core=CORE):
    ind = tmp_path / "industries" / "demo"
    (ind / "workflows").mkdir(parents=True)
    (ind / "brief.md").write_text("# index R-01 R-02 R-03 R-04 S-01\n", encoding="utf-8")
    (ind / "core.md").write_text(core, encoding="utf-8")
    path = ind / "eval.json"
    path.write_text(
        json.dumps({"industry": "demo", "version": 1, "frozen": False, "checks": checks}),
        encoding="utf-8",
    )
    return path


def check(i, rules):
    return {
        "id": f"DEM-E{i:02d}", "rule_ids": rules, "severity": "major", "type": "prompt",
        "description": "d", "pass_criteria": "p",
    }


def checks(baseline_only, domain_rules=("R-03", "R-04")):
    out = [check(i, ["R-01"]) for i in range(1, baseline_only + 1)]
    n = len(out)
    out += [check(n + i + 1, [domain_rules[i % len(domain_rules)]]) for i in range(20 - n)]
    return out


def test_five_baseline_only_checks_pass(tmp_path):
    path = build(tmp_path, checks(5))
    assert validate_eval.validate(path, root=tmp_path) == []


def test_six_baseline_only_checks_fail(tmp_path):
    path = build(tmp_path, checks(6))
    errors = validate_eval.validate(path, root=tmp_path)
    assert any("6 checks map only to baseline rules" in e for e in errors)


def test_check_with_a_domain_rule_is_not_baseline_only(tmp_path):
    cs = checks(5)
    cs[5]["rule_ids"] = ["R-01", "R-03"]
    assert validate_eval.validate(build(tmp_path, cs), root=tmp_path) == []


def test_uncovered_critical_rule_fails(tmp_path):
    path = build(tmp_path, checks(2, domain_rules=("R-04",)))
    errors = validate_eval.validate(path, root=tmp_path)
    assert "critical rule R-03 has no check" in errors


def test_major_rule_may_be_uncovered(tmp_path):
    path = build(tmp_path, checks(2, domain_rules=("R-03",)))
    assert validate_eval.validate(path, root=tmp_path) == []


def test_rules_in_workflow_files_are_found(tmp_path):
    path = build(tmp_path, checks(2))
    (path.parent / "workflows" / "01-x.md").write_text(
        "| R-09 | Workflow critical rule. | x | critical | S6 |\n", encoding="utf-8"
    )
    errors = validate_eval.validate(path, root=tmp_path)
    assert "critical rule R-09 has no check" in errors
