"""DECISIONS 129: every industry's saved outputs are in the compact form and keep every core and workflow rule."""
import importlib.util
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("compact_coverage", ROOT / "scripts" / "compact_coverage.py")
cc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cc)


@pytest.mark.parametrize("industry", cc.INDUSTRIES)
def test_every_rule_of_core_and_the_workflows_is_present_or_not_applicable(industry):
    rows, problems = cc.check(industry)
    assert problems == [], problems
    assert rows


@pytest.mark.parametrize("industry", cc.INDUSTRIES)
def test_saved_outputs_have_one_style_example_the_natural_speech_and_interruptions_blocks(industry):
    for key, path in cc.outputs(industry).items():
        t = cc.instructions(path)
        assert t.count("Example, ") == 1 and "a polite decline" not in t, path
        assert "The example below shows the style only" in t, path
        assert "If the caller says 'hello?'" in t, path
        assert "Sound like a friendly, cheerful person" in t, path


@pytest.mark.parametrize("industry", cc.INDUSTRIES)
def test_saved_outputs_have_one_handoff_list_and_no_leftover_two_example_sentence(industry):
    for key, path in cc.outputs(industry).items():
        t = cc.instructions(path)
        assert "The two examples below" not in t, path
        assert len(re.findall(r"(?i)hand off to the team when", t)) <= 1, path


def test_the_coverage_script_flags_a_missing_rule(tmp_path, monkeypatch):
    monkeypatch.setattr(cc, "ROOT", tmp_path)
    ind = tmp_path / "industries" / "demo"
    (ind / "sentence-tests").mkdir(parents=True)
    (ind / "workflows").mkdir()
    (ind / "core.md").write_text("| R-01 | rule | x | critical | S1 |\n| R-02 | rule | x | major | S5 |\n", encoding="utf-8")
    (ind / "sentence-tests" / "01-a.md").write_text("=== INSTRUCTIONS ===\n## Welcome Message\nHi\n\n## 1. Role\nNever do x.\n## 6. Main\nz\n=== DRAFT NOTES ===\n", encoding="utf-8")
    (ind / "compact-coverage.json").write_text('{"rules": {"R-01": {"section": "1", "phrases": ["Never do x."]}}, "not_applicable": {}}', encoding="utf-8")
    rows, problems = cc.check("demo")
    assert [r[3] for r in rows] == ["present"] and any("R-02" in p for p in problems)
