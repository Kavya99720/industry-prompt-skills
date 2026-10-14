#!/usr/bin/env python
"""Fill the progress table in README.md from the files in industries/*/.

Usage:
  python scripts/status.py           rewrite the table between the STATUS markers in README.md
  python scripts/status.py --check   exit 1 if the table in README.md is out of date

Standard library only. Status values are Todo, In progress and Done, with real
numbers in brackets where there are any. Industries in NO_EVAL have no eval.json:
their Evals, Last run and Pass rate columns say N/A, and Skill is Done once the skill
and industries/<slug>/v1-signoff.md exist.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import validate_eval  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
START = "<!-- STATUS:START -->"
END = "<!-- STATUS:END -->"
ORDER = (
    "pharmacy", "healthcare", "retail", "education",
    "logistics", "hr", "banking", "real-estate",
)
# Industries that get no eval.json and no eval runs (DECISIONS 108). If one still has an eval.json, the normal path applies.
NO_EVAL = ("retail", "education", "logistics", "hr", "real-estate")
HEADER = ("Industry", "Brief", "Skill", "Evals", "Last run", "Pass rate")
RUN_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-run(\d+)$")
RUN_FILE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})-run(\d+)(?:-.+)?$")
TODO_MARKER = re.compile(r"^Status:\s*Todo\s*$", re.IGNORECASE | re.MULTILINE)


def brief_status(industry_dir):
    brief = industry_dir / "brief.md"
    if not brief.is_file():
        return "Todo"
    if TODO_MARKER.search(brief.read_text(encoding="utf-8")):
        return "Todo"
    return "Done"


def eval_status(industry_dir):
    path = industry_dir / "eval.json"
    if not path.is_file():
        return "Todo"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        count = len(data["checks"])
    except (OSError, ValueError, KeyError, TypeError):
        return "In progress"
    done = not validate_eval.validate(path) and data.get("frozen") is True
    return f"{'Done' if done else 'In progress'} ({count})"


def latest_run(industry_dir):
    """Return (date, summary dict) of the newest run, or None.

    A run is a folder <date>-run<N> with a readable summary.json, or a file <date>-run<N>[-tag].json written
    by scripts/run_evals.py with a "summary" object. The highest (date, N) wins.
    """
    results = industry_dir / "results"
    if not results.is_dir():
        return None
    runs = []
    for d in results.iterdir():
        if d.is_dir():
            m = RUN_RE.match(d.name)
            if m:
                runs.append((m.group(1), int(m.group(2)), d / "summary.json", "folder"))
        elif d.suffix == ".json":
            m = RUN_FILE_RE.match(d.stem)
            if m:
                runs.append((m.group(1), int(m.group(2)), d, "file"))
    for date, _, path, kind in sorted(runs, key=lambda r: (r[0], r[1], r[3] == "file"), reverse=True):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            summary = data["summary"] if kind == "file" else data
            int(summary["total"]), int(summary["passed"]), int(summary["failed"])
        except (OSError, ValueError, KeyError, TypeError):
            continue
        return date, summary
    return None


def no_eval_row(root, slug, industry_dir):
    """Row for an industry without eval.json: Done needs the skill and a v1-signoff.md; eval columns are N/A."""
    skill = root / ".claude" / "skills" / f"{slug}-prompt-writer" / "SKILL.md"
    if not skill.is_file():
        skill_status = "Todo"
    else:
        skill_status = "Done" if (industry_dir / "v1-signoff.md").is_file() else "In progress"
    return (slug, brief_status(industry_dir), skill_status, "N/A", "N/A", "N/A")


def industry_row(root, slug):
    industry_dir = root / "industries" / slug
    if slug in NO_EVAL and not (industry_dir / "eval.json").is_file():
        return no_eval_row(root, slug, industry_dir)
    run = latest_run(industry_dir)
    all_pass = run is not None and run[1]["total"] > 0 and run[1]["failed"] == 0
    # v1 sign-off: industries/<slug>/v1-signoff.md exists and the newest run is at least 95% passed
    signed = (industry_dir / "v1-signoff.md").is_file() and run is not None and run[1]["total"] > 0         and 100 * run[1]["passed"] / run[1]["total"] >= 95
    skill = root / ".claude" / "skills" / f"{slug}-prompt-writer" / "SKILL.md"
    if not skill.is_file():
        skill_status = "Todo"
    else:
        skill_status = "Done" if all_pass else ("Done (v1)" if signed else "In progress")
    if run is None:
        last_run, pass_rate = "Todo", "Todo"
    else:
        date, s = run
        last_run = date
        label = "Done" if all_pass else ("Done (v1)" if signed else "In progress")
        pass_rate = f"{label} ({s['passed']}/{s['total']})"
    return (
        slug, brief_status(industry_dir), skill_status,
        eval_status(industry_dir), last_run, pass_rate,
    )


def industry_slugs(root):
    found = {p.name for p in (root / "industries").glob("*") if p.is_dir()}
    known = [s for s in ORDER if s in found]
    return known + sorted(found - set(ORDER))


def render_table(root):
    rows = [HEADER] + [industry_row(root, s) for s in industry_slugs(root)]
    lines = ["| " + " | ".join(r) + " |" for r in rows]
    lines.insert(1, "|" + "|".join("---" for _ in HEADER) + "|")
    return "\n".join(lines)


def replace_block(readme_text, table):
    if START not in readme_text or END not in readme_text:
        raise ValueError(f"README.md must contain {START} and {END}")
    head, rest = readme_text.split(START, 1)
    _, tail = rest.split(END, 1)
    return f"{head}{START}\n{table}\n{END}{tail}"


def main(argv=None, root=ROOT):
    argv = sys.argv[1:] if argv is None else argv
    check = "--check" in argv
    readme = Path(root) / "README.md"
    current = readme.read_text(encoding="utf-8").replace("\r\n", "\n")
    try:
        updated = replace_block(current, render_table(Path(root)))
    except ValueError as e:
        print(e, file=sys.stderr)
        return 1
    if check:
        if updated != current:
            print("README.md progress table is out of date. Run: python scripts/status.py", file=sys.stderr)
            return 1
        print("README.md progress table is up to date")
        return 0
    readme.write_text(updated, encoding="utf-8", newline="\n")
    print("README.md progress table updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
