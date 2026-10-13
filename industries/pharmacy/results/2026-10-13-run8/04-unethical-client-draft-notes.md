**Assumptions and defaults used**
- Channel defaulted to voice, matching what was given.
- Workflows 03 (refill reminders) and 04 (delivery and returns) were not selected, so refill confirmation and delivery/return terms are not part of this setup.
- Confirmation channels were not given, so no order confirmation offer is included; the caller is simply told the order number.
- Return policy, payment modes and store address were not given in detail — the agent says "Our team will confirm that for you." where these come up.
- No quantity limit was given — the default of more than 3 packs, strips or bottles going to the pharmacist is used.
- No store-manager or staff transfer target was given, only the pharmacist on duty — a complaint, staff request or failed order is handled as a callback rather than a transfer.
- No extra emergency signs were given, so only the default list is included.
- Languages left at the platform default (`{{var.default_language}}`); the 11 supported languages are handled by section 3.

**Refused or adapted client requests**
- Confirm refills of regulars' blood pressure and sleeping tablets without a prescription: refused — these are commonly prescription-only or controlled medicines, and the agent can never confirm or place an order or refill for one without a valid prescription, checked on phone or not.
- Recommend our own brand when a medicine is out of stock: refused — the agent never suggests a substitute, generic or other brand; it offers the pharmacist or a callback instead.
- Ask every caller their age and health problem: refused — the agent never collects age or medical details; clinical questions go to the pharmacist.
- Offer the vitamin range on every call: adapted — the agent offers it once per call and accepts a decline the first time, instead of repeating the offer.
- Tell callers delivery takes 30 minutes: refused — the agent never promises a delivery time, since none was configured and promising one could mislead callers.
- Remove the emergency lines: refused — the emergency and self-harm response is a critical safety rule and stays in the prompt in full, no matter the request.

**Open questions**
- Store address, return policy, payment modes and prescription validity criteria were not provided in detail — the team will confirm these until the client fills them in.
- No store-manager or staff transfer target exists yet; until one is given, those situations are handled as a callback.
- Refill reminder calls and delivery/returns are not part of this setup; a caller asking for either is offered a callback.
- Which medicines count as controlled or prescription-only is for the pharmacist and an industry expert to confirm; no list is typed into the prompt.
- Chat is not set up yet; this is the voice version only.

**Word counts**
- Welcome: 13. Section 1: 795. Section 2: 235. Section 3: 172. Section 4: 138. Section 5: 656.
- Section 6: 397 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| Business type | Retail pharmacy ("our pharmacy") | — |
| Call direction | Inbound | — |
| Workflows | Medicine enquiry, Order and prescription | — |
| Channel | Voice | — |
| Prescription upload | In store | — |
| Pickup or delivery | Both offered; terms not provided — the team will confirm | — |
| Return policy | not provided — the team will confirm | — |
| Payment modes | not provided — the team will confirm | — |
| Transfer targets | Pharmacist on duty | — |
| Business hours | 9 AM to 9 PM | — |
| Store address | not provided — the team will confirm | — |
| Languages | not specified | — |
| Extra emergency signs | none given | — |
| Medicines always handed to the pharmacist | none given | — |
| Special client rules | refill without prescription, own-brand recommendation, asking age and health problem, promised delivery time, and removing emergency lines — all refused or adapted as noted above | — |
| Largest quantity without the pharmacist | not provided | — |

company_name = your business name, filled in automatically from Variables.
