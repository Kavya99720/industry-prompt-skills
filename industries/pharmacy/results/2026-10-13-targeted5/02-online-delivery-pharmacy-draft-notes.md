**Assumptions and defaults used**
- Business word used throughout is "our online pharmacy" / "the pharmacy", per the client's instruction.
- Transfer targets given (pharmacist on duty, store manager, delivery desk) are all wired through `transfer`; no callback-only fallback was needed for the named handoffs.
- `confirmation_channels` (order-confirmation messages after a successful order) was not given, so no confirmation offer is written for a placed order; only the prescription upload link (WhatsApp, as given) is offered, since that is a separate flow.
- `prescription_upload_method` is WhatsApp, known at build time, so only the WhatsApp branch is written in section 5/6; the email fallback is kept as the "if no" branch per the rules, since the client gave no instruction to drop it.
- `max_qty_without_pharmacist` was not given: the default applies — any order above one pack or strip of a medicine goes to the pharmacist and is not placed.
- `store_address` was not given: online pharmacies may leave this empty; the agent says the team will confirm if asked for directions.
- `emergency_signs_extra`: none given, so only the default emergency signs list is in the prompt.
- Languages: start in English per the client; Hindi is expected and handled by the standard language-switching rules (no change needed).
- Channel defaulted to voice (not stated otherwise).

**Refused or adapted client requests**
- None. No client request conflicted with a critical rule.

**Open questions**
- No order-status tool is configured, so "where is my order?" is always answered with "I cannot see the status" plus a transfer or callback — confirm this matches what callers should expect, since delivery status is the client's stated main pain point.
- Confirmation messages after a placed order are not set up (no `confirmation_channels` given); if the client wants an order confirmation sent, that needs a value for that custom detail.
- Whether `check_stock` actually returns the prescription-needed and controlled flags is still open; until confirmed, a missing flag is always treated as prescription-needed.
- What counts as a valid prescription, and the exact controlled-medicine list, are for the pharmacist/compliance lead to confirm; none is typed into the prompt.
- Chat is not set up in this build; this is the voice version only.

**Word counts**
- Welcome: 13. Section 1: 393 (approx, prose paragraphs above — see note). Section 2: 162. Section 3: 123. Section 4: 92. Section 5: 520 (approx).
- Section 6: 573 words. Allowance: 615 (no roster). Status: within budget (42 words under, margin target of 20+ met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start), Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — (built in) | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items can be returned within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none | not used in these Instructions |
| `{{var.confirmation_channels}}` | not provided | not used in these Instructions |
| Business type | Online pharmacy with home delivery | — |
| Call direction | Inbound | — |
| Workflows | Medicine enquiry, order and prescription, refill (inbound), delivery status and returns | — |
| Channel | Voice | — |
| Prescription upload | WhatsApp | — |
| Pickup or delivery | Home delivery | — |
| Return policy | as above | — |
| Payment modes | as above | — |
| Transfer targets | Pharmacist on duty; store manager; delivery desk | — |
| Business hours | 9 AM to 9 PM, Monday to Saturday | — |
| Store address | not provided | — |
| Languages | English start, Hindi expected | — |
| Extra emergency signs | none | — |
| Always-hand-off medicines | none given | — |
| Special client rules | none | — |
| Largest quantity without the pharmacist | not provided | — |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
