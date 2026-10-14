# Education workflows

Core rules (industries/education/core.md) apply to every workflow. Inbound and outbound are separate Instructions sets. Word counts are the whitespace-separated words of each `main-lines` block (section 6 only; sections 1 to 5 do not count). The total for any chosen set must stay at 595 or less. Universal rules (payment, scam warning, promise line, student-data privacy line, discount line, child safety) are written in sections 1 and 5, so the workflow blocks only point to them.

| # | Workflow | Direction | Business types | Main-lines words |
|---|---|---|---|---|
| core | Core block (UNDERSTAND, HANDOFF with routing) | both | all | 142 |
| 01 | Inbound admissions, courses and campus information (owns the inbound closing) | Inbound | all | 75 |
| 02 | Inbound fees, payments, refunds and scholarships | Inbound | all | 94 |
| 03 | Inbound student records, exams, results and certificates | Inbound | all | 77 |
| 04 | Inbound demo class and counselling booking | Inbound | coaching, edtech, college, school | 67 |
| 05 | Inbound complaints, ragging, harassment and bullying | Inbound | all | 86 |
| 06 | Inbound payment problems, fake admission offers and guarantee claims | Inbound | all | 90 |
| 07 | Inbound online classes and technical help | Inbound | edtech, online coaching | 58 |
| 08 | Inbound preschool and daycare pickup and authorised persons | Inbound | preschool, daycare | 97 |
| 09 | Outbound frame (identity, voicemail, stop, source, summary; owns every outbound-only fixed line) | Outbound | all | 257 |
| 10 | Outbound admission follow-up | Outbound | all | 56 |
| 11 | Outbound fee reminder | Outbound | all with fees | 103 |
| 12 | Outbound demo class or counselling booking | Outbound | coaching, edtech, college, school | 60 |
| 13 | Outbound event, PTM or open-day reminder | Outbound | all | 64 |

## Default selections

| Business type and direction | Workflows | Section 6 estimate (words) |
|---|---|---|
| School, inbound | 01, 02, 03, 05, 06 | 142 + 75 + 94 + 77 + 86 + 90 = 564 |
| Preschool or daycare, inbound (profile 06) | 01, 02, 05, 06, 08 | 142 + 75 + 94 + 86 + 90 + 97 = 584 |
| College or university, inbound | 01, 02, 03, 05, 06 | 564 |
| Coaching or tuition centre, inbound with demo booking | 01, 02, 04, 05, 06 | 142 + 75 + 94 + 67 + 86 + 90 = 554 |
| Online course or edtech, inbound | 01, 02, 04, 06, 07 | 142 + 75 + 94 + 67 + 90 + 58 = 526 |
| Any type, outbound admission follow-up | 09, 10 | 142 + 257 + 56 = 455 |
| Any type, outbound fee reminder (profile 05) | 09, 11 | 142 + 257 + 103 = 502 |
| Coaching, college or edtech, outbound demo or counselling booking (profile 04) | 09, 12 | 142 + 257 + 60 = 459 |
| Any type, outbound event or PTM reminder | 09, 13 | 142 + 257 + 64 = 463 |

A business that wants more than the default set swaps one workflow for another to stay under 595 words; the draft notes name the workflows left out and the handoff covers them. A preschool uses 08 instead of 03. An inbound set for a business with the booking tool off still selects 04: it then takes a callback request and never says booked.

## Fixed-line check

`python scripts/check_fixed_lines.py OUTPUT.md --industry education --references industries/education --workflows ... --profile industries/education/test-profiles/NN-*.md` reads every `say exactly` line of core.md and the selected workflows. The script does not know education yet (open question in the brief, DECISIONS 117): it needs "education" in its AI-outbound and recording-in-welcome lists and the education settings (booking_tool, send_link, calls_recorded, confirmation_channels, callback) before the skill is checked. Outbound-only lines live in 09, so an inbound run never requires them. The skill itself is not written yet.
