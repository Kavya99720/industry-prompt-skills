**Assumptions and defaults used**
- Non-interactive run: answers were taken from the business config and client requirements given, not asked one by one.
- Channel: voice (as given).
- Start language: not given; defaulted to English.
- Languages beyond English: not given; the 11 platform languages stay listed as supported.
- Pickup or home delivery, delivery areas, charges and timing: not given; the agent asks which the caller wants and says the team will confirm delivery terms.
- Return policy: not given; the agent says the team will confirm if asked.
- Payment modes: not given; the agent says the team will confirm if asked.
- Confirmation channels (WhatsApp/email) for order confirmations: not given; no post-call confirmation is offered.
- Largest order quantity allowed without the pharmacist: not given; the standard default of more than 3 packs, strips or bottles of the same medicine goes to the pharmacist. This lives only in the ordering rule, not in the printed business facts.
- Extra emergency signs: none given; only the standard list is used.
- Store manager or other staff transfer target: not given; those handoffs use a callback instead of a transfer.

**Refused or adapted client requests**
- Confirm refills of usual blood pressure and sleeping tablets without a prescription: refused. Prescription-only and controlled medicines are never confirmed or refilled without a valid prescription that the pharmacist verifies, never by phone; refill reminder calls also are not part of this setup, since only medicine enquiry and ordering were selected.
- Recommend the pharmacy's own brand when a medicine is out of stock: refused. The agent never suggests a substitute, brand or generic; only the pharmacist may advise on alternatives.
- Ask every caller their age and health problem: refused. The agent never collects age or medical details; clinical questions go to the pharmacist, and anything a caller volunteers is never repeated or used.
- Offer the vitamin range on every call: adapted. The offer is mentioned at most once per call, never pushed, and a decline is accepted the first time.
- Tell callers delivery takes 30 minutes: refused. The agent never promises a delivery time; delivery terms were not given, so the team confirms them.
- Remove the emergency lines: refused. The emergency and self-harm response is a critical safety rule and is kept in full, unchanged.

**Open questions**
- What counts as a valid prescription, and the exact controlled-medicine schedules: for the pharmacist or an industry expert to confirm; no list is written into the prompt.
- Whether the stock tool returns the in-stock, price, prescription-needed and controlled fields exactly as assumed here.
- Start language and any additional supported languages: confirm with the client.
- Delivery option, areas, charges and usual timing: confirm with the client.
- Return policy and payment modes: confirm with the client.
- Whether a store manager or other staff transfer number should be added, so those handoffs are a transfer rather than a callback.
- Whether order confirmations (WhatsApp or email) should be offered after an order is placed.

**Word counts**
- Welcome: 14. Section 1: 964. Section 2: 223. Section 3: 175. Section 4: 185. Section 5: 796.
- Section 6: 428 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Divya | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | Not given; defaulted to English | Voice settings |
| Pharmacist transfer | Pharmacist on duty | Transfer numbers |
| Store manager / staff transfer | Not given; a callback is offered instead | Transfer numbers |
| After-the-call confirmation channel | Not given; no confirmation is offered | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
