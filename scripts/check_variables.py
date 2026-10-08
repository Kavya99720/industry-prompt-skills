#!/usr/bin/env python
"""Check that prompts, skills and briefs use platform variables correctly.

Usage:
  python scripts/check_variables.py                 scan .claude/skills, industries, outputs
  python scripts/check_variables.py --fix           also rewrite known old names to {{var.x}}
  python scripts/check_variables.py --paths a.md b/ scan only these files or folders
  python scripts/check_variables.py --include-docs  also scan docs/ and the README files

FAILS (exit 1) on:
  - a {{var.x}} whose name is not in docs/shared/variables.json
  - a wrong style: {{hospital_name}}, {{persona_name}}, {{doctors}}, @company_name, @agent_name ...
  - an example person name such as "Doctor Rao" or "Dr. Shah": write "Doctor <name>" (allowed only in
    test-profiles/, docs/shared/reference/ and eval.json test data)
  - a real client value: any term in scripts/denylist.txt (private, gitignored), or a phone number
WARNS on {{var.company_name}} used outside a welcome, closing or AI-disclosure line.

Put `check_variables: ignore` on a line to skip it (for text that explains a wrong style).
Industry custom details: an industry may define extra variables in industries/<x>/variables.json (same format as
docs/shared/variables.json). They are valid only in that industry's files.
Standard library only.
"""
import argparse
import difflib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SCOPE = (".claude/skills", "industries", "outputs")
DOCS_SCOPE = ("docs", "README.md", "CLAUDE.md")
SUFFIXES = {".md", ".json", ".txt"}
SKIP_DIRS = {"__pycache__", ".git", "node_modules"}


def is_results(path):
    """industries/<x>/results/ holds generated run output, not authored files."""
    parts = path.parts
    return "industries" in parts and "results" in parts[parts.index("industries"):]
IGNORE_MARK = "check_variables: ignore"

# Old or wrong names and the variable that replaces them. Only these are auto-fixed.
OLD_NAMES = {
    "hospital_name": "company_name",
    "clinic_name": "company_name",
    "business_name": "company_name",
    "center_name": "company_name",
    "persona_name": "agent_name",
    "agent_persona": "agent_name",
    "doctors": "roster",
    "doctor_list": "roster",
    "doctors_list": "roster",
    "hospital_hours": "business_hours",
    "clinic_hours": "business_hours",
    "opening_hours": "business_hours",
    "hospital_phone": "business_phone",
    "clinic_phone": "business_phone",
    "contact_number": "business_phone",
    "hospital_address": "clinic_address",
    "address": "clinic_address",
    "current_datetime": "now_local",
    "current_date": "now_local",
    "today": "now_local",
}
# Wrong names with no safe automatic replacement: only a suggestion is printed.
SUGGESTIONS = {
    "emergency_signs": "keep the default list in core rules; use {{var.emergency_signs_extra}} for additions",
    "transfer_target": "use the transfer tool; there is no variable for it",
    "ambulance_number": "say 108 or 112; the business ambulance number is not a variable (add a custom detail first)",
    "languages": "the supported languages are fixed by the platform; the start language is {{var.default_language}}",
    "fees": "read fees from {{var.roster}}",
    "timings": "read doctor timings from {{var.roster}}; business timings are {{var.business_hours}}",
    "accepted_insurers": "no variable; say the team will confirm, or add a custom detail first",
    "prep_instructions": "no variable; say the team will confirm, or add a custom detail first",
}

PHONE_RE = re.compile(r"(?<![\d])(?:\+?91[\s-]?)?[6-9]\d{4}[\s-]?\d{5}(?![\d])")
PIN_RE = re.compile(r"[A-Za-z],?\s+[1-9]\d{5}(?!\d)")
VAR_RE = re.compile(r"\{\{\s*var\.([A-Za-z0-9_]+)\s*\}\}")
BARE_RE = re.compile(r"\{\{\s*(?!var\.)([A-Za-z_][A-Za-z0-9_]*)\s*\}\}")
PERSON_RE = re.compile(r"\b(?:Doctor|Dr\.?)\s+(?!(?:On|Status|List|Roster)\b)[A-Z][a-z]+\b")
# Test data may name people (placeholders such as Doctor A, or probe text); authored rules and prompts may not.
PERSON_EXEMPT = ("/test-profiles/", "docs/shared/reference/")
AT_RE = re.compile(r"(?<![\w.@/])@([A-Za-z_][A-Za-z0-9_]*)")
# Lines where the caller hears the company name.
COMPANY_OK = re.compile(
    r"welcome|greet|opening|closing|close\b|goodbye|thank you for calling|"
    r"ai assistant|ai disclosure|are you (a )?(real |robot|human|person|an ai)|say you are|"
    r"voicemail|call us back|calling from|your business name",
    re.IGNORECASE,
)


