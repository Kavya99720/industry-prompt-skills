**Assumptions and defaults used**
- Business type given as "small clinic" with the agent saying "our clinic" — used as the plain word throughout (intake Q1, as given, no default needed).
- Booking style given as time slots — no TOKENS line added, R-78 not triggered (intake Q4, as given).
- Roster given as 2 doctors (General Physician, Paediatrics) from the platform roster — word allowance = 615 − (23 × 2) = 569; section 6 came to 331 words, well inside budget (intake Q5, as given).
- Languages not given → default start language and the 11 platform languages stay on the section 3 base default; no custom language was added (intake Q7 default).
- Emergency department not given → `{{var.emergency_department}}` defaults to "no"; section 1's emergency line is adapted to "We do not have an emergency department. Please call 108 or 112 now, or go to the nearest hospital" (R-09, intake Q8 default).
- Emergency transfer number not given → the agent offers a callback to on-duty staff instead of a transfer, throughout (R-81, intake Q8 default).
- Address not given → `{{var.clinic_address}}` is referenced only where directions would be given; it holds no value yet (intake Q9 area, Fixed business config).
- No custom details given → no extra emergency signs (`{{var.emergency_signs_extra}}` left out, nothing to add), `{{var.minors_may_book_alone}}` defaults false but is still referenced in section 1 so the clinic can toggle it later, and `{{var.business_info}}` is empty so unlisted facts fall back to "the team will confirm" (intake Q10 default).
- `{{var.confirmation_channels}}` not given → per R-18's own scope rule, the confirmation flow is skipped entirely; no WhatsApp/email offer is written into section 5 (intake Q10/R-18 default).
- Business hours were said to be "given" via `{{var.business_hours}}` — the Instructions use the variable normally wherever hours are spoken (callbacks, handoffs); no separate default needed.

**Refused or adapted client requests**
- none — "Just book appointments and answer questions" maps directly to workflows 01 and 02 as selected, and nothing in it touches a critical rule.

**Open items**
- `{{var.business_hours}}`, `{{var.business_phone}}`, `{{var.clinic_address}}` and the roster's doctor details (names, fees, about text, shifts) still need real values entered in the platform — none were given in this brief.
- Emergency department and transfer number are undecided; the Instructions currently default to "no ED, call 108/112 + callback." Needs sign-off once the clinic decides.
- No confirmation channel is set, so callers are never offered a post-booking WhatsApp or email confirmation until the client picks one.
- Workflow 03 (Reschedule and cancel) is part of the inbound default set but was not selected here — confirm whether callers who ask to cancel should be handled, since only 01 and 02 are wired in.
- `{{var.minors_may_book_alone}}` defaults to false — confirm if this clinic wants minors to be able to book alone.
- Languages: no start language or extra-language preference was given; left on the platform default.

**Word counts**
- Welcome: 13. Section 1: 219. Section 2: 155. Section 3: 110. Section 4: 92. Section 5: 318.
- Section 6: 331 words. Roster: 2 doctors × 23 = 46. Allowance: 615 − 46 = 569. Status: within budget (212 words below allowance, well past the 20-word margin).
