**Assumptions and defaults used**
- Business type is hospital, so the agent says "the hospital". Direction is inbound, so the default inbound welcome is used. The client may pick the Standard, Warm or Brief template.
- Workflows are 01 Enquiry, 02 Booking and 03 Reschedule/cancel. Booking style is time slots, as the profile says.
- Languages: the call starts in `{{var.default_language}}`. Hindi and Kannada are handled by section 3, along with the other platform languages.
- `{{var.emergency_signs_extra}}` is empty because no extra signs were given. `{{var.minors_may_book_alone}}` is false.
- `{{var.emergency_department}}` is yes, so the emergency line sends callers to the emergency department. No transfer number was given. The skill typed none, and the agent transfers to on-duty staff through the platform's transfer tool.
- The doctor count is 8. Doctor F's status, On leave, comes from the roster, so BOOK offers a callback and never books Doctor F.
- Closing line is inbound only. The AI-disclosure line is used only on a clear question.

**Refused or adapted client requests**
- "Callers may book any roster doctor with status Available": adapted. Doctors on call or on leave are never booked (R-41), and every booking needs the caller's yes at the read-back.
- "Confirmation by WhatsApp or email": accepted. The confirmation holds only doctor, date and time (R-18, R-19), and the caller chooses the channel.

**Open questions**
- Can a custom detail hold a list of extra emergency signs? Not needed here, since the field is empty.
- No emergency transfer number was given. Confirm that the platform transfer tool routes to on-duty staff.
- The default emergency signs list needs review by the client's clinical team.
- How do the platform's "How it ends" templates combine with the closing line in section 5?
- Workflow 03 verification uses name plus booked number only. No lookup tool exists to check them.
- Outbound calls need their own separate Instructions run.

**Word counts**
- Welcome: 16. Section 1: about 740. Section 2: about 290. Section 3: about 205. Section 4: about 150. Section 5: about 560. These are approximate. A word-count script was blocked in this environment, and I measured only the whole text (1,960 words for the welcome and sections 1 to 5).
- Section 6: 411 words (counted exactly). Roster: 8 doctors x 23 = 184. Allowance: 615 - 184 = 431. Status: within budget, with a 20-word margin.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 8 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 8 doctors (Doctor A to Doctor H), Doctor F On leave | Doctors |
| `{{var.emergency_department}}` | yes | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | false | Your business, Add a detail |
| `{{var.business_info}}` | the hospital's beds and services (details not provided) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
