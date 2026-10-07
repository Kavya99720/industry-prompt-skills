---
name: write-evals
description: 'Turn one industry''s approved brief (docs/industries/<industry>.md) into evals/<industry>/eval.json with 20-30 objective compliance checks (prompt and behaviour types), show them for approval, then save and freeze. Stops if the brief is missing. Never modifies a frozen eval.json. Never writes the industry skill.'
---

# Write Evals

Write the compliance checks for ONE industry from its approved brief. After approval the file is frozen: generated prompts are fixed to pass it, never the reverse.

## Before You Start

- Confirm which ONE industry. If the user did not name it, ask. Never write evals for two industries in one run.
- Read `docs/industries/<industry>.md`. If it is missing, STOP and tell the user to run spec-first first. Do not write checks from memory or from the grill-me or brainstorm files alone.
- Check `evals/<industry>/eval.json`. If it exists and has `"frozen": true`, STOP: do not modify it. Tell the user it is frozen. If it exists and is not frozen, ask before replacing it.
- Use the brief's S-xx and R-xx IDs exactly as written. Do not invent IDs. Use synthetic data only; never real customer, patient or company data.
- The brief's open questions are not settled. Do not write checks that depend on an unresolved item; mention it to the user instead.

## File Format

```json
{
  "industry": "<industry>",
  "version": 1,
  "frozen": false,
  "checks": [
    {
      "id": "<PREFIX>-E01",
      "rule_ids": ["R-03"],
      "scenario_ids": ["S-02"],
      "severity": "critical",
      "type": "prompt",
      "description": "what is being checked",
      "pass_criteria": "exact, objective condition an independent grader can mark PASS/FAIL"
    },
    {
      "id": "<PREFIX>-E02",
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

- `<PREFIX>` is a short uppercase industry code (for example PHA, HLT, RET, FIN, EDU, LOG, HR, BNK, RE, TRV). IDs are `<PREFIX>-E01`, `-E02`, ... unique and without gaps.
- `severity` is `critical`, `major` or `minor`, taken from the rule it checks. If a check covers several rules, use the highest severity.
- `type` is `prompt` or `behaviour`. `probe` is required for `behaviour` and must be absent for `prompt`.
- `rule_ids` and `scenario_ids` are arrays of IDs that exist in the brief. Every check lists at least one rule ID. Use an empty `scenario_ids` array only if no scenario fits.
- Write valid JSON: double quotes, no comments, no trailing commas.

## What Makes a Good Check

- **Count:** 20 to 30 checks in total.
- **Coverage:** every `critical` rule in the brief is covered by at least one check. Cover major rules as far as the count allows, and say which major or minor rules are left without a check.
- **Mix of types:**
  - `prompt` checks verify that the system prompt itself contains the right instruction (for example, it tells the agent to disclose it is an AI, or names the escalation path).
  - `behaviour` checks give the agent a probe and judge its reply. Include adversarial probes from the brainstorm (prompt injection, requests for other people's data, pressure to break rules) and high-risk scenarios.
  - Every critical rule should ideally have both a prompt check and a behaviour check, count permitting.
- **Objective pass criteria:** state the exact condition that means PASS, so an independent grader (eval-judge) with no other context reaches the same verdict. Name what the reply must contain or must not contain. Avoid vague terms such as "appropriate", "helpful" or "polite" unless defined.
- **One thing per check.** Do not bundle several rules into one pass criterion.
- **Probes:** realistic, short, synthetic caller messages. For a voice agent, write them as the caller would speak. Do not put the expected answer in the probe.
- Do not add checks that have no rule in the brief.

## Review and Save

- Show the checks as a table with columns: ID, type, severity, rule IDs, scenario IDs, description, pass criteria, probe (for behaviour). Add a short coverage summary: total count, count by type and severity, critical rules covered, rules not covered.
- Ask for approval with `AskUserQuestion` (for example: approve and freeze, request changes). Take specific edits from a freeform answer.
- Apply changes, re-check the rules above (count, unique IDs, critical coverage, probe presence), and show the revised table if the changes were significant.
- Only after explicit approval, write `evals/<industry>/eval.json` with `"frozen": true`. Create the folder if needed. Save as valid JSON and parse it back to confirm it is valid.

## Frozen Files

- Never modify a frozen `eval.json`, and never edit one to make a prompt pass.
- If a check seems genuinely wrong (for example it contradicts the brief or cannot be judged objectively), STOP and tell the user which check, why, and what change you would propose. Do not edit the file.
- Record the reason in `docs/DECISIONS.md` only after the user agrees, and only then change the eval, as the user directs.

Never write the industry skill or edit any other file. The `eval.json` is the only output beyond the conversation.
