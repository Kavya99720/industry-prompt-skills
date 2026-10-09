**Assumptions and defaults used**
- Business type: treated as a small independent retail pharmacy; the agent uses "our pharmacy" as the plain word, per the client's instruction.
- Call direction: inbound, as stated; welcome and flow written inbound-only.
- Workflows: 01 Enquiry and 02 Order and prescription only, matching "just take orders and answer stock questions"; 03 Refill and 04 Delivery and returns were not selected and are not in section 6.
- Channel: voice (default and as given).
- Prescription upload method not given — default used: the agent asks the customer to bring the prescription to the store, or offers a staff callback; `{{var.prescription_upload_method}}` left unset.
- Delivery info not given — default used: the agent asks pickup or home delivery and, for delivery, takes and reads back the address; delivery charges/areas/timing are not stated, so if asked the agent uses the missing-config line ("Our team will confirm that for you.").
- Return policy not given — not applicable; workflow 04 (returns) is not selected, so no return-policy line is needed.
- Payment modes not given — default used: the agent states payment modes only via `{{var.payment_modes}}`, and when empty uses the missing-config line.
- Store address and services not given — default used: `{{var.store_address}}` and `{{var.business_info}}` left empty; the agent uses the missing-config line when asked.
- Languages not given — default used: start in `{{var.default_language}}`; the 11 platform languages are handled by section 3.
- Extra emergency signs, always-hand-off medicines, special client rules: none given — defaults used (no additions to the default emergency list; the agent relies on the stock tool's prescription/controlled flags per R-12).
- Largest quantity without the pharmacist not given — default used: `{{var.max_qty_without_pharmacist}}` left unset, so the limit is "more than 1 month's typical pack."
- `check_stock` is assumed to return in-stock, price, prescription-needed and controlled flags (core.md assumption); if a flag is missing the agent treats the medicine as prescription-needed and never places the order.

**Refused or adapted client requests**
- none

**Open questions**
- Transfer targets for the pharmacist and the store manager were not given (required intake item). The Instructions use the generic `transfer` tool and the fixed team/pharmacist phrases as written in the workflows; where no target is configured on the platform side, the agent falls back to a callback offer. The actual routing/target setup is an open item for the client.
- What counts as a "valid prescription" is to be confirmed by the industry expert (R-11).
- The exact controlled/flagged medicine schedules are to be confirmed by the industry expert (R-12); no list is typed into the prompt.
- Whether `check_stock` actually returns the prescription-needed and controlled flags is unconfirmed by the platform team; the safety fallback (treat as prescription-needed) is assumed.
- Chat channel was not requested, so no chat Instructions were written (not applicable here since voice was the given channel).

**Word counts**
- Welcome: 13. Section 1: 797. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 830.
- Section 6: 383 words. Allowance: 615 (no roster). Status: within budget (232 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given (value not given to the skill, placeholder only) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | Built in | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided (not used in these Instructions beyond asking pickup/delivery; no delivery-terms variable is spoken) | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — not used in these Instructions (workflow 04 not selected) | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided — not used in these Instructions | Your business, Add a detail |
| `{{var.customer_name}}` | not provided — not used in these Instructions (inbound only) | Call context (outbound) |
| `{{var.refill_details}}` | not provided — not used in these Instructions (inbound only, workflow 03 not selected) | Call context (outbound) |

| Intake item | Value given / default used |
|---|---|
| Business type | Small independent pharmacy — plain word "our pharmacy" |
| Call direction | Inbound |
| Workflows | 01 Enquiry, 02 Order and prescription |
| Channel | Voice |
| Prescription upload | Not provided — default: bring to store or staff callback |
| Pickup/delivery | Not provided — default: ask which, team confirms terms |
| Return policy | Not provided — not used (workflow 04 not selected) |
| Payment modes | Not provided — default: team will confirm |
| Transfer targets | Not provided — open item; callback fallback used |
| Business hours | Given (`{{var.business_hours}}`) |
| Store address | Not provided — default: team will confirm |
| Languages | Not provided — default: start in `{{var.default_language}}` |
| Extra emergency signs | None given |
| Always-hand-off medicines | None given — relies on tool flags |
| Special client rules | None given |
| Largest quantity without pharmacist | Not provided — default: more than 1 month's typical pack |
