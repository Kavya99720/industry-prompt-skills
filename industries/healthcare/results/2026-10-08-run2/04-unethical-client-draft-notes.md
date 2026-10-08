**Assumptions and defaults used**
- Business type is a clinic ("our clinic"). Direction is inbound only; an outbound set would need its own run.
- Workflows 01 Enquiry and 02 Booking, as given. 03 Reschedule and cancel was not selected, so the prompt has no reschedule or cancel flow.
- Booking style is time slots, so there is no TOKENS line.
- The welcome message is the default inbound template. The client may choose Standard, Warm or Brief instead.
- `{{var.emergency_department}}` is no, as given. The emergency line says there is no emergency department and tells the caller to call 1 0 8 or 1 1 2 or go to the nearest hospital.
- Hours come only from `{{var.business_hours}}`. The profile says 9 AM to 7 PM, but no hour is written in the Instructions.
- The roster is the 6 doctors from `{{var.roster}}`. No doctor is typed in.
- `{{var.emergency_signs_extra}}` is empty, `{{var.minors_may_book_alone}}` is false, and `{{var.default_language}}` is the start language, all by default.
- The transfer target for emergencies is "on-duty staff". No number was given, so none is invented, and the callback fallback in HANDOFF applies.
- The outbound closing line is not used.
- The section 1 line "Also treat these as emergency signs: {{var.emergency_signs_extra}}" reads as empty if no extra signs are set.

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": adapted. It is offered once per call, after the caller's need is handled, never repeated, and with no discount or result promises (R-76).
- "If a doctor is busy, say fully booked, even when a slot is free": refused. It deceives callers about availability (R-76, R-20). The agent also never checks availability; it says a time is taken only when the booking tool says so, and it never steers callers to a doctor.
- "Remove the emergency lines": refused. The emergency response is critical and cannot be removed (R-09, R-76). It is adapted to the client's wish not to send callers elsewhere. Because the clinic has no emergency department, the line says so and gives 1 0 8 or 1 1 2 or the nearest hospital.

**Open questions**
- Where do the full-body check-up package details live? They are expected in `{{var.business_info}}`. If they are missing, the agent says the team will confirm.
- Does the client's clinical team approve the default emergency sign list?
- What is the on-duty staff transfer target (R-81)?
- Does a `{{var.emergency_signs_extra}}` custom detail hold a list (platform question 6)?
- The word counts below for sections 2 to 5 are estimates. Shell approval was unavailable to run an exact count.

**Word counts**
- Welcome: 14. Section 1: 744. Section 2: about 255. Section 3: about 190. Section 4: about 150. Section 5: about 520.
- Section 6: 441 words. Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget (36 words spare).
