# Real estate workflows

Core rules (industries/real-estate/core.md) apply to every workflow. Inbound and outbound are separate Instructions sets. Word counts are the whitespace-separated words of each `main-lines` block (section 6 only; sections 1 to 5 do not count). The total for any chosen set must stay at 595 or less.

| # | Workflow | Direction | Business types | Phase | Main-lines words |
|---|---|---|---|---|---|
| core | Core block (UNDERSTAND, HANDOFF) | both | all | 1 | 96 |
| 01 | Inbound enquiry, price and availability (owns the inbound closing) | Inbound | builder, broker | 1 | 102 |
| 02 | Inbound site visit and booking follow-up | Inbound | builder, broker (reused by 05, 07, 08) | 1 | 85 |
| 03 | Inbound documents | Inbound | builder, broker | 1 | 52 |
| 04 | Inbound complaints | Inbound | all | 1 | 68 |
| 05 | Outbound lead qualification and consultation or site-visit booking (owns every outbound-only fixed line) | Outbound | all | 1 | 299 |
| 06 | Outbound referral-partner recruitment, opt-in variant (selected with 05, only when the program is ON) | Outbound | all | 1 | 70 |
| 07 | Inbound rental, lighter variant (replaces 01; owns the inbound closing for it) | Inbound | rental | 1 (light) | 76 |
| 08 | Inbound advisory, lighter variant (replaces 01; owns the inbound closing for it) | Inbound | advisory | 1 (light) | 62 |

## Default selections

| Business type and direction | Workflows | Section 6 estimate (words) |
|---|---|---|
| Builder or broker, inbound | 01, 02, 03, 04 | 96 + 102 + 85 + 52 + 68 = 403 |
| Rental, inbound | 07, 02, 04 | 96 + 76 + 85 + 68 = 325 |
| Advisory, inbound | 08, 02, 04 | 96 + 62 + 85 + 68 = 311 |
| Any type, outbound | 05 | 96 + 299 = 395 |
| Any type, outbound, referral program ON | 05, 06 | 96 + 299 + 70 = 465 |

Sections 1, 4 and 5 carry the universal rules (emergency, price, payment, advice, privacy, no-collect, pressure, confirmation flow), so they never count here.

## Fixed-line check

`python scripts/check_fixed_lines.py OUTPUT.md --industry real-estate --workflows ... --profile industries/real-estate/test-profiles/NN-*.md` reads every `say exactly` line of core.md and the selected workflows. Pass the tool states the profile uses: `--tool booking_tool=on|off`, `--tool calls_recorded=on|off`, `--tool confirmation_channels=whatsapp|email|both`. Outbound-only lines live in 05 and 06 so an inbound run never requires them. The skill itself is not written yet; the references will be built from these files.
