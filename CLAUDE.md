# Industry Prompt Skills (CEL-53)
Prompt-writing skills for 8 industries (pharmacy, healthcare, retail, education, logistics, hr, banking, real-estate). Each skill generates system prompts for voice/chat agents. Pharmacy, healthcare and banking each have an eval.json of 20-30 compliance checks; generated prompts are validated against the evals and failures are fixed in the skill. The remaining industries (retail, education, logistics, hr, real-estate) get NO eval.json and no eval runs (docs/DECISIONS.md 108): quality is checked with check_variables.py, check_fixed_lines.py and manual /prompt-writer tests. This folder is separate from the platform codebase.

## Layout
- industries/<industry>/brief.md — industry brief (scenarios S-xx, rules R-xx)
- industries/<industry>/eval.json — compliance checks
- industries/<industry>/results/ — recorded eval runs
- .claude/skills/<industry>-prompt-writer/ — industry prompt-writing skills (deliverable: SKILL.md + references/)
- .claude/skills/ — workflow skills (grill-me, brainstorm, spec-first, write-evals, run-evals, release-check)
- .claude/agents/<industry>-agent.md — one domain subagent per industry (writes only inside its own industries/<industry>/ and its skill folder); eval-judge.md — shared neutral grader
- industries/<industry>/ also holds core.md, workflows/ and test-profiles/ (healthcare is the template); docs/shared/ also holds platform-contract.md, variables.json and reference/
- scripts/ — check_variables.py (variables and client-name check), validate_eval.py, run_evals.py (--industry <x> or --all), status.py
- docs/shared/baseline-rules.md — rules common to all voice agents; docs/shared/eval-schema.md — the one eval.json format
- docs/DECISIONS.md — decisions log

## Workflow per industry
grill-me -> brainstorm -> spec-first (brief) -> plan mode approval -> industry agent builds brief, test profiles -> write skill -> check_variables, check_fixed_lines, manual /prompt-writer tests -> fix the SKILL -> release-check. (Pharmacy, healthcare and banking followed the eval path: write-evals (then frozen) -> run-evals (eval-judge grades) -> fix the SKILL for failures -> re-run.)

Starter material for the 6 remaining industries: docs/shared/new-industry-template/ (start with its README.md) and docs/shared/prompting-guide.md. Healthcare and pharmacy are finished (Done v1) and locked.

### Workflow rules
- One grill-me at a time. Save it to industries/<x>/grill-me.md before the next industry's grill-me starts. An industry agent reads only its own grill-me.md.
- One commit per industry. The commit message starts with the industry name (for example "banking: brief and test profiles").
- Targeted reruns first (`--profiles`, `--cases`); one full run at the end, continued with `--resume` if it is cut.
- Finish line (industries with evals): a full run at 95% or better and no failure on a safety case (emergency, prescription or controlled items, privacy or verification, payment details, and any clinical or financial advice case). Then add industries/<x>/v1-signoff.md and lock the industry.
- Finish line (industries without eval.json): check_variables.py and check_fixed_lines.py pass, and manual /prompt-writer tests on the test profiles show no failure on a safety case. Then add industries/<x>/v1-signoff.md (it lists the manual tests done) and lock the industry. The README status table shows N/A for Evals, Last run and Pass rate, and Done for Skill.
- Isolation is enforced by hooks: an industry subagent writes only inside industries/<its-industry>/ and .claude/skills/<its-industry>-prompt-writer/. Industries listed in .claude/locked-industries.json (healthcare, pharmacy) cannot be edited by anyone; remove an industry from that file only when I say "unlock <industry>", and lock it again when the work is done.
- scripts/check_variables.py also fails on leakage: a term from another industry (scripts/leakage_terms.json) in an industry's files. Legitimate cross-references go in the allow list with a reason.

## Rules
- Never edit a frozen eval.json to make a prompt pass. Fix the skill instead. Only change an eval if it is genuinely wrong, and record why in docs/DECISIONS.md.
- Synthetic examples only. Never use real customer, patient or company data.
- Never add Co-Authored-By or any AI attribution to commits. Commit only when I ask. Never push.