class Issue:
    def __init__(self, path, line, level, problem, fix=""):
        self.path, self.line, self.level, self.problem, self.fix = path, line, level, problem, fix

    def __str__(self):
        text = f"{self.path}:{self.line}: {self.level} {self.problem}"
        return f"{text}\n    fix: {self.fix}" if self.fix else text


def load_variables(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return {v["name"] for v in data["variables"]}


def load_denylist(path):
    p = Path(path)
    if not p.is_file():
        return None
    terms = []
    for raw in p.read_text(encoding="utf-8").splitlines():
        term = raw.strip()
        if term and not term.startswith("#"):
            terms.append(re.compile(r"(?<!\w)" + re.escape(term) + r"(?!\w)", re.IGNORECASE))
    return terms


def industry_of(path, root):
    """The industry slug a file belongs to: industries/<x>/..., .claude/skills/<x>-prompt-writer/... or outputs/<x>/..."""
    try:
        parts = Path(path).resolve().relative_to(Path(root).resolve()).parts
    except ValueError:
        return None
    if len(parts) >= 2 and parts[0] in ("industries", "outputs"):
        return parts[1]
    if len(parts) >= 3 and parts[0] == ".claude" and parts[1] == "skills" and parts[2].endswith("-prompt-writer"):
        return parts[2][: -len("-prompt-writer")]
    return None


def industry_variables(industry, root):
    """Custom details an industry defines in industries/<x>/variables.json (same format as docs/shared/variables.json)."""
    if not industry:
        return set()
    p = Path(root) / "industries" / industry / "variables.json"
    return load_variables(p) if p.is_file() else set()


def collect_files(targets, root):
    files = []
    for t in targets:
        p = Path(t)
        if not p.is_absolute():
            p = root / p
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*")):
                if f.is_file() and f.suffix in SUFFIXES and not (SKIP_DIRS & set(f.parts)) and not is_results(f):
                    files.append(f)
    return files


def is_person_exempt(rel):
    rel = "/" + rel
    return rel.endswith("/eval.json") or any(x in rel or rel.startswith("/" + x) for x in PERSON_EXEMPT)


def replacement_for(name, known):
    if name in OLD_NAMES:
        return OLD_NAMES[name]
    if name in known:
        return name
    return None


def check_line(line, known):
    """Return a list of (level, problem, fix, span_or_None) for one line."""
    found = []
    for m in VAR_RE.finditer(line):
        if m.group(1) not in known:
            near = difflib.get_close_matches(m.group(1), sorted(known), n=1)
            hint = f"did you mean {{{{var.{near[0]}}}}}? " if near else ""
            found.append(("ERROR", f"unknown variable {m.group(0)}",
                          hint + "or add it to docs/shared/variables.json", None))
    for m in BARE_RE.finditer(line):
        name = m.group(1)
        rep = replacement_for(name, known)
        if rep:
            found.append(("ERROR", f"wrong variable style {m.group(0)}", f"use {{{{var.{rep}}}}}", (m, rep)))
        else:
            fix = SUGGESTIONS.get(name, "use a variable from docs/shared/variables.json or remove it")
            found.append(("ERROR", f"wrong variable style {m.group(0)} (no known replacement)", fix, None))
    for m in AT_RE.finditer(line):
        name = m.group(1)
        rep = replacement_for(name, known)
        if rep:
            found.append(("ERROR", f"wrong variable style @{name}", f"use {{{{var.{rep}}}}}", (m, rep)))
    return found


def scan_file(path, known, denylist, root):
    issues, fixes = [], []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError):
        return issues, fixes
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        rel = path.as_posix()
    for n, line in enumerate(lines, 1):
        if IGNORE_MARK in line:
            continue
        for level, problem, fix, span in check_line(line, known):
            issues.append(Issue(rel, n, level, problem, fix))
            if span:
                fixes.append((n, span[0].start(), span[0].end(), span[1]))
        if denylist:
            for rx in denylist:
                if rx.search(line):
                    issues.append(Issue(rel, n, "ERROR", "real client value (denylist match)",
                                        "replace with a variable or a neutral placeholder such as <business_name>"))
                    break
        if PERSON_RE.search(line) and not is_person_exempt(rel):
            issues.append(Issue(rel, n, "ERROR", "example person name in text",
                                "use a placeholder such as Doctor <name> or <patient_name>"))
        if PHONE_RE.search(line):
            issues.append(Issue(rel, n, "ERROR", "phone number in text",
                                "use {{var.business_phone}} or a placeholder such as <business_phone>"))
        if PIN_RE.search(line):
            issues.append(Issue(rel, n, "ERROR", "address with a PIN code",
                                "use {{var.clinic_address}} or a placeholder such as <address>"))
        if "{{var.company_name}}" in line and not COMPANY_OK.search(line):
            issues.append(Issue(rel, n, "WARN", "{{var.company_name}} used outside a welcome, closing or AI-disclosure line",
                                "say the hospital, our clinic, the lab or the centre, to match the business type"))
    return issues, fixes


