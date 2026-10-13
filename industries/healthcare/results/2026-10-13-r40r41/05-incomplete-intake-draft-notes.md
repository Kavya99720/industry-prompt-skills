**Assumptions and defaults used**
- Emergency department not given: defaulted to `{{var.emergency_department}}` = no, so the emergency line uses the "no emergency department, call 108 or 112" wording (R-81, intake #8).
- Emergency transfer number not given: no transfer target is written; the agent offers a callback instead (R-81, intake #8).
- Languages not given: defaulted to starting every call in `{{var.default_language}}`, with the 11 platform languages handled by section 3 as usual (intake #7).
- Custom details not given (none): defaulted to no extra emergency signs (`{{var.emergency_signs_extra}}` empty), `{{var.minors_may_book_alone}}` = false, and `{{var.business_info}}` empty — the agent says the team will confirm where this would be used (intake #10).
- `{{var.confirmation_channels}}` not given: defaulted to empty, so the confirmation flow (R-18) is skipped entirely — no confirmation text appears in the Instructions.
- Booking style (time slots) and the 2-doctor roster were given directly, so no TOKENS line was added and the word budget used 2 doctors.

**Refused or adapted client requests**
- none — "Just book appointments and answer questions" does not touch any critical rule.

**Open questions**
- Clinic address not provided: `{{var.clinic_address}}` is referenced for directions but has no value yet; set it or the agent can only say the team will confirm.
- Emergency department status (yes/no) and a real transfer number need a decision from the client; the default emergency list also needs review by the clinic's clinical team (per core R-09).
- Whether to enable WhatsApp/email confirmations (`{{var.confirmation_channels}}`) once the client decides.
- Whether any language besides `{{var.default_language}}` should be the default start language.

**Word counts**
- Welcome: 13. Section 1: 690. Section 2: 245. Section 3: 173. Section 4: 157. Section 5: 556.
- Section 6: 350 words. Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget (181 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given (not specified in this test) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | 2 doctors — Doctor A (General Physician), Doctor B (Paediatrics) | Doctors |
| `{{var.emergency_department}}` | not provided (default no) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (default none) | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (default empty) | Your business, Add a detail |
