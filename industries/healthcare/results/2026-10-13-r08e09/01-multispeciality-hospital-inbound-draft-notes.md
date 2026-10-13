**Assumptions and defaults used**
- Business type "hospital" and inbound direction taken as given; the agent says "the hospital" everywhere except the welcome, closing and AI-disclosure lines.
- Workflows 01 Enquiry, 02 Booking, 03 Reschedule/cancel, booking style time slots: all as given; no TOKENS line needed.
- Roster: the skill never types the 8 doctors; all doctor data (including Doctor F's On leave status) comes from `{{var.roster}}` at runtime, per R-41, R-64.
- Emergency department = yes, so section 1 says "our emergency department" in the default emergency line. No extra emergency signs given, so only the core default list is written (`{{var.emergency_signs_extra}}` is left unused).
- `{{var.minors_may_book_alone}}` kept as a live flag defaulting to false, matching the given "minors flag false".
- `{{var.business_info}}` (beds and services) is referenced only as a variable; the actual text is filled in on the platform, not typed into the Instructions (R-74).
- Agent persona name, gender and default language were not given in this profile; left as `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.default_language}}` for Voice settings (not an intake question with a required answer in this run).
- Languages: default_language assumed English per "English start"; Hindi and Kannada are already covered by the fixed list of 11 supported languages in section 3, so no extra config needed.
- No special client rules: none applied.

**Refused or adapted client requests**
- none

**Open questions**
- Doctor F's "On leave" status needs no skill change (handled by R-41 from roster data), but confirm the platform's Doctors config marks it correctly.
- `{{var.business_info}}` text (number of beds, services list) still needs to be written into the platform custom detail; only a description was given, not the actual wording.
- Agent persona name, gender and starting language need to be set in Voice settings before go-live.
- This run covers inbound only; if the hospital also wants outbound calls (for example reminders), that needs a separate Instructions set (R-72).

**Word counts**
- Welcome: 13. Section 1: 755. Section 2: 245. Section 3: 173. Section 4: 166. Section 5: 1101.
- Section 6: 408 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget (23 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (assumed English) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.business_info}}` | beds and services (text not provided) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.emergency_department}}` | yes | Your business, Add a detail (drives the emergency line wording; not inserted as a runtime token) |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| roster | 8 doctors, Doctor A to Doctor H, across General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT; Doctor F status On leave | Doctors |
`{{var.company_name}}` = your business name, filled in automatically from Variables.

The customer sets up the After-the-call trigger for WhatsApp and email on the platform, since confirmations are sent that way and not by an in-call tool.
