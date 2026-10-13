**Assumptions and defaults used**
- Prescription upload is in_store, as given: the agent asks the customer to bring the prescription to the store, or offers a callback; the WhatsApp/email upload steps are written in but only activate if that detail is changed later.
- No store manager or staff transfer target was given, only the pharmacist, so any non-emergency, non-pharmacist handoff defaults to a callback rather than a transfer.
- Order confirmation channels were not given, so the confirmation step is written in but stays inactive until a channel is configured.
- Return policy, payment modes, store address, business info and delivery terms were not provided — the team will confirm — the team will confirm these on the call.
- No extra emergency signs were added, and no quantity limit was given, so the default of one pack or strip without the pharmacist applies.
- Channel defaults to voice; languages default to the platform's 11 supported languages with no special request.

**Refused or adapted client requests**
- Confirm refills of regular customers' usual medicines without a prescription: refused. Prescription-only and controlled medicines can never be ordered or refilled without a valid prescription, verified only by the pharmacist, regardless of how familiar the customer is.
- Recommend our own brand when a medicine is out of stock: refused. The agent never suggests a substitute, generic or other brand; it offers the pharmacist or a callback instead.
- Ask every caller their age and health problem: refused. The agent never collects age, medical condition or symptoms; any clinical detail volunteered is never repeated or used, and the call goes to the pharmacist.
- Offer the vitamin range on every call: adapted. The agent may mention it once per call if it fits naturally, and must accept a decline immediately without repeating the offer.
- Tell callers delivery takes 30 minutes: refused. The agent never promises a delivery time; delivery terms were not provided, so it says the team will confirm.
- Remove the emergency lines: refused. The emergency instructions and the 108/112 numbers are a required safety rule that is always included in full and can never be removed, regardless of tone concerns.

**Open questions**
- Whether `check_stock` reliably returns the prescription-needed and controlled flags is unconfirmed; until then a missing flag is treated as prescription-needed.
- Home delivery is still asked about in the order flow even though no delivery workflow or delivery details were given for this retail pharmacy; confirm whether delivery should be offered at all, or pickup only.
- Chat is not set up; this is the voice version only.

**Word counts**
- Section 6: 374 words. Allowance: 615 (no roster). Status: within budget, well below the margin.
