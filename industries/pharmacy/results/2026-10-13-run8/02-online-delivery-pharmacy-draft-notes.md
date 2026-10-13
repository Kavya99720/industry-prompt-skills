**Assumptions and defaults used**
- Business type is "online or delivery pharmacy", so the agent says "our online pharmacy" everywhere except where the caller hears the business name.
- `max_qty_without_pharmacist` was not given: the default applies — more than 3 packs, strips or bottles of the same medicine goes to the pharmacist and no order is placed.
- No order-confirmation channels were given (separate from the prescription upload method), so no confirmation is offered after a successful order; the caller only gets "Is there anything else I can help with?" The prescription upload confirmation still runs, since WhatsApp was given for that.
- No extra emergency signs were given, so only the default list is in the prompt.
- Store address and extra business details (services, branches) were not given; the agent says the team will confirm if asked.
- Languages: call starts in English; Hindi (and the other 10 supported languages) are handled by the existing mid-call switching rules in section 3, no change needed.
- Transfer targets were given (pharmacist on duty, store manager, delivery desk), so the agent always has someone to transfer to; it never names the desk aloud, only "I'll connect you to our team," per the fixed team-handoff phrase.

**Refused or adapted client requests**
- none

**Open questions**
- There is no order-status tool, so "where is my order?" always ends in a transfer to staff or a callback, never a status, even though delivery status is the business's main reason for calls — confirm with the team whether a status lookup tool is planned.
- What counts as a valid prescription, and the exact controlled or prescription-only medicine list: for the industry expert, not typed into the prompt.
- Chat is not set up in this configuration; this is the voice version only.
- Whether `max_qty_without_pharmacist` should be set to something other than the default of 3.

**Word counts**
- Welcome: 13. Section 1: 912. Section 2: 235. Section 3: 172. Section 4: 138. Section 5: 859.
- Section 6: 592 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start), Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — (filled in automatically at call time) | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default of 3 applies | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| customer_name | not used in these Instructions | Call context (outbound only) |
| refill_details | not used in these Instructions | Call context (outbound only) |
| confirmation_channels | not provided | Your business, Add a detail |
| business type | online or delivery pharmacy | Intake |
| call direction | inbound | Intake |
| workflows | medicine enquiry, order and prescription, refill, delivery status and returns | Intake |
| channel | voice | Intake |
| prescription upload | whatsapp | Intake |
| pickup or delivery | home delivery | Intake |
| return policy | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Intake |
| payment modes | cash on delivery and UPI on delivery | Intake |
| transfer targets | pharmacist on duty, store manager, delivery desk | Intake |
| business hours | 9 AM to 9 PM, Monday to Saturday | Intake |
| store address | not provided — the team will confirm | Intake |
| languages | English start, Hindi expected | Intake |
| extra emergency signs | none | Intake |
| always-hand-off medicines | none given | Intake |
| special client rules | none | Intake |
| largest quantity without the pharmacist | not provided — default of 3 applies | Intake |

company_name = your business name, filled in automatically from Variables.
