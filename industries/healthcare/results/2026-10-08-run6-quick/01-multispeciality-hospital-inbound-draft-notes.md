**Assumptions and defaults used**
- Inbound only, as the profile states. An outbound agent needs its own run (R-72).
- Welcome is the default inbound template; the client may switch to Warm or Brief on the platform.
- Workflows 01, 02, 03 as selected. Booking style is time slots.
- Business word is "the hospital". Roster is 8 doctors (A to H), all through the roster variable. Doctor F's On leave status comes from the roster, so the agent offers a callback and never books Doctor F.
- Emergency department is yes, so the emergency line sends the caller to the hospital's emergency department. The no-emergency-department wording is kept as a conditional line in section 1.
- Extra emergency signs: none (the variable is empty). The default list is in full.
- Minors flag: false. Business info: beds and services, supplied through the custom detail, not typed here.
- Languages: start in the default language (English). Hindi and Kannada are covered by section 3, along with the other supported languages.
- The booking confirmation goes by WhatsApp or email (R-18), which matches the client's request.
- The 11 platform languages are handled by section 3.
- Section 6 includes the core lines and the lines for 01, 02 and 03. The tokens and standalone lines are not needed.

**Refused or adapted client requests**
- none. "Any roster doctor with status Available" is applied through the roster status. "No special client rules" means nothing to check.

**Open questions**
- No emergency transfer target was given. Section 1 uses the platform transfer tool to on-duty staff. If the transfer has no target, the agent should offer a callback (R-81). Please confirm the target.
- Can the emergency_signs_extra custom detail hold a list? It is empty here.
- The default emergency list needs review by the client's clinical team.
- How the "How it ends" template combines with the closing line in section 5 is unconfirmed.
- Whether a doctor with several shifts shows each shift in the roster is unconfirmed.

**Word counts**
- Welcome: 13. Section 1: 713. Section 2: 256. Section 3: 173. Section 4: 183. Section 5: 702.
- Section 6: 408 words (the roster placeholder is not counted). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget (23 under the allowance, so the margin of 20 is met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.company_name}}` | not provided | Your business (clinic name) |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.now_local}}` | built in | Automatic |
| `{{var.roster}}` | Doctors A to H (Doctor F: On leave); specialties, fees, shifts not provided | Doctors |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | beds and services (values not provided) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
