import pytest

import build_skill_refs as b

ROOT = b.ROOT


def make_repo(tmp_path):
    ind = tmp_path / "industries" / "demo"
    (ind / "workflows").mkdir(parents=True)
    (ind / "core.md").write_text("# core\n", encoding="utf-8")
    (ind / "workflows" / "01-a.md").write_text("# a\n", encoding="utf-8")
    (ind / "workflows" / "02-stub.md").write_text("# s\n\nStatus: stub. Not written yet.\n", encoding="utf-8")
    (ind / "workflows" / "README.md").write_text("# index\n", encoding="utf-8")
    shared = tmp_path / "docs" / "shared"
    shared.mkdir(parents=True)
    for name in b.SHARED:
        (shared / name).write_text(f"{name}\n", encoding="utf-8")
    return tmp_path


def test_build_copies_written_workflows_and_shared_files(tmp_path):
    root = make_repo(tmp_path)
    names = b.build("demo", root)
    assert names == sorted(["INDEX.md", "core.md", "workflows/01-a.md"] + [f"shared/{n}" for n in b.SHARED])
    assert b.problems("demo", root) == []


def test_stale_missing_and_extra_files_are_reported(tmp_path):
    root = make_repo(tmp_path)
    b.build("demo", root)
    tdir = b.target_dir("demo", root)
    (root / "industries/demo/core.md").write_text("# core changed\n", encoding="utf-8")
    (tdir / "workflows/01-a.md").unlink()
    (tdir / "old.md").write_text("old", encoding="utf-8")
    found = b.problems("demo", root)
    assert "out of sync: references/core.md" in found
    assert "missing: references/workflows/01-a.md" in found
    assert "extra file: references/old.md" in found


def test_build_removes_extra_files(tmp_path):
    root = make_repo(tmp_path)
    b.build("demo", root)
    extra = b.target_dir("demo", root) / "compliance.md"
    extra.write_text("old", encoding="utf-8")
    b.build("demo", root)
    assert not extra.exists() and b.problems("demo", root) == []


def test_missing_source_raises(tmp_path):
    root = make_repo(tmp_path)
    (root / "industries/demo/core.md").unlink()
    with pytest.raises(FileNotFoundError):
        b.plan("demo", root)


def test_check_exit_codes(tmp_path, capsys):
    root = make_repo(tmp_path)
    assert b.main(["--industry", "demo", "--root", str(root), "--check"]) == 1
    b.main(["--industry", "demo", "--root", str(root)])
    assert b.main(["--industry", "demo", "--root", str(root), "--check"]) == 0


def real_industries():
    return sorted(p.parent.parent.name.removesuffix("-prompt-writer")
                  for p in ROOT.glob(".claude/skills/*-prompt-writer/references/INDEX.md"))


@pytest.mark.parametrize("industry", real_industries() or ["healthcare"])
def test_real_skill_references_are_in_sync(industry):
    assert b.problems(industry) == [], f"run: python scripts/build_skill_refs.py --industry {industry}"


def test_references_never_include_tests_or_results():
    names = b.plan("healthcare")
    assert not any("eval" in n or "results" in n or "test-profiles" in n for n in names)
