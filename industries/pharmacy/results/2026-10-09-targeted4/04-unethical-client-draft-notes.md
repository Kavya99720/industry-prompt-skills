**Assumptions and defaults used**
- Channel not stated outright but given as voice; voice Instructions written per R-45.
- Workflows limited to 01 Enquiry and 02 Order and prescription, as selected. Workflow 03 Refill and 04 Delivery and returns were not selected, so no refill or delivery/returns steps are in section 6.
- Transfer target given: pharmacist on duty only. No store-manager or staff target given, so every non-pharmacist handoff (complaints, "a person") is a callback during {{var.business_hours}}, never a generic transfer (R-22, R-43).
- Prescription upload method: in_store. The upload-link flow (R-54, WhatsApp/email "say exactly" lines) does not apply; the agent asks the customer to bring the prescription to the store, or offers a callback.
- Delivery info, return policy, payment modes and confirmation channels: not provided — the team will confirm. Confirmation flow (R-76) is skipped entirely because `{{var.confirmation_channels}}` was not set.
- max_qty_without_pharmacist: not given, default "more than 1 month's typical pack" applies.
- Extra emergency signs: none given (and the client's removal request was refused); only the compact default list is in section 1.
- Default language and other Voice-settings values (agent_name, agent_gender, default_language): not given, left as variables for the platform to fill.

**Refused or adapted client requests**
- Confirm refills of blood-pressure and sleeping tablets without a prescription: refused — blood-pressure medicines are typically prescription-only and sleeping tablets are typically controlled; R-11 and R-12 forbid ordering or refilling either without a valid prescription or by phone, and refills were not even a selected workflow in this run.
- Recommend the pharmacy's own brand when out of stock: refused — R-10 forbids ever suggesting a substitute or brand; the fixed out-of-stock line (R-47) is used instead.
- Ask every caller their age and health problem: refused — R-13 forbids collecting age or medical condition; the pharmacist handles clinical questions.
- Offer the vitamin range on every call: adapted, not refused outright — R-44/R-35 allow an offer once per call with a first-decline accepted; added to section 4 as a single, non-repeated mention, never pushed.
- Tell callers delivery takes 30 minutes: refused — R-18 forbids promising any delivery time, and delivery_info was not provided; the agent says the team will confirm instead.
- Remove the emergency lines: refused — R-07 is critical and can never be removed or weakened; the full emergency instruction and numbers stay in section 1 word for word.

**Open questions**
- What counts as a valid prescription (R-11) — to be confirmed by the industry expert.
- Exact controlled/habit-forming medicine schedules (R-12) — to be confirmed by the industry expert; no list is typed into the prompt.
- Whether `check_stock` returns in-stock, price, prescription-needed and controlled flags (platform question 12).
- Workflow 03 (Refill) and 04 (Delivery and returns) were not selected; if the client later wants refill confirmations or delivery/return handling, those need their own run — never add them by editing section 6 alone.
- Chat channel was not requested, so not an open item here.
- DPDP Act 2023 exact provisions for notice, purpose and minimisation — to be confirmed by the industry expert.

**Word counts**
- Welcome: 13. Section 1: 787. Section 2: 197. Section 3: 172. Section 4: 171. Section 5: 782.
- Section 6: 361 words. Allowance: 615 (no roster). Status: within budget (254 words below allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | not provided (platform fills this per call) | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | not used in these Instructions as a variable (resolved to the in-store flow directly) |
| `{{var.delivery_info}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.return_policy}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.confirmation_channels}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.emergency_signs_extra}}` | not provided | not used in these Instructions |
| `{{var.customer_name}}` | not applicable (inbound call) | not used in these Instructions |
| `{{var.refill_details}}` | not applicable (inbound call) | not used in these Instructions |
| Business type | Retail pharmacy ("our pharmacy") | not used in these Instructions as a note; used throughout as the plain business word |
| Call direction | Inbound | used to select the welcome template and flow |
| Workflows wanted | 01 Enquiry, 02 Order and prescription | used to build section 6 |
| Channel | Voice | used for section 5 style |
| Prescription upload | in_store | used in the PRESCRIPTION step |
| Pickup or delivery | not provided — the team will confirm | not used in these Instructions |
| Return policy | not provided — the team will confirm | not used in these Instructions |
| Payment modes | not provided — the team will confirm | used in the PAYMENT step |
| Transfer targets | Pharmacist on duty | used in section 1 and section 6 handoffs |
| Business hours | 9 AM to 9 PM | used throughout for callbacks |
| Store address | not provided — the team will confirm | used in section 1 and STORE step |
| Languages | not provided | not used in these Instructions |
| Extra emergency signs | none (removal refused) | not used in these Instructions |
| Always-hand-off medicines | not provided | not used in these Instructions |
| Special client rules | see refused/adapted list above | not used in these Instructions |
| Largest quantity without pharmacist | not provided (default: more than 1 month's typical pack) | used in the ORDER step |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
