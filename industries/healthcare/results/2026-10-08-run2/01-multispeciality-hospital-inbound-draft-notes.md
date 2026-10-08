**Assumptions and defaults used**
- Business word "the hospital"; inbound only; workflows 01, 02, 03; booking style time slots (as given).
- Roster is 8 doctors, filled from `{{var.roster}}`; no doctor is typed. Doctor F's On leave status is handled by the BOOK rule (callback, never book). On call doctors are also never booked.
- Emergency department is yes, so the emergency line is written with a conditional on `{{var.emergency_department}}`. The default sign list is always in section 1, and `{{var.emergency_signs_extra}}` is empty.
- Minors flag false, so a lone minor is handled under R-40. Business info (beds, services) is only through `{{var.business_info}}`.
- Welcome is the default inbound template; the client may switch to Warm or Brief. The closing line is in section 5. Section 3 starts in `{{var.default_language}}`, and Hindi and Kannada are covered by the 11 supported languages.
- No emergency transfer number was given, so a callback is offered if no staff can be reached (R-81). Hours are given only through `{{var.business_hours}}`.
- Booking takes a WhatsApp number or email for the confirmation only, and the fee is not said at booking.
- To stay in budget, the UNDERSTAND, WAIT and symptom-to-specialty lines were moved out of section 6 into sections 1 and 5, where they already apply. Nothing was dropped.
- The client's additions are only the WhatsApp or email confirmation, which the booking workflow already covers.
- The outbound set (reminders) needs its own separate run.

**Refused or adapted client requests**
- Book any doctor with status Available: adapted. Only Available doctors are booked; On leave and On call doctors are never booked (R-41).
- Confirmation by WhatsApp or email: accepted as written. It holds only doctor, date and time and never the fee (R-18, R-19).
- Special client rules: none were given, so none were refused.

**Open questions**
- Can the platform pass a list in `{{var.emergency_signs_extra}}`? It is empty here.
- The default emergency signs list needs clinical review by the hospital.
- No emergency transfer target was given.
- How the platform's "How it ends" templates combine with the closing line is still open.
- How multi-shift doctors appear in the roster is still open.

**Word counts**
- Welcome: 16. Sections 1 to 5 were not counted exactly, because I could not run a script on the whole file. Estimates: Section 1 about 740, Section 2 about 270, Section 3 about 200, Section 4 about 210, Section 5 about 520.
- Section 6: 429 words, counted with wc on the section text, excluding the roster placeholder. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget.
