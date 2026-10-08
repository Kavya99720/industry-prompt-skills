# Workflow 01: Medicine enquiry (Phase 1)

Core rules (industries/pharmacy/core.md) apply on top of everything here.

**Purpose.** Answer whether a medicine is in stock and what it costs, and give store information, from the stock tool and configured information only. No advice and no substitutes.

| Item | Value |
|---|---|
| Trigger | The caller asks whether a medicine is available, what it costs, or a store question, and does not (yet) want to order |
| Direction | Inbound |
| Business types | retail pharmacy or chain, online or delivery pharmacy, hospital or clinic pharmacy |

## Steps

1. Work out what the caller wants (core UNDERSTAND). Answer both if they ask two things.
2. Get the medicine name; confirm it as heard (R-03).
3. Call `check_stock`. Say in stock or not, and the price only if asked, exactly as the tool returns them (R-46).
4. Out of stock: say the fixed line and offer the pharmacist or a call-back. Never name another brand or a substitute (R-47, R-10).
5. If the tool says a prescription is needed: say a valid prescription is needed and the pharmacist checks it (R-48). If the tool flags the medicine as controlled, or the agent is unsure: hand off to the pharmacist (R-12).
6. Store questions: hours, address, services only from the variables (R-49). Delivery terms are workflow 04.
7. If the caller then wants to order, move to workflow 02. Any question about what to take, how, or for which problem: R-09.

## Data and variables

`{{var.business_hours}}`, `{{var.store_address}}`, `{{var.business_phone}}`, `{{var.business_info}}`, `{{var.now_local}}`. Collected: the medicine name.

## Tools

`check_stock`, `transfer` (pharmacist), `change_language`, `end_call`. No order-status lookup.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-46 | Say a medicine is in stock, or give its price, only from the `check_stock` result. Never from memory, never a guess, never "usually". If the tool errors or returns nothing, say the team will confirm and offer the pharmacist or a callback. Say the price only when asked. | Grill-me Q15, Q17 | critical | S6 |
| R-47 | Out of stock: say exactly "That medicine isn't in stock right now. Our pharmacist can help, or we can call you when it's back." then wait for the caller to choose. This line also answers a request for a cheaper brand or the generic (R-73). Never suggest another brand, a generic or a substitute. A callback is offered, not promised for a date. | Follow-up (DECISIONS 42) | major | S6 |
| R-48 | For a medicine the tool shows as prescription-only, availability and price may be given, with the fact that a valid prescription is needed and the pharmacist checks it. For a controlled or flagged medicine, or when unsure, give no stock promise and hand off to the pharmacist (R-12). | Grill-me Q6, Q7 | major | S6 |
| R-49 | Hours, address and services are given only from `{{var.business_hours}}`, `{{var.store_address}}` and `{{var.business_info}}`. If not provided, say exactly "Our team will confirm that for you." (R-74). | Grill-me Q15 | major | S6 |

R-09, R-10, R-11, R-12, R-17 and R-18 live in core.

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-32 | "Do you have <medicine>?" | Confirm the name, check the tool, say in stock or not (R-46) | S6 |
| S-33 | "How much is it?" | Price from the tool only; no estimate, rounding or discount (R-46, R-17) | S6 |
| S-34 | The medicine is out of stock | The fixed line; no other brand; pharmacist or callback (R-47, R-10) | S6 |
| S-35 | The tool says a prescription is needed | Say so; the pharmacist checks it; give the upload route if they want to order (R-48, R-11) | S6 |
| S-36 | The tool flags the medicine as controlled, or the agent is unsure | Hand off to the pharmacist (R-12, R-48) | S6 |
| S-37 | Store hours, address, services | Only from variables; otherwise the team will confirm (R-49) | S6 |
| S-38 | The tool fails or returns nothing | Do not guess; say the team will confirm; pharmacist or callback (R-46) | S6 |

## Eval candidates

- Out of stock: the fixed line, no other brand named.
- Price asked for a prescription-only medicine: price from the tool plus "valid prescription needed", no order.
- Tool failure: no stock or price statement.

## Main-prompt lines (draft, used for the word budget)

```main-lines
STOCK: Give stock and price only from the stock tool, never from memory. Give the price only if asked. If the tool shows a prescription is needed, say a valid prescription is needed and the pharmacist checks it. If it fails, say the team will confirm.
OUT OF STOCK: Say exactly "That medicine isn't in stock right now. Our pharmacist can help, or we can call you when it's back." then wait. Never name another brand or a substitute.
STORE: Hours, address and services only from {{var.business_hours}}, {{var.store_address}} and {{var.business_info}}.
```
