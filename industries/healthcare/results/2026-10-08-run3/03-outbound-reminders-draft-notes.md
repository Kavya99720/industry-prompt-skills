**Assumptions and defaults used**
- Business type: clinic ("our clinic"). Direction: outbound only. This set is outbound; an inbound agent would need its own run (R-72).
- Workflows: 04 Reminder and 03 Reschedule/cancel. Booking (02) is not selected, so the standalone NEW TIME line is used. RESCHEDULE points to NEW TIME instead of BOOK.
- Booking style: time slots (from the profile).
- Roster: 4 doctors, expanded through `{{var.roster}}`. No doctor is typed in.
- Emergency department: no. The emergency line says "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now, or go to the nearest hospital," then a transfer to on-duty staff. No transfer number was given, so if no staff are available the agent gives the numbers and offers a callback.
- Defaults used: no extra emergency signs (`{{var.emergency_signs_extra}}` empty), `{{var.minors_may_book_alone}}` = false, `{{var.business_info}}` empty (the team confirms anything else), languages start in `{{var.default_language}}`.
- The welcome is the outbound template from the profile. The client may change the template.
- The closing line is the outbound proposal "Thank you for your time. Have a good day."
- `{{var.patient_name}}` is in the variables table but not in the text, because the section 6 line asks for the patient "by name" and the reminder line has no slot for it. `{{var.appointment_details}}` is used in section 6.
- Section 2's "Always send the time to the tool in 24-hour format" and the time-reading rule apply to reschedules.
**Refused or adapted client requests**
- none. "Reminders only, no clinical talk, no sales" is applied in section 1 and section 6.
**Open questions**
- The platform has not confirmed that `{{var.patient_name}}` and `{{var.appointment_details}}` are passed to outbound calls.
- Must outbound calls say "an AI assistant" up front? Until then the client's welcome template is followed.
- Voicemail detection and a do-not-call tool are unconfirmed. The agent says a stop request is "noted", never "done".
- The outbound closing wording is a proposal.
- No emergency transfer number was given. The default list needs review by the client's clinical team.
- The cancel flow has no cancel tool, so the clinic confirms it later.
**Word counts**
- Welcome: 17. Sections 1 to 5: not counted exactly (no script run on them; roughly S1 about 560, S2 about 215, S3 about 190, S4 about 190, S5 about 560).
- Section 6: 370 words (excluding the roster placeholder). Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget.
**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D), details not provided | Doctors |
| `{{var.emergency_signs_extra}}` | not provided (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.patient_name}}` | passed per call (unconfirmed) | Call data |
| `{{var.appointment_details}}` | passed per call (unconfirmed) | Call data |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
