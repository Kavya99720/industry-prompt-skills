**Assumptions and defaults used**
- Non-interactive run: answers read from test profile 02. Business type is a single-doctor clinic, so the agent says "our clinic". Direction is inbound.
- Workflow: 01 Enquiry only. Booking style is tokens and walk-in, so the TOKENS line from workflow 01 is included (R-78). There is no Booking, Reschedule or Cancel workflow.
- Roster: 1 doctor (Doctor A, General Physician), supplied through `{{var.roster}}`. I typed no doctor, fee or timing.
- Welcome message: the default inbound template. The client may choose another template (Standard, Warm or Brief). The closing line is the inbound default in section 5.
- Emergency department is no (given in the profile), so the emergency line is the adapted version: no emergency department, call 1 0 8 or 1 1 2, or go to the nearest hospital. No transfer number was given, so the agent transfers to on-duty staff and, if none are available, still gives the numbers. If the platform cannot transfer, offer a callback during `{{var.business_hours}}` (R-81).
- Default-language Hindi comes from `{{var.default_language}}`. Callers speak Hindi. The other platform languages are handled by section 3.
- `{{var.emergency_signs_extra}}` is not provided, so it is empty. `{{var.minors_may_book_alone}}` defaults to false.
- Outbound is not written. An outbound agent would need its own run (R-72).
- Section 6 holds no booking, reschedule or cancel steps. A caller who asks for a timed booking hears the TOKENS line. Rule R-14 (reports) and R-35 (no waiting-time or token-time promises) are in section 6. Both are critical or major rules from workflow 01.
- Rules R-12 and R-13 (verification by name plus booked number, no confirming who is a patient) are kept in section 5 even though Booking is not selected. They are critical and the agent could still be asked about an existing token.
- R-61 and R-60 are in section 2. Fees are given only if asked, from the roster (R-70).

**Refused or adapted client requests**
- Never promise a time the patient will be seen: accepted as written. It matches R-20 and R-35, and is in section 1 and the WAIT and TOKENS lines.
- Tell callers the OPD timings and how tokens work: accepted. The timings come from `{{var.business_hours}}` and the roster. The token explanation comes only from `{{var.business_info}}`. Nothing is invented.
- No emergency department: adapted, not removed, because the emergency response is critical (R-09, R-76).

**Open questions**
- The OPD timings (morning and evening) and the token explanation text were not given in the profile. They must be entered in `{{var.business_hours}}`, the roster shifts and `{{var.business_info}}`. If `{{var.business_info}}` is empty, the agent says the team will confirm.
- Whether the platform has a token tool or can pass the running token (platform question 6). Until then the agent never gives a token status or number.
- If `{{var.emergency_signs_extra}}` is empty, the line "Also treat these as emergency signs:" will read as an empty sentence. The client should add a value or the platform should omit the line when empty.
- The default emergency signs list needs review by the client's clinical team.
- Whether a custom detail can hold a flag or a list (platform question 1).
- No transfer target was given. Confirm whether staff can be reached by transfer.

**Word counts**
- Section counts are by hand; I could not run a counting script in this session, so only section 6 is exact. Welcome: 16. Section 1: about 800. Section 2: about 215. Section 3: about 215. Section 4: about 190. Section 5: about 560. These sections do not count against the 615-word budget.
- Section 6: 186 words (counted by hand, roster placeholder not counted). Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget, 406 words below the allowance, well over the 20-word margin.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi | Voice settings |
| `{{var.business_hours}}` | OPD in the morning and evening (exact timings not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A, General Physician, fee in the roster (fee, about text and shifts not provided) | Doctors |
| `{{var.emergency_signs_extra}}` | not provided (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | explains the token system (text not provided) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables. `{{var.now_local}}` is built in and filled by the platform.
