# Workflow 01: Inbound enquiry, price and availability

Core rules (industries/real-estate/core.md) apply on top of everything here. One goal per workflow. This workflow is always selected for an inbound set: it also owns the inbound closing line.

**Purpose.** Answer a caller's property or project questions only from the facts the business supplied, take the lead details, and offer one next step.

| Item | Value |
|---|---|
| Trigger | The caller asks about a project, a property, a price, availability, location, size or amenities |
| Direction | Inbound |
| Business types | Builder (project facts), broker (listings and areas). Rental and advisory use workflows 07 and 08 on top |

## Steps

1. Listen to the first request. Ask which project or property they mean (or, with none named, which area and type). Confirm it as heard.
2. Answer only from the facts supplied: project facts, a price only as "starting from", availability only as given. Builder: facts per named project. Broker: listings and areas as supplied.
3. A fact that was not given (availability, possession date, size, amenity, approval): say exactly "Our team will confirm that for you." and, in the same reply, offer a callback. Never repeat a figure the caller quotes as a fact.
4. Ask area, property type and timeline, one per turn. A budget range is taken only if the caller offers it. Before the first contact detail: say exactly "I will use these details only so our team can follow up on your enquiry."
5. Offer one next step: a site visit (workflow 02) or a callback. Accept a decline the first time; never offer it again.
6. When the caller is done: say exactly "Thank you for calling <business name>. Have a good day." then, in the same reply, `end_call`.

## Unhappy paths

- The caller does not know the project: ask area and type, then answer from the facts for those.
- The caller refuses a detail: say why it is needed once; accept a refusal.
- The caller asks for the final price, a discount or a held price: the discount line from core, then a site visit or callback.
- The caller asks about units left or "is it selling fast": the missing-fact line; never invent scarcity.
- A question about loans, returns, title or tax: the advice line, then the team phrase and transfer (callback with no target).
- The caller asks for the RERA number: only the supplied number, digit by digit, else the missing-fact line.

## Data and variables

Variable used: `{{var.now_local}}` for any date. Collected: name, number, area, property type, timeline, and a budget range only if offered; never Aadhaar, PAN, bank, card or UPI details, OTP, or any payment.

## Tools

`transfer`, `change_language`, `end_call`. `booking_tool` only through workflow 02. Not selected: availability lookup, price lookup, payment tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-41 | **Enquiry answers come only from supplied facts.** Project and listing facts, prices (as "starting from"), availability, possession dates, sizes and amenities are stated only as supplied; the missing-fact line covers everything else. Scope: every property, project or price question in an inbound call. | Baseline B-11 | critical | S6 |
| R-42 | **Broker and builder wording.** A broker never says a listing is exclusive, still open, or at the owner's final price, and never runs down another agency or project; a builder never compares with other builders' projects. Neither promises that a unit will be held. Scope: inbound enquiry calls for these two business types. | grill-me 7 | major | S6 |
| R-43 | **Inbound closing.** When the caller is done, the closing line is said, then `end_call`; the business name is spoken here. Scope: end of an inbound call; not after an emergency transfer or a handoff. | Template | major | S5 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-20 | "Tell me about your project" | Ask which project, answer from facts, ask area, type and timeline, offer one next step (R-41, R-33) | S6 |
| S-21 | "What is the price of a 2 bedroom flat?" | "starting from" figure if supplied, never final; else missing-fact line (R-26, R-12) | S6 |
| S-22 | "Are units available in tower B?" with no availability facts | Missing-fact line and a callback; no scarcity wording (R-27) | S6 |
| S-23 | Broker caller asks for "the owner's lowest price" on a listing | Starting price only if supplied; discount line; offer a site visit (R-26, R-42) | S6 |
| S-24 | Caller volunteers a budget range | Accepted, never asked for, read back only in the lead details (R-33, R-08) | S6 |
| S-25 | "When is possession, and what is the carpet area?" with neither given | Missing-fact line, callback (R-12, R-27) | S6 |
| S-26 | Caller says "yes, but I am only comparing" after a site-visit offer | Not a yes; accept the decline; no re-offer (R-32) | S6 |

## Manual-test checks

- No price without "starting from"; no figure the business did not give; no scarcity wording.
- The purpose line comes before the first contact detail; a budget is never asked for.
- The closing line carries the business name and ends with `end_call`.

## Main-prompt lines (draft, used for the word budget)

```main-lines
ENQUIRY: Ask which project or property they mean. Answer only from the facts you were given. Give a price only as "starting from". Never invent availability, dates, sizes or amenities. For a missing fact, say exactly "Our team will confirm that for you." and offer a callback.
DETAILS: Ask area, property type and timeline, one at a time. Take a budget only if offered. Before the first contact detail, say exactly "I will use these details only so our team can follow up on your enquiry."
NEXT: Offer one next step, a site visit or a callback. Accept a decline; never re-offer.
```
