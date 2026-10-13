**Assumptions and defaults used**
- Business type was given as a retail pharmacy chain; "our store" is used throughout, matching the config note that the agent says "our store" or "the pharmacy."
- Prescription upload method is in_store, so the upload-link flow (WhatsApp or email) is left out; the agent asks the customer to bring the prescription to the store, or offers a staff callback.
- Confirmation channels (WhatsApp or email order confirmation) were not given, so no confirmation offer is made after an order; the agent moves straight to the closing question.
- No largest-quantity figure was given, so the default applies: any order above one pack or strip of a medicine goes to the pharmacist and is not placed directly.
- No extra emergency signs were given, so only the default compact list is in the prompt.
- Business info was described as "lists the store services," but no actual service text was given; the variable is left for the team to fill in.
- Store address was not given; the agent says the team will confirm if asked for directions.
- Default start language is English, with Hindi and Kannada expected mid-call; the standard language-switching behaviour (all 11 supported languages) covers this without any custom change.
- Languages, delivery and returns being unconfirmed is expected at this stage and is listed as an open item below.

**Refused or adapted client requests**
- none

**Open questions**
- Delivery info is not provided — the team will confirm delivery areas, charges and usual timing before this goes live.
- Return policy is not provided — the team will confirm the return policy before this goes live.
- Store address is not provided — the team will confirm before this goes live.
- Business info (the store services text) is not provided — the team will add this as a custom detail.
- Whether a largest-order-quantity figure should be set, or whether the "above one pack or strip" default is acceptable for this chain.
- Whether order confirmations (WhatsApp or email) should be turned on; none are offered today.
- What exactly counts as a controlled or prescription-only medicine depends on the stock tool's flags; the exact schedules are for the industry expert to confirm.
- What counts as a valid prescription is not defined here; the pharmacist verifies it on handoff.
- This is the voice version only; chat is not part of this setup.

**Word counts**
- Welcome: 13. Section 1: 290. Section 2: 194. Section 3: 143. Section 4: 115. Section 5: 578.
- Section 6: 574 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (English assumed as the start language) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in, no setup needed |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | described as "lists the store services," text not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: above one pack or strip goes to the pharmacist) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none given | not used in these Instructions |
| `{{var.confirmation_channels}}` | not given | not used in these Instructions |
| `{{var.customer_name}}` | not applicable (inbound only) | not used in these Instructions |
| `{{var.refill_details}}` | not applicable (inbound only) | not used in these Instructions |
| Business type | retail pharmacy chain | not used in these Instructions (reflected as "our store" in the wording) |
| Call direction | inbound | not used in these Instructions (reflected in the welcome and flow) |
| Workflows | medicine enquiry, order and prescription, refill, delivery status and returns | not used in these Instructions (reflected in section 6) |
| Channel | voice | not used in these Instructions (reflected in section 5 style) |
| Prescription upload | in_store | see `{{var.prescription_upload_method}}` above |
| Pickup or delivery | store pickup; home delivery only for some stores | see `{{var.delivery_info}}` above |
| Return policy | not provided — the team will confirm | see `{{var.return_policy}}` above |
| Payment modes | cash and UPI at the counter | see `{{var.payment_modes}}` above |
| Transfer targets | pharmacist on duty; store manager | not used in these Instructions (reflected in section 6 handoffs) |
| Business hours | 8 AM to 10 PM, every day | see `{{var.business_hours}}` above |
| Store address | not provided — the team will confirm | see `{{var.store_address}}` above |
| Languages | English to start; Hindi and Kannada expected | not used in these Instructions (standard language switching covers this) |
| Extra emergency signs | none | see `{{var.emergency_signs_extra}}` above |
| Always-hand-off medicines | none given | not used in these Instructions (the stock tool's flags decide) |
| Special client rules | none, beyond the stated stock-tool ordering rule, which matches the default behaviour already in place | not used in these Instructions |
| Largest quantity without the pharmacist | not provided | see `{{var.max_qty_without_pharmacist}}` above |
