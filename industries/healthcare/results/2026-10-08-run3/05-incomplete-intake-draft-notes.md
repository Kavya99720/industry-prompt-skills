**Assumptions and defaults used**
- Business type: small clinic, so the agent says "our clinic". Direction: inbound, so the inbound welcome template is used (the client may switch to the Warm or Brief template). Booking style: time slots.
- Workflows: 01 Enquiry and 02 Booking, as selected. The TOKENS line is not used. Workflow 03 (reschedule/cancel) was not selected. A caller who wants to change or cancel is handed off through HANDOFF (transfer or callback).
- Roster: 2 doctors (Doctor A, General Physician; Doctor B, Paediatrics), taken from the platform roster through `{{var.roster}}`. Doctors are not typed into the prompt.
- Languages not given: calls start in `{{var.default_language}}` and the 11 platform languages are handled by section 3. No other language was added.
- Emergency department not given: `{{var.emergency_department}}` is assumed to be no. The emergency line says there is no emergency department and to call 1 0 8 or 1 1 2 or go to the nearest hospital.
- Emergency transfer number not given: none was invented. After giving the numbers the agent offers on-duty staff only if a transfer is possible, and otherwise offers a callback during `{{var.business_hours}}`.
- Address not given: none was invented. `{{var.clinic_address}}` is used only for directions. If it stays empty, the agent should say the team will confirm.
- Custom details: no extra emergency signs, `{{var.minors_may_book_alone}}` = false, and `{{var.business_info}}` is empty, so services and facts get "the team will confirm".
- Business hours were given as `{{var.business_hours}}`, so callbacks can name them.
- Only inbound was written. An outbound set would need its own run (R-72).

**Refused or adapted client requests**
- "Just book appointments and answer questions. We have not decided the rest.": accepted as the scope. The undecided items were filled with the documented defaults above and not invented. No critical rule was removed.

**Open questions**
- Does the clinic have an emergency department? If yes, set `{{var.emergency_department}}` to yes.
- What is the emergency or on-duty transfer number, if any?
- Which languages should the agent support, and what is the default language?
- What is the clinic address, for directions?
- Should reschedule and cancel (workflow 03) be added?
- Should the clinic's clinical team review the default emergency signs list?
- Do the doctors have shifts and statuses set in the platform roster? The booking flow depends on them.

**Word counts**
- I could not run the counting script because the command needed approval. Counts below are manual estimates by whitespace tokens, not exact.
- Welcome: about 15. Section 1: about 560. Section 2: about 230. Section 3: about 190. Section 4: about 130. Section 5: about 560.
- Section 6: about 380 words (estimate). Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget by a wide margin on the estimate. A script run should confirm the exact figure.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given (value not included in the test profile) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | Doctor A (General Physician), Doctor B (Paediatrics), from the platform roster | Doctors |
| `{{var.emergency_department}}` | not provided (assumed no) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (empty) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (assumed false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (empty) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
