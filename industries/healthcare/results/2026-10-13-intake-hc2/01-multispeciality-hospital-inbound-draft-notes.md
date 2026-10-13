**Assumptions and defaults used**
- Booking style confirmed as time slots, so the workflow 01 TOKENS line is not included.
- No extra emergency signs given, so only the core default emergency-sign list is written; nothing was added to it.
- Minors-may-book-alone flag left at its default, false.
- Business info custom detail is used for beds and services; not typed into the Instructions.
- Doctor roster, specialties and statuses (including Doctor F on leave) are not typed into the Instructions; they come from the platform's Doctors config through `{{var.roster}}`.
- Section 6 word allowance used 8 doctors (23 words each).

**Refused or adapted client requests**
- none

**Open questions**
- Business name, location, business phone and assistant name/gender were not given in this profile; set them in the platform (see the fill-in table).

**Word counts**
- Welcome: 13. Section 1: 302. Section 2: 148. Section 3: 101. Section 4: 92. Section 5: 538.
- Section 6: 411 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget (411 is 20 below the 431 allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (English assumed as the start language) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A to Doctor H) across General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT; Doctor F is On leave | Doctors |
| `{{var.business_info}}` | beds and services (exact text not given) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |

The customer also needs to set up the After-the-call trigger for WhatsApp and email confirmations on the platform; no in-call tool sends them.
