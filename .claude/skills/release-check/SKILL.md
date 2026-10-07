---
name: release-check
description: 'Pre-commit gate for this repo. Checks pytest, eval.json validity, per-industry completeness, frozen-eval changes, personal data or secrets in the diff, .env tracking, the commit message, and a clean tree after commit. Reports a PASS/FAIL table with evidence. If any item fails, stops and does not commit. Use only when the user asks to commit.'
---

# Release Check

Run before ANY commit. Report a PASS/FAIL table with evidence, then commit only if every item passes. Never push. Never add Co-Authored-By or any AI attribution to the commit.

## Before You Start

- Run only when the user has asked for a commit. Never commit on your own initiative.
- Work out what is being committed: `git status --short` and `git diff HEAD` (staged and unstaged). If there is no commit yet, treat every file as new. Untracked files the user wants committed count as part of the change; ask which ones if unclear.
- "Industries being committed" are the industries named in changed paths: `evals/<industry>/`, `docs/industries/<industry>.md`, `.claude/skills/<industry>-prompt/`, `.claude/agents/<industry>-expert.md`, `results/<industry>/`.
- This check is read-only. Fix nothing yourself; report failures and stop.

## Checks

For each item give PASS, FAIL or N/A, with evidence (command output, file path, id, or a short quote). An item with no evidence is FAIL.

1. **pytest.** If no test files exist (`test_*.py`, `*_test.py`, a `tests/` folder), N/A with "N/A - no tests yet". Otherwise run `pytest` and report the pass/fail counts. Any failure or error is FAIL.

2. **Eval files valid.** For EVERY `evals/*/eval.json` (not only the ones being committed): valid JSON; 20 to 30 checks; unique ids; every check has `id`, `rule_ids`, `scenario_ids`, `severity`, `type`, `description`, `pass_criteria`; `severity` is critical/major/minor; `type` is prompt/behaviour; `probe` present for behaviour and absent for prompt; at least one rule id per check; every rule id (and scenario id) exists in `docs/industries/<industry>.md`. Report per industry with the count and any offending id.

3. **Industry completeness.** For each industry being committed, all of these must exist: `docs/industries/<industry>.md`; `evals/<industry>/eval.json` with `"frozen": true`; `.claude/skills/<industry>-prompt/SKILL.md`; and at least one run folder in `results/<industry>/` whose `summary.json` has `"failed": 0`. Report per industry which parts are present. Check the latest run's `summary.json` too: if the most recent run has failures, FAIL even if an older run passed.

4. **Frozen evals untouched.** From `git diff HEAD --name-status -- evals/`, find any `eval.json` that is modified, renamed or deleted and was `"frozen": true` in HEAD (`git show HEAD:<path>`). A newly added file is not a modification. If one was modified, `docs/DECISIONS.md` must contain an entry for that industry's eval change with a reason; quote it. Otherwise FAIL. If there is no HEAD yet, this is N/A.

5. **No real personal data or secrets** in the diff and in new untracked files being committed. Search added lines for: phone numbers (other than obvious fakes such as 555-01xx or 0000000000), email addresses (other than example.com/example.org/test domains or obvious placeholders), Aadhaar-like (12 digits, optionally grouped 4-4-4) and PAN-like (`[A-Z]{5}[0-9]{4}[A-Z]`) numbers, card or account numbers, real-looking customer or patient names, and API keys or secrets (`sk-`, `AKIA`, `api_key`, `secret`, `token`, `password` followed by a value, private key headers). Report each hit with file and line, or "no matches" with the patterns searched. A hit that is clearly synthetic may be PASS only if you say why; if unsure, FAIL.

6. **.env not tracked.** `git ls-files` shows no `.env` or `.env.*` (other than a `.env.example` with no real values). Also confirm `.env` is in `.gitignore`; if it is not, FAIL.

7. **Commit message.** Draft the message and check it BEFORE committing: no `Co-Authored-By`, no "Generated with", no mention of Claude or AI attribution, no AI-tool signature. Show the exact message in the table. After committing, re-check with `git log -1 --format=%B`.

8. **Clean tree after commit.** After the commit, `git status --short` must be empty. Anything left over (including untracked files that were meant to be committed) is FAIL; report it and do not amend or force anything without asking.

## Flow

1. Run checks 1 to 7 before committing. Show the table.
2. If ANY item is FAIL, stop. Do not commit, do not stage fixes, and say what must change.
3. If all are PASS or N/A, commit with the checked message (stage only the files being committed). Then run the post-commit parts of 7 and 8 and show the final table.
4. If the post-commit check fails, report it. Do not rewrite history or push. Never push under any circumstances.

## Output

| # | check | result | evidence |
|---|-------|--------|----------|

End with one line: "Committed <short hash>" or "Not committed: <failed item numbers>".
