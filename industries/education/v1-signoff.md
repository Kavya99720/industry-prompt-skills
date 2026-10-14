# Education v1 sign-off

No eval.json and no eval runs (DECISIONS 108). Quality was checked with check_variables.py, check_fixed_lines.py and a reading of each generated output against its profile. All six test profiles were generated from the education-prompt-writer skill's text and its references and saved in `sentence-tests/`.

## Results

| Profile | Direction | Saved output | check_variables | check_fixed_lines | Section 6 words |
|---|---|---|---|---|---|
| 01 school inbound, links on, default student-data rule | inbound | 01-school-inbound.md | 0 errors, 0 warnings | 30 required, 0 missing | 594 |
| 02 college inbound, hostel, anti-ragging contact, staff-verify rule, calls recorded | inbound | 02-college-inbound.md | 0 errors, 0 warnings | 22 required, 0 missing | 578 |
| 03 coaching inbound, demo booking on | inbound | 03-coaching-inbound-demo-booking.md | 0 errors, 0 warnings | 25 required, 0 missing | 593 |
| 04 edtech outbound counselling, with assistant name, recorded | outbound | 04-edtech-outbound-counselling.md | 0 errors, 0 warnings | 36 required, 0 missing | 424 |
| 05 outbound fee reminder, no assistant name, one client request refused | outbound | 05-outbound-fee-reminder-no-assistant-name.md | 0 errors, 0 warnings | 30 required, 0 missing | 473 |
| 06 preschool and daycare inbound, pickup rule | inbound | 06-preschool-inbound-pickup.md | 0 errors, 0 warnings | 22 required, 0 missing | 577 |

Section 6 is under the 595-word budget on every profile. The checker reads each profile's own settings (booking, send link, callback, calls recorded, confirmation channels, transfer targets, contact-source wording). Profile 05's request for an exam-hall threat is refused and listed in its draft notes. Profile 04 carries the recording sentence only in the welcome; profiles 01, 03, 05 and 06 never say the call is recorded; profile 02 says it once inside section 5. Profile 05's wrong-person answer is the wrong-person line followed by the callback line, then the call ends, with none of the banned words. Profile 06 carries the pickup line word for word in sections 1 and 6.

## Safety lines checked in every output

"Call 1 1 2 right now.", "Childline: 1 0 9 8." (in the immediate block after the first line, and alone for a concern that is not immediate), "Tele-MANAS: 1 4 4 1 6. Emergency: 1 0 8 or 1 1 2.", the privacy line for student details, the child line, the promise line, the payment decline with the scam warning and the bank line (cybercrime helpline 1 9 3 0), all in Latin digits with spaces. "I'll connect you to our team." is inline in every transfer and written only because every profile has a target.

## What was not done

The tricky-caller tables of the profiles were not played as simulated calls. The checks read the Instructions text only; no safety case has been run as a conversation. The six outputs were assembled in the main session from the skill's text and the references with a script, with the profile's hidden caller tables already known, not in isolated runs, so the checks prove the fixed lines and the structure, not how a fresh run reads the profile. No profile uses callback OFF, a "portal link" student-data rule, or a business with no target (callback only); those branches are written in the skill and the checker's tests but were not generated. Workflows 07 (online classes and technical help), 10 (admission follow-up) and 13 (event or PTM reminder) have no profile of their own and were checked by reading their rules only. The owner has not reviewed the scam warning for fake admission offers ("expert review recommended" is in every draft note), the DPDP purpose line and the treatment of a child's data, the After-the-call message content, or the outbound closing.

## Known items

Open platform questions stay as written in the brief: there is no student lookup (approved: the agent states no student detail and offers a callback, or the transfer or link the sharing rule names); whether the booking tool fits a demo class or counselling slot; whether contact_name and call_details are passed on outbound calls; voicemail detection and a do-not-call tool. The wrong-person callback line ("Our team can call back during office hours.") is approved (DECISIONS 118). scripts/check_fixed_lines.py knows education (DECISIONS 118); the required lines of the other industries are unchanged (61,440 combinations compared before and after: no difference).

## Lock

Education is added to `.claude/locked-industries.json`. Unlock only when the owner says "unlock education".
