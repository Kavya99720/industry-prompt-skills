**Assumptions and defaults used**
- Outbound only. Workflows 04 Reminder and 03 Reschedule/cancel. Booking (02) is not selected, so the NEW TIME standalone line replaces BOOK. Business word: "our clinic".
- Welcome is the outbound template given in the profile. The client may change it.
- Emergency department: No, as the profile says. The emergency line is written to follow `{{var.emergency_department}}`. When it is no, the agent says "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now."
- Roster: 4 doctors, from `{{var.roster}}`. No doctor is typed in the prompt.
- Intake defaults used because nothing was given:
  - Languages: start in `{{var.default_language}}`.
  - Extra emergency signs: none. `{{var.emergency_signs_extra}}` is empty.
  - Minors may book alone: false.
  - Business info: empty, so the team confirms.
- Hours come only from `{{var.business_hours}}`. The profile value (9 AM to 6 PM, Monday to Saturday) is not typed in.
- `{{var.patient_name}}` and `{{var.appointment_details}}` are used as the profile gives them. The platform has not confirmed them.
- I added the verification, read-back and "changed only after the tool confirms" rules in section 5 so that RESCHEDULE works without workflow 02. I added the 24-hour time and passed-time rules in section 2 for the same reason. The tool-failure line in section 5 is an adaptation of booking rule R-22 for the reschedule tool.
- Outbound closing wording is the proposal in R-68.

**Refused or adapted client requests**
- "Reminders only. No clinical talk, no sales": accepted. The agent does scheduling only and makes no offers. Reschedule and cancel stay in because they are part of the reminder flow. Other enquiries go to HANDOFF.

**Open questions**
- Does the platform pass `{{var.patient_name}}` and `{{var.appointment_details}}` to outbound calls?
- Must outbound calls say "an AI assistant" up front? The client's welcome template is followed until this is decided (decision 14).
- Does the platform support voicemail detection or a do-not-call tool? The stop-calling and voicemail lines assume it only notes the request.
- The default emergency sign list needs review by the client's clinical team.
- If the client needs an inbound line too, it needs its own run. It is a separate Instructions set.

**Word counts**
- Welcome: 14. Section 1: 723. Section 2: 221. Section 3: 173. Section 4: 188. Section 5: 644.
- Section 6: 388 words, not counting the roster placeholder. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget.
