**Assumptions and defaults used**
- Business type spoken as "our online pharmacy" or "the pharmacy", as you asked.
- Channel: voice (not specified, platform default).
- Agent name, agent gender and the starting language are set in Voice settings and were not given here.
- Confirmation channel for an order (WhatsApp or email) was not specified, so no confirmation is offered after an order is placed; the prescription upload link still goes out on WhatsApp as you set it.
- Store address and general business info (services, branches) were not given; the agent says the team will confirm if asked, which fits an online-only pharmacy.
- Largest quantity the agent may order without the pharmacist was not set; the standard default applies — more than 3 packs, strips or bottles of the same medicine goes to the pharmacist.
- Medicines you always want handed to the pharmacist were not listed; the agent relies on the stock tool's prescription-needed and controlled flags, and hands off whenever unsure.
- Business phone number was not given; it is used for callbacks and the "can't speak that language" fallback.
- No extra emergency signs were added; only the default safety list is used.

**Refused or adapted client requests**
- none

**Open questions**
- Order confirmation channel (WhatsApp or email) — not set; decide if you want one offered after an order, separate from the prescription upload channel.
- Business phone number, store address and general business info — not provided yet.
- What exactly counts as a valid prescription, and the exact controlled/prescription-only medicine list — for your pharmacist or compliance lead to confirm; the agent currently relies only on the stock tool's flags.
- Whether the stock tool reliably returns the in-stock, price, prescription-needed and controlled fields — if a flag is ever missing, the agent treats the medicine as prescription-only and hands off.
- Refill reminder calls (outbound) are not part of this set — that would need its own separate Instructions.
- Chat is not set up yet; this is the voice version.

**Word counts**
- Welcome: 13. Section 1: 710. Section 2: 235. Section 3: 172. Section 4: 138. Section 5: 901.
- Section 6: 568 words. Allowance: 615 (no roster). Status: within budget (47 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English, with Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.now_local}}` | Built in | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist | Your business, Add a detail |
| Business type | Online pharmacy with home delivery | Your business |
| Call direction | Inbound | Your business |
| Workflows | Medicine enquiry, order and prescription, refill, delivery status and returns | Your business |
| Channel | Voice (default) | Your business |
| Prescription upload | whatsapp | Your business, Add a detail |
| Pickup or delivery | Home delivery | Your business |
| Return policy | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| Payment modes | cash on delivery and UPI on delivery | Your business, Add a detail |
| Transfer targets | Pharmacist on duty; store manager; delivery desk | Your business |
| Business hours | 9 AM to 9 PM, Monday to Saturday | Your business |
| Store address | not provided — the team will confirm | Your business |
| Languages | English to start, Hindi expected; all 11 platform languages supported | Voice settings |
| Extra emergency signs | none | Your business, Add a detail |
| Always-hand-off medicines | not provided | Your business, Add a detail |
| Special client rules | none | Your business |
| Largest quantity without the pharmacist | not provided — default: more than 3 packs, strips or bottles | Your business, Add a detail |

company_name = your business name, filled in automatically from Variables.
