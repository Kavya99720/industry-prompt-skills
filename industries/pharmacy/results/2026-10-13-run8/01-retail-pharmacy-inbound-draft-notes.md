**Assumptions and defaults used**
- No confirmation channel was given for order confirmations, so no confirmation offer is included in this call flow.
- Only the pharmacist and the store manager were given as transfer targets; there is no separate "staff" contact, so every non-pharmacist handoff (delivery, order status, returns, complaints) goes to the store manager with the team phrase.
- The agent is written to say "our store" consistently (the client allowed either "our store" or "the pharmacy").
- The agent starts calls in English, since "English start" was stated; the platform's 11 supported languages are handled by the language-switching rules either way.
- No limit was given for the largest quantity orderable without the pharmacist, so the default applies: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist.
- No medicines were named as "always hand off," so the agent relies entirely on the stock tool's prescription and controlled flags.

**Refused or adapted client requests**
- none

**Open questions**
- Home delivery is only available at some stores; the voice agent cannot tell which store a caller is at, so delivery terms are given only from the delivery information you configure. Confirm whether this should vary by branch.
- Return policy and delivery information were not provided — the team will confirm these on the call until you add them.
- Store address and business phone were not provided — the team will confirm these on the call until you add them.
- What exactly counts as a valid prescription is for your team or a pharmacy compliance expert to confirm.
- Whether the stock-check tool reliably returns the "prescription needed" and "controlled" flags for every medicine is unconfirmed; until then, a missing flag is treated as prescription-only and sent to the pharmacist.
- Chat was not requested; this is the voice version only.

**Word counts**
- Welcome: 13. Section 1: 880. Section 2: 235. Section 3: 172. Section 4: 138. Section 5: 824.
- Section 6: 591 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (assumed English, to match "English start") | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided — the team will confirm | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | filled in automatically | Built in |
| `{{var.business_info}}` | your store's services list (not provided — add it) | Your business, Add a detail |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 3 packs, strips or bottles goes to the pharmacist) | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| Business type | Retail pharmacy chain | not a variable |
| Call direction | Inbound | not a variable |
| Workflows | Medicine enquiry, ordering and prescriptions, refill, delivery status and returns | not a variable |
| Channel | Voice | not a variable |
| Prescription upload | In store — the customer brings it to the store, or is offered a staff callback | not a variable |
| Pickup or delivery | Store pickup; home delivery only at some stores | not a variable |
| Transfer targets | Pharmacist on duty; store manager | not a variable |
| Languages | English to start, with Hindi and Kannada expected | not a variable |
| Extra emergency signs | None given | not used in these Instructions |
| Always-hand-off medicines | None given — relies on the stock tool's flags | not a variable |
| Special client rules | None given | not used in these Instructions |

company_name = your business name, filled in automatically from Variables.
