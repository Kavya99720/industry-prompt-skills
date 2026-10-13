**Assumptions and defaults used**
- Business word: the agent says "our pharmacy" throughout, as given.
- Store address, business services and the general store-questions line (workflow 01's STORE step) were left out: not given, and this test profile selects only the STOCK and OUT OF STOCK lines of medicine enquiry.
- Delivery and returns (workflow 04) are not selected, so `{{var.delivery_info}}` and `{{var.return_policy}}` are not used; for a wanted home delivery the agent only says the team will confirm the delivery address and terms.
- No quantity limit was given, so `{{var.max_qty_without_pharmacist}}` is used with its documented fallback: any order above one pack or strip goes to the pharmacist.
- No order-confirmation channel (`{{var.confirmation_channels}}`) was given, so the general "confirmation on WhatsApp or email" offer after an order number is not offered; only the WhatsApp prescription-upload line is used, since the upload method was given.
- Extra emergency signs were not given, so only the default list is in the prompt.
- Languages, agent gender and the default start language were not given; the standard platform defaults and the 11 supported languages are used.
- Store address, services and languages are not provided — the team will confirm where relevant.

**Refused or adapted client requests**
- None of the client's stated requirements conflicted with a critical rule.
- Adapted: the order step's delivery-address line was changed from "take the address and read it back" (the inbound wording) to "say the team will confirm the delivery address, never say or take it aloud," because an outbound call must never say or collect the address (a safety rule for outbound calls).
- Adapted: the inbound REFILL step's wording (which re-asks the customer's name before the order number) was trimmed to pick up after the name is already confirmed and the order number given, since the outbound reminder step already handles that verification — asking again would break the "never ask twice" rule.

**Open questions**
- Whether the platform actually passes `{{var.customer_name}}` and `{{var.refill_details}}` on outbound calls is unconfirmed.
- Whether the platform detects voicemail or no-answer on outbound calls is unconfirmed; the voicemail line is written for when it does.
- Whether a do-not-call tool exists is unconfirmed; the agent can only say the request has been noted, never that calling has stopped.
- The exact fields `check_stock` returns (in stock, price, prescription needed, controlled) are unconfirmed; a missing flag is treated as prescription-needed.
- What counts as a valid prescription, and the exact list of controlled or always-hand-off medicines, are open questions for the pharmacy's clinical lead.
- This is the outbound Instructions set only. Inbound calls to this pharmacy would need a separate Instructions set.
- Chat is not set up in this profile; this is the voice version only.

**Word counts**
- Welcome: 16. Section 1: 398. Section 2: 139. Section 3: 123. Section 4: 85. Section 5: 428.
- Section 6: 565 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM, Monday to Saturday | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (filled in automatically from Variables) | Your business |
| `{{var.prescription_upload_method}}` | whatsapp | Your business, Add a detail |
| `{{var.payment_modes}}` | cash on delivery and UPI on delivery | Your business, Add a detail |
| `{{var.max_qty_without_pharmacist}}` | not provided | Your business, Add a detail |
| `{{var.customer_name}}` | passed by the platform on outbound calls, unconfirmed | Call context |
| `{{var.refill_details}}` | passed by the platform on outbound calls, unconfirmed | Call context |

| Intake item | Value you gave | Note |
|---|---|---|
| Business type | Pharmacy chain, the agent says "our pharmacy" | |
| Call direction | Outbound (refill reminders) | |
| Workflows wanted | Refill (outbound), order and prescription, medicine enquiry (stock and out-of-stock lines only) | Delivery and returns not used in these Instructions |
| Channel | Voice | |
| Prescription upload | whatsapp | |
| Pickup or delivery | not provided — the team will confirm | not used in these Instructions |
| Return policy | not provided — the team will confirm | not used in these Instructions |
| Payment modes | cash on delivery and UPI on delivery | |
| Transfer targets | Pharmacist on duty | No store-manager or staff target given; those handoffs fall back to a callback |
| Business hours | 9 AM to 7 PM, Monday to Saturday | |
| Store address | not provided — the team will confirm | not used in these Instructions |
| Languages | not provided — the team will confirm | |
| Extra emergency signs | none given | |
| Always-hand-off medicines | none given | |
| Special client rules | Refill reminders only; no sales, no offers, no medicine talk | |
| Largest quantity without the pharmacist | not provided — the team will confirm | |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
