# eval.json schema (all industries)

One format for every industry. File: `industries/<slug>/eval.json`. Validated by `scripts/validate_eval.py`. Written by the write-evals skill, then frozen.

## Format

```json
{
  "industry": "healthcare",
  "version": 1,
  "frozen": false,
  "checks": [
    {
      "id": "HLT-E01",
      "rule_ids": ["R-03"],
      "scenario_ids": ["S-02"],
      "severity": "critical",
      "type": "prompt",
      "description": "what is being checked",
      "pass_criteria": "exact, objective condition an independent grader can mark PASS or FAIL"
    },
    {
      "id": "HLT-E02",
      "rule_ids": ["R-05"],
      "scenario_ids": ["S-04"],
      "severity": "major",
      "type": "behaviour",
      "description": "what is being checked",
      "pass_criteria": "exact, objective condition on the agent's reply",
      "probe": "a synthetic caller message"
    }
  ]
}
```

## Fields

**Top level (all required)**
- `industry`: the folder slug (pharmacy, healthcare, retail, finance, education, logistics, hr, banking, real-estate, travel).
- `version`: integer, starting at 1.
- `frozen`: `true` once approved. A frozen file is never edited to make a prompt pass. Only a genuinely wrong eval may change, and the reason is recorded in docs/DECISIONS.md.
- `checks`: a list of 20 to 30 checks.

**Each check**
- `id`: unique, `<PREFIX>-E01`, `-E02`, ... without gaps. Prefixes: PHA, HLT, RET, FIN, EDU, LOG, HR, BNK, RE, TRV.
- `rule_ids`: non-empty list of IDs that exist in the industry's brief.md. A baseline rule is checked through the industry brief's own R-xx ID, which points to docs/shared/baseline-rules.md.
- `scenario_ids`: list of S-xx IDs from the brief. May be empty only if no scenario fits.
- `severity`: `critical`, `major` or `minor`, taken from the rule. A check covering several rules takes the highest.
- `type`: `prompt` (checks the system prompt text) or `behaviour` (checks the agent's reply to a probe).
- `description`: what is checked.
- `pass_criteria`: the exact condition for PASS.
- `probe`: required when `type` is `behaviour`, and must be absent for `prompt`.

## Rules for a valid file
- Valid JSON: double quotes, no comments, no trailing commas.
- Every critical rule in the brief is covered by at least one check.
- One thing per check. Pass criteria are objective, with no terms such as "appropriate" or "helpful" unless defined.
- Synthetic data only.

## Results
Runs are recorded under `industries/<slug>/results/<YYYY-MM-DD-runN>/`, with a `summary.json` containing `"failed": <n>`, and a one-line `history.md` in `industries/<slug>/results/`.
