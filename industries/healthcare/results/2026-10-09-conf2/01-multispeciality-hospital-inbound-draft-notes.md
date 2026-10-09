**Assumptions and defaults used**
- Non-interactive run: all answers taken from the profile text; nothing invented (R-81).
- Business type: Hospital → "the hospital" used everywhere except where the caller hears the name.
- Direction: Inbound → Instructions set is inbound only; welcome and flow match (R-72). Outbound would need its own separate run.
- Booking style: Time slots → no TOKENS line added.
- Roster: 8 doctors (placeholders Doctor A–H) across General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT. Doctor F's "On leave" status, and every other doctor's specialty, fee, about text and shifts, are set in the platform Doctors config, not typed into the Instructions (R-64, R-74); the Main prompt only references `{{var.roster}}`.
- Languages: default_language = English; Hindi and Kannada switches are already covered by the standard 11-language support in Section 3 — no custom change was needed.
- Emergency department: yes → the emergency line in Section 1 says "our emergency department" (R-09).
- Custom details: no extra emergency signs (emergency_signs_extra left unset, so it is not referenced in the text); minors_may_book_alone = false (default, matches client); business_info set to hold beds and services, referenced only through the variable (R-74).
- Confirmation channels: whatsapp, email → Section 5 confirmation flow included, offering both, sent only by the After-the-call trigger with no tool call, matching the client's request exactly (R-18).
- Special client rules: none given → none added.

**Refused or adapted client requests**
- none. The client's confirmation-channel request (After-the-call trigger, no tool) already matches how the platform and R-18 work, so nothing needed to be refused or changed.

**Open questions**
- Doctor F's "On leave" status and the other 7 doctors' specialty, fee, about text and shifts must still be entered in the platform's Doctors config under the placeholders Doctor A–H; the skill cannot set this.
- Platform open question (unresolved): whether a custom detail can hold a list or a flag — affects how `emergency_signs_extra` and `minors_may_book_alone` are actually stored even though neither is exercised here.
- Platform open question (unresolved): how the "How it ends" template (Warm/Brief/Formal) combines with the closing line kept in Section 5.
- Confirm whether the hospital wants to restrict supported languages to English, Hindi and Kannada only, or keep all 11 platform languages as written in Section 3 (currently all 11, per the base template).

**Word counts**
- Welcome: 13. Section 1: 285. Section 2: 150. Section 3: 120. Section 4: 100. Section 5: 390.
- Section 6: 406 words (excluding the `{{var.roster}}` placeholder line). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, 25 words below allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start; switches to Hindi/Kannada expected) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.now_local}}` | automatic | Built in |
| `{{var.roster}}` | 8 doctors (Doctor A–H): General Physician, Orthopaedics, Obstetrics, Paediatrics, Cardiology, ENT; Doctor F = On leave, others status/fees/shifts not provided | Doctors |
| `{{var.business_info}}` | beds and services (exact numbers/list not provided) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.confirmation_channels}}` | whatsapp, email | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
