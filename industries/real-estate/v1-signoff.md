# Real estate v1 sign-off

No eval.json and no eval runs (DECISIONS 108). Quality was checked with check_variables.py, check_fixed_lines.py and a reading of each generated output against its profile. All five test profiles were generated with the real-estate-prompt-writer skill and saved in `sentence-tests/`.

## Results

| Profile | Direction | Saved output | check_variables | check_fixed_lines | Section 6 words |
|---|---|---|---|---|---|
| 01 builder inbound | inbound | 01-builder-inbound.md | 0 errors, 0 warnings | 27 required, 0 missing | 402 |
| 02 broker inbound, six rule-breaking client requests | inbound | 02-broker-inbound.md | 0 errors, 0 warnings | 16 required, 0 missing | 337 |
| 03 advisory outbound, with assistant name | outbound | 03-advisory-outbound.md | 0 errors, 0 warnings | 26 required, 0 missing | 365 |
| 04 outbound, no assistant name | outbound | 04-outbound-no-assistant-name.md | 0 errors, 0 warnings | 20 required, 0 missing | 335 |
| 05 rental inbound | inbound | 05-rental-inbound.md | 0 errors, 0 warnings | 21 required, 0 missing | 326 |

Section 6 is under the 595-word budget on every profile. pytest and `status.py --check` pass; the skill references are in sync with the sources. Profile 02's six client requests are refused or adapted and listed in its draft notes.

## What was not done

The tricky-caller tables of the profiles were not played as simulated calls. The checks read the Instructions text only; no safety case has been run as a conversation. The owner has not reviewed the DPDP purpose line, the After-the-call message content or the outbound closing (DECISIONS 110 item 8).

## Changes since the first sign-off (DECISIONS 111)

- The outbound welcome with calls recorded puts the recording sentence before the question "Is this a good time to talk?". Profile 03 was regenerated; profiles 01, 02, 04 and 05 are unchanged (04 is not recorded, so it has no recording sentence).
- check_fixed_lines: a row naming several settings is required only when all are on (profile 05's email link line); the not-known source line is required only when no lead-source wording is given (profile 03); the "Not wanted" row needs a confirmation channel (profile 04). Tests added; no other industry's required lines changed.
- All five profiles now report 0 missing. The two earlier known items were checker false positives and are closed.

## Known items

Open platform questions stay as written in the brief: whether the booking tool fits a site visit, whether lead_name and lead_source are passed, voicemail detection and a do-not-call tool.

## Lock

Real estate is added to `.claude/locked-industries.json`. Unlock only when the owner says "unlock real-estate".
