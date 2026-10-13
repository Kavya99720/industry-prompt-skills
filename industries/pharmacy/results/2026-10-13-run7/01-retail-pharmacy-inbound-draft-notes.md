**Assumptions and defaults used**
- Confirmation channels for order confirmations were not given, so no WhatsApp or email confirmation is offered after an order is placed (the section 5 confirmation step is skipped until this is set).
- The largest quantity orderable without the pharmacist was not given, so any order above one pack or strip of a medicine goes to the pharmacist and is not placed directly.
- Store address was not given, so the team-will-confirm line is used when a caller asks for directions, until the client adds it in the platform.
- No separate "staff" transfer target was given for delivery and status handoffs; these use the same team handoff phrase and route to the store manager or pharmacist as configured.
- Default language was taken as the given start language (English), with Hindi and Kannada already covered by the platform's supported language list; no separate configuration was needed for the expected switches.
- Which medicines always go to the pharmacist was not given, so the agent relies only on the stock tool's prescription-needed and controlled flags, and treats a missing flag as prescription-needed.

**Refused or adapted client requests**
- none. The client's stated rule ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") matches the standard order gate already built into the Instructions, so nothing needed to be refused or changed.

**Open questions**
- Delivery info and return policy were not provided; the agent currently says the team will confirm whenever a caller asks about delivery charges, timing or returns.
- Business info (the store services list) was named as something to include but no actual text was given; the client still needs to add it as a custom detail in the platform.
- What exactly counts as a valid prescription, and the exact controlled-medicine schedules, are open questions for the industry expert; the agent relies entirely on the stock tool's flags in the meantime.
- Whether the stock tool reliably returns the prescription-needed and controlled flags is unconfirmed; until it is, a missing flag is always treated as prescription-needed.
- Confirmation channels and the maximum order quantity without the pharmacist are not configured yet; both use their safe defaults (no confirmation offered; one pack or strip limit) until the client sets them.

**Word counts**
- Welcome: 13. Section 1: 862. Section 2: 197. Section 3: 172. Section 4: 156. Section 5: 1075.
- Section 6: 584 words. Allowance: 615 (no roster). Status: within budget (31 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start language) | Voice settings |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — client said it should list store services | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — one pack or strip default applies | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — no confirmation offered | Your business, Add a detail |
| Business type | Retail pharmacy chain | Your business |
| Call direction | Inbound | Your business |
| Workflows | Medicine enquiry, order and prescription, refill, delivery status and returns | Your business |
| Channel | Voice | Your business |
| Prescription upload | In store | Your business |
| Pickup or delivery | Store pickup; home delivery only for some stores | Your business |
| Return policy | not provided — the team will confirm | Your business |
| Payment modes | Cash and UPI at the counter | Your business |
| Transfer targets | Pharmacist on duty; store manager | Your business |
| Business hours | 8 AM to 10 PM, every day | Your business |
| Store address | not provided — the team will confirm | Your business |
| Languages | English to start; Hindi and Kannada expected | Your business |
| Extra emergency signs | none | Your business |
| Medicines always handed to the pharmacist | not given — relies on the stock tool's flags | Your business |
| Special client rules | none | Your business |
| Largest quantity without the pharmacist | not provided — one pack or strip default applies | Your business |
| Confirmation channels for order confirmations | not provided — no confirmation offered | Your business |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
