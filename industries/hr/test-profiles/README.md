# HR test profiles

Six synthetic profiles, in-house HR deepest. Each is a business config, the selected workflows, client requirements, a hidden table of tricky callers (MUST and MUST NOT) and a hidden word-budget estimate. No eval (DECISIONS 108): quality is checked with check_variables.py, check_fixed_lines.py (using the profile) and a reading of each generated output against its tricky-caller table. All names, numbers, addresses and email addresses are synthetic.

| # | Profile | Direction | Workflows | What it tests |
|---|---|---|---|---|
| 01 | In-house HR, every setting on, recorded, POSH and ethics routes given | Inbound | 01, 02, 03, 04, 05 | Verification with the date of joining, the leave balance, sick leave, leave request "submitted", payroll boundary, resignation, POSH, ethics, distress versus self-harm, the claimed role, the job scam block |
| 02 | In-house HR, every setting off, one HR team target, POSH route but no ethics contact, no payroll dates | Inbound | 01, 02, 03, 04, 05 | The lookup-off line, callback notes, the missing-fact line, the missing-ethics route, a protected detail volunteered, emergency |
| 03 | Staffing agency, HR lookup on, three unsafe client requests | Inbound | 01, 03, 05, 06 | The safe second detail (the Aadhaar request refused), no outcome promised, no resume by voice, the scam block, staffing worker and client company, the age question, ethics |
| 04 | Payroll provider, no assistant name, recorded, balance lookup on | Inbound | 01, 02, 05, 06 | Published payroll dates only, no amounts, full-and-final, the claimed role, bank details refused, POSH |
| 05 | Training and background-verification vendor, no POSH route, no ethics contact, no transfer target, two unsafe client requests | Inbound | 01, 04, 05, 06 | Stage only for a check, the missing-route callback for harassment and ethics, the callback with no target, the crisis line with no target |
| 06 | Outbound interview reminder, assistant named, recorded, scheduling tool on | Outbound | 07, 08 | Welcome with disclosure and recording sentence before the question, wrong person, voicemail, stop request, source wording, no outcome on an outbound call |

Workflow 09 (outbound document follow-up and onboarding nudge) has no saved profile in this set: its rule R-32 is covered by the text of the workflow and the shared checks, and a hands-on test of it is still to be done.

The checks read the profile's own settings (tools, recording, transfer targets, contact-source wording) through scripts/check_fixed_lines.py `--profile`.
