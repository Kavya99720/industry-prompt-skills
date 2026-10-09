**Assumptions and defaults used**
- Prescription upload method: not provided — the team will confirm. Default behaviour: ask the customer to bring the prescription to the store, or offer a staff callback (intake #5).
- Delivery info: not provided — the team will confirm. Not operationalised in this build (only "pickup or home delivery" + address is asked in ORDER; delivery areas/charges/timing would need workflow 04, not selected) (intake #6).
- Return policy: not provided — the team will confirm. Not used, since workflow 04 (Delivery and returns) was not selected (intake #7).
- Payment modes: not provided — the team will confirm, via the missing-config fixed line in section 1 (intake #8).
- Transfer targets (pharmacist, store manager): not given, which is a required item with no default. Default applied: every non-emergency handoff offers a callback during {{var.business_hours}} instead of a transfer. Emergency and self-harm handoffs still name "transfer" word for word, since those fixed lines are mandatory regardless of configured targets.
- Store address: not provided — the team will confirm. {{var.store_address}} and {{var.business_info}} left as empty custom details.
- Languages: not given — default: start in {{var.default_language}}; the 11 platform languages are handled by section 3 as standard.
- Extra emergency signs: none given — default list only, nothing added or removed.
- Medicines always handed to the pharmacist: none given — relies on the stock tool's prescription/controlled flags and "when unsure" (R-12).
- Largest quantity without the pharmacist: not given — default is more than 1 month's typical pack, via {{var.max_qty_without_pharmacist}}.
- Confirmation channels for order confirmations: not given (not mentioned in the client's brief) — default: no confirmation offered; section 5's confirmation flow is written to skip entirely when {{var.confirmation_channels}} is not set.
- Channel: voice, as given (intake #4, matches default anyway).

**Refused or adapted client requests**
- none — the client's instruction ("just take orders and answer stock questions, we have not decided the rest") maps directly to workflows 01 and 02 and asked for nothing that conflicts with a critical rule. No refusal was needed.

**Open questions**
- Who the agent should transfer to for the pharmacist and the store manager — until set, every non-emergency handoff is a callback (intake #9).
- Prescription upload method, delivery info, return policy, payment modes, store address, confirmation channels — all "not provided", to be confirmed by the client and filled into business config.
- Whether workflow 04 (Delivery and returns) and workflow 03 (Refill) should be added later, since the client said "we have not decided the rest" — these were intentionally left out of this build at the client's own scoping, not defaulted in.
- What counts as a valid prescription, and the exact controlled/prescription-only medicine schedules — to be confirmed by the industry expert (R-11, R-12).
- The assumed `check_stock` result fields (in stock, price, prescription-needed, controlled) are unconfirmed by the platform team.
- Chat channel was not requested, so not applicable here; voice-only Instructions were written.

**Word counts**
- Welcome: 13. Section 1: 328 (approx, not counted against budget). Section 2: 90. Section 3: 101. Section 4: 109. Section 5: 505 (approx, not counted against budget).
- Section 6: 377 words. Allowance: 615 (no roster). Status: within budget, 238 words under allowance (well past the required 20-word margin).

**Fill these in the platform**
| Variable / Intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | not provided (variable given, value not set) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | filled in automatically from Variables |
| `{{var.now_local}}` | Built in | — |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided (default: more than 1 month's typical pack) | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided (default: no confirmation offered) | Your business, Add a detail |
| Business type | Small independent pharmacy | Intake — used as "our pharmacy" throughout |
| Call direction | Inbound | Intake |
| Workflows | 01 Enquiry, 02 Order and prescription | Intake — client scoped out 03 and 04 |
| Channel | Voice | Intake |
| Prescription upload | not provided — the team will confirm | Intake |
| Pickup or delivery | not provided — the team will confirm | Intake; not used in these Instructions beyond the pickup/delivery question |
| Return policy | not provided — the team will confirm | Intake; not used in these Instructions |
| Payment modes | not provided — the team will confirm | Intake |
| Transfer targets | not provided — the team will confirm | Intake — default is callback, see open questions |
| Business hours | given as `{{var.business_hours}}` | Intake |
| Store address | not provided — the team will confirm | Intake |
| Languages | not provided — the team will confirm | Intake |
| Extra emergency signs | none given | Intake; not used in these Instructions |
| Always-hand-off medicines | none given | Intake; not used in these Instructions |
| Special client rules | none given | Intake; not used in these Instructions |
| Largest quantity without pharmacist | not provided (default: more than 1 month's typical pack) | Intake |
| `{{var.delivery_info}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.return_policy}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.emergency_signs_extra}}` | none given | not used in these Instructions |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
