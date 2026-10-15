"""DECISIONS 126: every generated output has the unnumbered '## Welcome Message' heading above the welcome line."""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
HEADING = "## Welcome Message"
INDUSTRIES = ("healthcare", "pharmacy", "banking", "real-estate", "retail", "education", "logistics", "hr")

spec = importlib.util.spec_from_file_location("check_fixed_lines", ROOT / "scripts" / "check_fixed_lines.py")
cfl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cfl)
import run_evals  # noqa: E402


def saved_outputs():
    files = []
    for i in INDUSTRIES:
        files += sorted((ROOT / "industries" / i / "sentence-tests").glob("[0-9][0-9]-*.md"))
    files += sorted(p for p in (ROOT / "outputs").glob("*.md") if p.read_text(encoding="utf-8").startswith("=== INSTRUCTIONS ==="))
    return files


def test_every_saved_output_has_the_heading_then_the_welcome_then_section_1():
    files = saved_outputs()
    assert len(files) >= 38
    for f in files:
        lines = f.read_text(encoding="utf-8").splitlines()
        assert lines[0] == "=== INSTRUCTIONS ===", f
        assert lines[1] == HEADING, f
        assert lines[2].strip() and not lines[2].startswith("#"), f  # the welcome line itself
        assert lines[3] == "" and lines[4] == "## 1. Role & Identity", f
        text = "\n".join(lines)
        assert text.count(HEADING) == 1, f
        for n in range(1, 7):  # sections 1 to 6 keep their numbers
            assert re.search(rf"(?m)^## {n}\. ", text), (f, n)


def test_every_skill_and_the_template_show_the_heading_in_the_output_format():
    paths = [ROOT / ".claude" / "skills" / f"{i}-prompt-writer" / "SKILL.md" for i in INDUSTRIES]
    paths.append(ROOT / "docs" / "shared" / "new-industry-template" / "skill.template.md")
    for p in paths:
        t = p.read_text(encoding="utf-8")
        assert "=== INSTRUCTIONS ===\n" + HEADING + "\n<Welcome message>" in t, p
        assert "unnumbered heading" in t, p


def test_section_bases_and_templates_and_agents_mention_the_heading():
    paths = [ROOT / "docs" / "shared" / "section-bases.md", ROOT / "docs" / "shared" / "new-industry-template" / "section-bases.template.md",
             ROOT / "docs" / "shared" / "new-industry-template" / "README.md", ROOT / "docs" / "shared" / "prompting-guide.md"]
    paths += [ROOT / "industries" / i / "section-bases.md" for i in INDUSTRIES if (ROOT / "industries" / i / "section-bases.md").is_file()]
    paths += sorted((ROOT / ".claude" / "agents").glob("*-agent.md"))
    for p in paths:
        t = p.read_text(encoding="utf-8")
        if p.name.endswith("-agent.md") and "INSTRUCTIONS" not in t:
            continue
        assert HEADING in t, p


def test_references_hold_the_current_skill_output_format():
    for i in INDUSTRIES:
        refs = ROOT / ".claude" / "skills" / f"{i}-prompt-writer" / "references" / "shared" / "section-bases.md"
        assert HEADING in refs.read_text(encoding="utf-8"), i


def test_run_evals_lint_and_strip_accept_the_heading():
    welcome = "Thank you for calling Lakeview Hospital. This is Asha. How can I help you?"
    text = f"```\n{HEADING}\n{welcome}\n\n## 1. Role & Identity\nbody"
    clean, removed = run_evals.strip_before_welcome(text, welcome)
    assert clean.startswith(HEADING + "\n" + welcome) and removed == ["```"]
    clean, removed = run_evals.strip_before_welcome(f"{HEADING}\n{welcome}\nbody", welcome)
    assert clean.startswith(HEADING) and removed == []


def test_check_fixed_lines_finds_the_welcome_under_the_heading(tmp_path):
    out = f"=== INSTRUCTIONS ===\n{HEADING}\nHello, this is Asha, an AI assistant calling from Lakeview Hospital. Is this a good time to talk?\n\n## 1. Role & Identity\n"
    head = out.split("\n", 12)
    direction = "outbound" if any("calling from" in l for l in head) else "inbound"
    assert direction == "outbound"
    welcome = "Hello, this is Asha, an AI assistant calling from Lakeview Hospital. Is this a good time to talk?"
    assert cfl.norm(welcome) in cfl.norm(out)
