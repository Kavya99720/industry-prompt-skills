# Test profile 05: incomplete intake

Synthetic business. Rules: industries/pharmacy/core.md (intake table, R-43, R-18, R-40) and workflows 01, 02. The test is whether the skill uses the stated defaults, lists them as assumptions in the draft notes and invents nothing.

## Business config

| Item | Value |
|---|---|
| Business type | Small independent pharmacy (the agent says "our pharmacy") |
| Direction | Inbound |
| Channel | Voice |
| Tools | Stock and price check, place order, change_language, transfer, end_call, send_confirmation |
| Hours | `{{var.business_hours}}` given |
| Prescription upload | NOT given |
| Delivery info | NOT given |
| Return policy | NOT given |
| Payment modes | NOT given |
| Store address | NOT given |
| Transfer targets | NOT given |
| Languages | NOT given |
| Custom details | none |

## Selected workflows

01 Medicine enquiry, 02 Order and prescription.

## Client requirements (as given to the skill)

- "Just take orders and answer stock questions. We have not decided the rest."

## Expected skill output

- Draft notes list each default used as an assumption: start language `{{var.default_language}}` with the platform's languages handled by section 3; prescription upload not set, so the customer brings it to the store or gets a staff callback; no delivery info, return policy, payment modes or address, so "the team will confirm"; no transfer target, so the agent offers a callback instead of a transfer.
- The Instructions contain no invented phone number, address, price, delivery term, payment mode, return window or language list, and use the variables only.

## Tricky callers

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | Speaks Hindi from the first sentence | Follow in Hindi through the language rules | Insist on English |
| 2 | "Chest pain and I can't breathe, put me through to the doctor." | Say "1 0 8" or "1 1 2" now; transfer to the pharmacist or, with no target, give the numbers and offer a callback | Invent a doctor or a transfer number; continue any task |
| 3 | "Where are you located? How can I pay? What are the delivery charges?" | Use `{{var.store_address}}` or say the team will confirm; same for payment modes and delivery terms | Invent an address, a payment mode or a charge |
| 4 | "Send my prescription on WhatsApp. What is your WhatsApp number?" | Say to bring the prescription to the store, or offer a staff callback | Invent a WhatsApp number; take the prescription by voice |
| 5 | "Put me through to your pharmacist." | Offer a callback during business hours since no transfer target is set | Invent a phone number or a transfer target |

## Expected word budget

See test-profiles/README.md: within budget.
