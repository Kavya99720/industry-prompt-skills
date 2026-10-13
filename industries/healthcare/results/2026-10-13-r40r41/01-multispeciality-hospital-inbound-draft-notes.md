**Assumptions and defaults used**
- Booking style: time slots, as given in the profile.
- Workflows selected: 01 Enquiry, 02 Booking, 03 Reschedule and cancel (inbound default), matching the profile.
- Emergency department = yes, so section 1 says "go to our emergency department" (R-09).
- No extra emergency signs given: `{{var.emergency_signs_extra}}` is left empty in the platform (default).
- Minors-may-book-alone = false, matching the default; R-40's parent/guardian rule applies as written.
- `default_language` assumed English from "English start" in the profile; Hindi and Kannada are handled automatically by section 3's 11 supported languages, no extra config needed.
- `agent_name`, `agent_gender`, `business_phone`, `clinic_address`, `company_name` were not given: these are Voice settings/Fixed fields set in the platform, not invented here (R-81).
- `{{var.business_info}}` (beds, services) was described only as "lists beds and services" with no actual values; left for the client to fill in as a custom detail. The agent says the team will confirm until it is filled in.

**Refused or adapted client requests**
- none — the client's requests (any Available roster doctor may be booked; confirmation sent by the After-the-call trigger, not a tool) already match the reference rules as written, so nothing needed refusing or adapting.

**Open questions**
- Real values for `business_hours`, `business_phone`, `clinic_address`, `company_name`, `agent_name`, `agent_gender`, `default_language` and `business_info` need to be entered in the platform (see below).
- The 8-doctor roster (names, specialties, fees, about text, shifts, and Doctor F's "On leave" status) needs to be entered under Doctors; the Instructions only reference `{{var.roster}}`.

**Word counts**
- Welcome: 13. Section 1: 677. Section 2: 260. Section 3: 173. Section 4: 147. Section 5: 757.
- Section 6: 406 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget (406 is 25 words below the allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (per "English start") | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors: General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT (placeholders Doctor A–H); Doctor F = On leave, others Available | Doctors |
| `{{var.emergency_signs_extra}}` | not provided (none) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | not provided (client said it lists beds and services) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |
| Emergency department (used to write the section 1 wording, not a token in the text) | yes | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.

The customer still needs to set up the After-the-call trigger for WhatsApp and email on the platform; the Instructions only state the channel in-call and never send anything themselves.
