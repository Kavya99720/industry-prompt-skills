**Assumptions and defaults used**
- Business type: clinic, so the plain word is "our clinic". Inbound only; an outbound flow needs its own run (R-72).
- Workflows 01 Enquiry and 02 Booking, time slots. No workflow 03, so no reschedule or cancel. Reschedule and cancel requests go to the HANDOFF line.
- Emergency department = no, so the emergency line is the adapted one: "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now, or go to the nearest hospital." No transfer number was given, so the agent transfers to on-duty staff and offers a callback if none is available.
- Default language, extra emergency signs (none), minors-may-book-alone (false), business info (empty) and languages were not given. The documented defaults were used. The Prompt Variables table lists `{{var.emergency_signs_extra}}` and `{{var.business_info}}` though their values are empty.
- Welcome message: the default inbound template. The client may choose a different template on the platform.
- Roster: 6 doctors, from the platform Doctors config via `{{var.roster}}`. No doctor was typed in.

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": adapted. Pushing an offer on every call is not allowed (R-76), so the agent mentions the package once per call and never repeats it.
- "Say fully booked when a slot is free, to steer callers to a preferred doctor": refused. It deceives callers and the agent may never state unavailability unless the booking tool says so (R-76, R-21).
- "Remove the emergency lines; we do not want callers sent elsewhere": refused. The emergency response is critical and cannot be removed (R-76, R-09). It is adapted to the no-emergency-department wording and says to call 1 0 8 or 1 1 2 or go to the nearest hospital.

**Open questions**
- The package details (what it includes, price) were not provided. The agent says only what `{{var.business_info}}` holds, and the client must add the package text there. Without it the agent says the team will confirm.
- Emergency transfer target and a callback number for staff are not given.
- Doctor names, specialties, fees and shifts are to be set in the platform Doctors config.
- The default emergency signs list needs review by the client's clinical team.
- Is a steering preference for a particular doctor genuinely needed? If it is, the client can have the agent offer doctors truthfully, from the roster, when the caller has no preference.

**Word counts**
- Welcome: 17. Section 1: about 560. Section 2: about 250. Section 3: about 190. Section 4: about 150. Section 5: about 480. These are rough estimates; only section 6 was counted line by line by hand.
- Section 6: 391 words. Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget, 86 words below the allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.now_local}}` | automatic | Built in |
| `{{var.roster}}` | not provided (6 doctors, Doctor A to Doctor F) | Doctors |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (add the check-up package description here) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
