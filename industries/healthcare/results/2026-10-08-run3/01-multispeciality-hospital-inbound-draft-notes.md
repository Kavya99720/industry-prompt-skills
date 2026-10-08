**Assumptions and defaults used**
- Non-interactive run: answers were read from the profile. Business type is hospital, so the agent says "the hospital". Direction is inbound only. The default inbound welcome template was used, and the client may pick Standard, Warm or Brief instead.
- Workflows are 01 Enquiry, 02 Booking and 03 Reschedule/cancel. Booking style is time slots. The TOKENS and NEW TIME lines were not needed.
- Roster is 8 doctors (Doctor A to H). Doctor F's status is On leave. The prompt never names doctors. The roster variable carries their status, so the BOOK step refuses to book an On leave or On call doctor and offers a callback.
- `{{var.emergency_department}}` = yes. The emergency line says to come to "our emergency department".
- Extra emergency signs: none, so the `{{var.emergency_signs_extra}}` detail is left empty. `{{var.minors_may_book_alone}}` = false.
- No transfer phone number was given. The prompt says "transfer"; if no transfer target is configured on the platform, the agent offers a callback instead (R-81).
- Language: starts in `{{var.default_language}}` (English). Hindi and Kannada are covered by section 3, and `change_language` is called on a switch.
- Inbound only: an outbound set for this hospital needs its own run.
- The default emergency list needs review by the client's clinical team.
- To fit the budget, "It holds only doctor, date and time" (R-19) and "if unsure the team will confirm" (R-20) were moved out of section 6 into sections 5 and 1. No critical rule was dropped.

**Refused or adapted client requests**
- Confirmation by WhatsApp or email: accepted as written. It holds only doctor, date and time, with no fee or clinical detail, and the agent never says the WhatsApp number aloud.
- Callers may book any roster doctor with status Available: accepted. Doctor F (On leave) is never booked, because the platform status wins; a callback is offered and same-specialty doctors are named only if the caller asks.
- No special client rules: none to refuse.

**Open questions**
- Which transfer number or target should the "on-duty staff" and "front desk" transfers use? Without one the agent offers callbacks.
- Can the platform hold the emergency-signs list as a custom detail? It is empty here, so this is not blocking.
- Does the platform's "How it ends" template (Warm, Brief or Formal) combine with the closing line in section 5?
- Which medical specialty does Doctor F cover, and is another Available doctor in the same specialty? If not, the agent can only offer a callback.

**Word counts**
- Welcome: 16. Section 1: about 650. Section 2: about 270. Section 3: about 200. Section 4: about 190. Section 5: about 680. These five are estimates from my own line counts, not script counts.
- Section 6: 429 words (counted with `wc -w` on the 442-word draft, less the 13 words moved out; the roster placeholder is not counted). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 2 words spare. The first draft was 477, so it was compressed by merging WAIT into REPORTS, shortening wording, and moving two lines into sections 1 and 5.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors, Doctor A to Doctor H (General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT); Doctor F On leave; fees, about text and shifts not provided | Doctors |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | beds and services (values not provided) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
