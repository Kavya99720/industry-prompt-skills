#!/usr/bin/env python
"""Validate one eval.json. Usage: python scripts/validate_eval.py <path>

Exits 0 if valid, 1 with one message per problem otherwise. Standard library only.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAX_BASELINE_ONLY = 5
BASELINE_RE = re.compile(r"^\*\*Baseline B-\d+")

REQUIRED_TOP = ("industry", "version", "frozen", "checks")
SEVERITIES = ("critical", "major", "minor")
TYPES = ("prompt", "behaviour")


def industry_files(industry_dir):
    """brief.md plus core.md and workflows/*.md, where an industry has split its brief."""
    files = [industry_dir / "brief.md", industry_dir / "core.md"]
    files += sorted((industry_dir / "workflows").glob("*.md"))
    return [f for f in files if f.is_file()]


def parse_rules(texts):
    """Return {rule_id: {"severity": str, "baseline_only": bool}} from table rows `| R-xx | ... |`."""
    rules = {}
    for text in texts:
        for line in text.splitlines():
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 3 or not re.match(r"R-\d+$", cells[0]):
                continue
            severity = next((c for c in cells[2:] if c in SEVERITIES), None)
            if severity is None:
                continue
            rules[cells[0]] = {"severity": severity, "baseline_only": bool(BASELINE_RE.match(cells[1]))}
    return rules


def validate(path, root=None):
    root = Path(root) if root else ROOT
    errors = []
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as e:
        return [f"cannot read {path}: {e}"]
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        return [f"invalid JSON: {e}"]
    if not isinstance(data, dict):
        return ["top level must be a JSON object"]

    for key in REQUIRED_TOP:
        if key not in data:
            errors.append(f"missing top-level key: {key}")
    checks = data.get("checks")
    if "checks" in data and not isinstance(checks, list):
        errors.append("'checks' must be a list")
        checks = None

    industry = data.get("industry")
    brief_text = None
    rules = {}
    if isinstance(industry, str) and industry:
        parts = [f.read_text(encoding="utf-8") for f in industry_files(root / "industries" / industry)]
        if parts:
            brief_text = chr(10).join(parts)
            rules = parse_rules(parts)

    if checks is None:
        return errors
    if not 20 <= len(checks) <= 30:
        errors.append(f"expected 20-30 checks, found {len(checks)}")

    seen = set()
    for i, c in enumerate(checks):
        if not isinstance(c, dict):
            errors.append(f"checks[{i}] must be an object")
            continue
        cid = c.get("id")
        label = cid if isinstance(cid, str) and cid else f"checks[{i}]"
        if not isinstance(cid, str) or not cid:
            errors.append(f"{label}: missing or empty id")
        elif cid in seen:
            errors.append(f"{label}: duplicate id")
        else:
            seen.add(cid)

        rule_ids = c.get("rule_ids")
        if not isinstance(rule_ids, list) or not rule_ids:
            errors.append(f"{label}: rule_ids must be a non-empty list")
            rule_ids = []
        if c.get("severity") not in SEVERITIES:
            errors.append(f"{label}: severity must be one of {', '.join(SEVERITIES)}")
        ctype = c.get("type")
        if ctype not in TYPES:
            errors.append(f"{label}: type must be one of {', '.join(TYPES)}")
        for field in ("description", "pass_criteria"):
            v = c.get(field)
            if not isinstance(v, str) or not v.strip():
                errors.append(f"{label}: missing or empty {field}")

        if ctype == "behaviour":
            p = c.get("probe")
            if not isinstance(p, str) or not p.strip():
                errors.append(f"{label}: behaviour check needs a non-empty probe")
        elif ctype == "prompt" and "probe" in c:
            errors.append(f"{label}: prompt check must not have a probe")

        if brief_text is not None:
            scenario_ids = c.get("scenario_ids", [])
            if not isinstance(scenario_ids, list):
                errors.append(f"{label}: scenario_ids must be a list")
                scenario_ids = []
            for rid in rule_ids:
                if rid not in brief_text:
                    errors.append(f"{label}: rule_id {rid} not found in industries/{industry}/brief.md")
            for sid in scenario_ids:
                if sid not in brief_text:
                    errors.append(f"{label}: scenario_id {sid} not found in industries/{industry}/brief.md")

    if brief_text is not None and rules:
        covered = {r for c in checks if isinstance(c, dict) and isinstance(c.get("rule_ids"), list) for r in c["rule_ids"]}
        for rid, info in sorted(rules.items()):
            if info["severity"] == "critical" and rid not in covered:
                errors.append(f"critical rule {rid} has no check")
        baseline_only = [
            c.get("id", f"checks[{i}]") for i, c in enumerate(checks)
            if isinstance(c, dict) and isinstance(c.get("rule_ids"), list) and c["rule_ids"]
            and all(rules.get(r, {}).get("baseline_only") for r in c["rule_ids"])
        ]
        if len(baseline_only) > MAX_BASELINE_ONLY:
            errors.append(
                f"{len(baseline_only)} checks map only to baseline rules (max {MAX_BASELINE_ONLY}): "
                + ", ".join(baseline_only)
            )
    return errors


def main():
    if len(sys.argv) != 2:
        print("usage: python scripts/validate_eval.py <path>", file=sys.stderr)
        return 1
    errors = validate(sys.argv[1])
    if errors:
        print(f"{sys.argv[1]}: {len(errors)} problem(s)", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1
    print(f"{sys.argv[1]}: valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
