"""DECISIONS 127: each rule has one home in the Instructions (saved outputs) and in the sources."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDUSTRIES = ("healthcare", "pharmacy", "banking", "real-estate", "retail", "education", "logistics")
FIXED_S3 = 'A "say exactly" line keeps its exact meaning, not its English words'
BLOCK9 = "Never ask again for details the caller already gave."


def outputs():
    files = []
    for i in INDUSTRIES:
        files += sorted((ROOT / "industries" / i / "sentence-tests").glob("[0-9][0-9]-*.md"))
    return files


def instructions(f):
    return f.read_text(encoding="utf-8").split("=== DRAFT NOTES ===")[0]


def section(text, n):
    return re.search(rf"(?ms)^## {n}\. [^\n]*\n(.*?)(?=^## |\Z)", text).group(1)


def test_fixed_lines_in_another_language_is_in_section_3_only():
    for f in outputs():
        t = instructions(f)
        assert t.count(FIXED_S3) == 1 and FIXED_S3 in section(t, 3), f
        assert "Helpline and emergency digits stay as digits" not in t, f


def test_helpline_digits_statement_is_in_section_2_only_where_core_requires_it():
    for ind in ("healthcare", "banking", "pharmacy"):
        for f in sorted((ROOT / "industries" / ind / "sentence-tests").glob("[0-9][0-9]-*.md")):
            t = instructions(f)
            assert t.count("with Latin digits and spaces in every language") == 1, f
            assert "with Latin digits and spaces in every language" in section(t, 2), f


def test_never_ask_again_and_confirm_recognised_are_one_line_in_section_5():
    for f in outputs():
        t = instructions(f)
        assert t.count(BLOCK9) == 1 and BLOCK9 in section(t, 5), f
        assert t.count("confirm the part you recognised") == 1, f
        s5 = section(t, 5)
        interruptions = re.search(r"If the caller says 'hello\?'[^\n]*", s5)
        if interruptions:  # outputs saved before the interruptions rule do not carry it
            assert "ask again" not in interruptions.group(0), f
        change = re.search(r"If the caller changes their mind[^\n]*", s5).group(0)
        assert change == "If the caller changes their mind, follow the new request without starting over.", f


def test_read_back_and_clear_yes_rule_is_in_the_tool_call_line_only():
    for f in outputs():
        t = instructions(f)
        assert t.count("Never skip the read-back and a clear yes before an action") == 1, f
        assert "book only after a clear yes" not in t and "Place it only after a clear yes" not in t, f


def test_tone_in_section_4_and_filler_praise_ban_and_spoken_aloud_in_section_5_only():
    for f in outputs():
        t = instructions(f)
        assert "filler praise" not in section(t, 4), f
        assert "Everything you say is spoken aloud" not in t, f
        assert section(t, 5).lstrip().startswith("Everything you produce is spoken aloud."), f
        if "Great question!" in t:  # outputs saved before the natural-speech rule do not carry the block
            assert "Great question!" in section(t, 5), f
            assert t.count("this tone never changes them") == 1, f


def test_closing_line_text_appears_once_in_section_5():
    for f in outputs():
        t = instructions(f)
        m = re.search(r'"(Thank you for (?:calling [^"]*|your time)\. Have a good day\.)"', section(t, 5))
        assert m, f
        assert t.count(m.group(1)) == 1, f


def test_healthcare_fee_waiting_clinical_in_section_1_failure_in_section_6():
    for f in sorted((ROOT / "industries" / "healthcare" / "sentence-tests").glob("[0-9][0-9]-*.md")):
        t = instructions(f)
        s1, s5, s6 = section(t, 1), section(t, 5), section(t, 6)
        if "Give fees" in s1:  # outbound reminders carry no fee line
            assert "never estimate, round, discount or negotiate" in s1, f
            assert "waiting times, token times" in s1, f
        for bad in ("State a doctor's fee only from the roster", "Never estimate or promise a waiting time", "Transfer clinical questions", "If booking fails"):
            assert bad not in s5, (f, bad)
        assert "WAIT:" not in s6, f
        assert "FAIL: If booking fails" in s6 or "03-outbound" in f.name or "02-single" in f.name, f


def test_sources_carry_the_one_home_rules():
    shared = (ROOT / "docs" / "shared" / "section-bases.md").read_text(encoding="utf-8")
    assert "One home per rule (DECISIONS 127)" in shared
    flow = (ROOT / "docs" / "shared" / "call-flow.md").read_text(encoding="utf-8")
    assert "Never restart the call and never repeat the welcome." in flow and "never ask again for details" not in flow
    ns = (ROOT / "docs" / "shared" / "natural-speech.md").read_text(encoding="utf-8")
    s4 = re.search(r"## Section 4 text[^\n]*\n\n```\n(.*?)\n```", ns, re.S).group(1)
    assert "filler praise" not in s4
    for i in INDUSTRIES:
        skill = (ROOT / ".claude" / "skills" / f"{i}-prompt-writer" / "SKILL.md").read_text(encoding="utf-8")
        assert "DECISIONS 127" in skill, i
        base = ROOT / "industries" / i / "section-bases.md"
        text = (base if base.is_file() else ROOT / "docs" / "shared" / "section-bases.md").read_text(encoding="utf-8")
        assert text.count(FIXED_S3) == 1, i
        assert "Everything you say is spoken aloud." not in text, i
        assert BLOCK9 in text, i
