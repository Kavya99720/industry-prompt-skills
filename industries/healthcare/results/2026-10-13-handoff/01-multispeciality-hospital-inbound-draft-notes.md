**Assumptions and defaults used**
- Business type "hospital" given; plain word "the hospital" used throughout, {{var.company_name}} reserved for welcome, closing and AI-disclosure lines only.
- Direction, workflows (01/02/03) and booking style (time slots) were given explicitly and match the inbound defaults; no assumption needed there.
- `{{var.agent_name}}`, `{{var.agent_gender}}` not given: left as platform variables, not provided at authoring time.
- `{{var.default_language}}` set to English per "English start" in the intake.
- `{{var.business_phone}}`, `{{var.clinic_address}}` not given: left as platform variables with no value; used only where a callback or directions line needs them.
- `{{var.emergency_signs_extra}}`: none given, default empty; only the compact default emergency list is written.
- `{{var.minors_may_book_alone}}`: not given, default false, written literally into the rule text so the platform's stored value governs it at runtime.
- `{{var.emergency_department}}` = yes: resolved at authoring time into the "our emergency department" wording in section 1 (not left as a runtime variable, since the two wordings differ in substance).
- `{{var.business_info}}`: profile says it lists beds and services; no actual text given, so the Instructions reference the variable only and say "the team will confirm" where content is missing.
- Services/beds detail (intake Q6) and special client rules (intake Q11): none given beyond "beds and services" and "no special client rules".

**Refused or adapted client requests**
- none — "callers may book any roster doctor with status Available" already matches the existing default behaviour (R-41: On leave/On call doctors get a callback, never a booking); no change was needed.
- none — the WhatsApp/email confirmation sent by the After-the-call trigger, not a tool, already matches the fixed confirmation flow design (R-18/platform contract); the Instructions were written to that spec as-is.

**Open questions**
- `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.business_phone}}` and `{{var.clinic_address}}` have no value yet; fill them in on the platform before going live.
- Actual beds/services text for `{{var.business_info}}` was not supplied; add it as a custom detail so Enquiry answers are not limited to "the team will confirm".
- Doctor F is marked On leave in the roster; this is read live from the Doctors config (R-41 handles it) and needs no prompt change, flagged here only for visibility.

**Word counts**
- Welcome: 13. Section 1: 744. Section 2: 245. Section 3: 193. Section 4: 169. Section 5: 799.
- Section 6: 407 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 24 words below allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A–H) across General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT; Doctor F status On leave | Doctors |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | beds and services (text not provided) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |
| `{{var.emergency_department}}` | yes (resolved into section 1 wording; not a runtime variable in the text) | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.

The customer sets up the After-the-call trigger on the platform to send the confirmation on WhatsApp and email once a booking succeeds.
