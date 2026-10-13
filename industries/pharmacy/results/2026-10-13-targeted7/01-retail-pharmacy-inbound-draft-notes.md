**Assumptions and defaults used**
- Confirmation channels (WhatsApp/email for order confirmations) were not given, so no confirmation flow is offered after an order is placed; the caller is told only the order number.
- The largest quantity an order may reach without the pharmacist was not given, so the documented default is used: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist. This default lives only in the Main prompt's ORDER step, not in the business facts.
- Only "pharmacist on duty" and "store manager" transfer targets were given. There is no separate "staff" number for delivery and return handoffs, so those are routed to the store manager.
- No extra emergency signs were given, so only the default list is used.
- The prescription upload method is in_store, so callers are asked to bring the prescription to the store, or offered a staff callback; there is no upload-link flow.

**Refused or adapted client requests**
- none

**Open questions**
- Return policy: not given. Callers currently hear "Our team will confirm that for you."
- Delivery areas, charges and usual delivery timing for the stores that do offer home delivery: not given. Callers currently hear "Our team will confirm that for you."
- The largest order quantity without the pharmacist: confirm the number of 3 with the owner, or give your own.
- A separate transfer number for staff (delivery and return handoffs), if you want these handled apart from the store manager.
- Whether you want order confirmations sent by WhatsApp or email; none are offered today.
- What the stock tool returns (in stock, price, whether a prescription is needed, whether a medicine is controlled) is assumed; please confirm with the platform team.
- What counts as a valid prescription, and the exact list of controlled or habit-forming medicines: for your pharmacist or compliance lead to confirm.
- Chat is not part of this setup; this is the voice version.

**Word counts**
- Welcome: 14. Section 1: 353. Section 2: 150. Section 3: 101. Section 4: 94. Section 5: 497.
- Section 6: 589 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Asha | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Transfer target: pharmacist | Pharmacist on duty | Transfer numbers |
| Transfer target: store manager / staff | Store manager | Transfer numbers |
| After-the-call trigger channels | Not set (no confirmation channel given) | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
