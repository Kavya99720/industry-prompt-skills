from pathlib import Path

import pytest

import validate_eval

ROOT = Path(__file__).resolve().parent.parent
EVALS = sorted(ROOT.glob("industries/*/eval.json"))

if not EVALS:
    pytest.skip(
        "no industries/*/eval.json exist yet (no industry has reached write-evals)",
        allow_module_level=True,
    )


@pytest.fixture(params=EVALS, ids=lambda p: p.parent.name)
def eval_path(request):
    return request.param


def test_validator_passes(eval_path):
    assert validate_eval.validate(eval_path) == []


def test_is_frozen(eval_path):
    import json

    assert json.loads(eval_path.read_text(encoding="utf-8"))["frozen"] is True


def test_industry_has_brief_and_skill(eval_path):
    industry = eval_path.parent.name
    assert (ROOT / "industries" / industry / "brief.md").is_file()
    assert (ROOT / ".claude" / "skills" / f"{industry}-prompt-writer" / "SKILL.md").is_file()
