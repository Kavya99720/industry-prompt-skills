**Assumptions and defaults used**
- Business word: "our clinic". Direction: inbound only. Workflows: 01 Enquiry and 02 Booking. Booking style: time slots (as given).
- Roster: 2 doctors from the platform roster through `{{var.roster}}`. No doctor is typed in the prompt.
- Languages not given: calls start in `{{var.default_language}}`. Section 3 handles the 11 platform languages. No language list was invented.
- Emergency department not given: `{{var.emergency_department}}` is treated as no. The emergency line says there is no emergency department and gives 1 0 8 or 1 1 2.
- Emergency transfer number not given: nothing is transferred. Every handoff (emergency, clinical question, report, complaint, request for a person, pharmacy, billing, insurance) becomes a callback during `{{var.business_hours}}` (R-81).
- Address not given: the address is only used through `{{var.clinic_address}}` when the caller asks for directions. If the platform value is empty, the agent says the team will confirm.
- Custom details not given: no extra emergency signs, minors may not book alone (false), `{{var.business_info}}` empty. The agent says the team will confirm anything it does not know.
- Welcome message: the default inbound template. The client may choose another template.
- Hours: given as `{{var.business_hours}}`.
- The skill is written for inbound only. An outbound set needs its own run.

**Refused or adapted client requests**
- "Just book appointments and answer questions": accepted. Workflows 01 and 02 only.
- "We have not decided the rest": nothing was left out of the safety rules. The skipped intake answers use the documented defaults, not made-up values.
- Emergency department and transfer number not decided: the emergency line is adapted (R-09), not removed, and a callback replaces any transfer (R-81).

**Open questions**
- Languages: which languages should the agent support? Only `{{var.default_language}}` and the platform defaults are used for now.
- Emergency department: does the clinic have one? Is there an on-duty staff number to transfer to?
- Address: is `{{var.clinic_address}}` set on the platform?
- Services, fees and insurers: set `{{var.business_info}}` and the roster fees. Until then the agent says the team will confirm.
- Extra emergency signs, and whether minors may book alone.
- Reschedule and cancel (workflow 03) is not included. Callers who want to change or cancel are offered a callback. Add workflow 03 if wanted.
- The default emergency list needs review by the clinic's clinical team.

**Word counts**
- Counted by hand as whitespace-separated tokens, because the counting script could not be run. Each number may be off by a few words.
- Welcome: 13. Section 1: 655. Section 2: 229. Section 3: 173. Section 4: 182. Section 5: 547.
- Section 6: 406 words. Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget.
