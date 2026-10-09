**Assumptions and defaults used**
- Business type: client gave "small independent pharmacy" and specified the plain word to use is "our pharmacy" — used word for word, not a default.
- Call direction and workflows (inbound; 01 Medicine enquiry, 02 Order and prescription) were given directly, not defaulted.
- Prescription upload method not given → default used: ask the customer to bring the prescription to the store, or offer a staff callback (`{{var.prescription_upload_method}}` left unset).
- Delivery info not given, and workflow 04 (Delivery and returns) was not selected → no delivery-charges/areas text written; the order flow still asks pickup vs. home delivery only, per workflow 02.
- Return policy not given, and workflow 04 was not selected → no return text written.
- Payment modes not given → default used: "Our team will confirm that for you." when asked how to pay.
- Store address not given → default used: "the team will confirm" when asked for directions.
- Services/branches (`business_info`) not given → default used: "the team will confirm."
- Transfer targets not given → default used: medicine/safety handoffs still name "the pharmacist" (a safety-critical rule, never dropped); all other handoffs use the generic team phrase with no desk, person or extension named; if no one answers, a callback number and time are taken instead.
- Languages not given → default used: start in `{{var.default_language}}`; the 11 platform languages remain supported per the baseline language section.
- No custom emergency signs given → the default emergency sign list only; `{{var.emergency_signs_extra}}` left empty.
- Largest quantity without the pharmacist not given → default used: more than 1 month's typical pack.
- Medicines the client always wants handed to the pharmacist: none given → relies on `check_stock`'s prescription-needed/controlled flags and "when unsure" (R-12); no list typed into the prompt.
- Special client rules: none given.

**Refused or adapted client requests**
- none — "Just take orders and answer stock questions. We have not decided the rest." was taken as scope guidance (workflows 01 and 02 only); it asked for nothing that conflicts with a critical rule, so nothing was refused or adapted.

**Open questions**
- Transfer targets: who the pharmacist, store-manager and staff transfers actually connect to in the platform is not configured yet.
- Prescription upload channel (WhatsApp/email/in_store) still undecided by the client.
- Delivery info, return policy, payment modes and store address are all "not provided — the team will confirm"; if the client later wants refill or delivery/return handling, workflows 03 and 04 need their own run.
- Languages still undecided by the client.
- Controlled/prescription-only medicine schedules and what counts as a "valid prescription": to be confirmed by the industry expert (R-11, R-12).
- Whether `check_stock` reliably returns the prescription-needed and controlled flags is unconfirmed by the platform team; until then a missing flag is always treated as prescription-needed.

**Word counts**
- Welcome: 13. Section 1: 902. Section 2: 197. Section 3: 172. Section 4: 138. Section 5: 838.
- Section 6: 395 words. Allowance: 615 (no roster). Status: within budget (220 words under allowance).

**Fill these in the platform**
| Variable / Intake item | Value you gave | Where to set it | Note |
|---|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings | |
| `{{var.agent_gender}}` | not provided | Voice settings | |
| `{{var.default_language}}` | not provided | Voice settings | |
| `{{var.business_hours}}` | given | Your business | |
| `{{var.business_phone}}` | not provided | Your business | |
| `{{var.company_name}}` | your business name | Filled in automatically from Variables | |
| `{{var.now_local}}` | — | Built in | |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail | |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail | |
| `{{var.prescription_upload_method}}` | not provided — the team will confirm | Your business, Add a detail | |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail | |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail | |
| `{{var.emergency_signs_extra}}` | not provided (none) | Your business, Add a detail | |
| `{{var.delivery_info}}` | not provided | Your business, Add a detail | not used in these Instructions |
| `{{var.return_policy}}` | not provided | Your business, Add a detail | not used in these Instructions |
| `{{var.customer_name}}` | — | Call context (outbound only) | not used in these Instructions |
| `{{var.refill_details}}` | — | Call context (outbound only) | not used in these Instructions |
| Business type | Small independent pharmacy, agent says "our pharmacy" | Not a variable; fixed in the Instructions text | used |
| Call direction | Inbound | Platform call-direction setting | used |
| Workflows wanted | 01 Medicine enquiry, 02 Order and prescription | Not a variable | used |
| Channel | Voice (default) | Platform channel setting | used |
| Transfer targets | not provided | Not a variable; platform transfer routing | open item |
| Languages | not provided | Voice settings (`default_language`) | open item |
| Always-hand-off medicines | none given | Not a variable | relies on `check_stock` flags |
| Special client rules | none | — | — |
