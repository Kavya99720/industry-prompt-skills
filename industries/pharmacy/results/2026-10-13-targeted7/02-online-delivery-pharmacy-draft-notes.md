**Assumptions and defaults used**
- No largest-quantity limit was given, so the standard default applies: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist. This limit is only inside the ORDER step, not printed as a business fact.
- No confirmation channel (WhatsApp or email) was given for order confirmations, so the order-confirmation offer is skipped entirely. The prescription upload link still goes out by WhatsApp, since that method was given separately.
- No specific delivery charges or usual delivery timing were given, only "delivery in the city and nearby areas" (printed as given); a caller asking about charges or timing gets "Our team will confirm that for you."
- No services or branches beyond "online pharmacy with home delivery" were given, so none are listed separately in the business facts.
- No medicines were named for always going to the pharmacist; the agent relies on the stock tool's flags and the "unsure" rule.
- No extra emergency signs were given, so only the standard list is in the Instructions.
- Welcome template used is the standard inbound one; the client can choose Warm or Brief instead on the platform.

**Refused or adapted client requests**
- None. Nothing in the request conflicted with a safety rule.

**Open questions**
- Confirmation channel for order confirmations (WhatsApp, email or both) was not given — right now no confirmation offer is made after an order is placed.
- Exact delivery charges and usual delivery timing were not given — the agent currently says the team will confirm when asked.
- Largest quantity the agent may order without the pharmacist was not given — the standard default of 3 is being used; confirm if a different number is wanted.
- Whether there are specific medicines that should always go to the pharmacist regardless of the stock tool's flags.
- The exact fields the stock-check tool returns (in stock, price, prescription needed, controlled) still need confirming with the platform team.
- This is the voice version only; a chat version would need its own setup.
- Callers asking "where is my order" cannot get a status, since there is no order-status tool; they are verified and then handed to the delivery desk or offered a callback. Confirm this is the experience you want, since you mentioned this is a common question.

**Word counts**
- Welcome: 15. Section 1: 911. Section 2: 235. Section 3: 166. Section 4: 138. Section 5: 716.
- Section 6: 594 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Meera | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Pharmacist on duty transfer number | not provided | Transfer numbers |
| Store manager transfer number | not provided | Transfer numbers |
| Delivery desk transfer number | not provided | Transfer numbers |
| Prescription upload link channel | WhatsApp | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
