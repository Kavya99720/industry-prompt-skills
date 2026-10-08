**Assumptions and defaults used**
- Non-interactive run, so every answer came from the profile. The business is "our clinic", outbound only, with workflows 04 and 03.
- Booking (02) is not selected, so workflow 03's standalone NEW TIME line is used. Its RESCHEDULE line now points to NEW TIME instead of BOOK. I added a read-back, the missing-detail callback and "never promise a slot is held". These come from workflow 03's steps and rules R-04, R-12 and R-35.
- Roster: 4 doctors (Doctor A to D), filled from the platform Doctors config via `{{var.roster}}`. No doctor is typed in the prompt.
- Emergency department: not stated, so the default "no" applies. The emergency line says there is no emergency department. The prompt branches on `{{var.emergency_department}}` and the default list is in full. `{{var.emergency_signs_extra}}` is empty (no extra signs).
- Emergency transfer number: not given, and none is invented. The prompt says to transfer to on-duty staff, and the handoff offers a callback if no one is available.
- Minors may book alone: false (default). Business info: empty (default), so the agent says the team will confirm.
- Default language comes from `{{var.default_language}}`. The welcome is the outbound template from the profile. The closing is the proposed outbound line (R-68).
- `{{var.patient_name}}` and `{{var.appointment_details}}` are unconfirmed platform variables. The prompt uses `appointment_details` in section 6. It asks for the patient by name rather than inserting `patient_name`, so the flow still works if the platform does not pass it.
- Symptom-to-specialty (R-37) is kept in section 1 because it is critical, even though the client wants reminders only. It is limited to neutral specialty names.

**Refused or adapted client requests**
- "Reminders only. No clinical talk, no sales": accepted. Clinical questions go to a nurse or doctor, and offers are barred. Core safety rules still apply, so the emergency response, the self-harm response and the AI disclosure stay.

**Open questions**
- Must outbound calls say "an AI assistant" up front? The profile's welcome template does not, and it is followed as given (decision 14).
- Does the platform pass `patient_name` and `appointment_details`? Does it detect voicemail? Is there a do-not-call tool? Until confirmed, the agent never says a stop-calling request is done.
- Emergency transfer target: not provided.
- The outbound closing wording needs sign-off.
- The default emergency signs list needs review by the client's clinical team.
- The inbound twin of this agent would need its own run. This set is outbound only.

**Word counts**
- Welcome: 16. Section 1: about 620. Section 2: about 250. Section 3: about 190. Section 4: about 190. Section 5: about 560. These are estimates because I could not run a per-section count. They are not budgeted.
- Section 6: 420 words, counted with `wc` and excluding the roster placeholder. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget, 103 words under the allowance, which clears the 20-word margin.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A to Doctor D (details not provided) | Doctors |
| `{{var.emergency_department}}` | no (default) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false (default) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.patient_name}}` | passed per call (unconfirmed) | Call data |
| `{{var.appointment_details}}` | passed per call (unconfirmed) | Call data |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
