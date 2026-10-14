# Retail workflows

Core rules (industries/retail/core.md) apply to every workflow. Inbound and outbound are separate Instructions sets. Word counts are the whitespace-separated words of each `main-lines` block (section 6 only; sections 1 to 5 do not count). The total for any chosen set must stay at 595 or less. Universal rules (payment, scam warning, refund wording, order-details verification lines, price and stock) are written in sections 1 and 5, so the workflow blocks only point to them.

| # | Workflow | Direction | Business types | Main-lines words |
|---|---|---|---|---|
| core | Core block (UNDERSTAND, HANDOFF with routing) | both | all | 130 |
| 01 | Inbound product, price, delivery areas and store information (owns the inbound closing) | Inbound | all | 80 |
| 02 | Inbound order status and delivery | Inbound | e-commerce, chain, electronics (anyone who delivers) | 81 |
| 03 | Inbound returns, exchange and refund | Inbound | all | 70 |
| 04 | Inbound warranty and repair or service | Inbound | electronics or appliance with service | 79 |
| 05 | Inbound complaints and consumer grievances | Inbound | all | 63 |
| 06 | Inbound payment problems and refund scams | Inbound | all | 47 |
| 07 | Outbound frame (identity, voicemail, stop, source, summary; owns every outbound-only fixed line) | Outbound | all | 228 |
| 08 | Outbound order or delivery update | Outbound | any with orders | 49 |
| 09 | Outbound abandoned cart reminder | Outbound | e-commerce | 48 |
| 10 | Outbound feedback call | Outbound | all | 75 |
| 11 | Outbound repair or service-ready update | Outbound | electronics with service | 65 |

## Default selections

| Business type and direction | Workflows | Section 6 estimate (words) |
|---|---|---|
| Single store, inbound | 01, 03, 05, 06 | 130 + 80 + 70 + 63 + 47 = 390 |
| Chain or franchise, inbound | 01, 02, 03, 05, 06 | 130 + 80 + 81 + 70 + 63 + 47 = 471 |
| E-commerce, inbound | 01, 02, 03, 05, 06 | 471 |
| Electronics or appliance with service, inbound | 01, 02, 03, 04, 05, 06 | 471 + 79 = 550 |
| Any type, outbound order update | 07, 08 | 130 + 228 + 49 = 407 |
| Outbound abandoned cart | 07, 09 | 130 + 228 + 48 = 406 |
| Outbound feedback | 07, 10 | 130 + 228 + 75 = 433 |
| Outbound service ready | 07, 11 | 130 + 228 + 65 = 423 |

A single store that delivers adds 02. An inbound set for a business with no order lookup tool still selects 02: it then carries the order-off line and notes delivery problems.

## Fixed-line check

`python scripts/check_fixed_lines.py OUTPUT.md --industry retail --workflows ... --profile industries/retail/test-profiles/NN-*.md` reads every `say exactly` line of core.md and the selected workflows. Rows that name `order_lookup_tool`, `send_link`, `calls_recorded` or `confirmation_channels` need those settings, passed with `--tool name=on|off`. Outbound-only lines live in 07, so an inbound run never requires them. The checker does not know "retail" yet (brief, open question 9): it needs shared-script changes the owner must approve. The skill itself is not written yet.
