**Assumptions and defaults used**
- Business word: used "our store" (the client's own phrasing) as the plain word in the running text; "the pharmacy" is the client's alternative and may be swapped in at the platform.
- Delivery: client said home delivery is only for some stores, with no delivery areas, charges or timing given. `{{var.delivery_info}}` is left for the team to fill; until then the agent says "Our team will confirm that for you."
- Return policy: not provided — the team will confirm.
- Store address: not provided — the team will confirm.
- Largest quantity without the pharmacist (`{{var.max_qty_without_pharmacist}}`): not given, so the default applies — more than 1 month's typical pack.
- Confirmation channels (`{{var.confirmation_channels}}`): not given, so the default applies — empty, no order confirmation offered. The flow is written in Section 5 so it activates automatically if the client sets this later.
- Always-hand-off medicines: none named by the client. The agent relies on `check_stock`'s controlled/prescription flags and the "treat a missing flag as prescription-needed" safety fallback (R-12).
- Extra emergency signs: none given; only the default list is in the prompt.
- Transfer targets: pharmacist on duty and store manager were given; no separate "staff" contact was named for delivery-status or returns handoffs, so these use the same team-handoff phrase and route to the store manager (or a callback if unavailable).
- Languages: default_language left as a Voice-settings value (the client said "English start"); all 11 platform languages, including Hindi and Kannada, are already covered by the standard Section 3 language-switching rules.

**Refused or adapted client requests**
- none — the client's stated rule ("callers may order any medicine the stock tool shows as not prescription-only and not controlled") is exactly the default order gate in the brief (R-50); no change was needed.

**Open questions**
- `check_stock` fields: whether it reliably returns in-stock, price, prescription-needed and controlled flags (if not, every medicine is treated as prescription-needed and handed to the pharmacist).
- What counts as a valid prescription, and the exact controlled/prescription-only medicine schedules — to be confirmed by the industry/clinical expert.
- Whether the platform's After-the-call trigger reads the full transcript or needs specific extracted fields (channel, email address, order number) for the upload-link step, since `{{var.prescription_upload_method}}` is set to in_store for this profile and no upload link will actually be sent.
- No "staff" transfer target beyond the pharmacist and store manager — confirm whether delivery/returns handoffs should go to the store manager, a third contact, or always a callback.
- Chat channel was not requested; voice-only Instructions were written per the default.

**Word counts**
- Welcome: 13. Section 1: 978. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 1016.
- Section 6: 571 words. Allowance: 615 (no roster). Status: within budget (44 words below the 615 allowance, inside the 595 margin target).

**Fill these in the platform**

| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided (English implied by "English start") | Voice settings |
| `{{var.business_hours}}` | 8 AM to 10 PM, every day | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — (platform-generated) | Built in |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided (should list the store's services, as requested) | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | in_store | Your business, Add a detail |
| `{{var.payment_modes}}` | cash and UPI at the counter | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — default used (more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided — default used (empty, no confirmation offered) | Your business, Add a detail |
| `{{var.delivery_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.return_policy}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | none given | Your business, Add a detail |
| Business type | Retail pharmacy chain (agent says "our store" or "the pharmacy") | — |
| Call direction | Inbound | — |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns | — |
| Channel | Voice | — |
| Prescription upload | in_store | — |
| Pickup or delivery | Store pickup; home delivery only for some stores | — |
| Return policy | not provided — the team will confirm | — |
| Payment modes | cash and UPI at the counter | — |
| Transfer targets | Pharmacist on duty; store manager | — |
| Business hours | 8 AM to 10 PM, every day | — |
| Store address | not provided — the team will confirm | — |
| Languages | English start, switches to Hindi and Kannada expected | — |
| Extra emergency signs | none | — |
| Always-hand-off medicines | none given | — |
| Special client rules | callers may order any medicine the stock tool shows as not prescription-only and not controlled (matches the default rule) | — |
| Largest quantity without the pharmacist | not provided — default used | — |
| Confirmation channels | not provided — not used in these Instructions (no confirmation offered) | — |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
