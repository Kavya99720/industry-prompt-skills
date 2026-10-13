**Assumptions and defaults used**
- Assistant name and gender not given: the welcome drops "This is <agent name>", section 1 does not name the agent, and section 4 uses only gender-neutral address for the caller.
- Business phone not given: every callback is offered without a phone number.
- Languages not given: the 11 platform languages stay in section 3, with English first, and calls start in English (the default start language).
- Emergency department not given: treated as no emergency department, so the emergency line says to call 1 0 8 or 1 1 2 and go to on-duty staff, with no department name.
- Emergency transfer number not given: the agent offers a callback instead of a transfer.
- Address not given: directions requests get "Our team will confirm that for you."
- Custom details were none: no extra emergency signs were added beyond the default list, and minors may not book alone.
- Booking style was given as time slots, so no tokens or walk-in line was added.
- No confirmation channel (WhatsApp or email) was given, so the after-booking confirmation flow is skipped entirely; the CLOSE step only says the appointment is booked.

**Refused or adapted client requests**
- None. The client's request ("just book appointments and answer questions") fits the Enquiry and Booking workflows as given; nothing needed to be refused or adapted.

**Open questions**
- Assistant name and gender: not given. Set in Voice settings, or the agent stays unnamed and gender-neutral.
- Business phone: not given. Needed for callbacks to include a number.
- Languages the clinic can actually handle: not given. The Instructions currently keep all 11 platform languages.
- Start language: not given. English was assumed; confirm or change.
- Whether the clinic has an emergency department and its transfer number: not given. The Instructions currently assume no emergency department.
- Clinic address: not given. Needed so the agent can give directions instead of "our team will confirm."
- Whether a confirmation should go out by WhatsApp or email after booking: not given. The confirmation step is currently skipped.

**Word counts**
- Welcome: 13. Section 1: 742. Section 2: 283. Section 3: 174. Section 4: 137. Section 5: 915.
- Section 6: 350 words. Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget (219 words below the allowance).

**Fill these in the platform**
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | not provided | Voice settings |
| Agent gender | not provided | Voice settings |
| Start language | not provided (assumed English) | Voice settings |
| Doctors | Doctor A (General Physician), Doctor B (Paediatrics) | Doctors |
| Emergency transfer number | not provided | Transfer numbers |
| After-the-call trigger channels | not provided (flow skipped) | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
