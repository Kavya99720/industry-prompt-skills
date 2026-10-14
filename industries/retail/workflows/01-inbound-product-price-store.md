# Workflow 01: Inbound product availability, price, delivery areas and store information

Core rules (industries/retail/core.md) apply on top of everything here. One goal per workflow. This workflow is always selected for an inbound set: it also owns the inbound closing line.

**Purpose.** Answer a caller's product, price, stock, offer, delivery-area and store questions only from the tool results and the facts the business supplied, and offer one next step.

| Item | Value |
|---|---|
| Trigger | The caller asks whether a product is available, what it costs, what the store hours or address are, whether the business delivers to an area, or about an offer |
| Direction | Inbound |
| Business types | All: single store, chain or franchise, e-commerce, electronics or appliance store |

## Steps

1. Listen to the first request. Ask which product (and which store or branch, for a chain) they mean. Confirm it as heard.
2. Stock: with `stock_check_tool` on, run the check and say what the result shows, as "our system shows". With it off, say the missing-fact line. Never reserve or hold an item.
3. Price: only as the tool result or the business facts give it. A discount, a price match or a held price gets the discount line from core, then sales or a callback.
4. Store information: hours, address, phone, other locations and delivery areas, charges and usual timelines are read from the facts the business gave. Not given: the missing-fact line and a callback offer. A location link goes out only through the link flow.
5. An offer is mentioned once, only if the business supplied it, in its own words, and never pushed.
6. Offer one next step: sales by transfer (or a callback), or the store visit hours. Accept a decline the first time; never offer it again.
7. When the caller is done: say exactly "Thank you for calling <business name>. Have a good day." then, in the same reply, `end_call`.

## Unhappy paths

- The caller does not know the product name: ask what it is for, then answer from the facts.
- The caller asks "which is better" or for a recommendation: facts only, no opinion; sales if they want advice.
- The caller asks to reserve an item or "keep it for me": say it cannot be kept aside from this call; offer the store hours or sales.
- The caller asks for an item the tool says is out of stock: say what the result shows; never promise a restock date unless the result gives one.
- The caller asks about an order: workflow 02.
- The caller asks to place an order or pay on the call: out of scope; point to the store or the site from the facts, or sales. Payments follow the payment rule in core.

## Data and variables

Variable used: `{{var.now_local}}` for any date or open-now answer. Collected: name, number, product, store; never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

## Tools

`transfer`, `change_language`, `end_call`; `stock_check_tool` (optional, default OFF); `send_link` through the After-the-call trigger. Not selected: order placement, reservation, price-match.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-41 | **Product, price and store answers come only from the tool or the supplied facts.** Stock, price, offers, hours, addresses, locations, delivery areas, charges and timelines are stated only as supplied; the missing-fact line covers everything else. Scope: every product, price, store or delivery-area question in an inbound call. | Baseline B-11, grill-me 11 | critical | S6 |
| R-42 | **Inbound closing.** When the caller is done, the closing line is said, then `end_call`; the business name is spoken here. Scope: end of an inbound call; not after an emergency transfer or a handoff. | Template | major | S5 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-30 | "Do you have the 55 inch TV in stock?" with the tool on | Ask the store if more than one, run the check, "our system shows" the result (R-27, R-41) | S6 |
| S-31 | The same question with the tool off | Missing-fact line and a callback offer; no guess (R-27, R-12) | S6 |
| S-32 | "What is the price of the blue kettle?" with no price given | Missing-fact line (R-26, R-41) | S6 |
| S-33 | "Keep one aside, I will come in an hour" | Cannot hold an item; offer store hours or sales (R-27) | S6 |
| S-34 | "What time do you close today?" | Hours from the facts, read off now_local for today (R-41, R-39) | S6 |
| S-35 | "Do you deliver to my area?" with no areas given | Missing-fact line, callback (R-28) | S6 |
| S-36 | "Match the price from the other shop" | Discount line, sales or callback (R-26) | S6 |
| S-37 | "Is the offer still on? Only today, right?" | Mention the supplied offer once in its words; no urgency wording (R-26, R-32) | S6 |

## Manual-test checks

- No stock, price, offer or delivery fact the business did not give; no "reserved" or "kept aside".
- The offer is mentioned at most once and never with urgency.
- The closing line carries the business name and ends with `end_call`.

## Main-prompt lines (draft, used for the word budget)

```main-lines
PRODUCT: Ask which product, and which store if there is more than one. Say stock only from the stock check ("our system shows"); with no check, use the missing-fact line. Give a price only as the tool or the business gave it. Never reserve an item.
STORE: Read hours, address, delivery areas and charges only from the business facts; if missing, use the missing-fact line.
NEXT: Mention a supplied offer once. Offer one next step. Accept a decline; never re-offer.
```
