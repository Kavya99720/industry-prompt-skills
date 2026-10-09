import json

import pytest

import status


def make_root(tmp_path, slugs=("healthcare", "pharmacy")):
    for s in slugs:
        (tmp_path / "industries" / s).mkdir(parents=True)
    (tmp_path / "README.md").write_text(
        f"# T\n\n{status.START}\nold\n{status.END}\n\nafter\n", encoding="utf-8"
    )
    return tmp_path


def make_eval(path, n=20, frozen=True):
    checks = [
        {
            "id": f"X-E{i:02d}",
            "rule_ids": ["R-01"],
            "scenario_ids": ["S-01"],
            "severity": "major",
            "type": "prompt",
            "description": "d",
            "pass_criteria": "p",
        }
        for i in range(1, n + 1)
    ]
    path.write_text(
        json.dumps({"industry": "synthetic-none", "version": 1, "frozen": frozen, "checks": checks}),
        encoding="utf-8",
    )


def make_run(industry_dir, run_id, total, passed, date=None):
    d = industry_dir / "results" / run_id
    d.mkdir(parents=True)
    (d / "summary.json").write_text(
        json.dumps(
            {
                "run_id": run_id,
                "date": date or run_id[:10],
                "total": total,
                "passed": passed,
                "failed": total - passed,
            }
        ),
        encoding="utf-8",
    )


def row(root, slug):
    return status.industry_row(root, slug)


def test_empty_industry_is_all_todo(tmp_path):
    root = make_root(tmp_path)
    assert row(root, "pharmacy") == ("pharmacy", "Todo", "Todo", "Todo", "Todo", "Todo")


def test_brief_marker_means_todo_and_no_marker_means_done(tmp_path):
    root = make_root(tmp_path)
    brief = root / "industries" / "pharmacy" / "brief.md"
    brief.write_text("# P\n\nStatus: Todo\n\n## 1. Scope\n", encoding="utf-8")
    assert row(root, "pharmacy")[1] == "Todo"
    brief.write_text("# P\n\n## 1. Scope\nContent\n", encoding="utf-8")
    assert row(root, "pharmacy")[1] == "Done"


def test_skill_folder_means_in_progress(tmp_path):
    root = make_root(tmp_path)
    skill = root / ".claude" / "skills" / "pharmacy-prompt-writer"
    skill.mkdir(parents=True)
    assert row(root, "pharmacy")[2] == "Todo"  # folder without SKILL.md
    (skill / "SKILL.md").write_text("x", encoding="utf-8")
    assert row(root, "pharmacy")[2] == "In progress"


def test_eval_status_counts_cases(tmp_path):
    root = make_root(tmp_path)
    path = root / "industries" / "pharmacy" / "eval.json"
    make_eval(path, 24, frozen=True)
    assert row(root, "pharmacy")[3] == "Done (24)"
    make_eval(path, 24, frozen=False)
    assert row(root, "pharmacy")[3] == "In progress (24)"
    make_eval(path, 12, frozen=True)
    assert row(root, "pharmacy")[3] == "In progress (12)"
    path.write_text("not json", encoding="utf-8")
    assert row(root, "pharmacy")[3] == "In progress"


def test_latest_run_and_pass_rate(tmp_path):
    root = make_root(tmp_path)
    d = root / "industries" / "pharmacy"
    make_run(d, "2026-10-07-run2", 24, 20)
    make_run(d, "2026-10-07-run10", 24, 22)
    make_run(d, "2026-10-06-run1", 24, 5)
    r = row(root, "pharmacy")
    assert r[4] == "2026-10-07"
    assert r[5] == "In progress (22/24)"


def test_skill_and_pass_rate_done_when_latest_run_has_no_failures(tmp_path):
    root = make_root(tmp_path)
    d = root / "industries" / "pharmacy"
    skill = root / ".claude" / "skills" / "pharmacy-prompt-writer"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("x", encoding="utf-8")
    make_run(d, "2026-10-06-run1", 24, 20)
    make_run(d, "2026-10-07-run1", 24, 24)
    r = row(root, "pharmacy")
    assert r[2] == "Done"
    assert r[5] == "Done (24/24)"


def test_run_without_readable_summary_is_skipped(tmp_path):
    root = make_root(tmp_path)
    d = root / "industries" / "pharmacy"
    make_run(d, "2026-10-06-run1", 10, 10)
    (d / "results" / "2026-10-07-run1").mkdir()
    assert row(root, "pharmacy")[4] == "2026-10-06"


def test_table_lists_known_industries_in_order(tmp_path):
    root = make_root(tmp_path, ("travel", "pharmacy", "healthcare", "zeta"))
    lines = status.render_table(root).splitlines()
    assert lines[0].startswith("| Industry | Brief | Skill | Evals | Last run | Pass rate |")
    names = [l.split("|")[1].strip() for l in lines[2:]]
    assert names == ["pharmacy", "healthcare", "travel", "zeta"]


def test_main_writes_and_check_detects_stale(tmp_path, capsys):
    root = make_root(tmp_path)
    assert status.main(["--check"], root=root) == 1
    assert status.main([], root=root) == 0
    text = (root / "README.md").read_text(encoding="utf-8")
    assert "| healthcare |" in text and "old" not in text and text.endswith("after\n")
    assert status.main(["--check"], root=root) == 0
    (root / "industries" / "pharmacy" / "brief.md").write_text("# P\n", encoding="utf-8")
    assert status.main(["--check"], root=root) == 1


def test_missing_markers_fail(tmp_path):
    root = make_root(tmp_path)
    (root / "README.md").write_text("no markers", encoding="utf-8")
    assert status.main(["--check"], root=root) == 1


def make_run_file(industry_dir, stem, total, passed):
    res = industry_dir / "results"
    res.mkdir(parents=True, exist_ok=True)
    (res / f"{stem}.json").write_text(
        json.dumps({"summary": {"total": total, "passed": passed, "failed": total - passed}, "results": []}),
        encoding="utf-8")


def test_run_files_from_run_evals_are_counted(tmp_path):
    root = make_root(tmp_path)
    ind = root / "industries" / "pharmacy"
    make_run_file(ind, "2026-10-08-run1", 10, 7)
    make_run_file(ind, "2026-10-08-run2-full", 10, 10)
    assert row(root, "pharmacy")[4:] == ("2026-10-08", "Done (10/10)")


def test_newest_run_number_wins_over_older_passing_run(tmp_path):
    root = make_root(tmp_path)
    ind = root / "industries" / "pharmacy"
    make_run_file(ind, "2026-10-08-run1", 10, 10)
    make_run_file(ind, "2026-10-08-run3-quick", 10, 9)
    assert row(root, "pharmacy")[5] == "In progress (9/10)"


def test_v1_signoff_shows_done_v1_only_at_95_percent_or_better(tmp_path):
    root = make_root(tmp_path)
    d = root / "industries" / "pharmacy"
    skill = root / ".claude" / "skills" / "pharmacy-prompt-writer"
    skill.mkdir(parents=True)
    (skill / "SKILL.md").write_text("x", encoding="utf-8")
    make_run(d, "2026-10-09-run6", 65, 64)
    assert row(root, "pharmacy")[2] == "In progress"
    (d / "v1-signoff.md").write_text("signed off", encoding="utf-8")
    r = row(root, "pharmacy")
    assert r[2] == "Done (v1)" and r[5] == "Done (v1) (64/65)"
    make_run(d, "2026-10-09-run7", 65, 60)
    assert row(root, "pharmacy")[2] == "In progress"
