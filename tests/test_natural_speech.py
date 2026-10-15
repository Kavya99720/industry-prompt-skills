"""The shared natural-speech rule (DECISIONS 120 and 122) is defined once and every industry points to it."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RULE = ROOT / "docs" / "shared" / "natural-speech.md"
INDUSTRIES = ("healthcare", "pharmacy", "banking", "real-estate", "retail", "education", "logistics", "hr")


def blocks():
    text = RULE.read_text(encoding="utf-8")
    return re.findall(r"## Section [45] text[^\n]*\n\n```\n(.*?)\n```", text, re.S)


def test_the_rule_has_a_section_4_block_and_a_section_5_block_with_the_four_parts():
    b4, b5 = blocks()
    for word in ("kindly", "please be informed", "as per", "do the needful", "your request has been registered"):
        assert word in b4
    for word in ("Sure.", "Okay.", "Of course.", "Got it.", "I understand.", "Great!", "Perfect!", "Absolutely!", "May I have your name?"):
        assert word in b5
    assert "no jokes, no slang, no emoji" in b4
    for phrase in ("friendly, cheerful", "Happy to help.", "No problem.", "Sure, let me tell you.", "Thanks for waiting.",
                   "use it now and then, not in every turn", "Oh, I'm sorry to hear that.", "calm and serious, not cheerful",
                   "emergencies, safety, complaints, scams and bad news"):
        assert phrase in b4, phrase
    assert "say exactly" in b5 and "word for word" in b5
    assert "Great question!" in b5
    assert b5.count("Example, ") == 1 and "a normal question" in b5 and "a polite decline" not in b5


def test_the_rule_adds_no_rule_id_and_no_fixed_line_of_its_own():
    text = RULE.read_text(encoding="utf-8")
    b4, b5 = blocks()
    assert not re.search(r"\b[RS]-\d+\b", b4 + b5)
    assert "say exactly \"" not in b4 + b5


def test_every_section_bases_points_to_the_rule_and_does_not_copy_it():
    paths = [ROOT / "docs" / "shared" / "section-bases.md", ROOT / "docs" / "shared" / "new-industry-template" / "section-bases.template.md"]
    paths += [ROOT / "industries" / i / "section-bases.md" for i in INDUSTRIES if (ROOT / "industries" / i / "section-bases.md").is_file()]
    b4, b5 = blocks()
    for p in paths:
        text = p.read_text(encoding="utf-8")
        assert "docs/shared/natural-speech.md" in text, p
        assert "section 4 text" in text and "section 5 text" in text, p
        assert b4 not in text and b5 not in text, p  # defined once, in the shared file
        s4 = re.search(r"## 4\. [^\n]*\n(.*?)\n## 5\.", text, re.S).group(1)
        lines = [l for l in s4.splitlines() if l.strip() and l.strip() != "```"]
        assert "section 4 text" in lines[0], p  # the natural-speech block starts section 4


def test_every_skill_and_the_template_name_the_rule_and_the_references_hold_a_current_copy():
    shared = RULE.read_text(encoding="utf-8")
    for i in INDUSTRIES:
        skill = ROOT / ".claude" / "skills" / f"{i}-prompt-writer"
        text = (skill / "SKILL.md").read_text(encoding="utf-8")
        assert "references/shared/natural-speech.md" in text, i
        assert "end section 4 with" not in text and "end Section 4 with" not in text, i
        assert (skill / "references" / "shared" / "natural-speech.md").read_text(encoding="utf-8") == shared, i
    template = (ROOT / "docs" / "shared" / "new-industry-template" / "skill.template.md").read_text(encoding="utf-8")
    assert "natural-speech.md" in template
