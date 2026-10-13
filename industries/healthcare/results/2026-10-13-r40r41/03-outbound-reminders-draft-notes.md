**Assumptions and defaults used**
- `{{var.emergency_department}}` = no (given): emergency line adapted to "no emergency department, call 108 or 112."
- `{{var.emergency_signs_extra}}`: none given, default list only.
- `{{var.minors_may_book_alone}}`: none given, default false; core R-40 applied as written.
- `{{var.business_info}}`: none given; agent says the team will confirm when asked for services or facts.
- `{{var.confirmation_channels}}`: none given, so the confirmation flow (R-18) is skipped entirely per the skill's rule.
- Booking style "time slots" and workflow 02 (Booking) not selected: workflow 03's standalone NEW TIME lines are used in place of the "follow BOOK" reference, as the profile specifies.
- `{{var.patient_name}}` is not embedded as a token in the Main prompt, matching the reference workflow pattern: the agent elicits and verifies the patient's name in conversation rather than reading a pre-filled value, since the variable's platform support is unconfirmed.

**Refused or adapted client requests**
- None. "Reminders only, no clinical talk, no sales" aligns with the scheduling-only, no-advice design already required by core rules (R-11, R-27, workflow 04 step 5) and required no change.

**Open questions**
- Whether the platform actually passes `{{var.patient_name}}` and `{{var.appointment_details}}` to outbound calls (both marked "unconfirmed" in variables.json).
- Whether voicemail/no-answer is detected by the platform, and whether a do-not-call tool exists (R-45, R-73 assume neither is confirmed).
- Whether outbound calls must say "an AI assistant" up front (legal/product open item); until confirmed, the given outbound welcome template is used as is.

**Word counts**
- Welcome: 14. Section 1: 620. Section 2: 198. Section 3: 173. Section 4: 148. Section 5: 541.
- Section 6: 404 words. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget (119 words below allowance, well past the 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D); no names, specialties, fees or timings given | Doctors |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
