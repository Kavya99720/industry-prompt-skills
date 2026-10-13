**Assumptions and defaults used**
- Business type "Clinic" → plain word "our clinic" throughout, per the given intake.
- Direction: inbound (given); workflows 01 Enquiry and 02 Booking only, as given — workflow 03 Reschedule/cancel was not requested, so it is out of scope for this run.
- Booking style: time slots (given) — no TOKENS line added.
- Roster: 6 doctors (given) — used for the word-budget allowance (23 × 6 = 138 words).
- Emergency department = no (given) — the R-09 line is adapted, not removed: "we do not have an emergency department, call 108 or 112 or go to the nearest hospital."
- `{{var.default_language}}`: not given — the variable is left for the client to set; no value assumed or invented.
- `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.clinic_address}}`, `{{var.business_phone}}`: not given — left as variables, flagged below as open items; nothing invented (R-81).
- `{{var.minors_may_book_alone}}`: not given, default false.
- `{{var.emergency_signs_extra}}`: not given, default empty (default list only).
- `{{var.confirmation_channels}}`: not given — the R-18 confirmation flow is skipped entirely (the CLOSE step in section 6 has no confirmation offer), per the rule's own "if not set, skip the flow."

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": refused as stated — repeating an upsell on every call is an unethical pressure pattern (R-76). Adapted: the agent may mention the package once in a call, only if relevant, never repeated or pushed.
- "Say fully booked when a doctor is busy, even when a slot is free, to steer callers to a preferred doctor": refused outright, no adaptation possible — this is a direct instruction to lie to callers about availability (R-76, R-21). Section 6's BOOK/TAKEN steps report only the real tool status.
- "Remove the emergency lines; we do not want callers sent elsewhere": refused — a critical safety rule cannot be removed (R-09, R-76). Adapted instead: since this clinic has no emergency department, the line tells callers to call 108/112 or go to the nearest hospital, rather than being deleted.

**Open questions**
- `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.default_language}}`, `{{var.clinic_address}}`, `{{var.business_phone}}` were not given — the client fills these in on the platform.
- No details were given for the full-body check-up package (name, price, what's included). If the clinic wants the agent to answer questions about it, add that as a `{{var.business_info}}` custom detail; as written, the agent can only mention that it exists.
- `{{var.confirmation_channels}}` was not given, so the WhatsApp/email confirmation flow is skipped. If the client wants it, they set up the After-the-call trigger for WhatsApp and/or email on the platform and add the channels as a custom detail.
- Whether the clinic also wants workflow 03 (Reschedule/cancel) is open — this run only covers Enquiry and Booking.

**Word counts**
- Welcome: 13. Section 1: 678. Section 2: 251. Section 3: 174. Section 4: 155. Section 5: 538.
- Section 6: 342 words. Roster: 6 doctors × 23 = 138. Allowance: 615 − 138 = 477. Status: within budget, 135 words below allowance (well past the 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | 6 doctors (Doctor A to Doctor F) — no further detail given | Doctors |
| `{{var.business_info}}` | not provided (package details not given) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (defaults false) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — confirmation flow skipped | Your business, Add a detail |
