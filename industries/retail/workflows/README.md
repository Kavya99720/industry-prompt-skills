# Retail workflows

Core rules (industries/retail/core.md) apply to every workflow. Inbound and outbound are separate Instructions sets. Word counts are the whitespace-separated words of each `main-lines` block (section 6 only; sections 1 to 5 do not count). The total for any chosen set must stay at 595 or less. Universal rules (payment, scam warning, refund wording, order-details verification lines, price and stock) are written in sections 1 and 5, so the workflow blocks only point to them.

| # | Workflow | Direction | Business types | Main-lines words |
|---|---|---|---|---|
| core | Core block (UNDERSTAND, HANDOFF with routing) | both | all | 130 |
| 01 | Inbound product, price, delivery areas and store information (owns the inbound closing) | Inbound | all | 91 |
| 02 | Inbound order status and delivery | Inbound | e-commerce, chain, electronics (anyone who delivers) | 81 |
| 03 | Inbound returns, exchange and refund | Inbound | all | 70 |
| 04 | Inbound warranty and repair or service | Inbound | electronics or appliance with service | 80 |
| 05 | Inbound complaints and consumer grievances | Inbound | all | 72 |
| 06 | Inbound payment problems and refund scams | Inbound | all | 47 |
| 07 | Outbound frame (identity, voicemail, stop, source, summary; owns every outbound-only fixed line) | Outbound | all | 228 |
| 08 | Outbound order or delivery update | Outbound | any with orders | 49 |
| 09 | Outbound abandoned cart reminder | Outbound | e-commerce | 48 |
| 10 | Outbound feedback call | Outbound | all | 75 |
| 11 | Outbound repair or service-ready update | Outbound | electronics with service | 65 |

## Default selections

| Business type and direction | Workflows | Section 6 estimate (words) |
|---|---|---|
| Single store, inbound | 01, 03, 05, 06 | 130 + 91 + 70 + 72 + 47 = 410 |
| Chain or franchise, inbound | 01, 02, 03, 05, 06 | 130 + 91 + 81 + 70 + 72 + 47 = 491 |
| E-commerce, inbound | 01, 02, 03, 05, 06 | 491 |
| Electronics or appliance with service, inbound | 01, 02, 03, 04, 05, 06 | 491 + 80 = 571 |
| Any type, outbound order update | 07, 08 | 130 + 228 + 49 = 407 |
| Outbound abandoned cart (profile 06) | 07, 09 | 130 + 228 + 48 = 406 |
| Outbound feedback | 07, 10 | 130 + 228 + 75 = 433 |
| Outbound service ready | 07, 11 | 130 + 228 + 65 = 423 |

A single store that delivers adds 02. An inbound set for a business with no order lookup tool still selects 02: it then carries the order-off line and notes delivery problems.

## Fixed-line check

`python scripts/check_fixed_lines.py OUTPUT.md --industry retail --references industries/retail --workflows ... --profile industries/retail/test-profiles/NN-*.md` reads every `say exactly` line of core.md and the selected workflows (once the skill exists, drop `--references` and its references folder is used). With `--industry retail` and a profile, the checker reads the profile's Tools row (order_lookup_tool, stock_check_tool, send_link), Calls recorded, Confirmation channels, Transfer targets and Contact-source wording rows; `--tool name=on|off` overrides them. The two order verification lines are required by the lookup setting (off line when off, no-match line when on). Outbound-only lines live in 07, so an inbound run never requires them. The skill itself is not written yet.
