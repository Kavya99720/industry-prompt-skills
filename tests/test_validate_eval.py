import importlib.util
import json
import shutil
from pathlib import Path

import pytest

import validate_eval

ROOT = Path(__file__).resolve().parent.parent


def make_check(i, ctype="prompt"):
    c = {
        "id": f"C-{i:02d}",
        "rule_ids": ["R-01"],
        "severity": "major",
        "type": ctype,
        "description": "Synthetic check",
        "pass_criteria": "Synthetic criteria",
    }
    if ctype == "behaviour":
        c["probe"] = "Synthetic caller message"
    return c


def make_eval(n=20):
    return {
        "industry": "synthetic-nonexistent",
        "version": 1,
        "frozen": False,
        "checks": [make_check(i) for i in range(1, n + 1)],
    }


def run(tmp_path, data):
    p = tmp_path / "eval.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    return validate_eval.validate(p)


def test_valid_file_passes(tmp_path):
    assert run(tmp_path, make_eval()) == []


def test_valid_file_with_behaviour_check_passes(tmp_path):
    data = make_eval()
    data["checks"][0] = make_check(1, "behaviour")
    assert run(tmp_path, data) == []


@pytest.mark.parametrize("n", [19, 31])
def test_check_count_out_of_range_fails(tmp_path, n):
    errors = run(tmp_path, make_eval(n))
    assert any("expected 20-30 checks" in e for e in errors)


@pytest.mark.parametrize("n", [20, 30])
def test_check_count_boundaries_pass(tmp_path, n):
    assert run(tmp_path, make_eval(n)) == []


def test_duplicate_ids_fail(tmp_path):
    data = make_eval()
    data["checks"][1]["id"] = data["checks"][0]["id"]
    assert any("duplicate id" in e for e in run(tmp_path, data))


@pytest.mark.parametrize(
    "field", ["id", "rule_ids", "severity", "type", "description", "pass_criteria"]
)
def test_missing_check_field_fails(tmp_path, field):
    data = make_eval()
    del data["checks"][0][field]
    assert run(tmp_path, data)


@pytest.mark.parametrize("key", ["industry", "version", "frozen", "checks"])
def test_missing_top_level_key_fails(tmp_path, key):
    data = make_eval()
    del data[key]
    assert any(f"missing top-level key: {key}" in e for e in run(tmp_path, data))


def test_probe_on_prompt_check_fails(tmp_path):
    data = make_eval()
    data["checks"][0]["probe"] = "should not be here"
    assert any("must not have a probe" in e for e in run(tmp_path, data))


def test_behaviour_check_without_probe_fails(tmp_path):
    data = make_eval()
    data["checks"][0] = make_check(1, "behaviour")
    del data["checks"][0]["probe"]
    assert any("needs a non-empty probe" in e for e in run(tmp_path, data))


def test_unknown_rule_id_fails_when_brief_exists(tmp_path):
    # The validator finds briefs relative to its own location, so run a copy
    # of it inside a temporary repo layout with a synthetic brief.
    (tmp_path / "scripts").mkdir()
    (tmp_path / "industries" / "synthetic").mkdir(parents=True)
    shutil.copy(ROOT / "scripts" / "validate_eval.py", tmp_path / "scripts")
    (tmp_path / "industries" / "synthetic" / "brief.md").write_text(
        "# Synthetic\nR-01 a rule\n", encoding="utf-8"
    )
    spec = importlib.util.spec_from_file_location(
        "validate_eval_copy", tmp_path / "scripts" / "validate_eval.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    data = make_eval()
    data["industry"] = "synthetic"
    p = tmp_path / "eval.json"
    p.write_text(json.dumps(data), encoding="utf-8")
    assert mod.validate(p) == []

    data["checks"][0]["rule_ids"] = ["R-99"]
    p.write_text(json.dumps(data), encoding="utf-8")
    assert any("rule_id R-99 not found" in e for e in mod.validate(p))
