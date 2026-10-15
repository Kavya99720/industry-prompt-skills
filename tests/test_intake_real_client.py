"""DECISIONS 134: real-client mode is the default at intake; sample answers are offered only in test mode."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDUSTRIES = ("healthcare", "pharmacy", "banking", "real-estate", "retail", "education", "logistics", "hr")
KEY = ("How to ask (real-client mode is the default)", "Never offer a synthetic or sample value", '"Not provided"', '"Online only"', '"Other"',
       '"test mode" or "use samples"')


def test_every_skill_and_the_shared_intake_flow_state_the_real_client_rule():
    texts = {i: (ROOT / ".claude" / "skills" / f"{i}-prompt-writer" / "SKILL.md").read_text(encoding="utf-8") for i in INDUSTRIES}
    texts["intake-flow"] = (ROOT / "docs" / "shared" / "intake-flow.md").read_text(encoding="utf-8")
    for name, t in texts.items():
        for phrase in KEY:
            assert phrase in t, (name, phrase)
        assert t.count("How to ask (real-client mode is the default)") == 1, name


def test_the_template_carries_the_rule_and_the_references_hold_the_current_intake_flow():
    t = (ROOT / "docs" / "shared" / "new-industry-template" / "skill.template.md").read_text(encoding="utf-8")
    assert "real-client mode is the default" in t and '"test mode" or "use samples"' in t
    shared = (ROOT / "docs" / "shared" / "intake-flow.md").read_text(encoding="utf-8")
    for i in INDUSTRIES:
        copy = ROOT / ".claude" / "skills" / f"{i}-prompt-writer" / "references" / "shared" / "intake-flow.md"
        if copy.is_file():
            assert copy.read_text(encoding="utf-8") == shared, i


def test_no_intake_text_offers_a_sample_value_as_an_option():
    for i in INDUSTRIES:
        core = (ROOT / "industries" / i / "core.md").read_text(encoding="utf-8")
        intake = core.split("## Intake", 1)[1].split("\n## ", 1)[0]
        for bad in ("Test City", "sample synthetic", "Maple Ridge", "Swift Lane"):
            assert bad not in intake, (i, bad)
