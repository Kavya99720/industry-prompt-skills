"""DECISIONS 125: the short form, the section 2 and 3 rules, the section 5 lines and --translated."""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDUSTRIES = ("healthcare", "pharmacy", "banking", "real-estate", "retail", "education", "logistics")

spec = importlib.util.spec_from_file_location("check_fixed_lines", ROOT / "scripts" / "check_fixed_lines.py")
cfl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cfl)

CHANGE_MIND = "If the caller changes their mind, follow the new request without starting over."
UNCLEAR = "confirm the part you recognised, like '<name>, is that right?' If nothing is clear, ask them to say it again."
FIXED_LANG = 'A "say exactly" line keeps its exact meaning, not its English words'
TOOL_CALL = 'Before any tool call'
SWITCH = 'Switch when the caller\'s last sentence has Indian-language words, in Indian script or in English letters'


def bases():
    out = {"shared": ROOT / "docs" / "shared" / "section-bases.md", "template": ROOT / "docs" / "shared" / "new-industry-template" / "section-bases.template.md"}
    for i in INDUSTRIES:
        p = ROOT / "industries" / i / "section-bases.md"
        if p.is_file():
            out[i] = p
    return out


def test_shared_base_has_the_writing_it_short_rules():
    text = (ROOT / "docs" / "shared" / "section-bases.md").read_text(encoding="utf-8")
    assert "## Writing it short (DECISIONS 125)" in text
    for phrase in ("Each rule once", "Define once, then name", "the Role line", "under 700", "under 595"):
        assert phrase in text.replace("**", ""), phrase


def test_every_section_bases_and_the_template_carry_the_new_section_2_3_5_text():
    for name, p in bases().items():
        t = p.read_text(encoding="utf-8")
        assert SWITCH in t, name
        assert CHANGE_MIND in t and UNCLEAR in t, name
        assert FIXED_LANG in t and TOOL_CALL in t, name
        assert "सुबह नौ बजे" in t and "ಬೆಳಿಗ್ಗೆ ಒಂಬತ್ತು ಗಂಟೆ" in t, name  # language examples, supported languages only
        assert 'Dr. is "Doctor"' in t, name
        assert "never AM or PM" in t and "weekdays and months" in t, name
        assert '"next Monday"' in t and "find the exact date" in t, name


def test_healthcare_booking_lines_are_in_the_shared_base():
    t = (ROOT / "docs" / "shared" / "section-bases.md").read_text(encoding="utf-8")
    for phrase in ("24-hour format", "one slot length before the end time", "unless the tool said so", "always new", "by name and specialty",
                   "nearest two free times it returned", "never call the caller by the patient's name"):
        assert phrase in t, phrase


def test_saved_outputs_use_the_business_name_in_the_role_line_and_no_slots_or_extra_variables():
    for ind in INDUSTRIES:
        d = ROOT / "industries" / ind / "sentence-tests"
        for f in sorted(d.glob("[0-9][0-9]-*.md")):
            t = f.read_text(encoding="utf-8")
            ins = t.split("=== DRAFT NOTES ===")[0]
            assert not re.search(r"\{\{var\.(company_name|agent_name|business_hours|business_info)\}\}", ins), f
            assert CHANGE_MIND in ins and UNCLEAR in ins, f
            assert SWITCH in ins, f
            role = next(l for l in ins.splitlines() if l.startswith("You are"))
            welcome = ins.splitlines()[1]
            m = re.search(r"(?:calling(?: from)?|calling from) ([^.]+)\.", welcome)
            if m and "our " not in m.group(1)[:4]:
                assert m.group(1) in role, (f, role)


def test_translated_mode_accepts_digit_lines_and_lists_the_rest_as_notes():
    missing = [("core.md", "Call 1 1 2 right now."), ("core.md", "Our team will confirm that for you."), ("core.md", cfl.MUST_PREFIX + "x"), ("welcome (profile)", "Hello")]
    still, notes = cfl.split_translated(missing, "आप अभी 1 1 2 पर कॉल करें")
    assert [q for _, q in notes] == ["Call 1 1 2 right now.", "Our team will confirm that for you."]
    assert [q for _, q in still] == [cfl.MUST_PREFIX + "x", "Hello"]
    still, notes = cfl.split_translated([("core.md", "Call 1 1 2 right now.")], "no digits here")
    assert [q for _, q in still] == ["Call 1 1 2 right now."] and notes == []


def test_section_one_is_shorter_in_every_saved_profile_01_than_before():
    # profile 01 section 1 word counts before the trim (saved outputs at the start of the branch)
    before = {"retail": 1241, "education": 1795, "real-estate": 1206, "logistics": 1400, "healthcare": 794, "pharmacy": 918, "banking": 996}
    names = {"retail": "01-single-store-inbound.md", "education": "01-school-inbound.md", "real-estate": "01-builder-inbound.md",
             "logistics": "01-courier-inbound-tools-off.md", "healthcare": "01-multispeciality-hospital-inbound.md",
             "pharmacy": "01-retail-pharmacy-inbound.md", "banking": "01-public-private-bank-inbound.md"}
    for ind, n in before.items():
        t = (ROOT / "industries" / ind / "sentence-tests" / names[ind]).read_text(encoding="utf-8")
        s1 = re.search(r"## 1\. [^\n]*\n(.*?)\n## 2\.", t, re.S).group(1)
        assert len(s1.split()) < n, ind
        s6 = re.search(r"## 6\. [^\n]*\n(.*?)\n## Prompt Variables", t, re.S).group(1)
        assert len(s6.split()) <= 595, ind
