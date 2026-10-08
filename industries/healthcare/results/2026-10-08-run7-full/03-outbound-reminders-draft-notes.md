**Assumptions and defaults used**
- Business type clinic ("our clinic"), outbound only. This is one Instructions set. An inbound set would need its own run (R-72).
- Workflows 04 Reminder and 03 Reschedule and cancel. Workflow 02 is not selected, so the standalone NEW TIME line is used and RESCHEDULE points to NEW TIME instead of BOOK.
- Time slots is the booking style, as given.
- 4 doctors as given. The roster comes only from `{{var.roster}}`. No doctor names are typed.
- No emergency department (as given), so the emergency line is adapted: "call 1 0 8 or 1 1 2 now, or go to the nearest hospital."
- Defaults for the optional intake items: no extra emergency signs, `{{var.minors_may_book_alone}}` = false, `{{var.business_info}}` empty (the team confirms anything not given), languages start in `{{var.default_language}}`.
- No emergency transfer number was given. Transfers to on-duty staff use the `transfer` tool. If no one is available, the agent gives the numbers and offers a callback (R-81).
- The welcome is the outbound default template, and it matches the client's template.
- The outbound closing line "Thank you for your time. Have a good day." is a proposal (R-68).
- Not a client request: `{{var.patient_name}}` is said when asking "Am I speaking with…?", which is before the person is confirmed as the patient. The variable's description says to use it only after confirmation. Without the name the agent cannot ask for the patient.
- The reminder details come from `{{var.appointment_details}}`, which is not confirmed as a platform variable. Reschedule still needs the booked number from the caller (R-12).
- Section 2 uses the base text with no extra lines. Section 3 uses the base.

**Refused or adapted client requests**
- "Reminders only. No clinical talk, no sales.": applied, not refused. Sales and offers are excluded, and clinical talk is routed to a nurse or doctor. The emergency check, self-harm line and AI honesty rule stay in force on every call (R-09, R-10, R-08).
- No emergency department: adapted, not refused. The emergency line is kept and reworded (R-09, R-76).

**Open questions**
- Does the platform pass `{{var.patient_name}}` and `{{var.appointment_details}}` to outbound calls? Does it support voicemail detection or a do-not-call tool?
- Must outbound calls say "an AI assistant" up front? (decision 14; the client's template is followed for now.)
- Is the outbound closing wording approved?
- What is the transfer target for on-duty staff?
- The default emergency list needs review by the client's clinical team.

**Word counts**
- I could not run a counting script in this session (shell commands were not approved), so only the section 6 count is exact. I counted it by hand. The others are rough estimates.
- Welcome: 14. Section 1: about 560. Section 2: about 215. Section 3: about 190. Section 4: about 190. Section 5: about 560.
- Section 6: 370 words (excluding the roster placeholder). Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget, 153 words below the allowance (the 20-word margin is met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.now_local}}` | built in | Built in (automatic) |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D), details not provided | Doctors |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.patient_name}}` | passed per call (unconfirmed) | Call context |
| `{{var.appointment_details}}` | passed per call (unconfirmed) | Call context |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
