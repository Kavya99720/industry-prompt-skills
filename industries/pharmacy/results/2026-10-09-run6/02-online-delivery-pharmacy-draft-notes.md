**Assumptions and defaults used**
- Welcome template: used the default Standard inbound template word for word; client may pick Warm or Brief in the platform instead.
- confirmation_channels: not provided — not used. No order-confirmation offer is made after `place_order`; only the prescription upload-link flow runs (governed separately by `prescription_upload_method`).
- max_qty_without_pharmacist: not provided — default "more than 1 month's typical pack" used; orders above that go to the pharmacist.
- store_address and business_info: not provided — the agent says "our team will confirm" if asked for directions or services (online pharmacy may reasonably leave these empty).
- default_language: left as a platform variable; client said "English start, Hindi expected," which matches the default English(IN) start plus mid-call switching already built into section 3; no English-only restriction was added.
- agent_gender: left as a platform variable with no assumed value.
- emergency_signs_extra: not used — "no extra emergency signs" means the default compact list only.
- Transfer targets (pharmacist on duty, store manager, delivery desk) are used for routing in section 1 and section 6 (HANDOFF, team phrase, store-manager escalation) but no target name is hard-coded; these are set in the platform's transfer configuration.

**Refused or adapted client requests**
- none

**Open questions**
- `check_stock` result fields (in-stock, price, prescription-needed, controlled) are assumed per core.md; to be confirmed with the platform team.
- Mechanics of the After-the-call trigger (what it reads to send the WhatsApp upload link) are unconfirmed; the agent states the channel aloud as a workaround.
- What counts as a "valid prescription," and the exact controlled/prescription-only medicine schedules, are to be confirmed by the industry expert — no list is typed into the prompt.
- This run covers inbound only, as specified. If the client later wants outbound refill reminders, that is a separate Instructions set and needs its own run (R-39).
- Chat channel was not requested (voice given) — not applicable here.

**Word counts**
- Welcome: 13. Section 1: 346 (approx, does not count against budget). Section 2: 169 (approx). Section 3: 164 (approx). Section 4: 128 (approx). Section 5: 544 (approx, does not count against budget).
- Section 6: 571 words. Allowance: 615 (no roster). Status: within budget (44 words below allowance, past the 20-word margin target).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | English start, Hindi expected | Voice settings |
| `{{var.business_hours}}` | 9 AM to 9 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (your business name) | Your business / Variables |
| `{{var.now_local}}` | — | Built in |
| `{{var.store_address}}` | not provided | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.return_policy}}` | unopened, unexpired items returnable within 7 days with the bill; wrong, damaged or expired items go to staff | Your business, Add a detail |
| `{{var.delivery_info}}` | delivery in the city and nearby areas; charges and usual timing as the business states | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| Business type | online or delivery pharmacy ("our online pharmacy") | Intake |
| Call direction | inbound | Intake |
| Workflows | 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns | Intake |
| Channel | voice | Intake |
| Pickup or delivery | home delivery (main channel) | Intake |
| Transfer targets | pharmacist on duty; store manager; delivery desk | Intake (transfer configuration) |
| Languages | English start, Hindi expected | Intake |
| Extra emergency signs | none | Intake |
| Always-hand-off medicines | none given — relies on `check_stock` flags | Intake |
| Special client rules | none | Intake |
| Confirmation channels | not provided — not used in these Instructions | Intake |
