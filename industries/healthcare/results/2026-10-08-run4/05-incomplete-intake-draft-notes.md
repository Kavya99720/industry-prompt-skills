**Assumptions and defaults used**
- Business type "small clinic": the agent says "our clinic". Inbound only, so the inbound welcome template is used. The client can pick Standard, Warm or Brief on the platform.
- Workflows 01 Enquiry and 02 Booking only. Time slots, so no TOKENS line.
- Languages not given: the call starts in `{{var.default_language}}`. The 11 platform languages are handled by section 3. No language was invented.
- Emergency department not given: assumed no (`{{var.emergency_department}}` = no). The emergency line says there is no emergency department and to call 1 0 8 or 1 1 2 or go to the nearest hospital.
- Emergency transfer number not given: the agent offers a callback during `{{var.business_hours}}` instead of a transfer (R-81). Emergency and self-harm lines say this.
- Address not given: `{{var.clinic_address}}` is kept for directions, but it has no value yet. Until it is set, directions should get "the team will confirm".
- Business phone not given: `{{var.business_phone}}` is used only in the unsupported-language fallback and has no value yet.
- Custom details not given: no extra emergency signs, `{{var.minors_may_book_alone}}` = false, `{{var.business_info}}` empty (the team will confirm).
- Roster has 2 doctors (General Physician, Paediatrics) and comes from the platform. No doctor, fee or timing is typed in the Instructions.
- Workflow 03 is not selected. The agent cannot change or cancel a booking and offers a callback. Verification (patient name plus booked number) is kept in section 5 for any existing-booking request.

**Refused or adapted client requests**
- "We have not decided the rest": nothing refused. Undecided items used the intake defaults above and are not invented.

**Open questions**
- Emergency department (yes or no) and an emergency transfer number: please confirm. Until then the agent gives 1 0 8 or 1 1 2 and offers a callback.
- Languages the clinic wants to support.
- Clinic address and business phone to fill in.
- Reschedule and cancel (workflow 03) is not included; the client may want it.
- Outbound calls (reminders) would need their own Instructions set.
- The default emergency signs list needs review by the client's clinical team.

**Word counts**
- Welcome: 16. Section 1: about 720. Section 2: about 255. Section 3: about 255. Section 4: about 190. Section 5: about 620. The per-section figures are estimates. The exact total for the welcome and sections 1 to 5 is 2,055 words. These sections do not count against the budget.
- Section 6: 405 words (exact; the roster placeholder is not counted). Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget, 164 words below the allowance.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given by the client (enter it as given) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A (General Physician), Doctor B (Paediatrics) from the platform roster | Doctors |
| `{{var.emergency_department}}` | not provided (treated as no) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (empty) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
