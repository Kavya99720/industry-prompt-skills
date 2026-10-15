"""The shared call-flow rule (DECISIONS 123): goal line and done condition in section 1, interruptions in section 5."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULE = ROOT / "docs" / "shared" / "call-flow.md"
INDUSTRIES = ("healthcare", "pharmacy", "banking", "real-estate", "retail", "education")
GOALS = {
    "healthcare": "Your goal: help the caller with clinic information, doctor availability or an appointment request, using only the business facts and the roster, or connect them to the right team.",
    "pharmacy": "Your goal: help the caller with medicine availability, orders and store information, using only the business facts, or connect them to the right team.",
    "banking": "Your goal: help the caller with general product, branch and card questions, using only the business facts, or connect them to the right team.",
    "real-estate": "Your goal: help the caller with project information and site visit requests, using only the business facts, or connect them to the right team.",
    "retail": "Your goal: help the caller with store, product, order and return questions, using only the business facts and system data, or connect them to the right team.",
    "education": "Your goal: help the caller with admissions, fees and school information, using only the business facts, or connect them to the right team.",
    "logistics": "Your goal: help the caller with their shipment, such as tracking, delivery, pickup or a problem, using only system data and the business facts, or connect them to the right team.",
    "hr": "Your goal: help the caller with general job, application and HR questions, using only the business facts, or connect them to the right team.",
}


def blocks():
    text = RULE.read_text(encoding="utf-8")
    return re.findall(r"## (?:Done condition|Interruptions) text[^\n]*\n\n```\n(.*?)\n```", text, re.S)


def section_bases(industry):
    if industry == "healthcare":
        return ROOT / "docs" / "shared" / "section-bases.md"
    return ROOT / "industries" / industry / "section-bases.md"


def section(text, n):
    return re.search(rf"## {n}\. [^\n]*\n(.*?)(?=\n## \d\.|\n## [A-Z]|\Z)", text, re.S).group(1)


def test_the_rule_has_the_done_condition_and_the_interruptions_text():
    done, interruptions = blocks()
    assert done == "The call is done when the caller has their answer, has been transferred, or a callback has been noted. Then say the closing line and end the call."
    for phrase in ("'hello?'", "'Yes, I'm here.'", "Never restart the call", "never repeat the welcome", "never ask again for details the caller already gave",
                   "stop, listen, answer the new point, then go back to the open step", "'Are you still there?' twice"):
        assert phrase in interruptions, phrase
    assert not re.search(r"\b[RS]-\d+\b", done + interruptions)


def test_the_rule_lists_the_eight_inbound_goal_lines_word_for_word():
    text = RULE.read_text(encoding="utf-8")
    for goal in GOALS.values():
        assert goal in text, goal


def test_every_section_bases_has_its_goal_then_the_done_pointer_then_the_interruptions_pointer():
    done, interruptions = blocks()
    for i in INDUSTRIES:
        text = section_bases(i).read_text(encoding="utf-8")
        assert done not in text and interruptions not in text, i  # defined once
        s1 = [l for l in section(text, 1).splitlines() if l.strip() and l.strip() != "```"]
        assert s1[0].startswith("You are"), i
        assert s1[1].startswith("<Goal line.") and GOALS[i] in s1[1], i
        assert s1[2].startswith("<Done condition:") and "docs/shared/call-flow.md" in s1[2], i
        assert "Goal lines (DECISIONS 123)" in section(text, 1) or "Goal lines (DECISIONS 123)" in text, i
        s5 = section(text, 5)
        assert "<Interruptions:" in s5 and "docs/shared/call-flow.md" in s5, i
        assert "stop at once and listen" not in text, i  # the old one-liner is not said twice


def test_the_template_carries_the_pointers_and_the_logistics_and_hr_goals_are_ready():
    text = (ROOT / "docs" / "shared" / "new-industry-template" / "section-bases.template.md").read_text(encoding="utf-8")
    assert "<Goal line" in text and "<Done condition:" in text and "<Interruptions:" in text
    rule = RULE.read_text(encoding="utf-8")
    assert GOALS["logistics"] in rule and GOALS["hr"] in rule


def test_every_skill_and_the_template_name_the_rule_and_the_references_hold_a_current_copy():
    shared = RULE.read_text(encoding="utf-8")
    for i in INDUSTRIES:
        skill = ROOT / ".claude" / "skills" / f"{i}-prompt-writer"
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        assert "references/shared/call-flow.md" in text and '"Done condition" block' in text and '"Interruptions text" block' in text, i
        assert (skill / "references" / "shared" / "call-flow.md").read_text(encoding="utf-8") == shared, i
    template = (ROOT / "docs" / "shared" / "new-industry-template" / "skill.template.md").read_text(encoding="utf-8")
    assert "call-flow.md" in template


def test_saved_profile_outputs_carry_the_goal_the_done_condition_and_the_interruptions():
    done, interruptions = blocks()
    for ind, name, goal in (("retail", "01-single-store-inbound", GOALS["retail"]), ("education", "01-school-inbound", GOALS["education"]),
                            ("real-estate", "01-builder-inbound", GOALS["real-estate"])):
        text = (ROOT / "industries" / ind / "sentence-tests" / f"{name}.md").read_text(encoding="utf-8")
        s1 = [l for l in section(text, 1).splitlines() if l.strip()]
        assert s1[0].startswith("You are") and s1[1] == goal and s1[2] == done, ind
        assert interruptions in section(text, 5), ind
