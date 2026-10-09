**Assumptions and defaults used**
- Business type "Clinic" → agent uses the plain word "our clinic" everywhere except where the name is heard (welcome, closing, AI-disclosure), per given config.
- Direction: Outbound (given) → workflows selected are 04 Reminder and 03 Reschedule/cancel, matching the outbound default in core.md's intake table.
- Booking style "Time slots" given, but workflow 02 (Booking) is not selected for this agent, so RESCHEDULE in section 6 follows workflow 03's standalone NEW TIME lines rather than a BOOK block.
- Roster: 4 doctors (given) → word-budget allowance = 615 − (23 × 4) = 523 words for section 6.
- Emergency department = No (given) → the section 1 emergency line is adapted to "we do not have an emergency department, call 1 0 8 or 1 1 2."
- `{{var.emergency_signs_extra}}` not given → default empty; only the compact default signs list is included.
- `{{var.minors_may_book_alone}}` not given → default false.
- `{{var.business_info}}` not given → the agent says the team will confirm for any business fact not on the roster.
- `{{var.confirmation_channels}}` not given → the R-18 confirmation flow is skipped entirely (it also has no natural trigger here, since no booking tool is used by this agent).
- `{{var.default_language}}` and `{{var.agent_gender}}` not given → left as platform variables to be set in Voice settings.
- `{{var.patient_name}}` is listed in the client's call-data config but is not inserted as a token anywhere in the Instructions text — the agent asks for the patient by name conversationally in OUTBOUND REMINDER, matching the reference workflow file, which also does not use a `{{var.patient_name}}` token. `{{var.appointment_details}}` is used directly.

**Refused or adapted client requests**
- None. The stated requirement "Reminders only — no clinical talk, no sales" already matches default rules (R-11 no diagnosis/clinical talk; S-70 scheduling only) and the no-upsell default; nothing needed to be refused or changed to satisfy it.

**Open questions**
- `{{var.patient_name}}` and `{{var.appointment_details}}` are marked "status: unconfirmed" in variables.json — whether the platform actually passes these on an outbound call is still open.
- Voicemail/no-answer detection by the platform is unconfirmed; the R-45 voicemail line is included as specified but depends on platform support.
- No do-not-call tool is confirmed, so the "stop calling" line only notes the request and never claims it is actioned.
- Whether outbound calls must say "an AI assistant" up front (vs. only on direct question) is pending legal/lead sign-off; this build follows the client's welcome template as given.
- The outbound closing line ("Thank you for your time. Have a good day.") is still a proposal pending sign-off (R-68).

**Word counts**
- Welcome: 14. Section 1: 604. Section 2: 198. Section 3: 173. Section 4: 149. Section 5: 536.
- Section 6: 384 words. Roster: 4 doctors × 23 = 92. Allowance: 615 − 92 = 523. Status: within budget (384 is 139 words below the allowance, well past the 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 4 doctors, Doctor A to Doctor D (no further detail given) | Doctors |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided (flow skipped) | Your business, Add a detail |
| `{{var.emergency_department}}` | no (baked into section 1 wording; not a live token) | Your business, Add a detail |
| `{{var.patient_name}}` | not provided / unconfirmed | Call context (platform-passed) |
| `{{var.appointment_details}}` | not provided / unconfirmed | Call context (platform-passed) |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
