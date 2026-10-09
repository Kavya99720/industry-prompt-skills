# New-industry template

Start point for the 8 industries still to build (retail, finance, education, logistics, hr, banking, real-estate, travel). Healthcare and pharmacy are finished (Done v1) and locked; copy their LAYOUT from this template, never their content, and never edit them.

Everything below comes from building healthcare and pharmacy (docs/DECISIONS.md entries 29 to 56). Each lesson is already written as a rule in the template files, with its scope.

## Files

| File | Use |
|---|---|
| [core.template.md](core.template.md) | industries/<x>/core.md: tools, intake, the common rules (R-xx) with scope, fixed lines, scenarios |
| [workflow.template.md](workflow.template.md) | one workflow file under industries/<x>/workflows/ |
| [section-bases.template.md](section-bases.template.md) | industries/<x>/section-bases.md: welcome, sections 1 to 5, output markers |
| [skill.template.md](skill.template.md) | .claude/skills/<x>-prompt-writer/SKILL.md skeleton |
| [test-profile.template.md](test-profile.template.md) | industries/<x>/test-profiles/NN-*.md |
| [../confirmation-flow.md](../confirmation-flow.md) | the confirmation flow, copied into the industry's core with its scope |
| [../prompting-guide.md](../prompting-guide.md) | the rules, the risk and tone table for all 10 industries, Sarvam's guidance |

## Build order (one industry at a time)

1. grill-me, saved to industries/<x>/grill-me.md before the next industry starts. The agent reads only its own grill-me.md.
2. brainstorm, then the brief (spec-first): scope, scenarios S-xx, rules R-xx, vocabulary, escalation, data handling. Plan approved by the owner.
3. The industry agent builds core.md, workflows/, variables.json (custom details only), section-bases.md, test-profiles/.
4. write-evals (20 to 30 checks), approved by the owner, then frozen.
5. The skill, then `python scripts/build_skill_refs.py --industry <x>`.
6. Targeted reruns first (`--profiles`, `--cases`), fix the SKILL for failures, never the eval. One full run at the end with `--resume`.
7. Finish line: at least 95% and no failure on a safety case. Then `industries/<x>/v1-signoff.md` and a lock entry in `.claude/locked-industries.json`.

One commit per industry; the message starts with the industry name.

## Lessons, as rules (all are in core.template.md and skill.template.md)

1. Priority when rules meet: emergency, privacy and verification, "say exactly" lines, one question at a time, the task.
2. Output markers: `=== INSTRUCTIONS ===` and `=== DRAFT NOTES ===`, each alone on its own line, each once, never inside a sentence. The first line of the output is the INSTRUCTIONS marker, the next is the welcome.
3. Fixed-line format: say exactly "X", then the action in the same reply. A fixed line keeps its own full stop; a follow-up question is a separate sentence.
4. Every rule states its scope: when it applies and when it does not. Fixed phrases never override safety rules or required lines.
5. Helpline and emergency numbers are spoken digit by digit with spaces ("1 0 8"); never hyphens, never grouped digits, never words.
6. Never say back a sensitive detail the caller mentions (a condition, an amount, a balance); acknowledge with "I understand." and hand off.
7. Wrong person on an outbound call: a fixed line, a banned-words list, never the purpose, then end the call.
8. The no-collect list is named item by item for the industry (government IDs, card, bank or UPI details, OTP, PIN, passwords, payment details and so on).
9. A missing config value is "not provided - the team will confirm"; the draft notes list every intake item with its value or default, and mark an item "not used in these Instructions" only in the Fill table's note column.
10. The handoff phrase "I'll connect you to our team." is for staff handoffs only. No transfer target means a callback, never a transfer.
11. Confirmations and links follow docs/shared/confirmation-flow.md: sent by the After-the-call trigger, no in-call tool, only channels enabled in config.
12. "calling from" appears only in outbound Instructions. The welcome matches the call direction.
13. Variables only from docs/shared/variables.json or industries/<x>/variables.json. The company name only where the caller hears it: welcome, closing, AI-disclosure answer, voicemail line.
14. Word budget: section 6 (Main prompt) at most 595 words (20 under the 615 allowance); universal behaviour goes to sections 1, 4 and 5, and a long how-to can sit in section 5.
15. Evals: at most 5 checks map only to baseline rules; the rest test the industry's own critical risks. A critical rule without a check fails `validate_eval.py`, so a wording-only rule is major and its critical behaviour stays under the parent rule. Never loosen an eval; if one conflicts with a rule, show the owner the case text first.
16. Leakage: a term that belongs to another industry (scripts/leakage_terms.json) must not appear in your files unless it is a listed cross-reference. Do not copy another industry's cases or wording.

## Harness facts to remember

- The simulated agent sees the Instructions plus a note with the profile's variable values; probe placeholders (<customer_name>, <order_number>) are filled from the profile's hidden "## Test values" section.
- A profile whose Instructions come out empty after splitting is a harness error, not a skill failure.
- Runs write per-profile files, so `--resume` continues a cut run; the runner waits 60 s and retries on auth or network errors.
- The lint reports fixed lines missing word for word, stray text outside the markers, and a prescription or upload route the profile does not enable.
