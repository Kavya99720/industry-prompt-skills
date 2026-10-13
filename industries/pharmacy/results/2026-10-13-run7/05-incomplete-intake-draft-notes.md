**Assumptions and defaults used**
- Business type: the client said "small independent pharmacy" but gave no business-type category; used the plain word "our pharmacy" throughout.
- Workflows: only medicine enquiry and ordering were selected, as given; the refill and delivery/returns workflows are not part of this setup.
- Prescription upload: not provided — the agent asks the customer to bring the prescription to the store, or offers a staff callback, instead of a WhatsApp or email upload link.
- Delivery info: not provided — the team will confirm; delivery terms and charges are not stated on the call.
- Return policy: not provided — not used, since no return/delivery workflow was selected.
- Payment modes: not provided — the agent says the team will confirm if asked how to pay.
- Store address and services: not provided — the agent says the team will confirm if asked.
- Languages: not specified — the call starts in the configured default language; the other platform languages are handled by the language-switching rules.
- Extra emergency signs: none given — only the default emergency signs list is in the prompt.
- Order confirmation channels: not specified — no WhatsApp/email confirmation offer is made after an order; the call simply closes.
- Largest order quantity without the pharmacist: not set — any order above one pack or strip is handed to the pharmacist.

**Refused or adapted client requests**
- "Just take orders and answer stock questions" was read as scope (which workflows to build), not as permission to skip safety rules: emergency handling, no-advice, no-substitute, prescription and controlled-medicine, privacy, verification and no-payment-details rules are included in full even though the client did not mention them — reason: these are critical safety rules that apply to every pharmacy setup regardless of what the client asked for.

**Open questions**
- No one was named to transfer calls to (pharmacist or store manager), so every handoff in this setup defaults to offering a callback; please confirm a transfer target before go-live, especially for the emergency line.
- What counts as a "valid prescription" for the prescription check is not defined yet; to be confirmed by the pharmacy's own compliance process.
- Whether the stock-check tool actually returns the prescription-needed and controlled flags is unconfirmed; until confirmed, a medicine with missing flags is always treated as prescription-only and sent to the pharmacist.
- The default emergency signs list should be reviewed by the pharmacy's own clinical lead before go-live.

**Word counts**
- Welcome: 13. Section 1: 683. Section 2: 190. Section 3: 172. Section 4: 175. Section 5: 720.
- Section 6: 393 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | provided (hours given as a variable, no value stated to us) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | — | Built in, no setup needed |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided — bring it to the store, or a staff callback | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — any order above one pack or strip goes to the pharmacist | Your business, Add a detail |
| Business type | small independent pharmacy (plain word "our pharmacy" used) | — |
| Call direction | inbound | — |
| Workflows | medicine enquiry, ordering and prescription | — |
| Channel | voice | — |
| Prescription upload | not provided — the team will confirm | not used in these Instructions |
| Pickup or delivery | not provided — the team will confirm | not used in these Instructions |
| Return policy | not provided | not used in these Instructions |
| Payment modes | not provided — the team will confirm | Your business, Add a detail |
| Transfer targets | not provided — a callback is offered instead | — |
| Business hours | provided | Your business |
| Store address | not provided — the team will confirm | Your business, Add a detail |
| Languages | not provided | not used in these Instructions |
| Extra emergency signs | not provided — no extra signs | not used in these Instructions |
| Medicines always handed to the pharmacist | not provided — none | not used in these Instructions |
| Special client rules | none | — |
| Largest quantity without the pharmacist | not provided — one pack or strip default | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
