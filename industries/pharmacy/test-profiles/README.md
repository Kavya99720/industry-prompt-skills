# Pharmacy test profiles

Five synthetic profiles. Each has business config, selected workflows, client requirements and 5 to 6 tricky callers with expected MUST and MUST NOT. They are the inputs for scripts/run_evals.py (one generated Instructions set per profile).

| # | File | Business | Direction | Workflows |
|---|---|---|---|---|
| 01 | [01-retail-pharmacy-inbound.md](01-retail-pharmacy-inbound.md) | Retail pharmacy chain, in-store upload, no return policy | Inbound | 01, 02, 03, 04 |
| 02 | [02-online-delivery-pharmacy.md](02-online-delivery-pharmacy.md) | Online and delivery pharmacy, WhatsApp upload, policy given | Inbound | 01, 02, 03, 04 |
| 03 | [03-outbound-refill-reminders.md](03-outbound-refill-reminders.md) | Pharmacy chain, outbound refill reminders | Outbound | 03 outbound, 02, 01 (stock lines) |
| 04 | [04-unethical-client.md](04-unethical-client.md) | Retail pharmacy with unethical client requests | Inbound | 01, 02 |
| 05 | [05-incomplete-intake.md](05-incomplete-intake.md) | Small independent pharmacy, intake answers missing | Inbound | 01, 02 |

## Main prompt word budget

Budget: about 615 words for section 6 (platform warning at 616). Pharmacy has no roster, so nothing is deducted for doctors. Words are whitespace-separated tokens in the draft `main-lines` blocks of core.md and the workflow files. Sections 1 to 5 are not counted. These are estimates from drafts, not from a written skill.

Per-part words: core 77 (UNDERSTAND 20, HANDOFF 57); Enquiry 99 (STOCK 51, OUT OF STOCK 30, STORE 18); Order and prescription 194 (ORDER 109, PRESCRIPTION 68, PAYMENT 17); Refill inbound 55; Refill outbound 164; Delivery and returns 112.

| Profile | Core | Enquiry | Order | Refill | Delivery/returns | Extras | Total | Budget | Status |
|---|---|---|---|---|---|---|---|---|---|
| 01 Retail inbound | 77 | 99 | 194 | 55 | 112 | 0 | 537 | 615 | OK (78 spare) |
| 02 Online inbound | 77 | 99 | 194 | 55 | 112 | 0 | 537 | 615 | OK (78 spare) |
| 03 Outbound refill reminders | 77 | 81 (STOCK, OUT OF STOCK) | 194 | 219 (outbound 164 + REFILL 55) | 0 | 0 | 571 | 615 | OK (44 spare) |
| 04 Unethical client | 77 | 99 | 194 | 0 | 0 | 0 | 370 | 615 | OK (245 spare) |
| 05 Incomplete intake | 77 | 99 | 194 | 0 | 0 | 0 | 370 | 615 | OK (245 spare) |

Profile 03 is the tightest: 44 words spare. The skill's margin rule (at least 20 words below the allowance) still holds. If a client adds wording, the first cuts are the OUT OF STOCK line's second half and the STORE line, never a critical rule. The skill reports the budget line in its draft notes and never silently cuts a critical rule (critical rules are in sections 1, 4 and 5 where possible).
