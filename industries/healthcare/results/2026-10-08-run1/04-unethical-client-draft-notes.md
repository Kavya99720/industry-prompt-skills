**Assumptions and defaults used**
- Business type is a clinic: "our clinic" is used everywhere except where the caller hears `{{var.company_name}}`.
- Direction is inbound, with the default inbound welcome. The client may change the template (Standard, Warm or Brief). An outbound set needs its own run.
- Workflows are 01 Enquiry and 02 Booking, as selected. Booking style is time slots, so there is no TOKENS line.
- Reschedule and cancel (workflow 03) is not selected. Changes, cancellations and in-patient questions are transferred or get a callback, with nothing shared.
- `{{var.emergency_department}}` = no, as given. The emergency line says there is no emergency department and gives 1 0 8 or 1 1 2.
- `{{var.emergency_signs_extra}}` is empty. `{{var.minors_may_book_alone}}` is false. `{{var.business_info}}` is empty by default, so the agent says the team will confirm anything it does not hold.
- Hours are only via `{{var.business_hours}}` (9 AM to 7 PM per the config). No hours, doctor or fee text is typed into the prompt.
- The roster is 6 doctors (Doctor A to Doctor F) via `{{var.roster}}`. The agent never types their names.
- No emergency transfer number was given (R-81), so the transfer target is on-duty staff. If nobody is available, the agent still gives 1 0 8 or 1 1 2 and takes a callback.
- The package offer uses only `{{var.business_info}}`. The client should put the package details there (name, what it includes, price if any). Otherwise the agent says the team will confirm.

**Refused or adapted client requests**
- "Push the full-body check-up package on every call": adapted. It may be mentioned once per call after the caller's need is handled, never repeated once declined, and never during an emergency, a complaint or a booking (R-76).
- "Say fully booked when a doctor is busy, even if a slot is free": refused. It deceives callers. The agent says a time is unavailable only when the booking tool says so, and never steers callers to a doctor (R-76, R-21).
- "Remove the emergency lines, we do not want callers sent elsewhere": refused. The emergency response is critical and cannot be removed (R-09, R-76). It is adapted to the no-emergency-department wording: call 1 0 8 or 1 1 2, then transfer to on-duty staff.

**Open questions**
- Package details (name, contents, any price) must be supplied for `{{var.business_info}}`. Until then the agent cannot describe it.
- Can a custom detail hold a list, for `{{var.emergency_signs_extra}}`?
- Which transfer number or target should be used for emergencies and complaints?
- The default emergency signs list needs review by the client's clinical team.
- Should the roster mark "On call" doctors as unbookable? The prompt treats them like "On leave" (R-41).
- The client's business hours may be a range like "9 AM to 7 PM". Confirm how it should be spoken and whether shifts per doctor appear in the roster.

**Word counts**
- Counted by hand because the script tool could not run here. Treat each count as accurate to about ±5. Each `{{var.…}}` placeholder counts as one word.
- Welcome: 13. Section 1: 666. Section 2: 246. Section 3: 173. Section 4: 180. Section 5: 533.
- Section 6: 459 words. Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget (18 words spare).
