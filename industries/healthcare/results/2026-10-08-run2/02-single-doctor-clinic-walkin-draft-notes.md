**Assumptions and defaults used**
- Non-interactive run, so the profile was used as given. Business type is a single-doctor clinic, so the plain word is "our clinic". Direction is inbound, so the inbound welcome was used. The client may change the welcome template (Standard, Warm or Brief).
- Workflow 01 Enquiry only, with the TOKENS line (R-78). Workflow 02 Booking and workflow 03 Reschedule and cancel are not included. The agent never books, changes or cancels, and there is no timed booking.
- Start language is `{{var.default_language}}`, taken from the profile (Hindi). It is not typed into the prompt. The other 10 platform languages are handled by section 3.
- `{{var.emergency_department}}` = no, per the profile. The emergency line says there is no emergency department and gives 1 0 8 or 1 1 2 or the nearest hospital. The yes branch is kept in case the value changes.
- `{{var.emergency_signs_extra}}` is empty (default). `{{var.minors_may_book_alone}}` is false (default).
- The profile gives no transfer number. The agent transfers to on-duty staff through the `transfer` tool, and if nobody is available it takes a callback number and says when to expect the call (R-81).
- Doctor, fee and OPD timings come only from `{{var.roster}}`, `{{var.business_hours}}` and `{{var.business_info}}`. Nothing is typed into the prompt.
- The "booked" and "changed" and verification lines are kept in section 5 because the core rules require them. They are inactive in this setup.
- I added a PEOPLE line to section 6 for the S6 rules R-24, R-25 and R-79. It is not a draft line from the workflow files.
- I added "never estimate, round or negotiate" and the "about text only as written" wording to the INFO line (R-42, R-43). I added a sentence to TOKENS for callers who ask for a timed booking (S-79).

**Refused or adapted client requests**
- Tell callers the OPD timings and how tokens work: accepted, through the TOKENS and INFO lines using `{{var.roster}}`, `{{var.business_hours}}` and `{{var.business_info}}`.
- Never promise a time the patient will be seen: accepted. It is kept in TOKENS and WAIT, and it also covers waiting times and token timings (R-35).
- No emergency department: adapted, not removed. The emergency line is rewritten as "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now, or go to the nearest hospital" (R-09, R-76).

**Open questions**
- How the token system works is not in the profile. The agent can explain it only if `{{var.business_info}}` holds it. If that is empty, it says the team will confirm.
- A clinic with no timed booking may want a phone or desk option for callers who want a token. The platform has no token tool, so the agent only explains. Confirm this with the client.
- Whether `{{var.emergency_signs_extra}}` can hold a list is still open (platform-contract question 6).
- The default emergency sign list needs review by the client's clinical team.
- For outbound calls, a separate Instructions set would be needed. None was asked for here.

**Word counts**
- I could not run a counting script because command approval was denied. The section 6 count was done by hand. The other sections are not counted, so I am not giving numbers for them. Please recount them with a script.
- Welcome: 16. Sections 1 to 5: not counted.
- Section 6: 275 words (excluding the roster placeholder). Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget.
