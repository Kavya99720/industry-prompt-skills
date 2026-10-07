#!/usr/bin/env python
"""Validate one eval.json. Usage: python scripts/validate_eval.py <path>

Exits 0 if valid, 1 with one message per problem otherwise. Standard library only.
"""
import json
import sys
from pathlib import Path

REQUIRED_TOP = ("industry", "version", "frozen", "checks")
SEVERITIES = ("critical", "major", "minor")
TYPES = ("prompt", "behaviour")


def validate(path):
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
    if isinstance(industry, str) and industry:
        brief = Path(__file__).resolve().parent.parent / "docs" / "industries" / f"{industry}.md"
        if brief.exists():
            brief_text = brief.read_text(encoding="utf-8")

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
                    errors.append(f"{label}: rule_id {rid} not found in docs/industries/{industry}.md")
            for sid in scenario_ids:
                if sid not in brief_text:
                    errors.append(f"{label}: scenario_id {sid} not found in docs/industries/{industry}.md")
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
