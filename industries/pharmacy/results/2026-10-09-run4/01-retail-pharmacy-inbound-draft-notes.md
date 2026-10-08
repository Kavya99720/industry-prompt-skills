**Assumptions and defaults used**
- Business word: the profile allows "our store" or "the pharmacy"; the Instructions use "our store" as the main word (R-41), with "the pharmacy" kept in one fixed workflow line (place_order failure) since that line is copied word for word from the reference.
- Channel: voice (as stated). No chat requested.
- Prescription upload method: in_store, as given — the agent asks the customer to bring the prescription to the store, or offers a staff callback; `send_confirmation` is not used for upload instructions on this profile.
- Fulfilment: pickup, plus home delivery for some stores — delivery terms not given, so the agent says the team will confirm (R-66, R-74); the agent never states which stores deliver.
- Payment modes given (cash and UPI at the counter) — real value recorded only in the draft notes "Fill these in the platform" table, never in the Instructions (R-40).
- Delivery info and return policy: not provided — the agent uses the fixed missing-config line for both (R-74).
- Languages: start in English; Hindi and Kannada expected — `{{var.default_language}}` = English (IN); all 11 platform languages stay supported per the base (R-30), no restriction added.
- Custom detail, extra emergency signs: none given — the default emergency list is used as is; `{{var.emergency_signs_extra}}` is not referenced in the text since nothing was added.
- Largest quantity without the pharmacist (`{{var.max_qty_without_pharmacist}}`): not given — default is "more than 1 month's typical pack" (intake default, item 16).
- Medicines the client always wants handed to the pharmacist: none given — the agent relies on the stock tool's flags and the safety fallback (R-12).
- Transfer targets (pharmacist on duty, store manager) are used as named in the generic HANDOFF and store-manager routing; no specific names or numbers are written into the prompt (R-40).
- `check_stock` result fields (in stock, price, prescription-needed, controlled) are assumed per core.md; this is an open question for the platform team.

**Refused or adapted client requests**
- none — the one client requirement ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") matches the existing order gate (R-50) exactly and needed no change. No special client rules were given.

**Open questions**
- Whether `check_stock` actually returns in-stock, price, prescription-needed and controlled flags (core.md, platform question 12).
- Whether `send_confirmation` is the platform's real tool name for a WhatsApp or email send (platform question 13) — not used on this profile since upload method is in_store, but relevant if the client later switches methods.
- What counts as a valid prescription, and the exact controlled/habit-forming medicine schedules — to be confirmed by the industry expert (R-11, R-12).
- Whether a custom detail can hold a list, for `{{var.emergency_signs_extra}}` if the client later adds signs.
- Which stores offer home delivery is not written into the prompt; if needed, it should go into `{{var.delivery_info}}` or `{{var.business_info}}` once the client provides it.
- Chat channel was not requested, so no chat Instructions were written (R-45 not triggered).

**Word counts**
- Welcome: 13. Section 1: 713. Section 2: 185. Section 3: 172. Section 4: 138. Section 5: 639.
- Section 6: 582 words. Allowance: 615 (no roster). Status: within budget (33 words below allowance, margin requirement of ≥20 met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (start), with Hindi and Kannada expected mid-call | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business (filled in automatically from Variables) |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | store services (list not provided) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail |
| `{{var.return_policy}}` | not provided | Your business, Add a detail |
