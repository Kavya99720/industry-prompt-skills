# Pharmacy workflows

Each workflow file has: purpose, trigger, direction, steps, data and variables, tools, rules, scenarios (S-xx), section placement and the draft Main-prompt lines used for the word budget. Rules that apply to every workflow are in industries/pharmacy/core.md. The brief index is industries/pharmacy/brief.md.

## Workflow catalogue

| # | Workflow | Phase | Direction | Purpose | Main-prompt words (draft) |
|---|---|---|---|---|---|
| 01 | [Medicine enquiry](01-enquiry.md) | 1 | Inbound | Availability and price from the stock tool; store information | 83 (STOCK 40, OUT OF STOCK 32, STORE 11) |
| 02 | [Order and prescription](02-order-prescription.md) | 1 | Inbound; also after an outbound reminder | Order a medicine with read-back; prescription route; payment modes | 206 (ORDER 129, PRESCRIPTION 70, PAYMENT 7) |
| 03 | [Refill](03-refill.md) | 1 | Inbound and outbound (two sets) | Inbound refill; outbound refill reminder | Inbound 69 (REFILL); outbound 154 (OUTBOUND REFILL 93, stop-calling 36, voicemail 25); R-61, R-63 and R-64 are written in section 5 |
| 04 | [Delivery status and returns](04-delivery-returns.md) | 1 | Inbound | No-status delivery calls; delivery terms; returns per policy | 122 (STATUS 35, DELIVERY 14, RETURNS 73) |
| 05 | [Hospital pharmacy counter](05-hospital-pharmacy.md) | 2 | Inbound | Collection counter, discharge medicines, queue questions | stub |
| 06 | [Other outbound calls](06-other-outbound.md) | 2 | Outbound | Delivery updates, payment reminders, promotions | stub |
| 07 | [Chat channel](07-chat-channel.md) | 2 | Chat | Chat behaviour, prescription image upload | stub |
| 08 | [Feedback and complaint](08-feedback-complaint.md) | 3 | Inbound | Take a complaint and route it to the store manager | stub |

Core Main-prompt lines (UNDERSTAND 20, HANDOFF 71) add 91 words to every prompt. Pharmacy has no roster, so all 615 words are for our own text (platform-contract.md).

## Which Main-prompt lines each Instructions set uses

| Set | Lines | Words |
|---|---|---|
| Inbound, all four Phase 1 workflows | core 91 + 01 (83) + 02 (206) + 03 REFILL (69) + 04 (122) | 571 |
| Outbound refill reminders | core 91 + 03 OUTBOUND REFILL block (154) + REFILL (69) + 01 STOCK and OUT OF STOCK (72) + 02 (206) | 592 |

Outbound uses STOCK and OUT OF STOCK but not STORE, because it is a reminder call. If the client does not want a refill ordered on the call, drop 01 and 02 (the outbound set falls to 314 words and the agent offers the pharmacist or a callback).

## Which business types use which workflow

Legend: ● normally used, ○ optional or depends on the business, – not used.

| Workflow | Retail pharmacy or chain | Online or delivery pharmacy | Hospital or clinic pharmacy |
|---|---|---|---|
| 01 Medicine enquiry | ● | ● | ● |
| 02 Order and prescription | ● | ● | ○ (counter orders; discharge medicines are Phase 2) |
| 03 Refill, inbound | ● | ● | ○ |
| 03 Refill, outbound reminder | ○ | ● | ○ |
| 04 Delivery status and returns | ○ (only with home delivery) | ● | ○ |
| 05 Hospital pharmacy counter | – | – | ● |
| 06 Other outbound calls | ○ | ○ | ○ |
| 07 Chat channel | ○ | ○ | – |
| 08 Feedback and complaint | ○ | ○ | ○ |

## ID ranges

| Range | Where |
|---|---|
| S-01 to S-31 | Core scenarios (core.md) |
| S-32 to S-38 | Workflow 01 |
| S-39 to S-47, S-68, S-69 | Workflow 02 |
| S-48 to S-58, S-65 | Workflow 03 |
| S-59 to S-64, S-66, S-67 | Workflow 04 |
| R-01 to R-45, R-71 to R-76 | Core rules |
| R-46 to R-49 | Workflow 01 |
| R-50 to R-56, R-70, R-77 | Workflow 02 |
| R-57 to R-64 | Workflow 03 |
| R-65 to R-69 | Workflow 04 |
