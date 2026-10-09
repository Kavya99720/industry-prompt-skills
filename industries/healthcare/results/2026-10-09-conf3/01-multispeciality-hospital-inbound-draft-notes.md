**Assumptions and defaults used**
- Business type "hospital" and direction "inbound" taken as given; welcome message and flow use the inbound template.
- Workflows 01 Enquiry, 02 Booking, 03 Reschedule/cancel taken as given (matches the inbound default anyway).
- Booking style "time slots" taken as given (matches the default, so no TOKENS line added).
- Roster: 8 doctors, used only through `{{var.roster}}`; the skill never types doctor names, specialties, fees or Doctor F's "On leave" status into the Instructions — those are set in the platform's Doctors config.
- `{{var.emergency_signs_extra}}` left empty (no extra signs given); the compact default emergency list is used as-is.
- `{{var.minors_may_book_alone}}` defaulted to false (not given); R-40's parent/guardian rule applies as written.
- `{{var.business_info}}` assumed to hold beds and services (given), used for enquiry answers only, never typed as a value.
- `{{var.emergency_department}}` = yes, so the emergency line says "our emergency department" rather than the no-ED variant.
- `{{var.default_language}}` assumed English, matching "English start"; Hindi and Kannada are already covered by the standard 11-language switching rules in section 3 — no extra scope needed.
- `{{var.confirmation_channels}}` = whatsapp, email, offered through the no-tool confirmation flow sent by the After-the-call trigger, exactly as the client asked.
- `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.business_hours}}` (value), `{{var.business_phone}}`, `{{var.clinic_address}}` not given in this profile; no value was invented — these are filled directly in the platform's Voice settings / Your business pages.

**Refused or adapted client requests**
- none — "callers may book any roster doctor with status Available" already matches the standing rule (R-41: On leave/On call doctors are never booked, Available ones are); no change to the skill was needed.
- none — the WhatsApp/email confirmation sent by the After-the-call trigger, not a tool, is already the only supported mechanism; the client's requirement needed no adaptation.
- No other special client rules were given.

**Open questions**
- Exact values for `{{var.agent_name}}`, `{{var.agent_gender}}`, `{{var.business_phone}}`, `{{var.clinic_address}}` and full business hours still need to be entered in the platform; none were supplied for this test profile.
- Doctor F's "On leave" status and the other 7 doctors' names, specialties, fees, about text and shifts are entered in the Doctors config, not this document.

**Word count**
- Section 6 (Main prompt): 406 words. Roster allowance: 8 doctors × 23 = 184. Budget: 615 − 184 = 431. Status: within budget, 25 words below the allowance (≥20-word margin met).
