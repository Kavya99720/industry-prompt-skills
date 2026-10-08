**Assumptions and defaults used**
- Business type is a single-doctor clinic, so the agent says "our clinic". Direction is inbound only, so I used the default inbound welcome. The client may pick another welcome template.
- Only workflow 01 (Enquiry) is written. Booking and Reschedule/cancel are left out, so the agent takes no bookings and changes none.
- Booking style is tokens and walk-in. I added the TOKENS line from workflow 01 (R-78). How tokens work comes from `{{var.business_info}}`.
- Hindi start: I assumed `{{var.default_language}}` is set to Hindi in Voice settings. No Hindi text is hard-coded.
- 1 doctor on the roster, taken from the profile.
- `{{var.emergency_department}}` = no. The emergency line says there is no emergency department and sends the caller to 1 0 8, 1 1 2 or the nearest hospital.
- `{{var.emergency_signs_extra}}` is empty and `{{var.minors_may_book_alone}}` is false (defaults).
- No transfer number was given, so the agent offers a callback during `{{var.business_hours}}` where a transfer is not possible (R-81).
- I added one sentence to HANDOFF: share nothing about an admitted person (R-79, placement S6). I also added the "OPD timings are stored in English, convert them" line to section 2.
- The 108/112 and Tele-MANAS 14416 numbers are the fixed safety numbers from the references.

**Refused or adapted client requests**
- Tell callers the OPD timings and how tokens work: applied, using `{{var.business_hours}}`, the roster shifts and `{{var.business_info}}`. If those are empty, the agent says the team will confirm.
- Never promise a time the patient will be seen: applied as written (R-35, WAIT and TOKENS lines).
- No emergency department: adapted, not removed. The emergency line is rewritten for a clinic with no emergency department (R-09, R-76).

**Open questions**
- Business name, agent name and gender, business hours, phone, address, doctor details and fee: not provided.
- Does `{{var.business_info}}` carry the token explanation? It is not yet filled.
- Does the platform provide any running-token status? The agent assumes it does not and never quotes one.
- Emergency transfer target: not provided.
- The default emergency list needs review by the client's clinical team.
- Outbound calls need their own run.

**Word counts**
- Approximate, counted by hand (no script run): Welcome: 15. Section 1: about 640. Section 2: about 240. Section 3: about 215. Section 4: about 190. Section 5: about 560.
- Section 6: 186 words (counted by hand; the roster placeholder is not counted). Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget, 406 words under the allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi (from the profile) | Voice settings |
| `{{var.business_hours}}` | OPD morning and evening (exact times not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A, General Physician, fee in the roster (details not provided) | Doctors |
| `{{var.business_info}}` | explanation of the token system (text not provided) | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
