**Assumptions and defaults used**
- Business type read as "single-doctor clinic" → the agent says "our clinic" (R-75).
- Booking style: tokens and walk-in, no time slots → workflow 02 (Booking) not selected; the TOKENS line (R-78) added to workflow 01.
- Roster: 1 doctor assumed from the config table (Doctor A, General Physician, fee in the roster) → word-budget allowance uses 1 × 23 words.
- `{{var.emergency_department}}` = no → the S1 emergency line is adapted to "we do not have an emergency department, call 108 or 112" (R-09); this is config handling, not a refusal.
- `{{var.emergency_signs_extra}}` not given → default empty, no extra signs added.
- `{{var.minors_may_book_alone}}` not given → default false, R-40 applies as written.
- `{{var.confirmation_channels}}` not given → the After-the-call confirmation flow (R-18) is skipped entirely; it also has no scope here since workflow 02/Booking was not selected.
- `{{var.default_language}}` set to Hindi per "Hindi start; callers speak Hindi."
- `{{var.business_phone}}` and `{{var.clinic_address}}` not given in the profile → "not provided"; used only if a caller asks or a language-fallback callback is needed.

**Refused or adapted client requests**
- none — both client requirements ("tell callers OPD timings and how tokens work", "never promise a time the patient will be seen") align with R-78, R-35 and workflow 01 as written; no critical rule conflict.

**Open questions**
- `{{var.business_info}}` must actually contain the OPD timings and an explanation of the token system for the INFO/TOKENS lines to work — the client needs to fill this in on the platform.
- `{{var.business_phone}}` and `{{var.clinic_address}}` were not given; set them if callbacks or directions are needed.
- Workflows 02 (Booking) and 03 (Reschedule/cancel) were excluded per the client's "Enquiry only" selection; a later request for booking needs its own run.

**Word counts**
- Welcome: 13. Section 1: 677. Section 2: 198. Section 3: 173. Section 4: 133. Section 5: 515.
- Section 6: 181 words. Roster: 1 doctor × 23 = 23. Allowance: 615 − 23 = 592. Status: within budget (181 words, 411 words below the allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi | Voice settings |
| `{{var.business_hours}}` | OPD in the morning and evening (exact hours not given) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A, General Physician, fee in the roster (1 doctor) | Doctors |
| `{{var.business_info}}` | must explain the token system (text not given) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (none added) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
