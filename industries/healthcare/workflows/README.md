# Healthcare workflows

Each workflow file has: trigger, direction, steps, data and variables, tools, rules, scenarios (S-xx), section placement and the draft Main-prompt lines used for the word budget. Rules that apply to every workflow are in industries/healthcare/core.md. The brief index is industries/healthcare/brief.md.

## Workflow catalogue

| # | Workflow | Phase | Direction | Purpose | Main-prompt words (draft) |
|---|---|---|---|---|---|
| 01 | [Enquiry](01-enquiry.md) | 1 | Inbound | Doctors, timings, fees, services, directions, reports | 85 (+25 for token or walk-in clinics) |
| 02 | [Booking](02-booking.md) | 1 | Inbound | Book a new appointment with a named doctor | 229 |
| 03 | [Reschedule and cancel](03-reschedule-cancel.md) | 1 | Inbound, outbound | Change an appointment; note a cancellation (no cancel tool) | 84 (+54 when Booking is not selected) |
| 04 | [Reminder, outbound](04-reminder-outbound.md) | 1 | Outbound | Remind a patient of a booked appointment | 170 |
| 05 | [Lab tests](05-lab-tests.md) | 2 | Inbound | Lab test and home sample booking | stub |
| 06 | [Check-up packages](06-checkup-packages.md) | 2 | Inbound | Package enquiry and booking | stub |
| 07 | [Admission](07-admission.md) | 3 | Inbound | Admission and in-patient queries | stub |
| 08 | [Billing and insurance](08-billing-insurance.md) | 3 | Inbound | Route billing and insurance questions | stub |
| 09 | [Post-discharge follow-up](09-post-discharge-followup.md) | 3 | Outbound | Review-visit scheduling after discharge | stub |
| 10 | [Chronic care](10-chronic-care.md) | 3 | Outbound | Recurring check-ins and reminders | stub |
| 11 | [Vaccination](11-vaccination.md) | 3 | Inbound | Vaccination appointments | stub |
| 12 | [Feedback and complaint](12-feedback-complaint.md) | 3 | Inbound | Take feedback or a complaint and route it | stub |

Core Main-prompt lines (UNDERSTAND, HANDOFF, DOCTOR LIST) add 80 words to every prompt. The roster adds about 23 words per doctor. The Main prompt budget is about 615 words including the roster (platform-contract.md).

## Which business types use which workflow

Legend: ● normally used, ○ optional or depends on the business, – not used.

| Workflow | Hospital | Single-doctor clinic | Dental clinic | Diagnostic lab | Home care |
|---|---|---|---|---|---|
| 01 Enquiry | ● | ● | ● | ● | ● |
| 02 Booking | ● | ○ (only with time slots; tokens and walk-in clinics use 01 only) | ● | – (uses 05) | ● |
| 03 Reschedule and cancel | ● | ○ | ● | ● | ● |
| 04 Reminder, outbound | ● | ○ | ● | ○ | ● |
| 05 Lab tests | ○ | – | – | ● | ● |
| 06 Check-up packages | ● | – | ○ | ● | – |
| 07 Admission | ● | – | – | – | – |
| 08 Billing and insurance | ● | ○ | ○ | ○ | ○ |
| 09 Post-discharge follow-up | ● | ○ | – | – | ● |
| 10 Chronic care | ○ | ○ | – | – | ● |
| 11 Vaccination | ○ | ○ | – | – | ○ |
| 12 Feedback and complaint | ● | ○ | ○ | ○ | ○ |

## ID ranges

| Range | Where |
|---|---|
| S-01 to S-62 | Original brief, now split by workflow; every ID is in exactly one file (see the register in industries/healthcare/brief.md) |
| S-63 to S-74 | Approved 2026-10-08: S-63, S-64, S-67 in 02; S-65, S-66 in 01; S-68 to S-74 in 04 |
| S-75 to S-90 | New 2026-10-08, from live calls and the test profiles |
| R-01 to R-40 | Original brief, now split by workflow |
| R-41 to R-47 | Approved 2026-10-08 (R-41 = callback for On leave or On call) |
| R-48 to R-81 | New 2026-10-08, from live calls, decisions and the test profiles |
