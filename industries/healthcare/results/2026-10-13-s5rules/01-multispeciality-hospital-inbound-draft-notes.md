**Assumptions and defaults used**
- Business type "hospital" and direction "inbound" taken as given; workflows 01 Enquiry, 02 Booking, 03 Reschedule and cancel match the inbound default.
- Booking style "time slots" taken as given (no TOKENS line added).
- Roster: 8 doctors, 6 specialties, Doctor F "On leave" — not typed into the Instructions; comes entirely from `{{var.roster}}` and the platform Doctors config, per R-74/R-81.
- `agent_name` and `agent_gender`: not given in the profile — left as "not provided"; must be set in Voice settings before go-live.
- `default_language`: set to English, matching "English start" in the profile. Hindi and Kannada switches need no extra configuration — section 3's base covers all 11 platform languages.
- `business_phone` and `clinic_address`: not given — listed as open items below.
- `business_info` (beds and services): the profile says this detail should exist but gives no actual figures — until filled in, the agent says "the team will confirm" for anything not present in it.
- `emergency_signs_extra`: none given — the default emergency list (R-09) is used as is, with no additions, and the variable is not referenced in the Instructions text.
- `minors_may_book_alone`: not given — defaulted to false, so R-40 is written as is (parent or guardian required for a minor calling alone).
- "No special client rules" — nothing further to assume.

**Refused or adapted client requests**
- none. "Callers may book any roster doctor with status Available" matches the default On-leave/On-call handling (R-41) exactly, so nothing needed changing. The WhatsApp/email confirmation sent by the After-the-call trigger, not a tool, matches R-18 exactly as written.

**Open questions**
- `agent_name`, `agent_gender`, `business_phone`, `clinic_address`: not provided in the profile; needed before the agent can go live.
- `business_info`: the profile says beds and services should be listed, but gave no real numbers or list — needs real text from the client.
- Whether this hospital wants `minors_may_book_alone` set to true was not stated; left at the default (false).
- Doctor F's "On leave" status, and all other roster fields, are set directly in the platform's Doctors config, not in these Instructions.

**Word counts**
- Welcome: 13. Section 1: 640. Section 2: 250. Section 3: 173. Section 4: 153. Section 5: 1135.
- Section 6: 409 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 22 words below the allowance (margin requirement met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A–H), General Physician / Orthopaedics / Obstetrics / Paediatrics / Cardiology / ENT, Doctor F = On leave, all others Available | Doctors |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (none) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false (default) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (should list beds and services) | Your business, Add a detail |

The customer sets up the After-the-call trigger for WhatsApp and email on the platform, since `{{var.confirmation_channels}}` = whatsapp, email.
`{{var.company_name}}` = your business name, filled in automatically from Variables.
