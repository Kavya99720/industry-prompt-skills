**Assumptions and defaults used**
- agent_name, agent_gender, default_language: not given; left as platform Voice settings, no value assumed.
- company_name, business_phone, clinic_address: not given by the client; not invented (R-81), to be filled in the platform.
- emergency_signs_extra: none given; default empty, only the compact default list is in section 1.
- minors_may_book_alone: not given; default false (R-40 as written).
- confirmation_channels: not given; default empty, so the confirmation flow is written but will self-skip until the client sets a channel.
- business_info: not given; the agent says "the team will confirm" for any fact not in it, and the full-body check-up package is offered only once per call and only if it is present in this field — the client must add it there.
- Booking style confirmed as time slots (given), so no TOKENS line is included.

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": refused as stated (repeated upsell forbidden, R-76); adapted to a single, non-repeated mention per call, sourced only from {{var.business_info}}.
- "Say fully booked when a doctor is busy, even when a slot is free, to steer callers to a preferred doctor": refused outright — this is a direct lie to callers and a critical rule violation (R-76); the prompt instead keeps the truthful TAKEN/BOOK flow and explicitly forbids saying "fully booked" unless the booking tool itself reports the time as taken.
- "Remove the emergency lines; we do not want callers sent elsewhere": refused — the emergency response can never be removed (R-09, R-76); adapted instead to the "no emergency department" wording, which still sends the caller to 108/112 or the nearest hospital rather than naming this clinic's own emergency department.

**Open questions**
- Business name, phone number, clinic address and business hours are not provided in this draft; these must be filled in on the platform before launch (see table below).
- The clinical team should review the default emergency signs list (standing open question in core.md).
- Whether this clinic wants to add a waitlist or multiple shifts per doctor is not addressed; none was mentioned.

**Word counts**
- Welcome: 13. Section 1: 668. Section 2: 261. Section 3: 192. Section 4: 168. Section 5: 730.
- Section 6: 379 words. Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget (98 words of margin, well past the 20-word minimum).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.business_hours}}` | 9 AM to 7 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 6 doctors (Doctor A to Doctor F) — names, status, specialty, fees, about text and shifts not provided | Doctors |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided (needed for the full-body check-up package text) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided | Your business, Add a detail |
