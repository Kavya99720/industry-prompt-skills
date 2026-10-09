# Banking workflows

Phase 1 workflows are written in full; later phases are stubs (the skill and the reference builder skip a file whose header says "Status: stub"). Core rules are in `industries/banking/core.md` and apply to every workflow. Inbound and outbound are separate Instructions sets.

| # | Workflow | Direction | Phase | Status | Main-lines words (largest variant) |
|---|---|---|---|---|---|
| 01 | Account and card enquiry | Inbound | 1 | written | 107 (lookup on), 77 (lookup off) |
| 02 | Lost or stolen card and fraud | Inbound | 1 | written | 158 (block on), 83 (block off) |
| 03 | Disputes and complaints | Inbound | 1 | written | 125 |
| 04 | Outbound KYC reminder and card activation (one purpose per set) | Outbound | 1 | written | 314 (KYC) or 308 (card activation) |
| 05 | Outbound fraud-alert verification | Outbound | 1 | written | 452 (block on), 403 (block off) |
| 06 | Account opening and KYC help | Inbound | 2 | stub | - |
| 07 | Charges, cheque book and statement requests | Inbound | 2 | stub | - |
| 08 | Digital banking help | Inbound | 3 | stub | - |
| core | UNDERSTAND and HANDOFF (every set) | Both | 1 | written | 76 |

Word counts are whitespace-separated tokens of each `main-lines` block. The largest inbound set (core plus 01, 02 and 03, tool-on blocks) and the largest outbound sets must stay at 595 words or less. See test-profiles/README.md for the per-profile estimate.
