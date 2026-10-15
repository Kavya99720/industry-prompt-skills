# Logistics workflows

Core rules (industries/logistics/core.md) apply to every workflow. Inbound and outbound are separate Instructions sets. Word counts are the whitespace-separated words of each `main-lines` block (section 6 only; sections 1 to 5 do not count). The total for any selection must stay under 595.

| # | Workflow | Direction | Business types | Main-lines words |
|---|---|---|---|---|
| core | Core block (UNDERSTAND, HANDOFF with routing) | both | all | 123 |
| 01 | Inbound shipment status and delivery (owns the inbound closing) | Inbound | courier and parcel | 94 |
| 02 | Inbound reschedule, address change, failed delivery, return to sender | Inbound | courier and parcel | 70 |
| 03 | Inbound pickup request, rate card, sender calls | Inbound | courier and parcel | 92 |
| 04 | Inbound claims, damage, COD, business customers | Inbound | courier and parcel (claim steps serve all) | 100 |
| 05 | Inbound courier scams, OTP, customs holds, restricted goods | Inbound | all | 89 |
| 06 | Inbound freight and trucking, warehouse and 3PL, forwarder and customs (lighter set) | Inbound | freight, warehouse, forwarder | 87 |
| 07 | Outbound frame (identity, voicemail, stop, source, summary; owns every outbound-only fixed line) | Outbound | all | 229 |
| 08 | Outbound delivery update | Outbound | courier and parcel | 67 |
| 09 | Outbound pickup and COD calls | Outbound | courier and parcel | 99 |

## Default selections

| Business type and direction | Workflows | Section 6 estimate (words) |
|---|---|---|
| Courier or parcel, inbound (all tools off or on) | 01, 02, 03, 04, 05 | 123 + 94 + 70 + 92 + 100 + 89 = 568 |
| Courier or parcel, inbound, a lighter selection | 01, 03, 05 | 123 + 94 + 92 + 89 = 398 |
| Freight and trucking, inbound | 06, 05, 04 | 123 + 87 + 89 + 100 = 399 |
| Warehouse or 3PL, inbound | 06, 05 | 123 + 87 + 89 = 299 |
| Freight forwarder or customs, inbound | 06, 05 | 299 |
| Outbound delivery update | 07, 08 | 123 + 229 + 67 = 419 |
| Outbound pickup and COD | 07, 09 | 123 + 229 + 99 = 451 |

Workflow 04 is added for freight, warehouse and forwarder businesses that want claims and COD handled; a business that gives no claim facts still gets the claim steps (the claim note and the claims team). Driver check-ins are v2 and not written. A confirmation or link flow is not part of v1 (an open item in the draft notes).

## Fixed-line check

`python scripts/check_fixed_lines.py OUTPUT.md --industry logistics --references industries/logistics --workflows ... --profile industries/logistics/test-profiles/NN-*.md` reads every `say exactly` line of core.md and the selected workflows (once the skill's references are built, use `.claude/skills/logistics-prompt-writer/references` instead). Use the profile of the output: it supplies the tool settings, the recording setting, the transfer targets and the contact-source wording.
