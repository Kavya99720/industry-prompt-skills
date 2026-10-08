**Assumptions and defaults used**
- Business word is "the hospital"; inbound only (the outbound set needs its own run); time-slot booking; workflows 01, 02, 03.
- Welcome is the default inbound template; the client may pick Standard, Warm or Brief on the platform.
- Roster is 8 doctors via `{{var.roster}}`; no doctor is typed. Doctor F's On leave status is handled by the booking rule (callback, never book, same-specialty doctors only if asked).
- Languages: start in `{{var.default_language}}` (English); Hindi and Kannada are covered by the 11 platform languages in section 3.
- Emergency signs: default list plus `{{var.emergency_signs_extra}}` (none given, empty). The `{{var.emergency_department}}` = yes line is in section 1. The default list needs review by the client's clinical team.
- `{{var.minors_may_book_alone}}` = false (default).
- The workflow 03 `NEW TIME` line is omitted because Booking is selected.
- No transfer number was given, so the agent offers a callback when no one is available (R-81).
- The 24-hour time rule, no past times and "3 without morning or evening" are placed in section 2.
- Sections 1 to 5 hold the universal rules. UNDERSTAND (in section 1) and WAIT (in section 1, "never promise waiting times") were moved out of section 6 to stay within budget.
**Refused or adapted client requests**
- Confirmation by WhatsApp or email: accepted as written, sent only after the tool confirms, with no fee or clinical detail in it.
- Callers may book any doctor with status Available: accepted; On leave and On call doctors are never booked.
- No special client rules: none.
**Open questions**
- Whether the platform fills `{{var.emergency_signs_extra}}` when it is empty.
- Whether the platform's "How it ends" templates (Warm, Brief, Formal) replace the closing line.
- The emergency transfer target is not given; confirm the on-duty staff number or keep the callback.
- Business info (beds, services) is not given; the agent says the team will confirm until it is filled.
**Word counts**
- Counts are approximate except section 6. The shell would not let me split the file by section, so I estimated sections 1 to 5 by hand.
- Welcome: 14. Section 1: about 790. Section 2: about 260. Section 3: about 215. Section 4: about 175. Section 5: about 720.
- Section 6: 411 words (counted exactly, without the roster placeholder). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 20 words below the allowance.
**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A to Doctor H, 6 specialties); Doctor F is On leave | Doctors |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | lists beds and services (values not provided) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
