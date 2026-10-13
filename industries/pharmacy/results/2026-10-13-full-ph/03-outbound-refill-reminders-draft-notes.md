**Assumptions and defaults used**
- "Pharmacy chain" is spoken as "our pharmacy" throughout, as you specified.
- No start language was given; calls default to starting in English, with all 11 platform languages kept as supported since no language list was given either.
- No largest-order-without-the-pharmacist limit was given; defaulted to 3 packs, strips or bottles of the same medicine, a placeholder meant for your team to review.
- No order-confirmation channel (separate from the prescription upload) was given, so no confirmation offer is included after an order is placed; only the WhatsApp prescription upload link is offered.
- Only "Pharmacist on duty" was given as a transfer target. Any handoff that would otherwise go to a store manager or other staff falls back to a callback instead.
- Delivery charges, areas and timing, and a return policy, were not given; the agent says the team will confirm if asked.

**Refused or adapted client requests**
- none

**Open questions**
- This is the outbound refill-reminder call only. Inbound calls to the pharmacy need a separate Instructions set.
- Whether the platform actually passes the customer's name and the refill/medicine details on these outbound calls is unconfirmed; until it is, those steps rely on it being provided.
- Whether the platform detects voicemail or no-answer on an outbound call is unconfirmed.
- Whether there is a do-not-call tool is unconfirmed; the agent currently only promises your team will "update this," never that calling has stopped.
- Whether placing an order already captures a delivery address on its own (so the agent truly never needs to ask for one) is unconfirmed.
- What counts as a "valid" prescription, and the exact medicines or schedules that must always go to the pharmacist, are for your pharmacist or compliance lead to define; the agent currently relies only on the stock tool's flags.
- Whether the stock-check tool reliably returns prescription-needed and controlled flags is unconfirmed; until then, a medicine with missing flags is always treated as needing the pharmacist.
- Start language and the list of supported Indian languages were not given; confirm if English-only start and the full 11-language list are correct for your callers.
- The largest order quantity before the pharmacist gets involved (currently a placeholder of 3) should be confirmed by your team.

**Word counts**
- Welcome: 15. Section 1: 772. Section 2: 220. Section 3: 173. Section 4: 138. Section 5: 741.
- Section 6: 559 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Kiran | Voice settings |
| Agent gender | Male | Voice settings |
| Start language | Not provided — defaulted to English | Voice settings |
| Transfer number — pharmacist on duty | Pharmacist on duty | Transfer numbers |
| Transfer number — store manager / other staff | Not provided | Transfer numbers |
| After-the-call trigger channel | WhatsApp (prescription upload link only) | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
