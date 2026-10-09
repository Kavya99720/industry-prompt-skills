**Assumptions and defaults used**
- Business word: "our clinic" (given directly).
- Direction: inbound (given). Workflows: 01 Enquiry, 02 Booking (given). No workflow 03/04 written, so no reschedule/cancel flow included — not asked for.
- Booking style: time slots (given); no TOKENS line needed.
- Roster: 6 doctors, counted for the word budget (given).
- Emergency department: no (given) — R-09 line adapted to "no emergency department, call 108 or 112."
- agent_name, agent_gender, default_language, business_phone, clinic_address, confirmation_channels, emergency_signs_extra, minors_may_book_alone: not provided — platform/intake defaults used (Voice settings defaults; no extra emergency signs; minors_may_book_alone = false; confirmation flow skipped until {{var.confirmation_channels}} is set).
- business_info: assumed to be where the full-body check-up package name and any service details live; the client gave no package details, fee or duration, so the agent can only mention it once per call and otherwise say the team will confirm.

**Refused or adapted client requests**
- "Push the full-body check-up package on every call": refused as stated — repeated upselling on every call is an unethical pressure pattern (R-76). Adapted: the agent may mention the package once per call, from {{var.business_info}}, never repeated.
- "Say fully booked when a doctor is busy, even when a slot is free": refused outright, no adaptation — lying about availability to steer callers is forbidden (R-76, R-21); availability is always read from the real doctor timings/status only.
- "Remove the emergency lines": refused — the emergency response can never be removed (R-09, R-76). Adapted instead to the required no-emergency-department wording ("call 108 or 112, or go to the nearest hospital") already dictated by emergency_department = no.

**Open questions**
- agent_name, agent_gender, default_language, business_phone, clinic_address: not provided — set in the platform.
- business_info: package name/fee/duration not given by the client — needed before the package can be mentioned usefully.
- confirmation_channels: not provided — confirmation flow stays inactive until set.
- emergency_signs_extra, minors_may_book_alone: not provided — defaults (none / false) in effect.
- The default emergency signs list still needs review by the client's clinical team (standing open item).

**Word counts**
- Welcome: 13. Section 1: 676. Section 2: 262. Section 3: 173. Section 4: 149. Section 5: 693.
- Section 6: 346 words. Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget (131 words below allowance, well past the required 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 6 doctors (Doctor A to Doctor F) | Doctors |
| `{{var.business_info}}` | not provided (package name/fee/duration needed) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
```

That's the complete output from the healthcare-prompt-writer skill. Section 6 came in at 346 words against a 477-word allowance (6 doctors × 23), well within budget. Two of the three client requests were refused outright (fake "fully booked," blanket package pushing) and the third — removing the emergency lines — was refused but adapted to the required no-ED wording, per R-76/R-09.
