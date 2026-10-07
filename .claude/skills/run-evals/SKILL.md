---
name: run-evals
description: 'Run ONE evaluation round for ONE industry: generate a system prompt with the <industry>-prompt skill, simulate agent replies to each behaviour probe in isolated subagents, have eval-judge grade every check, save the results under results/<industry>/, and propose SKILL.md fixes for failures. Stops if evals/<industry>/eval.json or .claude/skills/<industry>-prompt/SKILL.md is missing. Never edits eval.json.'
---

# Run Evals

Run one evaluation round for ONE industry. Generated prompts are fixed to pass the evals, never the reverse.

## Before You Start

- Confirm which ONE industry. If the user did not name it, ask. Never run two industries in one run.
- Check that BOTH files exist: `evals/<industry>/eval.json` and `.claude/skills/<industry>-prompt/SKILL.md`. If either is missing, STOP and say which one. Do not continue.
- Read `eval.json` once to know the check ids. Do not paste it, `pass_criteria` or any part of it into the prompt or into any reply-simulating subagent.
- Choose the sample business: use the synthetic one in `docs/industries/<industry>.md` unless the user specified another. Synthetic data only; never real customer, patient or company data.
- Choose the run id: today's date plus run number, `<YYYY-MM-DD>-run<N>`, where N is one higher than the existing run folders for that date in `results/<industry>/` (start at 1). Run folder: `results/<industry>/<YYYY-MM-DD-runN>/`. Never overwrite an existing run folder.

## Steps

1. **Generate the prompt.** Use the `<industry>-prompt` skill (via Skill) to write a system prompt for the sample business. Save it to `<run folder>/prompt.md`. Save only the prompt, with no commentary.

2. **Collect behaviour replies.** For every check with `"type": "behaviour"`:
   - If the user provided a replies file captured from the real platform, use it instead of simulating. Verify it has a reply for every behaviour check id; tell the user about any missing ones.
   - Otherwise, spawn a FRESH `general-purpose` subagent per check. Run them in parallel where possible. Its prompt contains ONLY: the full text of `prompt.md` as its instructions, and the check's `probe` as the caller message, with a request to reply as that agent would and return the reply verbatim. It must not see `eval.json`, `pass_criteria`, check descriptions, rule ids or the check id. Do not let one subagent see another's output.
   - Save all replies to `<run folder>/replies.json` as an object keyed by check id, value the reply verbatim.

3. **Grade.** Invoke the `eval-judge` subagent with the industry, the path to `prompt.md` and the path to `replies.json`. Do not give it your opinion of the results. Save its full output verbatim to `<run folder>/report.md`. Write `<run folder>/summary.json`:
   ```json
   {
     "run_id": "<YYYY-MM-DD-runN>",
     "industry": "<industry>",
     "date": "<YYYY-MM-DD>",
     "total": 0,
     "passed": 0,
     "failed": 0,
     "failed_checks": [{"id": "<PREFIX>-E01", "severity": "critical"}]
   }
   ```
   Take the counts and failed ids from the judge's report. Do not re-grade or override any verdict.

4. **Record history.** Append one line to `results/<industry>/history.md` (create it if missing, never rewrite earlier lines): `<run id> | <YYYY-MM-DD> | passed: X | failed: Y`.

5. **Report.**
   - If everything passed, say so and point to the run folder.
   - If anything failed: list each failure (id, severity, judge's reason, evidence), critical first. Then propose specific changes to `.claude/skills/<industry>-prompt/SKILL.md` only, each tied to the failed check ids it should fix. Then STOP and wait for the user's approval. Do not edit the skill before approval. After approval and edits, the user starts a new run, which is a new run folder.

## Rules

- Never edit `eval.json`, even if a check seems wrong. If one seems genuinely wrong, tell the user which check and why, and let them decide; any change must be recorded in `docs/DECISIONS.md`.
- Never edit prompt.md, replies.json or the judge's report after saving them.
- Never edit the industry skill without approval, and never commit or push.
- The only files this skill writes are inside the run folder and `results/<industry>/history.md`.
