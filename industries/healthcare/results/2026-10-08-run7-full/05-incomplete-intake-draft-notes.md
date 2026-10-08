**Assumptions and defaults used**
- Business type is a small clinic, so the agent says "our clinic". Direction is inbound with time-slot booking, and workflows 01 and 02 are included, as given.
- Languages were not given. The call starts in `{{var.default_language}}`, and section 3 covers the 11 platform languages. No language was invented.
- Emergency department was not given, so `{{var.emergency_department}}` = no. The emergency line says there is no emergency department and tells the caller to call 1 0 8 or 1 1 2 or go to the nearest hospital.
- Emergency transfer number was not given. The agent offers a callback during business hours instead of a transfer (R-81). Because of this I also removed "transfer" from REPORTS and HANDOFF in section 6 and left only callbacks. This is a deviation from the draft main-lines wording.
- Address was not given. Directions use `{{var.clinic_address}}` only when asked. If it is empty, the agent says the team will confirm.
- Services and years of service were not given, so `{{var.business_info}}` is empty and the agent says the team will confirm. Extra emergency signs are empty. `{{var.minors_may_book_alone}}` = false.
- Doctors are not typed in. They come from `{{var.roster}}` (Doctor A, General Physician; Doctor B, Paediatrics), so there are 2 doctors for the budget.
- The welcome message is the default inbound template. The client may change it to Warm or Brief in the platform.
- Rules from workflow 03 (reschedule and cancel) are not included because it was not selected. Reschedule and cancel requests are not handled. They fall under the callback line, and the agent cannot verify or change an existing booking.

**Refused or adapted client requests**
- "We have not decided the rest": nothing was refused. Every undecided item uses the documented default above, and nothing was invented (R-81).
- Missing emergency department: adapted to the "no emergency department, call 1 0 8 or 1 1 2" line. The emergency response is never removed (R-09, R-76).

**Open questions**
- Which languages the clinic needs, beyond the platform default.
- Whether the clinic has an emergency department, and an emergency transfer number or on-duty staff line.
- Clinic address, and the `{{var.business_phone}}` value (used for the "language not supported" fallback).
- Services, years of service and insurers the clinic accepts, if the agent should answer these.
- Whether the clinic wants reschedule and cancel (workflow 03) added.
- Whether the doctor timings and fees are filled in the platform roster, since the agent depends on them.
- The default emergency signs list needs review by the clinic's clinical team.

**Word counts**
- Welcome: 13. Sections 1 to 5 were not counted with a script, so these are estimates: Section 1: about 560. Section 2: about 230. Section 3: about 185. Section 4: about 190. Section 5: about 640. None of these are limited by the budget.
- Section 6: 357 words. Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget, with 212 words of margin.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given by the client (enter it as given) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A (General Physician), Doctor B (Paediatrics); status, fees, about text and shifts not provided | Doctors |
| `{{var.emergency_signs_extra}}` | not provided (none) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.emergency_department}}` | not provided (no) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
