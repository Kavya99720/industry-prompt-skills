# Banking test profiles

Five synthetic businesses. The runner treats every file here (except this README) as a profile. The hidden sections (Tricky callers, Expected word budget, Test values) are not shown to the skill.

| # | File | Business | Direction | Banking tools | Workflows | Section 6 estimate (words) |
|---|---|---|---|---|---|---|
| 01 | 01-public-private-bank-inbound.md | Private bank | Inbound | card block ON, lookup ON | 01, 02, 03 | 466 |
| 02 | 02-small-finance-or-cooperative-bank-inbound.md | Co-operative bank | Inbound | both OFF; branch staff only | 01, 02, 03 | 361 |
| 03 | 03-outbound-kyc-reminder.md | Public bank | Outbound | none | 04 (KYC reminder) | 390 |
| 04 | 04-outbound-fraud-alert-verification.md | Private bank | Outbound | card block ON | 05 | 528 |
| 05 | 05-unethical-client-incomplete-intake.md | Small finance bank | Inbound | not stated (defaults off); no targets | 01, 02, 03 | 361 |

Word-budget table (main-lines blocks, whitespace-separated tokens; Main prompt limit 595):

| Block | Words |
|---|---|
| core (UNDERSTAND, HANDOFF) | 76 |
| 01 lookup on / off | 107 / 77 |
| 02 block on / off | 158 / 83 |
| 03 | 125 |
| 04 KYC set (GATE, WHO, PROVE, KYC, FRAUD, VOICEMAIL, STOP) | 314 |
| 04 card activation set | 308 |
| 05 block on / off | 452 / 403 |

Largest inbound set (01 profile): 466. Largest outbound set (04 profile): 528. Both are under 595.

Notes: profile 05 combines the unethical client (eight forbidden or doubtful requests) with an incomplete intake. Profile 03 covers the KYC purpose; card activation is the same pattern in its own set and is not a separate profile. Test values are the same in every profile because the eval probes use the same placeholders.
