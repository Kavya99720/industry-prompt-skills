**Assumptions and defaults used**
- Business type: small clinic, so the agent says "our clinic". Direction: inbound only, with the default inbound welcome. Outbound would need its own run.
- Workflows: 01 Enquiry and 02 Booking, as the client asked. 03 Reschedule/cancel is not included ("we have not decided the rest"). The client may change the welcome template (Standard, Warm or Brief).
- Booking style: time slots, as stated in the profile.
- Roster: 2 doctors (a General Physician and a Paediatrician) come from the platform Doctors config via `{{var.roster}}`. No doctor is typed into the prompt.
- Languages not given: the call starts in `{{var.default_language}}`, and section 3 handles the 11 platform languages. No language was invented.
- Emergency department not given: `{{var.emergency_department}}` is treated as no. The emergency line says "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now." The default emergency signs list is in full. `{{var.emergency_signs_extra}}` is empty, so there are no extra signs.
- Emergency transfer number not given: no transfer target was invented. The agent gives 1 0 8 or 1 1 2, connects to on-duty staff if it can, and otherwise offers a callback during `{{var.business_hours}}` (R-81).
- Address not given: directions use `{{var.clinic_address}}` only when asked. If it is empty, the agent says the team will confirm.
- Business info is empty: services and facilities are answered only from `{{var.business_info}}`. If it is empty, the team will confirm.
- `{{var.minors_may_book_alone}}` is false by default.
- Business hours were given as `{{var.business_hours}}` and are used for callbacks.
- Phone number: `{{var.business_phone}}` appears only in the unsupported-language fallback line in section 3.
- Doctor "about" text and fees are shared only from the roster.

**Refused or adapted client requests**
- "Just book appointments and answer questions. We have not decided the rest.": accepted as scope (Enquiry and Booking). The safety rules in core (emergency, self-harm, no diagnosis, verification, handoff) stay in because they are not optional.
- Missing emergency department and transfer number: adapted to the no-emergency-department wording and a callback instead of a transfer. The emergency response is not removed (R-09, R-76, R-81).

**Open questions**
- Does the clinic have an emergency department? Until confirmed, the prompt says it does not.
- Which number or staff group should emergency and handoff transfers go to? Until then the agent offers a callback.
- What languages does the clinic want to support? The default is the platform default language plus the 11 platform languages.
- Clinic address: needed in `{{var.clinic_address}}` so the agent can give directions.
- Should the clinic add Reschedule/cancel (03), or other flows later?
- Business info (services, facilities) is still empty.
- Clinical review of the default emergency signs list.
- The 24-hour time rule and the confirmation by WhatsApp or email depend on the booking and message tools being set up on the platform.

**Word counts**
- Word counts could not be computed by script in this run (script execution was not permitted), so the figures below are by hand. Only section 6 was counted line by line. The others are estimates.
- Welcome: 15. Section 1: about 720. Section 2: about 270. Section 3: about 215. Section 4: about 190. Section 5: about 660.
- Section 6: 473 words (without the roster placeholder). Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget, with about 96 words spare.
