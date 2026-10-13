**Assumptions and defaults used**
- Booking style: time slots, as given.
- Languages: calls start in English; Supported list in section 3 is English, Hindi, Kannada, in that order, per the profile.
- Emergency signs: no extra signs added; the default compact list is used as-is.
- Minors flag: `{{var.minors_may_book_alone}}` left at its default, false — a minor calling alone goes through a parent or guardian (R-40).
- Business info: profile says it lists beds and services but gives no actual text, so `{{var.business_info}}` is left for the client to fill in; the agent says "the team will confirm" until it is set.
- Assistant name and gender: not given — default to the team setting them in Voice settings.
- Business name, location and business phone: not given — "not provided" in the fill-in table.

**Refused or adapted client requests**
- none

**Open questions**
- Business name, location/address, business phone, assistant name and gender were not given in the profile.
- Content of `{{var.business_info}}` (beds, services) was not given — only that the custom detail should hold it.
- Doctor roster details (names, fees, about text, shifts) are configured directly in the platform's Doctors list, not written here; Doctor F's "On leave" status is set there and handled automatically by the on-leave line in section 5/6.

**Word counts**
- Welcome: 13. Section 1: 324 (approx, not budget-counted). Section 2: 130 (approx, not budget-counted). Section 3: 86 (approx, not budget-counted). Section 4: 80 (approx, not budget-counted). Section 5: 585 (approx, not budget-counted).
- Section 6: 408 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 23 words below allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A–H), across General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT; Doctor F status On leave | Doctors |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | beds and services (text not supplied) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |

The customer sets up the After-the-call trigger for WhatsApp and email on the platform; there is no send tool in the Instructions.

`{{var.company_name}}` = your business name, filled in automatically from Variables.