def apply_fixes(path, fixes):
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    by_line = {}
    for n, s, e, rep in fixes:
        by_line.setdefault(n, []).append((s, e, rep))
    for n, items in by_line.items():
        text = lines[n - 1]
        for s, e, rep in sorted(items, reverse=True):
            text = text[:s] + "{{var." + rep + "}}" + text[e:]
        lines[n - 1] = text
    path.write_text("".join(lines), encoding="utf-8")


def run(root, targets, variables_path, denylist_path, fix=False, out=sys.stdout):
    """Scan and return (errors, warnings, fixed_count, issues_left)."""
    base_known = load_variables(variables_path)
    industry_known = {}
    denylist = load_denylist(denylist_path)
    files = collect_files(targets, root)
    all_issues, fixed = [], 0
    for f in files:
        ind = industry_of(f, root)
        if ind not in industry_known:
            industry_known[ind] = base_known | industry_variables(ind, root)
        known = industry_known[ind]
        issues, fixes = scan_file(f, known, denylist, root)
        if fix and fixes:
            apply_fixes(f, fixes)
            fixed += len(fixes)
            issues, _ = scan_file(f, known, denylist, root)
        all_issues.extend(issues)
    errors = [i for i in all_issues if i.level == "ERROR"]
    warns = [i for i in all_issues if i.level == "WARN"]
    for i in all_issues:
        print(i, file=out)
    if denylist is None:
        print("note: scripts/denylist.txt not found; client-name check skipped "
              "(phone and PIN checks still ran)", file=out)
    print(f"{len(files)} files scanned: {len(errors)} errors, {len(warns)} warnings"
          + (f", {fixed} fixed" if fix else ""), file=out)
    return len(errors), len(warns), fixed, all_issues


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fix", action="store_true", help="rewrite known old names to {{var.x}}")
    ap.add_argument("--paths", nargs="+", help="files or folders to scan instead of the default scope")
    ap.add_argument("--include-docs", action="store_true", help="also scan docs/ and the README files")
    ap.add_argument("--root", default=str(ROOT))
    ap.add_argument("--variables", default=None)
    ap.add_argument("--denylist", default=None)
    args = ap.parse_args(argv)
    root = Path(args.root)
    targets = args.paths or list(DEFAULT_SCOPE) + (list(DOCS_SCOPE) if args.include_docs else [])
    variables = args.variables or root / "docs" / "shared" / "variables.json"
    denylist = args.denylist or root / "scripts" / "denylist.txt"
    errors, _, _, _ = run(root, targets, variables, denylist, fix=args.fix)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
