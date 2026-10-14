# Real estate v1 sign-off (scoped)

No eval.json (DECISIONS 108). Quality is checked with check_variables.py, check_fixed_lines.py and manual /prompt-writer tests. This sign-off exists so the README shows the skill as Done and /prompt-writer offers it. It covers the tests listed below and nothing else.

## Manual tests done

| Profile | Direction | Saved output | check_variables | check_fixed_lines |
|---|---|---|---|---|
| 01 builder inbound | inbound | sentence-tests/01-builder-inbound.md | 0 errors, 0 warnings | 27 required, 0 missing |
| 04 outbound, no assistant name | outbound | sentence-tests/04-outbound-no-assistant-name.md | 0 errors, 0 warnings | 21 required, 1 missing (see Known items) |

Section 6 word counts: profile 01 = 402, profile 04 = 335 (budget 595).

## Not done yet

- Profiles 02 (broker inbound with six rule-breaking client requests), 03 (advisory outbound with assistant name, calls recorded) and 05 (rental inbound) have not been generated.
- The tricky-caller tables of the profiles have not been played against the generated prompts. No safety case has been run as a simulated call; the checks so far read the Instructions text only.
- The owner has not reviewed the DPDP purpose line, the After-the-call message content or the outbound closing (DECISIONS 110 item 8).

## Known items

- Profile 04 reports "Is there anything else I can help with?" as missing. That line is the "Not wanted" row of the confirmation table in core.md, which names no channel, so the checker requires it even when no confirmation channel is set and the flow is left out. The skill leaves the flow out when no channel is given, so the line is absent. A fix is a source change (mark the row with confirmation_channels in core.md) or a skill change; neither is made here.
- The industry is not locked (.claude/locked-industries.json). Lock it after the remaining profiles are run.
