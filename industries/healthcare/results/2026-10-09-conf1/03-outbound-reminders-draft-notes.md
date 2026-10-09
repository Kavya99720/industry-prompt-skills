**Assumptions and defaults used**
- Business type word set to "our clinic" per the client's instruction.
- Booking style (time slots) and roster size (4 doctors) taken from the profile; no booking workflow (02) selected, so workflow 03's standalone NEW TIME lines carry the "new day and time" steps instead.
- `{{var.emergency_department}}` = no, per profile; the emergency line in section 1 is hard-written as "we do not have an emergency department... call 1 0 8 or 1 1 2" rather than left conditional, since the answer is already known.
- `{{var.emergency_signs_extra}}`, `{{var.minors_may_book_alone}}`, `{{var.business_info}}` not given by the client: left as empty/false defaults per the Intake table; the variables still appear in the Instructions so the client can fill them later.
- `{{var.default_language}}` and `{{var.agent_gender}}` not given: left as platform defaults, filled in Voice settings.
- `{{var.confirmation_channels}}` not given, and no booking tool is used anywhere in this profile (no workflow 02): the R-18 confirmation flow is not applicable here and was omitted from section 5 entirely, rather than included unused.
- Languages: not specified, so section 3's full 11-language base applies unchanged.

**Refused or adapted client requests**
- None. "Reminders only, no clinical talk, no sales" matches existing critical rules (R-11 no diagnosis/clinical talk, R-20 no promised discounts or sales pressure) with no conflict, so nothing needed refusing or adapting.

**Open questions**
- Whether the platform actually passes `{{var.patient_name}}` and `{{var.appointment_details}}` to an outbound call (both marked "unconfirmed" in variables.json).
- Whether outbound calls must say "an AI assistant" up front (legal/lead sign-off pending); current wording follows the client's welcome template and discloses only when asked.
- The outbound closing line ("Thank you for your time. Have a good day.") is still a proposal pending sign-off.
- Whether the platform detects voicemail/no-answer on outbound calls, and whether a do-not-call tool exists (R-73 handling assumes neither).
- The default emergency signs list still needs review by the client's clinical team.

**Word counts**
- Welcome: 14. Section 1: 611. Section 2: 186. Section 3: 173. Section 4: 133. Section 5: 428.
- Section 6: 389 words. Roster: 4 doctors x 23 = 92. Allowance: 615 - 92 = 523. Status: within budget (134 words below allowance, well past the 20-word safety margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 6 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 4 doctors (Doctor A to Doctor D); no names, specialties, fees or timings given | Doctors |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (defaults to false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.patient_name}}` | platform call-context value (unconfirmed) | Not set by the client |
| `{{var.appointment_details}}` | platform call-context value (unconfirmed) | Not set by the client |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
