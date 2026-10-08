# Healthcare test profiles

Four synthetic profiles. Each has business config, selected workflows, client requirements and 4 to 7 tricky callers with expected MUST and MUST NOT. They are the inputs for scripts/run_evals.py (one generated Instructions set per profile).

| # | File | Business | Direction | Workflows |
|---|---|---|---|---|
| 01 | [01-multispeciality-hospital-inbound.md](01-multispeciality-hospital-inbound.md) | Multi-speciality hospital | Inbound | 01, 02, 03 |
| 02 | [02-single-doctor-clinic-walkin.md](02-single-doctor-clinic-walkin.md) | Single-doctor clinic, tokens or walk-in | Inbound | 01 |
| 03 | [03-outbound-reminders.md](03-outbound-reminders.md) | Clinic, outbound reminders | Outbound | 04, 03 |
| 04 | [04-unethical-client.md](04-unethical-client.md) | Clinic with unethical client requests | Inbound | 01, 02 |

## Main prompt word budget

Budget: about 615 words for section 6 INCLUDING the roster (platform warning at 616). Words are whitespace-separated tokens in the draft `main-lines` blocks of core.md and the workflow files. The roster counts about 23 words per doctor. Sections 1 to 5 are not counted. These are estimates from drafts, not from a written skill.

Per-part words: core 80; Enquiry 85 (+25 token line); Booking 240; Reschedule and cancel 77 (+54 when Booking is not selected); Reminder 170.

| Profile | Core | Enquiry | Booking | Reschedule/cancel | Reminder | Extras | Doctors | Roster words | Total | Budget | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 Hospital inbound | 80 | 85 | 240 | 77 | 0 | 0 | 8 | 184 | **666** | 615 | **OVER by 51** |
| 02 Single-doctor walk-in | 80 | 85 | 0 | 0 | 0 | 25 (token line) | 1 | 23 | 213 | 615 | OK (402 spare) |
| 03 Outbound reminders | 80 | 0 | 0 | 77 | 170 | 54 (new-time lines) | 4 | 92 | 473 | 615 | OK (142 spare) |
| 04 Unethical client | 80 | 85 | 240 | 0 | 0 | 0 | 6 | 138 | 543 | 615 | OK (72 spare) |

**Flag: profile 01 is over budget.** With Enquiry, Booking and Reschedule/cancel (482 words of our text) the roster can hold at most 5 doctors (115 words) inside 615. With 8 doctors it is 51 words over. Options, in order of preference: shorten the roster "about" text (the client controls it; about 23 words per doctor includes it); drop Enquiry lines that section 1 already covers; compress CLOSE in Booking; split into two agents. The skill must report the budget line in its draft notes and never silently cut a critical rule (critical rules are in sections 1, 4 and 5 where possible).
