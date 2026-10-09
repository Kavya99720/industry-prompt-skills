**Assumptions and defaults used**
- Business type read as "single-doctor clinic" → plain word "our clinic" used throughout (intake Q1, given).
- Direction read as inbound (given); welcome message uses the inbound template, no "calling from" anywhere.
- Workflow selection: 01 Enquiry only, as given. No Booking, Reschedule or Cancel content, tools or fixed lines included — R-18 confirmation flow, R-78's booking-tool line, and the cancel fixed line are all out of scope for this profile and were omitted rather than adapted.
- Booking style read as tokens/walk-in (given) → the TOKENS line (R-78/workflow 01 extra block) is included in section 6.
- Roster: 1 doctor given (Doctor A, General Physician, fee in roster) → word budget computed for 1 doctor. Doctor details themselves are never typed into the Instructions; they come from `{{var.roster}}`.
- `{{var.emergency_department}}` = no (given) → section 1 emergency line adapted to "we do not have an emergency department... call 1 0 8 or 1 1 2... or go to the nearest hospital," never removed.
- Languages: "Hindi start" read as `{{var.default_language}}` = Hindi (to be set in Voice settings); section 3 base (all 11 platform languages) used unchanged since the brief does not restrict supported languages, only the starting one.
- `{{var.business_info}}` assumed to hold the token-system explanation (given, custom detail) — no value invented.
- `{{var.emergency_signs_extra}}` — not given → default empty (intake default).
- `{{var.minors_may_book_alone}}` — not given → default false (intake default), per R-40/core.md.
- `{{var.confirmation_channels}}` — not given and not applicable (no booking/order event occurs in Enquiry-only); line skipped per the skill's scope rule rather than forced in.
- Agent name, agent gender, company name, business hours, business phone, clinic address — none given as concrete values; left as variables only, to be filled in the platform.
- Added an ADMISSION line (R-79, core, S6) even though a single-doctor OPD clinic is unlikely to have wards, because the rule applies to every business type and the word budget has large headroom.

**Refused or adapted client requests**
- None refused. The one adaptation already covered above: no emergency department → the 108/112/nearest-hospital line, never a removed emergency response (R-09, R-76).

**Open questions**
- Exact business name, agent persona name/gender, business hours, phone number and clinic address were not given — must be filled in the platform (see table below).
- Whether `{{var.business_info}}` can hold free text long enough to fully "explain the token system" is a platform open question (variables.json, custom detail capacity) — not something this skill can confirm.
- Whether a token number (vs. a booking number) is ever usable for the R-12-style verification line in section 5 is unconfirmed; written generically as "token or booking number" since no booking tool exists in this workflow.

**Word counts**
- Welcome: 18. Section 1: 398. Section 2: 112. Section 3: 150. Section 4: 95. Section 5: 318.
- Section 6: 185 words. Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget (185 words, 407 below the allowance — well past the 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi (callers speak Hindi; start in Hindi) | Voice settings |
| `{{var.business_hours}}` | not provided (described only as "OPD in the morning and evening") | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.emergency_signs_extra}}` | none given (default empty) | Your business → Add a detail |
| `{{var.minors_may_book_alone}}` | none given (default false) | Your business → Add a detail |
| `{{var.business_info}}` | "explains the token system" — exact wording not provided | Your business → Add a detail |
| `{{var.emergency_department}}` | no | Your business → Add a detail |
| `{{var.roster}}` | 1 doctor: Doctor A, General Physician, fee in roster (no fee amount given) | Doctors |
| `{{var.company_name}}` = your business name, filled in automatically from Variables. |
