**Assumptions and defaults used**
- Business type: small independent pharmacy, referred to as "our pharmacy" throughout, as given.
- Call direction: inbound, as given.
- Workflows: medicine enquiry and order/prescription only, as given; refill and delivery/returns were not requested, so they are not in this setup.
- Channel: voice, as given.
- Prescription upload method not given: default used — the agent asks the customer to bring the prescription to the store, or offers a staff callback. No WhatsApp or email upload step is written.
- Delivery info not given: the agent asks pickup or home delivery and takes the address for delivery, but states no delivery areas, charges or timing.
- Return policy not given: not used in this setup (no return workflow selected).
- Payment modes not given: default used — if asked, the agent says "Our team will confirm that for you." and offers a callback.
- Store address not given: the agent gives directions only if `{{var.store_address}}` is filled in; otherwise it says the team will confirm.
- Transfer targets (pharmacist, store manager) not given: default used — the agent offers a callback instead of a transfer for medicine questions, substitutes, controlled/unsure medicines, and complaints. The emergency and self-harm lines still say "transfer to the pharmacist" / "connect to the pharmacist" word for word, since those are fixed safety lines that apply regardless of a configured target.
- Languages not given: default used — the call starts in `{{var.default_language}}`; all 11 platform languages are supported through section 3.
- No extra emergency signs were given, so only the default list is in the prompt.
- No custom quantity limit was given, so the default applies: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist and no order is placed.
- No confirmation channels were given, so no WhatsApp or email order confirmation is offered after an order is placed.

**Refused or adapted client requests**
- none — "Just take orders and answer stock questions" matches the two workflows selected; nothing in the request conflicted with a critical rule.

**Open questions**
- Prescription upload method, delivery terms, return policy, payment modes, store address, transfer targets and supported languages are all not provided — the team will confirm these before go-live.
- Whether `check_stock` actually returns the prescription-needed and controlled flags is unconfirmed; until then, a missing flag is treated as prescription-needed and no order is placed.
- What counts as a valid prescription is for the pharmacist/industry expert to define; the agent only asks for one and never judges it.
- The exact medicines that should always go to the pharmacist (controlled/habit-forming schedules) are not listed in the prompt; the agent relies on the stock tool's flags and "when unsure."
- Chat is not part of this setup; this is the voice version only.
- Refill reminder calls (outbound) and delivery/returns are not part of this setup; they would need their own setup if wanted later.

**Word counts**
- Welcome: 13. Section 1: 822. Section 2: 235. Section 3: 172. Section 4: 138. Section 5: 766.
- Section 6: 442 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | not provided (given as a variable only, no value) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.now_local}}` | built in, no setup needed | Built in |
| `{{var.business_info}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.store_address}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.payment_modes}}` | not provided — the team will confirm | Your business, Add a detail |
| `{{var.prescription_upload_method}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.delivery_info}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.return_policy}}` | not provided — the team will confirm | not used in these Instructions |
| `{{var.emergency_signs_extra}}` | not provided | not used in these Instructions |
| `{{var.confirmation_channels}}` | not provided | not used in these Instructions |
| `{{var.customer_name}}` | not provided | not used in these Instructions (outbound only) |
| `{{var.refill_details}}` | not provided | not used in these Instructions (outbound only) |
| Business type | small independent pharmacy, agent says "our pharmacy" | Your business |
| Call direction | inbound | Your business |
| Workflows | medicine enquiry, order and prescription | Your business |
| Channel | voice | Your business |
| Prescription upload | not provided — the team will confirm | not used in these Instructions |
| Pickup or delivery | not provided — the team will confirm | not used in these Instructions |
| Return policy | not provided — the team will confirm | not used in these Instructions |
| Payment modes | not provided — the team will confirm | Your business, Add a detail |
| Transfer targets | not provided — the team will confirm | Your business |
| Business hours | given as `{{var.business_hours}}`, no value supplied | Your business |
| Store address | not provided — the team will confirm | Your business, Add a detail |
| Languages | not provided — the team will confirm | Voice settings |
| Extra emergency signs | not provided | not used in these Instructions |
| Always-hand-off medicines | not provided | not used in these Instructions |
| Special client rules | none | not used in these Instructions |
| Largest quantity without the pharmacist | not provided — the team will confirm | Your business, Add a detail |

company_name = your business name, filled in automatically from Variables.
