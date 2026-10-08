**Assumptions and defaults used**
- Business type: retail pharmacy chain, written as "our store" everywhere except where the caller hears the name, as the profile specified (R-41).
- Call direction: inbound only; outbound refill reminders need a separate Instructions run (R-39).
- Workflows: 01 Enquiry, 02 Order and prescription, 03 Refill (inbound steps only), 04 Delivery and returns, as listed.
- Channel: voice (default, not stated otherwise).
- Prescription upload: in_store, as given; the PRESCRIPTION step keeps the whatsapp/email branch too since `{{var.prescription_upload_method}}` is a platform variable the client can change later without a new prompt.
- Delivery info and return policy: not provided, so the agent says the team will confirm in both cases (defaults in R-66, R-67).
- Transfer targets: pharmacist on duty and store manager, as given. No separate "on-duty staff" target was named for delivery-status and return handoffs (core R-21 names staff as a third route); until a distinct target is given, those handoffs go to the store manager or a callback — listed again as an open item below.
- Store address: not explicitly given; left as `{{var.store_address}}`, said only when asked, never invented.
- Languages: start in English (`{{var.default_language}}`); Hindi and Kannada are both already in the platform's 11 supported languages, so no section 3 change was needed beyond noting them.
- Custom details: no extra emergency signs, so `{{var.emergency_signs_extra}}` is left unused and the default list is unchanged.
- `{{var.max_qty_without_pharmacist}}` not given: default is more than 1 month's typical pack (R-70).
- No client list of medicines that must always go to the pharmacist (intake Q14): the agent relies only on the stock tool's prescription/controlled flags and the "when unsure" fallback (R-12).

**Refused or adapted client requests**
- none — "callers may order any medicine the stock tool shows as not prescription-only and not controlled" already matches the standing order gate (R-50) word for word, so no rule was changed or added for it.

**Open questions**
- No distinct transfer target was given for delivery-status and return-problem handoffs (core R-21 calls for pharmacist / store manager / on-duty staff as three separate routes); for now these route to the store manager or a callback.
- Store address not given; the agent says the team will confirm until `{{var.store_address}}` is filled in.
- What counts as a "valid prescription" is to be confirmed by the industry expert (R-11).
- Exact controlled/prescription-only medicine schedules are to be confirmed by the industry expert (R-12); none are typed into the prompt.
- Whether `check_stock` reliably returns the prescription-needed and controlled flags is unconfirmed; until then a missing flag is always treated as prescription-needed (R-12 safety fallback).
- Chat channel was not requested, so it is not an open item here; voice only was written.

**Word counts**
- Welcome: 13. Section 1: 631. Section 2: 197. Section 3: 186. Section 4: 161. Section 5: 551.
- Section 6: 553 words. Allowance: 615 (no roster). Status: within budget (62 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (call starts here) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided (to list store services) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.now_local}}` | automatic, call date and time | Built in |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
```
