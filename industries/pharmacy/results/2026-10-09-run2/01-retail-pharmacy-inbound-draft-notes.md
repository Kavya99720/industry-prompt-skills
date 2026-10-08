**Assumptions and defaults used**
- Workflows: 01, 02, 03 (inbound only), 04 used exactly as specified; no outbound Instructions set written (none requested).
- `prescription_upload_method` = in_store, as given: agent asks the customer to bring the prescription to the store, or offers a staff callback.
- `delivery_info` not provided: default used — agent says the team will confirm delivery areas, charges and timing. The "home delivery only for some stores" nuance cannot be encoded per-store in one generic Instructions set; see open items.
- `return_policy` not provided: default used — agent says the team will confirm.
- `store_address`: not given, default empty; agent says the team will confirm if asked for directions.
- `emergency_signs_extra`: none given, so only the compact default emergency list is in section 1; variable not referenced since it is empty.
- `max_qty_without_pharmacist`: not given, default "more than 1 month's typical pack" used (R-70).
- Languages: default_language left as the platform Voice-settings variable; Hindi and Kannada are already covered by the standard 11-language support in section 3, so no custom config was needed.
- `business_info` is expected to hold the store services list per the client's note; exact text not given, so it is left as a variable, to be filled in the platform.

**Refused or adapted client requests**
- none — the stated client requirement ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") matches the existing order gate (R-50) exactly and required no change.

**Open questions**
- Whether `check_stock` returns the in-stock, price, prescription-needed and controlled fields assumed by core.md; until confirmed a missing flag is treated as prescription-needed (R-12).
- What counts as a valid prescription (R-11) and the exact controlled/prescription-only medicine schedules (R-12) — to be confirmed by the industry expert.
- "Home delivery only for some stores": this profile's Instructions offer pickup or delivery generically; how a per-store delivery toggle is reflected in `{{var.delivery_info}}` or store config is open.
- Whether the platform's send tool for prescription-upload instructions is in fact named `send_confirmation` (assumed per the tools given).
- Chat channel not requested — not applicable here.

**Word counts**
- Welcome: 13. Section 1: 686. Section 2: 197. Section 3: 172. Section 4: 188. Section 5: 625.
- Section 6: 555 words. Allowance: 615 (no roster). Status: within budget (60 words under allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start language); Hindi and Kannada expected mid-call | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | lists the store services (exact text not given) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided (no extra signs) | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
