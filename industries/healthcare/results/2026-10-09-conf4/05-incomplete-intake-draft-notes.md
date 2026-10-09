**Assumptions and defaults used**
- Business type "small clinic" and direction "inbound" were given explicitly; the agent says "our clinic" everywhere except the welcome, closing and AI-disclosure lines (R-75).
- Booking style "time slots" was given explicitly, so no TOKENS line (R-78 not applicable).
- Languages: not given. Default used (intake #7): the call starts in `{{var.default_language}}`; no value was invented.
- Emergency department: not given. Default used (intake #8, R-81): `{{var.emergency_department}}` = no, so section 1 carries the adapted line "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now, or go to the nearest hospital."
- Emergency transfer number: not given. Default used (intake #8, R-81): no transfer target was invented; the agent offers a callback to on-duty staff instead.
- Address: not given. `{{var.clinic_address}}` is left as the platform variable; no address was invented. The agent only speaks it when asked and will otherwise say the team will confirm.
- Custom details (extra emergency signs, minors-may-book-alone, business info, confirmation channels): none given. Defaults used (intake #10, R-81): no extra emergency signs added to the default list; `{{var.minors_may_book_alone}}` left false (R-40 as written); `{{var.business_info}}` left empty, so Enquiry answers fall back to "the team will confirm"; `{{var.confirmation_channels}}` left unset, so the R-18 post-booking confirmation flow is skipped entirely, as its own scope rule requires.
- Roster: 2 doctors (Doctor A, General Physician; Doctor B, Paediatrics) were given only to size the word budget. No doctor name, fee or timing is written into the Instructions; the Main prompt uses only `{{var.roster}}` (R-64, R-74).
- Workflows: only 01 Enquiry and 02 Booking were requested and selected; 03 Reschedule/cancel (part of the inbound default set) was not requested and so is not included.

**Refused or adapted client requests**
- none

**Open questions**
- Business name, hours value, phone, address, agent name/gender and default language were not given and must be filled in on the platform before this agent can go live.
- Languages beyond `{{var.default_language}}` were not confirmed; section 3 already supports all 11 platform languages if enabled.
- Emergency department status (currently defaulted to "no") and any transfer number need confirmation from the client/clinical team; the default emergency signs list also needs their clinical review (per core R-09).
- No confirmation channel is configured, so callers are not currently offered a WhatsApp or email confirmation after booking; confirm with the client whether to add `{{var.confirmation_channels}}`.
- The client said "we have not decided the rest" — workflow 03 (Reschedule and cancel) was left out; add it in a separate run if the client wants callers to reschedule or cancel by phone.

**Word counts**
- Welcome: 13. Section 1: 652. Section 2: 238. Section 3: 173. Section 4: 133. Section 5: 575.
- Section 6: 322 words. Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget (322 words, 247 below the allowance and well past the 20-word safety margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given as a variable reference only; no value supplied | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided ("small clinic" business type given, no name) | Your business |
| `{{var.now_local}}` | Built in automatically | n/a |
| `{{var.roster}}` | 2 doctors: Doctor A (General Physician), Doctor B (Paediatrics) | Doctors |
| `{{var.business_info}}` | not provided | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
