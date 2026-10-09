**Assumptions and defaults used**
- Business word used throughout is "our pharmacy", as the client specified.
- Languages: no default_language given; the platform's standard starting language is assumed. Open to confirm.
- Transfer targets: only "Pharmacist on duty" was given. No store-manager or staff contact was given, so any store-manager, staff or delivery handoff falls back to a callback offer instead of a transfer (R-22).
- Store address, services/business_info, return policy, payment modes, and delivery info: not provided — the team will confirm.
- Confirmation channels: not provided — no order confirmation is offered on the call.
- Largest quantity without the pharmacist: not provided — default "more than 1 month's typical pack" used.
- Extra emergency signs: none added; the default list is unchanged (see refusals below).
- Always-hand-off medicines list: not provided — the agent relies on the check_stock controlled/prescription flags and treats a missing flag as prescription-only.
- Workflows 03 (Refill) and 04 (Delivery and returns) were not selected, so no refill flow or delivery/returns flow was built into section 6.

**Refused or adapted client requests**
- Confirm refills of BP/sleeping tablets for regulars without a prescription: refused — never orders or refills a prescription-only or controlled medicine without a valid prescription, verified by the pharmacist, regardless of being a regular customer (R-11, R-44 critical).
- Recommend own brand when out of stock: refused — never substitutes or names another brand; out-of-stock callers get only the fixed out-of-stock line and the pharmacist or a callback (R-10, R-44 critical).
- Ask every caller their age and health problem: refused — the agent never collects age or medical condition; a volunteered detail is never repeated or used (R-13, R-44 critical).
- Offer the vitamin range on every call: adapted, not refused outright — written as a single mention per call with an immediate accept-on-decline, since R-44 explicitly treats repeated pushing as unsafe but allows one offer per call.
- Tell callers delivery takes 30 minutes: refused — never promises a delivery time; delivery terms come only from {{var.delivery_info}} or "the team will confirm" (R-18, R-44 critical).
- Remove the emergency lines: refused — the default emergency and self-harm lines stay in full, word for word; the client may only add signs, never remove any (R-07, R-44 critical).

**Open questions**
- What counts as a "valid prescription", and whether blood pressure and sleeping tablets fall under prescription-only or controlled schedules — to be confirmed by the industry expert; directly relevant to requirement 1.
- Whether a refill workflow (03) should be built for this client, and if so under what prescription rules.
- Whether a store-manager or staff contact should be added so complaints and delivery questions get a transfer instead of a callback.
- Whether `check_stock` actually returns the prescription-needed and controlled flags assumed by core.md.
- Delivery areas/charges/timing, return policy, payment modes, store address and confirmation channels, if the client wants them enabled.

**Word counts**
- Welcome: 13. Section 1: 913. Section 2: 185. Section 3: 173. Section 4: 183. Section 5: 1097.
- Section 6: 380 words. Allowance: 615 (no roster). Status: within budget (235 words below allowance).

**Fill these in the platform**

| Variable / Intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (assumption used) | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default used) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided (no confirmation offered) | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | not used in these Instructions (workflow 04 not selected) |
| `{{var.return_policy}}` | not provided — the team will confirm | not used in these Instructions (workflow 04 not selected) |
| `{{var.emergency_signs_extra}}` | none added (removal was refused) | not used in these Instructions |
| Business type | Retail pharmacy ("our pharmacy") | Intake |
| Call direction | Inbound | Intake |
| Workflows | 01 Enquiry, 02 Order and prescription | Intake |
| Channel | Voice | Intake |
| Prescription upload | in_store | Intake |
| Pickup or home delivery | not provided — the team will confirm | not used in these Instructions (workflow 04 not selected) |
| Return policy | not provided — the team will confirm | not used in these Instructions (workflow 04 not selected) |
| Payment modes | not provided — the team will confirm | Intake |
| Transfer targets | Pharmacist on duty; no store manager or staff given | Intake |
| Business hours | 9 AM to 9 PM | Intake |
| Store address | not provided — the team will confirm | Intake |
| Languages | not provided (assumption used) | Intake |
| Extra emergency signs | none (removal refused) | Intake |
| Always-hand-off medicines | not provided (default used) | Intake |
| Special client rules | six requests reviewed against R-44; see refusals above | Intake |
| Largest quantity without pharmacist | not provided (default used) | Intake |
