**Assumptions and defaults used**
- Doctor A–E, G and H are assumed status Available for narrative purposes (only Doctor F was given as On leave); the actual status per doctor is set in the platform's Doctors config and the Instructions never hard-code it.
- Opening template assumed Standard (not specified); the client can pick Standard, Warm or Brief on the platform — wording is unaffected since the base welcome text is template-neutral.
- Closing template assumed the base inbound wording (Warm/Brief/Formal not specified); the client can pick a template on the platform.
- `{{var.default_language}}` assumed English (IN) from "English start"; Hindi and Kannada are reachable through the standard mid-call switch in section 3, not a default-language setting.
- `{{var.agent_name}}` and `{{var.agent_gender}}` are not intake items in this workflow; they are set directly in Voice settings and left as "not provided" below.

**Refused or adapted client requests**
- none — both requirements (booking any Available roster doctor; WhatsApp/email confirmation sent by the After-the-call trigger, no tool) already match the platform's default rules (R-41 and R-18), so nothing needed refusing or adapting.

**Open questions**
- Confirm the status (Available / On call / On leave) of Doctor A–E, G and H in the Doctors config; only Doctor F (On leave) was specified.
- Pick the opening template (Standard, Warm or Brief) and closing template (Warm, Brief or Formal) on the platform.
- Provide the actual beds and services text for `{{var.business_info}}`.
- Provide `{{var.clinic_address}}` and `{{var.business_phone}}` if directions or a language-fallback callback number should be spoken.
- The customer still needs to set up the After-the-call trigger for WhatsApp and email on the platform; the agent only states the channel in-call.

**Word counts**
- Welcome: 13. Section 1: 714. Section 2: 260. Section 3: 173. Section 4: 141. Section 5: 1092.
- Section 6: 411 words. Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 20 words below allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (IN), assumed from "English start" | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors, General Physician/Orthopaedics/Obstetrics/Paediatrics/Cardiology/ENT, Doctor F = On leave | Doctors |
| `{{var.business_info}}` | beds and services (exact text not given) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.

The customer sets up the After-the-call trigger for WhatsApp and email on the platform.
