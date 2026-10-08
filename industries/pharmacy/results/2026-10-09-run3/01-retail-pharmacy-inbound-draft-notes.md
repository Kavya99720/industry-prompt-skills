**Assumptions and defaults used**
- Business type: retail pharmacy chain, written as "the pharmacy" throughout (R-41); the client may ask the platform welcome/closing to say "our store" instead, same meaning.
- `store_address`: not given; default empty, agent offers "Our team will confirm that for you." if asked for directions.
- `delivery_info`: not provided; default empty, fixed missing-config line used (R-74).
- `return_policy`: not provided; default empty, fixed missing-config line used (R-74).
- `max_qty_without_pharmacist`: not given; default is "more than 1 month's typical pack" (intake default).
- `emergency_signs_extra`: client said no extra signs, so only the default list is written; variable not used in the text.
- Inbound welcome template: Standard wording used as written in the references; client may pick Warm or Brief in the platform without changing the flow.
- Workflow 04's generic "transfer to staff" (delivery status, returns/complaints) was mapped to the store manager, since only "pharmacist on duty" and "store manager" were given as transfer targets and no separate delivery/returns staff role was named.
- Section 3 lists all 11 platform-supported languages per the fixed base text, not only Hindi and Kannada; the client's "Hindi and Kannada expected" describes likely traffic, not a restriction.

**Refused or adapted client requests**
- none. The one client requirement given ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") matches the skill's existing order gate (R-50) exactly, so nothing needed to be refused or changed.

**Open questions**
- Whether `check_stock` actually returns the in-stock, price, prescription-needed and controlled flags is unconfirmed; until then a missing flag is treated as prescription-needed (R-12).
- Home delivery is only available at some stores, but `{{var.delivery_info}}` is a single free-text field; the client should word it so the agent can say delivery is store-dependent (for example "available at select stores, confirmed at order time"), or this stays unresolved.
- Confirm whether "staff" in the delivery-status/returns steps should route to the store manager (assumed here) or to a separate role not yet named.
- `store_address`, `business_info`, `delivery_info`, `return_policy`, `payment_modes` and `max_qty_without_pharmacist` all need real values filled in on the platform; none were given beyond "payment_modes = cash and UPI at the counter."
- Chat channel was not requested, so no chat Instructions were written.

**Word counts**
- Welcome: 13. Section 1: 404. Section 2: 139. Section 3: 123. Section 4: 100. Section 5: 433.
- Section 6: 584 words. Allowance: 615 (no roster). Status: within budget (31 words of margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start), Hindi and Kannada expected mid-call | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | store services (text not given) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided (home delivery only at some stores) | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.now_local}}` | — | Built in |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
