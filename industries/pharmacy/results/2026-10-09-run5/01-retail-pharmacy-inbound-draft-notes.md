**Assumptions and defaults used**
- Business word: "our store" (chain, retail) used throughout; `{{var.company_name}}` reserved for welcome, closing, AI-disclosure line.
- Store address: not given — `{{var.store_address}}` defaults empty; the agent says the team will confirm if asked for directions.
- Return policy: not provided — the team will confirm (R-74 line used).
- Delivery info: not provided — the team will confirm. The fact that home delivery exists "only for some stores" cannot be enforced per store since there is no per-store lookup tool; this is listed as an open item below.
- Payment modes real value ("cash and UPI at the counter") is never written into the Instructions; only `{{var.payment_modes}}` is referenced, with the value going in the Fill table.
- Max quantity without the pharmacist: not given — default "more than 1 month's typical pack" used for `{{var.max_qty_without_pharmacist}}`.
- Extra emergency signs: none given — only the compact default list is written; `{{var.emergency_signs_extra}}` is not referenced in the prompt since it would be empty.
- Always-hand-off medicines list and what counts as a "valid prescription": not given — the agent relies on the stock tool's flags and the safety fallback (R-12), as the intake table allows.
- Languages: default_language is English; Hindi and Kannada are "expected" switches but section 3 already supports all 11 platform languages, so no change was needed.
- `send_confirmation` is listed among the tools and kept in section 5's WhatsApp/email branch, but with `prescription_upload_method` = in_store it will not actually be called in this configuration; this is expected, not an error.
- Client requirement "callers may order any medicine the stock tool shows as not prescription-only and not controlled" matches the existing order-gate default (R-50) exactly — treated as a confirmation, not a change, so it is not listed as a refusal or adaptation.

**Refused or adapted client requests**
- none

**Open questions**
- Stock tool fields: does `check_stock` actually return in-stock, price, prescription-needed and controlled flags? Until confirmed, a missing flag is treated as prescription-needed (R-12).
- Is the platform's send tool really named `send_confirmation`? It is currently unused in this flow (upload method is in_store) but is wired for future use.
- "Home delivery only for some stores": no per-store flag or tool exists, so the Instructions cannot restrict delivery offers by store; the lead should confirm whether this needs a custom detail or a tool.
- Exact definition of a "valid prescription", and the controlled/prescription-only medicine schedules: to be confirmed by the industry expert (R-11, R-12).
- Chat channel was not requested — voice-only is correct per intake default.

**Word counts**
- Welcome: 13. Section 1: 917. Section 2: 223. Section 3: 196. Section 4: 203. Section 5: approx. 740 (sections 1–5 do not count against the Main prompt budget).
- Section 6: 588 words. Allowance: 615 (no roster). Status: within budget, 27 words below allowance (margin target of ≤595 met).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English (implied start language) | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (retail pharmacy chain name) | Your business |
| `{{var.now_local}}` | — (platform-filled) | Built in |
| `{{var.business_info}}` | store services list (text not given, to be filled in) | Your business, Add a detail |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default "more than 1 month's typical pack" applies | Your business, Add a detail |
| Business type | Retail pharmacy chain | not a variable — used only to choose the plain business word |
| Call direction | Inbound | not a variable — Instructions written for inbound only |
| Workflows wanted | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound only), 04 Delivery and returns | not a variable |
| Channel | Voice | not a variable |
| Pickup or delivery | Store pickup; home delivery only for some stores (not enforceable per store — see open items) | not used in these Instructions as a per-store flag |
| Transfer targets | Pharmacist on duty; store manager | not a variable — used as the two `transfer` destinations |
| Languages | English start; Hindi and Kannada expected | not a variable — covered by the 11-language base in section 3 |
| Extra emergency signs | none | not used in these Instructions |
| Always-hand-off medicines | none given | not used in these Instructions |
| Special client rules | none | not used in these Instructions |
| Largest quantity without the pharmacist | not given | see `{{var.max_qty_without_pharmacist}}` above |
