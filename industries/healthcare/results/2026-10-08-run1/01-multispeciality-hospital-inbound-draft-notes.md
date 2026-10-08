**Assumptions and defaults used**
- Booking style is time slots (given). Languages: start in `{{var.default_language}}`, English per profile; all 11 platform languages are handled by section 3.
- Doctors, status, fees, timings and "about" text come only from `{{var.roster}}`. Doctor F (On leave) is covered by the status rule: the agent never books them and offers a callback.
- Business hours (8 AM to 8 PM, every day), the beds and services text, and emergency department = yes are values for the platform config. They are not typed into the prompt.
- The welcome message is the default inbound template. The client can switch to the Warm or Brief template.
- No emergency transfer number was given. The emergency line says to transfer to on-duty staff and gives 1 0 8 or 1 1 2 even if no staff answer.
- The core UNDERSTAND line is in section 1, so it is not repeated in section 6, which keeps section 6 within budget.
- The workflow 01 DOCTORS symptom sentence is in section 1 (symptom to specialty rule). INFO's directions sentence is also in section 1 (`{{var.clinic_address}}`).
- Closing line is inbound only. A confirmation holds only doctor, date and time.
- `{{var.emergency_signs_extra}}` is empty (no extra signs). `{{var.minors_may_book_alone}}` is false.
**Refused or adapted client requests**
- Callers may book any roster doctor with status Available: accepted. It is the same rule as the booking workflow (On leave and On call doctors are never booked).
- Confirmation by WhatsApp or email: accepted as written. It is the workflow's confirmation step, and the agent never says the WhatsApp number aloud.
**Open questions**
- Can a custom detail hold a list (extra emergency signs)? Not needed for this profile (no extra signs).
- The default emergency signs list needs review by the client's clinical team.
- The transfer target for the emergency department and on-duty staff is not given.
- How the platform's "How it ends" templates combine with the closing line kept in section 5.
- Inbound only. An outbound reminder set needs its own run.
- Hindi and Kannada are expected. Confirm that the agent persona name and gender are set in Voice settings.
**Word counts**
- Welcome: 16 (counted by hand). Sections 1 to 5 were not counted with a script, because script execution was not permitted in this run. Hand estimates: Section 1: about 640. Section 2: about 300. Section 3: about 190. Section 4: about 190. Section 5: about 640.
- Section 6: 427 words (counted with wc). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget (4 words to spare).
