**Assumptions and defaults used**
- Assistant name and gender not given: the welcome drops "This is <agent name>", no example in the language section, and only the gender-neutral caller-address line is used.
- Address not given: directions default to "Our team will confirm that for you."
- Business phone not given: callbacks are offered without a number.
- Business hours not given: callbacks say "during business hours" with no times.
- Transfer targets (fraud team, grievance team, branch staff) not given: every handoff offers a callback instead of a transfer.
- Branch and ATM information not given: branch/ATM/hours questions get "Our team will confirm that for you."
- Escalation path and grievance contact not given: complaint escalation questions get "Our team will confirm that for you."
- Confirmation channels not set: the confirmation flow is left out entirely.
- Languages not given: default to the 11 supported platform languages, calls start in English.
- Card blocking and balance lookup: not stated by the client, so both stay off, the documented default.
- Festival savings offer: only the name was given, no terms; it is mentioned by name once, only at the end of a general enquiry call, never pushed; any question about its terms gets "Our team will confirm that for you."

**Refused or adapted client requests**
- Verify by OTP readback instead of three questions: refused — reading back an OTP is never allowed; verification stays full name, registered mobile number, last 4 digits.
- Skip verification for familiar-sounding regular customers: refused — verification applies to every caller regardless of how familiar they sound, to block impersonation.
- Let callers move money or change their mobile number by voice when they sound sure: refused — no money movement or profile change is ever done by voice, whatever the caller's confidence.
- Promise complainants a refund within seven working days: refused — no refund, reversal, outcome or timeline is ever promised on a complaint call.
- Skip the cybercrime helpline and card block, offer a new credit card on fraud calls: refused — the helpline line is always said first on every fraud call, and no product is ever offered on a fraud or complaint call.
- Give the balance to a family member reporting the holder is ill: refused — account details go only to the verified account holder directly; a third party is told to have the holder call.
- Never say the agent is AI, present as a human officer: refused — the agent must disclose it is an AI whenever a caller clearly asks.
- Mention the festival offer once at the end of a general enquiry call: adapted — kept, but by name only, never on a fraud or complaint call, never pushed, and a decline is accepted; no offer terms are invented.

**Open questions**
- Assistant name and gender (not given).
- Bank address (not given).
- Business phone number (not given).
- Business hours (not given).
- Transfer targets: fraud team, grievance team, branch staff (not given).
- Branch and ATM information (not given).
- Escalation path and grievance contact (not given).
- Confirmation channels, WhatsApp or email (not set).
- Languages the bank can handle and the call's start language (not given).
- Terms of the festival savings offer (not given).
- Legal references and timelines are never quoted, since none were configured.
- Outbound calls need their own separate setup; this run covers inbound only.

**Word counts**
- Welcome: 13. Section 1: 1095. Section 2: 195. Section 3: 67. Section 4: 97. Section 5: 384. Section 6: 433 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | not provided | Voice settings |
| Agent gender | not provided | Voice settings |
| Start language | not provided (defaults to English) | Voice settings |
| Fraud team transfer number | not provided | Transfer numbers |
| Grievance team transfer number | not provided | Transfer numbers |
| Branch staff transfer number | not provided | Transfer numbers |
| Confirmation channels | not set | After-the-call trigger |
| Card blocking | off (default) | Banking tools |
| Balance lookup | off (default) | Banking tools |

If your hours, phone or address change, regenerate these Instructions.
