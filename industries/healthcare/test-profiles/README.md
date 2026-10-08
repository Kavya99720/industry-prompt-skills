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

Per-part words: core 65; Enquiry 81 (+25 token line); Booking 212; Reschedule and cancel 80 (+54 when Booking is not selected); Reminder 170.

| Profile | Core | Enquiry | Booking | Reschedule/cancel | Reminder | Extras | Doctors | Roster words | Total | Budget | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 01 Hospital inbound | 65 | 81 | 212 | 80 | 0 | 0 | 8 | 184 | **622** | 615 | **OVER by 7** (draft lines; the generated prompt compresses them) |
| 02 Single-doctor walk-in | 65 | 81 | 0 | 0 | 0 | 25 (token line) | 1 | 23 | 194 | 615 | OK (421 spare) |
| 03 Outbound reminders | 65 | 0 | 0 | 80 | 170 | 54 (new-time lines) | 4 | 92 | 461 | 615 | OK (154 spare) |
| 04 Unethical client | 65 | 81 | 212 | 0 | 0 | 0 | 6 | 138 | 496 | 615 | OK (119 spare) |
| 05 Incomplete intake | 65 | 81 | 212 | 0 | 0 | 0 | 2 | 46 | 404 | 615 | OK (211 spare) |

**Flag: profile 01 is over budget.** With Enquiry, Booking and Reschedule/cancel (438 words of our text) the roster can hold at most 7 doctors (161 words) inside 615. With 8 doctors the draft lines are 7 words over. Options, in order of preference: shorten the roster "about" text (the client controls it; about 23 words per doctor includes it); drop Enquiry lines that section 1 already covers; compress CLOSE in Booking; split into two agents. The skill must report the budget line in its draft notes and never silently cut a critical rule (critical rules are in sections 1, 4 and 5 where possible).
