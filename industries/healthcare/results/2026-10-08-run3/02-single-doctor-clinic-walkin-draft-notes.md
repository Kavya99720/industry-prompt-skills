**Assumptions and defaults used**
- Business word "our clinic"; inbound only; workflow 01 Enquiry only. Booking style is tokens/walk-in, so workflow 02 is not used and the TOKENS line from workflow 01 is included (R-78).
- Welcome is the default inbound template (Standard). The client may pick Warm or Brief on the platform.
- The default language is set through `{{var.default_language}}`. The profile says Hindi start, so set it to Hindi in Voice settings. Section 3 still handles all 11 platform languages.
- Roster is 1 doctor (Doctor A, General Physician). Fee, timings and the "about" text come only through `{{var.roster}}`.
- `{{var.emergency_department}}` = no, so the emergency line is the adapted one: no emergency department, call 1 0 8 or 1 1 2, or go to the nearest hospital.
- `{{var.emergency_signs_extra}}` is empty (default; no extra signs given). `{{var.minors_may_book_alone}}` is false (default).
- `{{var.business_info}}` holds the token explanation per the profile. If it is empty, the agent says the team will confirm.
- No emergency transfer number was given. The transfer target is not invented; the agent offers a callback when no one is available.
- The agent has no booking or lookup tool. Section 5 still carries the name-plus-booked-number verification rule (R-12); with no lookup, the agent will in practice share nothing about a token or booking and offer a callback.
- Booking-only wording is left out: the "booked/changed only after the tool confirms" rule (R-51) and the booking-time name requirement (R-50). Only the bare-title name check is kept, for when a name is needed.
- The other direction (outbound) would need its own run (R-72).

**Refused or adapted client requests**
- "Never promise a time the patient will be seen": kept as a rule (WAIT and TOKENS lines, plus section 1). No change needed.
- No refused requests. No emergency department is handled by adapting the emergency line (R-09), not by removing it.

**Open questions**
- What is the on-duty staff or transfer number for emergencies and for reports, complaints and clinical questions? Not provided, so the callback fallback is used.
- Do tokens run on a first-come order or by issue at the desk, and can they be given by phone? This belongs in `{{var.business_info}}`. If it is not filled in, the agent can only say the team will confirm.
- The default emergency sign list needs review by the client's clinical team.

**Word counts**
- Section 6 was hand-counted exactly: 171 words, with the roster placeholder excluded.
- I could not run a script here, so the other counts are hand estimates, not exact. Welcome: about 16. Section 1: about 640. Section 2: about 215. Section 3: about 195. Section 4: about 170. Section 5: about 560. Sections 1 to 5 do not count against the 615-word budget.
- Section 6: 171 words. Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi | Voice settings |
| `{{var.business_hours}}` | OPD morning and evening (exact hours not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.now_local}}` | built in | Built in, filled automatically |
| `{{var.roster}}` | Doctor A, General Physician, fee not provided | Doctors |
| `{{var.business_info}}` | Token system explanation (text not provided) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
