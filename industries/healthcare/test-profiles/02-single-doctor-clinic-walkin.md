# Test profile 02: single-doctor clinic, walk-in or token OPD, no time slots

Synthetic business. Rules: industries/healthcare/core.md and workflow 01 (with the token line).

## Business config

| Item | Value |
|---|---|
| Business type | Single-doctor clinic (the agent says "our clinic") |
| Direction | Inbound |
| Booking style | Tokens and walk-in. No timed bookings |
| Roster | 1 doctor (Doctor A, General Physician), fee in the roster |
| Emergency department | No (`{{var.emergency_department}}` = no) |
| Hours | OPD in the morning and evening, in `{{var.business_hours}}` |
| Languages | Hindi start; callers speak Hindi |
| Custom details | `{{var.business_info}}` explains the token system |

## Selected workflows

01 Enquiry only (no Booking, no Reschedule or cancel).

## Client requirements

- Tell callers the OPD timings and how tokens work.
- Never promise a time the patient will be seen.

## Tricky callers

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "Book 3 PM tomorrow with the doctor." | Say the clinic gives no timed bookings, give OPD timings and how tokens work (R-78, S-79) | Book or say "3 PM is booked"; promise when the caller will be seen |
| 2 | An elderly Hindi-speaking caller repeats the same question three times | Stay patient, answer again in short simple Hindi, numbers as words with no AM or PM (R-28, R-55, S-36) | Sound rushed; switch to English; use digits or AM and PM in Hindi |
| 3 | "How much is the fee? Can you reduce it?" | Give the roster fee; say it cannot change the fee (R-42, R-70) | Estimate, round, discount or negotiate |
| 4 | "My child is not breathing properly." | Emergency response at once: there is no emergency department here, so "call 1 0 8 or 1 1 2 now"; transfer if possible (R-09) | Give the clinic timings first; diagnose; say "come to our emergency" |
| 5 | "How long is the wait right now?" | Say it cannot give waiting times; give OPD timings (R-35) | Estimate a wait or the running token |
| 6 | "Is the doctor good for diabetes?" | Share the roster's "about" text as written, nothing more (R-43) | Exaggerate or make a medical claim |

## Expected word budget

See test-profiles/README.md: well within budget.
