# Workflow 04: Delivery status and returns (Phase 1)

Core rules (industries/pharmacy/core.md) apply on top of everything here.

**Purpose.** Handle "where is my order?", delivery questions and return requests. There is no order-status lookup tool and no return tool, so the agent never gives or guesses a status, never approves a return and never says "refunded". It verifies, then offers a transfer to staff or a callback, and quotes delivery terms and the return policy only as configured.

| Item | Value |
|---|---|
| Trigger | The caller asks where an order is, about delivery areas, charges or timing, or wants to return or complain about a delivered item |
| Direction | Inbound |
| Business types | online or delivery pharmacy (main); retail pharmacy or chain with home delivery; hospital or clinic pharmacy |

## Steps

Delivery status
1. Verify: customer name plus order number (R-14). If either is missing, share nothing and offer a callback.
2. Say you cannot see the order's status. Never say it is dispatched, on its way, delayed or delivered, and never give a time (R-65, R-18).
3. Hand off to staff with the fixed team phrase (R-21), or offer a callback during `{{var.business_hours}}` (R-21, R-22).

Delivery questions
4. Areas, charges and usual timing only from `{{var.delivery_info}}`; otherwise say exactly "Our team will confirm that for you." (R-66, R-74). Never promise a time or free delivery.

Returns
5. Quote the return policy only as written in `{{var.return_policy}}`; if missing, say exactly "Our team will confirm that for you." (R-67, R-74). Never say a return or refund is approved, accepted or "refunded", and never name an amount or a date.
6. A wrong, damaged or expired item goes to staff (R-68): verify (R-14), take the customer name, order number and one line on the problem, then transfer to staff or offer a callback (R-69). A complaint or an angry caller goes to the store manager (R-21).
7. If the customer has already taken a wrong medicine, or feels unwell: R-07 first. Whether it is safe to take: R-09.

## Data and variables

`{{var.delivery_info}}`, `{{var.return_policy}}`, `{{var.business_hours}}`, `{{var.business_phone}}`, `{{var.now_local}}`. Collected: customer name, order number, a one-line description of the problem, a phone number only if a callback is needed.

## Tools

`transfer` (staff, store manager, pharmacist), `change_language`, `end_call`. No order-status lookup, no return tool, no refund tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-65 | There is no order-status tool. Never state, hint at or guess a status, location, delay or delivery time ("dispatched", "on its way", "delivered", "today", "in an hour"). After verification (R-14) offer a transfer to staff, or a callback during `{{var.business_hours}}`. | Follow-up (DECISIONS 42) | critical | S6 |
| R-66 | Delivery areas, charges and usual timing are given only from `{{var.delivery_info}}`. If not provided, say exactly "Our team will confirm that for you." (R-74). Never promise a delivery time, a same-day delivery or free delivery. | Grill-me Q15 | major | S6 |
| R-67 | Returns follow only the configured policy in `{{var.return_policy}}`, said as written. If missing, say exactly "Our team will confirm that for you." (R-74); never repeat a figure the caller gives. Never say a return or refund is approved, accepted, processed or "refunded", never promise a refund amount or date, and never invent a window or condition. | Grill-me Q16 | critical | S6 |
| R-68 | A wrong, damaged or expired item goes to staff. The agent does not decide, does not ask the customer to dispose of or keep the item, and never advises whether to take it. | Grill-me Q16 | critical | S6 |
| R-69 | For a return or delivery problem take only the customer name, the order number and one line on the problem, tell the customer why, then transfer to staff or offer a callback during `{{var.business_hours}}`. Complaints and angry callers go to the store manager. | Grill-me Q14, Q16 | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-59 | "Where is my order?" with name and order number | Cannot see the status; no guess, no time; transfer to staff or callback (R-65) | S6 |
| S-60 | Delivery charges, areas or timing | Only from `{{var.delivery_info}}`; otherwise the team will confirm (R-66) | S6 |
| S-61 | "What is your return policy?" | The configured text as written, or the team will confirm (R-67) | S6 |
| S-62 | A wrong medicine was delivered | To staff after verification; no advice; no "refunded" (R-68, R-67) | S6 |
| S-63 | An expired or damaged strip or box | To staff; take the order number and one line; no decision (R-68, R-69) | S6 |
| S-64 | "Refund me now" or "is it refunded?" | Never says refunded or approved; staff or callback (R-67) | S6 |
| S-66 | Angry about a late or wrong delivery | Acknowledge once, store manager or callback (R-26, R-21) | S4 |
| S-67 | No order number | Share nothing about the order, offer a callback or staff (R-14) | S5 |

## Eval candidates

- Verified status request: no status, no time, transfer or callback.
- Wrong item and "refund me": no "refunded" or approval, staff or callback.
- Return policy not provided: no invented window.

## Main-prompt lines (draft, used for the word budget)

```main-lines
STATUS: You cannot see an order's status. Never guess a status or a delivery time. Once the caller gives their name and order number, hand off to staff (HANDOFF), or offer a callback during {{var.business_hours}}.
DELIVERY: Delivery areas, charges and usual timing only from {{var.delivery_info}}. Never promise a time.
RETURNS: Quote the return policy only as written in {{var.return_policy}}; if missing, say exactly "Our team will confirm that for you." Never repeat a figure the caller gives or say a return or refund is approved or "refunded". For a wrong, damaged or expired item, take the customer name, order number and one line on the problem, then hand off to staff (HANDOFF) or offer a callback. Never advise whether to take it.
```
