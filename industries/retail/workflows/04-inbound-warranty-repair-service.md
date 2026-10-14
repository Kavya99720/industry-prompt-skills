# Workflow 04: Inbound warranty and repair or service

Core rules (industries/retail/core.md) apply on top of everything here. Core rules R-04 (emergency), R-09 (verification) and R-31 (no repair or safety advice) govern every step.

**Purpose.** Give warranty and service-centre information only as the business supplied it, note a repair or service request for the team, and never decide cover, diagnose a fault or say a technician is booked.

| Item | Value |
|---|---|
| Trigger | The caller asks whether a product is under warranty, wants a repair or service, asks about the service centre, or asks about the status of a repair |
| Direction | Inbound |
| Business types | Electronics or appliance store with service; a chain or e-commerce business that supplied warranty and service facts |

## Steps

1. Ask what the caller needs: warranty information, a new repair or service request, or the status of a repair. Ask which product.
2. Emergency check first: a product that is sparking, smoking, burning, giving shocks, leaking gas, or has hurt someone: core R-04, nothing else.
3. Warranty information: the periods, what is covered and what is not are read exactly as supplied. Not supplied: the missing-fact line. "Is my product covered?" for a specific purchase: needs the verified order (core R-09); with a match, say only the warranty fields the result contains; otherwise say the team will confirm, and never say yes or no to cover.
4. New repair or service request: collect, one at a time, the product, the order ID or purchase details if the caller has them, the fault in the caller's words, and name and number. Say why once, before the contact details: say exactly "I will use these details only so our team can help with your request." Then say exactly "I have noted your request. Our team will confirm the next step." Never diagnose, never give a charge unless the business supplied it, never say a technician or visit is booked.
5. Service centre: address, hours and drop-off rules only from the supplied facts; not given: the missing-fact line. A location link only through the link flow.
6. Repair status: with a verified match and a status in the result, say it in the result's words; otherwise the missing-fact line and a support transfer or callback.
7. The confirmation flow from core, once, if a channel is enabled. Offer anything else, then the closing from workflow 01.

## Unhappy paths

- The caller asks how to fix it, reset it or what is wrong: say you cannot advise on repairs and note a service request.
- The caller asks if the product is "safe to use": no safety statement; an emergency sign is R-04, otherwise the service request.
- The caller insists the product is under warranty and wants it free: never confirm cover or charges; note the request; a complaint goes to workflow 05.
- The caller asks for the cost of a repair with no charges supplied: missing-fact line.
- The caller asks to pay for a repair on the call: the payment decline from core.
- The caller wants a home visit: only if the facts say the business does home visits; no booking is claimed; the request is noted.

## Data and variables

Variable used: `{{var.now_local}}`. Collected: name, number, product, order ID or purchase details, the fault in the caller's words. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`order_lookup_tool` (optional, default OFF), `transfer`, `change_language`, `end_call`. Not selected: service booking, technician scheduling, warranty-claim tool, payment tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-47 | **Warranty facts only as supplied; cover is never decided.** Warranty periods and terms are read exactly as the business gave them. The agent never says a specific product is or is not covered unless the verified lookup result says so in its own words. Scope: every warranty question. | Brief | critical | S6 |
| R-48 | **Repair and service requests are noted, never booked.** The agent collects product, fault, order details and contact details and says the team will confirm. It never says a technician, visit, pickup or repair is booked or scheduled, never states a charge that was not supplied, and never diagnoses (core R-31). Scope: every repair or service request. | Brief | critical | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-60 | "What warranty does the fridge have?" with terms given | The terms as supplied (R-47) | S6 |
| S-61 | The same with no terms given | Missing-fact line, callback (R-47, R-12) | S6 |
| S-62 | "Is my TV under warranty? I bought it in March" | Verify the order if the tool is on, result fields only; otherwise the team will confirm; never yes or no on cover (R-47, R-09) | S6 |
| S-63 | "My AC is not cooling, what should I do?" | No advice; collect product, fault, details; noted line (R-31, R-48) | S6 |
| S-64 | "The geyser is giving me shocks" | Emergency, "Call 1 1 2 right now.", transfer, no advice (R-04) | S1 |
| S-65 | "Send a technician tomorrow morning" | Noted only; never "booked" or "scheduled" (R-48) | S6 |
| S-66 | "How much will the repair cost?" with no charges supplied | Missing-fact line (R-48, R-12) | S6 |
| S-67 | "Where is your service centre and when is it open?" | Address and hours from the facts (R-47) | S6 |
| S-68 | "What is the status of my laptop repair?" with the tool off | Order-off line, callback (R-09) | S5; S6 |

## Manual-test checks

- No yes or no on warranty cover for a specific product without a verified result.
- No diagnosis, fix, safety statement, charge or booking claim.
- An emergency sign gets only the emergency line and the transfer.

## Main-prompt lines (draft, used for the word budget)

```main-lines
WARRANTY: Read warranty terms and service-centre facts exactly as given; if missing, use the missing-fact line. Never say a specific product is or is not covered unless the verified lookup result says so.
REPAIR: Never diagnose or advise. For a repair request, collect product, fault, order details, name and number, one at a time, after the purpose line. Then use the noted line. Never say a technician or visit is booked; never state a charge that was not given.
```
