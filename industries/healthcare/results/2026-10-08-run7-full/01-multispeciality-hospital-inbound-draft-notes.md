**Assumptions and defaults used**
- Business type: hospital, so the agent says "the hospital". Direction: inbound. Workflows: 01 Enquiry, 02 Booking, 03 Reschedule and cancel.
- Booking style: time slots. The TOKENS line is not included.
- Roster: 8 doctors. Doctor F (On leave) is never booked; the agent offers a callback and names same-specialty doctors only if the caller asks. Any Available doctor can be booked. On-call doctors are treated the same as On leave.
- Welcome: the default inbound template. The client may change it to Warm or Brief.
- Extra emergency signs: none. Minors flag: false. Emergency department: yes, so the agent says "our emergency department" in the emergency line.
- Languages: starts in `{{var.default_language}}`. Section 3 handles the switches to Hindi and Kannada.
- No emergency transfer number was given, so the agent offers a callback instead of a transfer if no staff can be reached (R-81).
- To fit the budget, the booking-failure rule (R-22) sits in section 5. The waiting-time promise (WAIT) is covered by the no-promise line in section 1. Neither rule was weakened.
- Confirmation channel: WhatsApp or email, as the client asked.
- Inbound only. An outbound set (for example reminders) needs its own run.
- Cancel wording is the fixed line, "The clinic will confirm it with you." It is kept as written even though this is a hospital.
- The tokens and workflow 04 lines are not used.

**Refused or adapted client requests**
- none. "Callers may book any roster doctor with status Available" and "confirmation by WhatsApp or email" match the rules as written. Doctor F stays unbookable because of the On leave status (R-41).

**Open questions**
- Emergency transfer target and a front-desk or nurse transfer number are not given. The platform "transfer" tool needs one.
- Can `{{var.emergency_signs_extra}}` hold an empty value or a list on the platform? When it is empty the line reads "Also treat as emergency signs:" with nothing after it.
- Does the cancel line say "The clinic" correctly for a hospital, or should it say "The hospital"? It is a fixed line (R-52).
- Which "How it ends" template does the client want? The closing line is kept in section 5.
- The default emergency signs list needs review by the client's clinical team.
- Do the hospital's beds and services exist in `{{var.business_info}}`? If it is empty, the agent says the team will confirm.

**Word counts**
- These per-section counts are approximate. I could count words exactly only for section 6 and for the whole text together, because the counting commands for the other sections were blocked. The Instructions total, without section 6 and the table, is about 1,680 words.
- Welcome: about 15. Section 1: about 780. Section 2: about 250. Section 3: about 175. Section 4: about 190. Section 5: about 530.
- Section 6: 405 words (exact, excluding the roster placeholder). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 26 words below the allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A to Doctor H) across General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology and ENT; Doctor F On leave; fees, about text and shifts not provided | Doctors |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | beds and services (values not provided) | Your business, Add a detail |
| `{{var.now_local}}` | automatic | Built in |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
