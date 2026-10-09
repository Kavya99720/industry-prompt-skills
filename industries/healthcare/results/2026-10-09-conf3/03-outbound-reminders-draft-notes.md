**Assumptions and defaults used**
- Workflows: 04 Reminder (outbound) + 03 Reschedule/cancel, as stated; Booking (02) not selected, so RESCHEDULE refers to the standalone NEW TIME block from workflow 03 instead of a BOOK step.
- `{{var.emergency_department}}` = no (given) — the emergency line is adapted to "call 1 0 8 or 1 1 2 or go to the nearest hospital" instead of naming an emergency department.
- `{{var.confirmation_channels}}` not given — default empty, so no post-action confirmation flow (R-18) is included; nothing is sent via WhatsApp/email.
- `{{var.emergency_signs_extra}}`, `{{var.minors_may_book_alone}}`, `{{var.business_info}}` not given — intake defaults used (no extra signs; minors-alone false; business info empty, agent says the team will confirm).
- `{{var.default_language}}`, `{{var.agent_gender}}` not given — left as variables for the platform's Voice settings default.
- Roster count (4 doctors) used only for the word-budget calculation; no doctor names, specialties or fees are typed into the Instructions — they come from `{{var.roster}}`.
- `{{var.patient_name}}` is referenced implicitly (asking for the patient by name) and `{{var.appointment_details}}` is used in OUTBOUND REMINDER per workflow 04, even though variables.json marks both "unconfirmed" — flagged as an open item below.

**Refused or adapted client requests**
- none refused. "Reminders only — no clinical talk, no sales" was adopted directly: section 1 states scheduling-only scope, R-11/R-27 (no diagnosis, no medical history) and R-20 (no promised discounts/outcomes) already enforce "no sales," so no conflict with any critical rule.
- Adapted (not a refusal): no emergency department → emergency line reworded to the 108/112-and-nearest-hospital version (R-09), as the rules require rather than removing the emergency response.

**Open questions**
- Whether the platform actually passes `{{var.patient_name}}` and `{{var.appointment_details}}` to an outbound call (both marked unconfirmed in variables.json).
- Whether outbound calls must say "an AI assistant" up front, or whether the client's welcome template (used here, unchanged) is sufficient.
- Outbound closing wording ("Thank you for your time. Have a good day.") is still a proposal pending sign-off (R-68).
- Whether the platform detects voicemail/no-answer, and whether a do-not-call tool exists — until confirmed, the agent gives the fixed voicemail line and the fixed "noted, never says it's done" stop-calling line.
- Default emergency signs list still needs clinical-team review (unchanged from core).

**Word counts**
- Welcome: 14. Section 1: 663. Section 2: 197. Section 3: 173. Section 4: 133. Section 5: 511.
- Section 6: 389 words. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget (margin of 134 words below the allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D); names, specialties, fees and shifts not provided | Doctors |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided (flow skipped) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (defaults false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.patient_name}}` | n/a — passed per call if the platform supports it (unconfirmed) | Call context |
| `{{var.appointment_details}}` | n/a — passed per call if the platform supports it (unconfirmed) | Call context |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
```
