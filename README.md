# Industry Prompt Skills (CEL-53)

Prompt-writing skills for 10 industries: pharmacy, healthcare, retail, finance, education, logistics, hr, banking, real-estate, travel. Each skill generates system prompts for voice and chat agents. Each industry has an eval.json of 20-30 compliance checks. Generated prompts are validated against the evals, and failures are fixed in the skill until all evals pass. This folder is separate from the platform codebase.

## Layout

```
industries/<slug>/brief.md            scenarios (S-xx), rules (R-xx), vocabulary, escalation, data handling, open questions
industries/<slug>/eval.json           20-30 compliance checks (frozen once approved)
industries/<slug>/results/            recorded validation runs
.claude/skills/<slug>-prompt-writer/  the industry skill (SKILL.md + references/)
.claude/skills/                       workflow skills: grill-me, brainstorm, spec-first, write-evals, run-evals, release-check
.claude/agents/                       eval-judge (shared neutral grader)
.claude/hooks/                        frozen-eval guard and eval validation
docs/shared/baseline-rules.md         rules common to ALL voice agents
docs/shared/eval-schema.md            the one eval.json format
docs/DECISIONS.md                     decisions log
scripts/validate_eval.py              eval.json validator
tests/                                pytest suite
```

## Workflow per industry

grill-me -> brainstorm -> spec-first (brief) -> plan approval -> expert researches rules -> write-evals (then frozen) -> write the skill -> run-evals (eval-judge grades) -> fix the SKILL for failures -> re-run until all pass -> release-check -> commit.

Rules:
- Never edit a frozen eval.json to make a prompt pass. Fix the skill instead. Only change an eval if it is genuinely wrong, and record why in docs/DECISIONS.md.
- Synthetic examples only. Never use real customer, patient or company data.

## Status

| Industry | Brief | Skill | eval.json | Validated | Evals passing |
|----------|-------|-------|-----------|-----------|---------------|
| pharmacy | todo | todo | todo | todo | todo |
| healthcare | done | draft (smoke-tested, not eval-validated) | todo | todo | todo |
| retail | todo | todo | todo | todo | todo |
| finance | todo | todo | todo | todo | todo |
| education | todo | todo | todo | todo | todo |
| logistics | todo | todo | todo | todo | todo |
| hr | todo | todo | todo | todo | todo |
| banking | todo | todo | todo | todo | todo |
| real-estate | todo | todo | todo | todo | todo |
| travel | todo | todo | todo | todo | todo |

## Development

```
python -m pip install -r requirements-dev.txt
python -m pytest -q
python scripts/validate_eval.py industries/<slug>/eval.json
```
