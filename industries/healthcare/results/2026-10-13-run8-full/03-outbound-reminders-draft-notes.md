**Assumptions and defaults used**
- Workflows: outbound default (04 Reminder, 03 Reschedule and cancel) matches the client's selection; Booking (02) not selected, so workflow 03's standalone NEW TIME lines were used in place of BOOK (per R-78/workflow 03).
- `{{var.confirmation_channels}}` not given → the confirmation flow (R-18) is skipped entirely; no WhatsApp/email lines appear in section 5. Set it later if the client wants after-call confirmations.
- `{{var.emergency_signs_extra}}`, `{{var.minors_may_book_alone}}`, `{{var.business_info}}` not given → defaults used (empty, false, empty) per the Intake table (R-81).
- `{{var.default_language}}` and `{{var.agent_gender}}` not given → left as platform Voice-settings fill-ins, no value assumed.
- `{{var.clinic_address}}` and `{{var.business_phone}}` not given → referenced only where needed (directions, callbacks); no value invented (R-74, R-81).
- `patient_name` is listed in the workflow's data but is not quoted as a literal token in the Instructions text (the fixed main-lines wording says "ask for the patient by name" rather than inserting the variable); kept as an open item below.

**Refused or adapted client requests**
- none — "reminders only, no clinical talk, no sales" matches the existing rules (R-11 no diagnosis, R-20 no promises/upsell) with no change needed.
- Emergency line adapted, not refused: with `{{var.emergency_department}}` = no, the line reads "We do not have an emergency department. Call 1 0 8 or 1 1 2 now, or go to the nearest hospital" (R-09); the default emergency signs list is kept in full, never removed.

**Open questions**
- `{{var.patient_name}}` and `{{var.appointment_details}}` are unconfirmed platform variables (workflow 04); if the platform does not pass them, the agent cannot state the appointment details and must fall back to asking the caller directly.
- Whether an outbound call must say "an AI assistant" up front (legal/product sign-off pending); the current welcome follows the client's template as given.
- Whether the platform detects voicemail/no-answer at all, and whether a do-not-call tool exists; until confirmed, "stop calling me" is only noted, never marked as done (R-73).
- Outbound closing wording ("Thank you for your time. Have a good day.") is still a proposal pending sign-off (R-68).

**Word counts**
- Welcome: 14. Section 1: 632. Section 2: 198. Section 3: 173. Section 4: 149. Section 5: 625.
- Section 6: 404 words. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget, 119 words below allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.company_name}}` | not provided (filled in automatically from Variables) | Your business |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D), details not provided | Doctors |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — flow skipped | Your business, Add a detail |
