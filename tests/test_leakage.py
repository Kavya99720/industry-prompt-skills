import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_variables  # noqa: E402


def make_root(tmp_path, allow=(), mode="fail"):
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "leakage_terms.json").write_text(json.dumps({
        "mode": mode,
        "terms": {"pharmacy": ["pharmacist"], "banking": ["debit card"], "hr": ["payslip"]},
        "allow": list(allow),
    }), encoding="utf-8")
    for slug in ("pharmacy", "banking", "hr"):
        (tmp_path / "industries" / slug).mkdir(parents=True)
    return tmp_path


def test_a_term_of_another_industry_is_a_hit(tmp_path):
    root = make_root(tmp_path)
    (root / "industries" / "banking" / "core.md").write_text("ask the pharmacist\nfine line\n", encoding="utf-8")
    hits = check_variables.find_leakage(root)
    assert len(hits) == 1
    h = hits[0]
    assert (h["owner"], h["term_of"], h["term"], h["line"], h["allowed"]) == ("banking", "pharmacy", "pharmacist", 1, False)


def test_an_industry_may_use_its_own_terms(tmp_path):
    root = make_root(tmp_path)
    (root / "industries" / "pharmacy" / "core.md").write_text("the pharmacist helps", encoding="utf-8")
    assert check_variables.find_leakage(root) == []


def test_allowlist_marks_a_hit_as_allowed_and_results_are_skipped(tmp_path):
    root = make_root(tmp_path, allow=[{"industry": "hr", "term": "pharmacist", "reason": "boundary note"}])
    (root / "industries" / "hr" / "brief.md").write_text("pharmacist queries go elsewhere", encoding="utf-8")
    (root / "industries" / "banking" / "results").mkdir()
    (root / "industries" / "banking" / "results" / "run.md").write_text("pharmacist", encoding="utf-8")
    hits = check_variables.find_leakage(root)
    assert len(hits) == 1 and hits[0]["allowed"] is True


def test_words_are_matched_whole_and_case_insensitively(tmp_path):
    root = make_root(tmp_path)
    (root / "industries" / "hr" / "a.md").write_text("PharmacistS no, but a Pharmacist yes, debit card too", encoding="utf-8")
    terms = sorted(h["term"] for h in check_variables.find_leakage(root))
    assert terms == ["debit card", "pharmacist"]


def test_fail_mode_makes_an_open_hit_an_error(tmp_path, capsys):
    root = make_root(tmp_path)
    (root / "docs" / "shared").mkdir(parents=True)
    (root / "docs" / "shared" / "variables.json").write_text(json.dumps({"variables": []}), encoding="utf-8")
    (root / "industries" / "hr" / "a.md").write_text("ask the pharmacist", encoding="utf-8")
    assert check_variables.main(["--root", str(root)]) == 1
    assert "leakage: 1 hits, 1 not allowed" in capsys.readouterr().out


def test_report_mode_never_fails(tmp_path, capsys):
    root = make_root(tmp_path, mode="report")
    (root / "docs" / "shared").mkdir(parents=True)
    (root / "docs" / "shared" / "variables.json").write_text(json.dumps({"variables": []}), encoding="utf-8")
    (root / "industries" / "hr" / "a.md").write_text("ask the pharmacist", encoding="utf-8")
    assert check_variables.main(["--root", str(root)]) == 0
    assert check_variables.main(["--root", str(root), "--leakage"]) == 0
    assert "HIT 'pharmacist'" in capsys.readouterr().out


def test_shared_safety_terms_are_allowed_in_every_industry(tmp_path):
    root = make_root(tmp_path)
    cfg = json.loads((root / "scripts" / "leakage_terms.json").read_text(encoding="utf-8"))
    cfg["terms"]["healthcare"] = ["Tele-MANAS"]
    cfg["shared_allow"] = ["Tele-MANAS"]
    (root / "scripts" / "leakage_terms.json").write_text(json.dumps(cfg), encoding="utf-8")
    (root / "industries" / "banking" / "core.md").write_text("Say Tele-MANAS: 1 4 4 1 6.", encoding="utf-8")
    hits = check_variables.find_leakage(root)
    assert len(hits) == 1 and hits[0]["allowed"] is True and hits[0]["term"] == "Tele-MANAS"

