**Assumptions and defaults used**
- Business word: "our store", as given.
- Transfer targets given were the pharmacist on duty and the store manager; no separate "staff" person was named, so delivery-status, return and complaint handoffs route to the store manager (using the fixed team phrase), and complaints also go to the store manager.
- Largest quantity without the pharmacist: not given, so the default applies — more than 3 packs, strips or bottles of the same medicine goes to the pharmacist and no order is placed.
- Confirmation channels (WhatsApp or email confirmation after an order): not configured, so no confirmation offer is made; the agent only gives the order number and asks if there's anything else.
- Store address: not provided — not used in these Instructions is noted below.
- Languages: default_language starts in English as given; all 11 platform languages remain supported, with Hindi and Kannada expected in practice.
- Extra emergency signs: none added, so only the default list is used.
- Medicines always handed to the pharmacist: none given; the agent relies on the stock tool's prescription and controlled flags, plus "when unsure."
- Special client rules: none given.

**Refused or adapted client requests**
- none

**Open questions**
- Whether the stock tool returns in-stock, price, prescription-needed and controlled flags as assumed; if a flag is missing, the agent treats the medicine as prescription-needed.
- What counts as a valid prescription is for the pharmacist to judge; not defined here.
- Whether the platform can detect which stores offer home delivery, so the agent can tell a caller whether their specific store delivers (the agent currently relies on {{var.delivery_info}} for this).
- Store address and return policy are not provided — the team will confirm these if asked.
- Chat is not part of this setup; this is the voice version.

**Word counts**
- Welcome: 13. Section 1: 854. Section 2: 235. Section 3: 172. Section 4: 165. Section 5: 854.
- Section 6: 575 words. Allowance: 615 (no roster). Status: within budget (40 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (your business name) | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | store services (list to be filled in) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 3 packs, strips or bottles) | Your business, Add a detail |
| Business type | Retail pharmacy chain | — |
| Call direction | Inbound | — |
| Workflows | Medicine enquiry, Order and prescription, Refill, Delivery status and returns | — |
| Channel | Voice | — |
| Prescription upload | In store | — |
| Pickup or delivery | Store pickup; home delivery only for some stores | — |
| Return policy | not provided — the team will confirm | — |
| Payment modes | cash and UPI at the counter | — |
| Transfer targets | Pharmacist on duty; store manager | — |
| Business hours | 8 AM to 10 PM, every day | — |
| Store address | not provided — the team will confirm | — |
| Languages | English to start; Hindi and Kannada expected | — |
| Extra emergency signs | none | — |
| Always-hand-off medicines | none given | — |
| Special client rules | none | — |
| Largest quantity without the pharmacist | not provided (default: more than 3 packs, strips or bottles) | — |

company_name = your business name, filled in automatically from Variables.
