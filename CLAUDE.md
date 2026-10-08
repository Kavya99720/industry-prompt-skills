# Industry Prompt Skills (CEL-53)
Prompt-writing skills for 10 industries (pharmacy, healthcare, retail, finance, education, logistics, hr, banking, real-estate, travel). Each skill generates system prompts for voice/chat agents. Each industry has an eval.json of 20-30 compliance checks. Generated prompts are validated against the evals; failures are fixed in the skill until all evals pass. This folder is separate from the platform codebase.

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
grill-me -> brainstorm -> spec-first (brief) -> plan mode approval -> industry agent builds brief, test profiles -> write-evals (then frozen) -> write skill -> run-evals (eval-judge grades) -> fix the SKILL for failures -> re-run until all pass -> release-check.

## Rules
- Never edit a frozen eval.json to make a prompt pass. Fix the skill instead. Only change an eval if it is genuinely wrong, and record why in docs/DECISIONS.md.
- Synthetic examples only. Never use real customer, patient or company data.
- Never add Co-Authored-By or any AI attribution to commits. Commit only when I ask. Never push.