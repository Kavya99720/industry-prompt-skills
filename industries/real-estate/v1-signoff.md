# Real estate v1 sign-off

No eval.json and no eval runs (DECISIONS 108). Quality was checked with check_variables.py, check_fixed_lines.py and a reading of each generated output against its profile. All five test profiles were generated with the real-estate-prompt-writer skill and saved in `sentence-tests/`.

## Results

| Profile | Direction | Saved output | check_variables | check_fixed_lines | Section 6 words |
|---|---|---|---|---|---|
| 01 builder inbound | inbound | 01-builder-inbound.md | 0 errors, 0 warnings | 27 required, 0 missing | 402 |
| 02 broker inbound, six rule-breaking client requests | inbound | 02-broker-inbound.md | 0 errors, 0 warnings | 16 required, 0 missing | 337 |
| 03 advisory outbound, with assistant name | outbound | 03-advisory-outbound.md | 0 errors, 0 warnings | 27 required, 1 missing (known item 1) | 365 |
| 04 outbound, no assistant name | outbound | 04-outbound-no-assistant-name.md | 0 errors, 0 warnings | 20 required, 0 missing | 335 |
| 05 rental inbound | inbound | 05-rental-inbound.md | 0 errors, 0 warnings | 22 required, 1 missing (known item 2) | 326 |

Section 6 is under the 595-word budget on every profile. pytest and `status.py --check` pass; the skill references are in sync with the sources. Profile 02's six client requests are refused or adapted and listed in its draft notes.

## What was not done

The tricky-caller tables of the profiles were not played as simulated calls. The checks read the Instructions text only; no safety case has been run as a conversation. The owner has not reviewed the DPDP purpose line, the After-the-call message content or the outbound closing (DECISIONS 110 item 8).

## Known items

1. **Profile 03, source line.** check_fixed_lines requires "I don't have that detail with me. Would you like us to stop calling you?" on every outbound set. Profile 03 gives lead-source wording ("the advice request form on our website"), so the rule says the agent states that source and never uses the not-known line. The skill follows the rule, so the line is absent. The line is a fixed line of workflow 05 with no condition the checker can read.
2. **Profile 05, link line.** check_fixed_lines requires "You will get the link on email shortly." with sending links OFF and email set. The row names both `confirmation_channels` and `send_link`, and the checker treats a row as required when any named setting is on. The row needs both. No link exists in profile 05, so the line is correctly absent.
3. Fixed in this round: the "Not wanted" row of the confirmation table in core.md now names `confirmation_channels`, so "Is there anything else I can help with?" is required only when a channel is set (profile 04 went from 1 missing to 0).
4. Open platform questions stay as written in the brief: whether the booking tool fits a site visit, whether lead_name and lead_source are passed, voicemail detection and a do-not-call tool.

## Lock

Real estate is added to `.claude/locked-industries.json`. Unlock only when the owner says "unlock real-estate".
