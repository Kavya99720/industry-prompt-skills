**Assumptions and defaults used**
- Business type "retail pharmacy chain" rendered as the plain word "our store" throughout, per the config instruction to say "our store" or "the pharmacy".
- Channel assumed voice (given explicitly in the profile); chat is not written.
- store_address: not given — left as a variable only, no value assumed; agent says the team will confirm if asked and the value is empty.
- business_info: config says it "lists the store services" but no actual text was given — left as a variable only.
- Medicines the client always wants handed to the pharmacist (intake #14): none specified — default used, relying solely on the stock tool's prescription/controlled flags and "when unsure" (R-12).
- max_qty_without_pharmacist (intake #16): not specified — default used ("more than 1 month's typical pack").
- Fulfilment detail "home delivery only for some stores" is a business fact, not a rule the agent can check (no tool exists to verify per-store delivery eligibility); the agent asks pickup or delivery and relies on {{var.delivery_info}} / team confirmation for anything store-specific.
- Languages: default_language assumed English per "English start"; Hindi and Kannada are both already in the platform's supported list, so no custom handling was needed.

**Refused or adapted client requests**
- None. The client requirement ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") matches the existing order gate (R-50) exactly and needed no change. "No special client rules" meant nothing else to evaluate against R-44.

**Open questions**
- Does `check_stock` actually return in-stock, price, prescription-needed and controlled flags? Until confirmed, a missing flag is treated as prescription-needed (R-12).
- Is the platform's WhatsApp/email send tool named `send_confirmation`? Confirmed as given in this profile's tool list, but not yet platform-verified elsewhere.
- What exactly counts as a "valid prescription" and the exact controlled-medicine schedules are to be confirmed by the industry expert; no list is typed into the prompt.
- Whether a custom detail can hold a list is irrelevant here since no extra emergency signs were requested.

**Word counts**
- Welcome: 13. Section 1: 834. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 888.
- Section 6: 574 words. Allowance: 615 (no roster). Status: within budget, 41 words below allowance (comfortably past the 20-word margin target).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business (filled in automatically from Variables) |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | store services (list text not provided) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| Business type | retail pharmacy chain | — |
| Call direction | inbound | — |
| Workflows | 01 Medicine enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery status and returns | — |
| Channel | voice | — |
| Pickup or delivery | store pickup; home delivery only for some stores | — |
| Return policy | not provided | — |
| Payment modes | cash and UPI at the counter | — |
| Transfer targets | pharmacist on duty; store manager | — |
| Business hours | 8 AM to 10 PM, every day | — |
| Store address | not provided | — |
| Languages | English start; Hindi and Kannada expected (both platform-supported) | — |
| Extra emergency signs | none | — |
| Medicines always handed to the pharmacist | none specified (default: stock-tool flags only) | — |
| Special client rules | none | — |
| Largest quantity without the pharmacist | not provided (default: more than 1 month's typical pack) | — |
