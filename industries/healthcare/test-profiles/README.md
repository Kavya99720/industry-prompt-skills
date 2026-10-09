# Healthcare test profiles

Five synthetic profiles. Each has business config, selected workflows, client requirements and 4 to 7 tricky callers with expected MUST and MUST NOT. They are the inputs for scripts/run_evals.py (one generated Instructions set per profile).

| # | File | Business | Direction | Workflows |
|---|---|---|---|---|
| 01 | [01-multispeciality-hospital-inbound.md](01-multispeciality-hospital-inbound.md) | Multi-speciality hospital | Inbound | 01, 02, 03 |
| 02 | [02-single-doctor-clinic-walkin.md](02-single-doctor-clinic-walkin.md) | Single-doctor clinic, tokens or walk-in | Inbound | 01 |
| 03 | [03-outbound-reminders.md](03-outbound-reminders.md) | Clinic, outbound reminders | Outbound | 04, 03 |
| 04 | [04-unethical-client.md](04-unethical-client.md) | Clinic with unethical client requests | Inbound | 01, 02 |
| 05 | [05-incomplete-intake.md](05-incomplete-intake.md) | Small clinic, intake answers missing | Inbound | 01, 02 |

## Main prompt word budget

Budget: about 615 words for section 6 INCLUDING the roster (platform warning at 616). Words are whitespace-separated tokens in the draft `main-lines` blocks of core.md and the workflow files. The roster counts about 23 words per doctor. Sections 1 to 5 are not counted. These are estimates from drafts, not from a written skill.

Per-part words: core 65; Enquiry 81 (+25 token line); Booking 185; Reschedule and cancel 80 (+54 when Booking is not selected); Reminder 170.

| Profile | Core | Enquiry | Booking | Reschedule/cancel | Reminder | Extras | Doctors | Roster words | Total | Budget | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 Hospital inbound | 65 | 81 | 185 | 80 | 0 | 0 | 8 | 184 | **595** | 615 | OK (20 spare; confirmation flow moved to section 5, DECISIONS 53) |
| 02 Single-doctor walk-in | 65 | 81 | 0 | 0 | 0 | 25 (token line) | 1 | 23 | 194 | 615 | OK (421 spare) |
| 03 Outbound reminders | 65 | 0 | 0 | 80 | 170 | 54 (new-time lines) | 4 | 92 | 461 | 615 | OK (154 spare) |
| 04 Unethical client | 65 | 81 | 185 | 0 | 0 | 0 | 6 | 138 | 469 | 615 | OK (146 spare) |
| 05 Incomplete intake | 65 | 81 | 185 | 0 | 0 | 0 | 2 | 46 | 377 | 615 | OK (238 spare) |

Profile 01 was over budget by 7 words with 8 doctors; moving the confirmation flow from the Main prompt (CLOSE) to section 5 saved 27 words, so profile 01 now has 20 words to spare (allowance 431 for our text, 411 drafted). The skill must still report the budget line in its draft notes and never silently cut a critical rule (critical rules are in sections 1, 4 and 5 where possible).
