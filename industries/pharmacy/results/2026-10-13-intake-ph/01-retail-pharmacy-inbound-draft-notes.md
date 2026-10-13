**Assumptions and defaults used**
- Business type given as "retail pharmacy chain"; the agent uses the plain word "our store" throughout, matching the client's instruction.
- Prescription upload method given as in_store, so section 5 and section 6 write only the in-store branch (bring it to the store, or a staff callback); the WhatsApp and email upload-link lines are left out.
- Confirmation channels (whatsapp/email, after an order number) were not given, so the whole post-order confirmation flow is left out; the agent does not offer a confirmation message.
- The fulfilment detail ("store pickup; home delivery only for some stores") is carried in business_info as a store service, since it was not given as a separate delivery terms value.
- Largest quantity without the pharmacist was not given, so the default applies: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist.
- Languages: English, Hindi, Kannada, in that order, from "English start, switches to Hindi and Kannada expected"; calls start in English.
- No extra emergency signs were given, so only the default emergency list is in the prompt.
- Medicines the client always wants handed to the pharmacist: none given; the agent relies on the stock tool's flags.

**Refused or adapted client requests**
- none

**Open questions**
- Business name, store address, business phone, and assistant name and gender were not given; "not provided" in the fill-in table below.
- Delivery terms (areas, charges, usual timing) and the return policy were not provided; the agent says the team will confirm.
- What counts as a valid prescription, and the exact controlled/prescription-only schedules, are for the industry expert to confirm; the agent relies only on the stock tool's flags.
- Whether the check_stock tool actually returns the in-stock, price, prescription-needed and controlled fields assumed here is still to be confirmed with the platform team.
- Chat is not set up in this request; this is the voice version only.

**Word counts**
- Welcome: 13. Section 1: 911. Section 2: 220. Section 3: 167. Section 4: 178. Section 5: 873.
- Section 6: 590 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | store pickup; home delivery only for some stores | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 3 goes to the pharmacist) | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (no extra signs) | Not used in these Instructions |
| `{{var.confirmation_channels}}` | not provided | Not used in these Instructions |
| business type | retail pharmacy chain | — |
| call direction | inbound | — |
| workflows | medicine enquiry, order and prescription, refill (inbound), delivery status and returns | — |
| channel | voice | — |
| prescription upload | in_store | — |
| pickup or delivery | store pickup; home delivery only for some stores | — |
| return policy | not provided — the team will confirm | — |
| payment modes | cash and UPI at the counter | — |
| transfer targets | pharmacist on duty, store manager | — |
| business hours | 8 AM to 10 PM, every day | — |
| store address | not provided | — |
| languages | English (start), Hindi, Kannada | — |
| extra emergency signs | none | — |
| always-hand-off medicines | none given | — |
| special client rules | none | — |
| largest quantity without the pharmacist | not provided (default: more than 3) | — |

company_name = your business name, filled in automatically from Variables.
