**Assumptions and defaults used**
- Confirmation channels were not set, so no confirmation offer is written (no WhatsApp or email lines), matching the rule that the flow is never used on outbound calls anyway.
- No extra emergency signs were given, so only the default emergency signs list is in the prompt.
- No offer or scheme was given, so no offer line is included.
- Balance lookup is off (default) and is not used in this fraud-alert call in any case.
- No branch, ATM, escalation, grievance, KYC-update or card-activation information was given; none of these are needed for this call type, so nothing was left out of the prompt.

**Refused or adapted client requests**
- none

**Open questions**
- The outbound welcome names Nisha as an AI assistant up front; this is the required outbound wording and differs from a plain "calling from" greeting.
- No legal references, RBI rules or grievance timelines are quoted anywhere, since none were configured.
- This is the outbound fraud-alert verification set only; an inbound set for this bank needs its own separate setup.
- This is written for voice only; a chat version was not requested and is not written.
- Branch staff was not given as a transfer target, so every handoff in this set (claimed authority, a reported death, out-of-scope requests, a failed block, a "no" answer) goes to the fraud team.
- Whether the platform actually passes the customer's name into this call is assumed yes; if it is ever empty, the agent asks "Am I speaking with the customer?" instead of using the name.

**Word counts**
- Welcome: 19. Section 1: 947. Section 2: 195. Section 3: 82. Section 4: 109. Section 5: 427. Section 6: 485 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Nisha | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Fraud team transfer number | given (not shown here) | Transfer numbers |
| Branch staff transfer number | not provided | Transfer numbers |
| Confirmation channels | not set | After-the-call trigger |
| Card blocking | on | Banking tools |
| Balance lookup | off (default) | Banking tools |

If your hours, phone or address change, regenerate these Instructions.
