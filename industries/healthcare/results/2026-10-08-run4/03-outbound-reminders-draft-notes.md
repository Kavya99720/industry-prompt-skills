**Assumptions and defaults used**
- Direction outbound, workflows 04 and 03. Workflow 02 is not selected, so the standalone NEW TIME line is used. An inbound set needs its own run.
- Welcome is the client's outbound template. It matches the direction.
- Emergency department: the profile says No. The emergency line is adapted to "call 1 0 8 or 1 1 2 now, or go to the nearest hospital". The default signs list is intact. `{{var.emergency_department}}` is set to no in the platform.
- Defaults for skipped optional answers: no extra emergency signs, `{{var.minors_may_book_alone}}` false, `{{var.business_info}}` empty (the team will confirm), default language from Voice settings, and no emergency transfer target (the agent offers a callback).
- The outbound closing line "Thank you for your time. Have a good day." is a proposal.
- Doctor timings come only from `{{var.roster}}` (4 doctors).
- Rules I placed outside their usual spot, with the reason:
  - The admitted-person rule (R-79) is not written, because it has no main-lines text. It is not in the Instructions.
  - Time and booked-number rules for rescheduling are put in sections 2 and 5.
- The lines with the voicemail text and the "patient name" ask use `{{var.patient_name}}`, added to the OUTBOUND REMINDER line (no extra words).

**Refused or adapted client requests**
- "Reminders only, no clinical talk, no sales": applied as stated. Section 1 also bans offers. Reschedule and cancel stay in because workflow 04 hands over to 03.
- "Emergency department: No": adapted, not removed (R-09). The emergency response stays.

**Open questions**
- Does the platform pass `{{var.patient_name}}` and `{{var.appointment_details}}` to outbound calls? Both are unconfirmed.
- Must outbound calls say "an AI assistant" up front? The client template is followed for now (decision 14).
- Does the platform support voicemail detection and a do-not-call tool? The prompt avoids claiming either.
- No emergency transfer number was given, so transfers fall back to a callback.
- Ward and admitted-person questions (R-79) are not covered in this set. Say if you want them added.
- The word counts below are estimates. I could not run a counting script in this session, so I counted by hand.

**Word counts**
- Welcome: 19. Section 1: about 640. Section 2: about 260. Section 3: about 210. Section 4: about 200. Section 5: about 560. (Estimates.)
- Section 6: about 420 words, estimated by hand. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget, with a margin of roughly 100 words, which is above the 20-word target. Please confirm the exact count with a script.

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
| `{{var.business_info}}` | not provided (empty) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.patient_name}}` | passed per call (unconfirmed) | Call data |
| `{{var.appointment_details}}` | passed per call (unconfirmed) | Call data |
| `{{var.now_local}}` | built in | Built in |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
