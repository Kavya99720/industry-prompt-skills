**Assumptions and defaults used**
- Business word used throughout: "our online pharmacy" / "the pharmacy" per the given business type.
- Channel: voice (no chat requested).
- Prescription upload method: whatsapp, as given; the email branch of the upload flow (R-54) is kept as the fallback the rule requires if the caller says the number isn't on WhatsApp.
- No pickup option offered: fulfilment is home delivery only per the given config, so ORDER takes the delivery address directly instead of asking pickup-or-delivery.
- Transfer targets given for all three roles (pharmacist, store manager, delivery desk), so no callback-only default applies to HANDOFF or the team phrase.
- `max_qty_without_pharmacist` not given — default used: more than 1 month's typical pack.
- `confirmation_channels` not given — default used: empty, so no post-order confirmation offer is included; only the prescription upload link flow is written (that one is driven by `prescription_upload_method`, not `confirmation_channels`).
- `store_address` and `business_info` not given — left as custom details the client fills in; if empty the agent says the team will confirm, per default for an online pharmacy.
- `default_language` assumed English (IN) per "English start, Hindi expected"; Hindi is already in the supported list in section 3.

**Refused or adapted client requests**
- None. No special client rules were given, and the request to prioritise "where is my order?" handling was implemented through workflow 04's STATUS step (verify, then staff handoff or callback) rather than inventing an order-status tool, since none exists.

**Open questions**
- What counts as a valid prescription, and the exact controlled/flagged medicine schedules — to be confirmed by the industry expert.
- Whether `check_stock` returns the prescription-needed and controlled flags (R-12 safety fallback currently treats a missing flag as prescription-needed).
- Whether a custom detail can hold a list, relevant if `{{var.emergency_signs_extra}}` is ever used (not used here — none were given).
- Whether `place_order` already holds/accepts the delivery address, or whether the agent must always read it back as free text.
- The default emergency signs list needs review by the client's clinical team.

**Word counts**
- Welcome: 13. Section 1: 361. Section 2: 165. Section 3: 136. Section 4: 94. Section 5: 497.
- Section 6: 565 words. Allowance: 615 (no roster). Status: within budget (56 words of margin below the 595 target).

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (assumed start language) | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items can be returned within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default: more than 1 month's typical pack | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — not used in these Instructions | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided — not used in these Instructions | Your business, Add a detail |

| Intake item | Value given / default used | Note |
|---|---|---|
| Business type | Online pharmacy with home delivery | — |
| Call direction | Inbound | — |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns | — |
| Channel | Voice | — |
| Prescription upload | whatsapp | — |
| Pickup or delivery | Home delivery only | — |
| Return policy | 7-day return for unopened/unexpired items with bill; wrong/damaged/expired to staff | — |
| Payment modes | Cash on delivery and UPI on delivery | — |
| Transfer targets | Pharmacist on duty; store manager; delivery desk | — |
| Business hours | 9 AM to 9 PM, Monday to Saturday | — |
| Store address | not given | not used in these Instructions (online pharmacy) |
| Languages | English start, Hindi expected | — |
| Extra emergency signs | None given | not used in these Instructions |
| Always-hand-off medicines | None given | default: rely on check_stock flags (R-12) |
| Special client rules | None given | — |
| Max qty without pharmacist | not given | default: more than 1 month's typical pack |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
