**Assumptions and defaults used**
- Business type is a clinic, outbound only, time slots, 4 doctors, no emergency department. The profile's "No" sets `{{var.emergency_department}}` = no, so the emergency line says there is no emergency department and to call 1 0 8 or 1 1 2.
- Workflows used: 04 Reminder (outbound) and 03 Reschedule and cancel. Booking (02) is not selected, so I used workflow 03's standalone NEW TIME line and the reschedule-related date and time rules in section 2.
- The profile gave no emergency transfer number. The prompt uses the platform `transfer` tool to on-duty staff, and the agent gives 1 0 8 or 1 1 2 even if no staff are available.
- The welcome is the outbound template from the profile, unchanged. It has no "an AI assistant" line, which follows decision 14.
- No extra emergency signs, no business info, and the minors flag is false. Languages start in `{{var.default_language}}`.
- The closing line "Thank you for your time. Have a good day." is the outbound proposal in R-68 and needs sign-off.
- `{{var.patient_name}}` and `{{var.appointment_details}}` are unconfirmed platform variables. If the platform does not pass them, the reminder step cannot name the patient or the appointment.
- Voicemail detection and a do-not-call tool are unconfirmed. The voicemail line, the "I've noted that you don't want further calls" line and the "team will update this" line are written so they never claim the action is done.
- Because 02 is not selected, I added a read-back before rescheduling ("Shall I change it?") and short rules for reschedule-tool failure and for times that have passed, to keep the critical rules R-04, R-49 and R-51.

**Refused or adapted client requests**
- "Reminders only. No clinical talk, no sales": accepted as written. The agent also makes no offers, which is consistent with R-76. Emergency, self-harm and clinical-routing rules still apply and cannot be switched off.
- "Emergency department: No": adapted, not removed. The emergency response stays and says to call 1 0 8 or 1 1 2 (R-09, R-76).

**Open questions**
- Must outbound calls say "an AI assistant" up front (legal or product lead)?
- Does the platform pass `patient_name` and `appointment_details`, detect voicemail, and offer a do-not-call tool?
- Who is the emergency transfer target? None was given.
- The client's clinical team must review the default emergency signs list.
- Reschedule needs a booked number. An outbound reminder that does not carry one means the caller must supply it, or the agent offers a callback.

**Word counts**
- Welcome: 14. Sections 1 to 5 are approximate because I could not run a counting script in this session. Section 1: about 570. Section 2: about 215. Section 3: about 150. Section 4: about 165. Section 5: about 570.
- Section 6: 379 words (counted by hand, roster placeholder excluded). Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget, 144 words under the allowance (margin of 20 met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D); details not provided | Doctors |
| `{{var.emergency_signs_extra}}` | not provided (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (empty) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.patient_name}}` | passed per call by the platform (unconfirmed) | Call data |
| `{{var.appointment_details}}` | passed per call by the platform (unconfirmed) | Call data |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
