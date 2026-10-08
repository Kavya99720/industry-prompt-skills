**Assumptions and defaults used**
- Welcome message: used the standard outbound template given; matches the pharmacy section-base default exactly.
- max_qty_without_pharmacist: not given by the client; default applied is "more than 1 month's typical pack" (R-70).
- store_address, business_info, return_policy, delivery_info: not given; agent says the team will confirm where asked. return_policy and delivery_info are unused since workflow 04 was not selected.
- default_language, agent_gender: not given; left as the bare variables, filled by Voice settings.
- emergency_signs_extra: no extra signs given; default list only.
- Outbound closing line "Thank you for your time. Have a good day." used as the documented proposal (R-24); not yet signed off by legal/product per the open questions in platform-contract.md.
- check_stock result fields (in-stock, price, prescription-needed, controlled) assumed per core.md; missing flags are treated as prescription-needed (R-12, safety fallback).

**Refused or adapted client requests**
- None. The client's "refill reminders only, no sales, no offers, no medicine talk" request matches R-63 exactly and required no change. "Normal order gates apply if the customer wants the refill" matches the existing REFILL/ORDER/PRESCRIPTION gates and required no change.

**Open questions**
- Whether the platform passes `{{var.customer_name}}` and `{{var.refill_details}}` on outbound calls (both marked unconfirmed).
- Whether outbound calls must say "an AI assistant" up front (legal/product sign-off pending); current behaviour follows the client's welcome template and answers honestly only if asked.
- Whether the platform detects voicemail/no-answer on outbound calls, and whether a do-not-call tool exists; until confirmed the agent never says a stop-calling request is "done".
- Exact controlled/prescription-only medicine schedules, and what counts as a "valid prescription" — to be confirmed by the industry expert.
- Whether `check_stock` actually returns the prescription-needed and controlled flags assumed in core.md.
- Chat channel was not requested; voice only was written, per R-45 (noted for completeness, not applicable here since voice was specified).

**Word counts**
- Welcome: 14. Section 1: 618. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 565.
- Section 6: 573 words. Allowance: 615 (no roster). Status: within budget (margin of 42 words below the 615 allowance, meeting the ≤595 target).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `customer_name` | passed by the platform on outbound calls, unconfirmed | Call context |
| `refill_details` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.now_local}}` | built in | Built in |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
