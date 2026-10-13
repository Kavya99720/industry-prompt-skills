# Workflow 02: Order and prescription (Phase 1)

Core rules (industries/pharmacy/core.md) apply on top of everything here. Medicine questions inside an order are handed to the pharmacist (R-09).

**Purpose.** Take an order for a medicine that needs no prescription, with a read-back and a clear yes before `place_order`. For a prescription-only, controlled or unsure medicine, place no order: ask for the prescription, share the upload route and hand off to the pharmacist, who verifies.

| Item | Value |
|---|---|
| Trigger | The caller wants to order or buy a medicine, or asks how to send a prescription |
| Direction | Inbound; also used after an outbound refill reminder (workflow 03) |
| Business types | retail pharmacy or chain, online or delivery pharmacy, hospital or clinic pharmacy |

## Steps

1. Ask the customer's name (R-33), the medicine name (confirm as heard, R-03) and the quantity as the caller says it (packs, strips or units). Never suggest a quantity (R-53).
2. Call `check_stock`. Not in stock: workflow 01 out-of-stock line (R-47).
3. Order gate (R-50, R-70). Place an order only when the tool shows the medicine is not prescription-only and not controlled, and the quantity is within the limit. If the flags are missing, it is prescription-only, controlled or unsure, or the quantity is above the limit, place no order and confirm nothing: go to step 4 or hand off to the pharmacist (R-11, R-12). A quantity above the limit goes straight to the pharmacist.
4. Prescription (R-54, R-77): ask "Do you have a valid prescription from your doctor?" Never judge it and never take it by voice. Then say the no-prescription line (R-77). The upload step comes right after the question: if the prescription upload method is whatsapp or email, run the upload-link flow (R-76, no tool); if in_store or not set, ask them to bring it to the store, or offer a staff callback.
5. Ask pickup or home delivery. For home delivery take the address (R-56).
6. Read back medicine, quantity, price from the tool, and pickup or delivery. Ask "Shall I place the order?" Act only on a clear yes (R-51, R-32). If they change a detail, update it and read back again.
7. Payment: modes only, from the payment modes in the business facts (R-55, R-16).
8. Call `place_order`. Only when it returns an order number say the order is placed and read the number digit by digit (R-52). On failure: say exactly "I'm sorry, that order did not go through. Our team will call you to confirm.", never say it is placed. After an order number, offer the confirmation (R-76).
9. Close (R-24); "Is there anything else I can help with?" comes from the confirmation flow or the close.

## Data and variables

the prescription upload method (the customer's answer), `{{var.now_local}}` and the business facts of section 1 (largest quantity, payment modes, delivery terms, hours, phone). Collected: customer name, medicine name, quantity, pickup or delivery, a delivery address only for home delivery, a phone number only if a callback is needed, a WhatsApp number or email only to send the upload instructions (read back to confirm).

## Tools

`check_stock`, `place_order` (order number only on success), `transfer`, `change_language`, `end_call`.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-50 | Order gate: call `place_order` only for a medicine the `check_stock` result shows as not prescription-only and not controlled. If the result does not return the prescription-needed or controlled flags, treat the medicine as prescription-needed. For a prescription-only, controlled or unsure medicine, place no order, give no order number and never say the order is confirmed; ask for the prescription and hand off to the pharmacist. The caller's promise to send a prescription later does not open the gate. | Grill-me Q6, Q7, Q17 | critical | S6 |
| R-51 | **Partly baseline B-05.** Before `place_order`, read back the medicine, quantity, price from the tool, and pickup or delivery, and ask for explicit confirmation. Act only after a clear yes. If the caller says no or changes a detail, update it and read back again. | Baseline | critical | S6 |
| R-52 | Say an order is placed or confirmed only after `place_order` returns an order number. Read the number back digit by digit. Never invent or guess an order number. If the tool errors, times out or returns nothing, say exactly "I'm sorry, that order did not go through. Our team will call you to confirm." and never say the order is placed, confirmed or done, not even to deny it. | Grill-me Q17; healthcare pattern | critical | S6 |
| R-53 | Ask the quantity as packs, strips or units. Never suggest, round or advise a quantity, and never say how many to take. | Grill-me Q9 | major | S5 |
| R-54 | Prescription upload link: right after the prescription question, run the upload-link flow of R-76 when the prescription upload method is whatsapp or email. There is no tool call; the After-the-call trigger sends the link. The two branches are rows R-54a (whatsapp) and R-54b (email) below. Never read the number aloud; never say the link has been sent. If in_store or not set: skip the flow, ask the customer to bring the prescription to the store, or offer a staff callback. Never take a prescription, or what it says, by voice. Write only the branch of the customer's upload method in section 5 (WhatsApp only, or email only) and drop the other; no method given: the in_store step (bring the prescription to the store, or a staff callback). With WhatsApp, the first question for a prescription medicine is "Is this number on WhatsApp?", before any other question, including the customer's name. Scope: prescription-only medicines and refills only; not for controlled or unsure medicines (R-12), which go to the pharmacist. | Follow-up (DECISIONS 42, 50, 51) | major | S5 |
| R-54a | [upload: whatsapp] If the prescription upload method is whatsapp: say exactly "Is this number on WhatsApp?" then, if yes, say exactly "You will get the upload link on WhatsApp shortly."; if no, say exactly "I'm sorry, we can only send the upload link on WhatsApp. Please bring the prescription to the store, or I can arrange a staff callback." Never offer email unless the upload method is email. | Follow-up (DECISIONS 42, 50, 51) | major | S5 |
| R-54b | [upload: email] If the prescription upload method is email: say exactly "Please tell me your email address.", read it back once (spelled, "at", "dot"), get a yes, then say exactly "You will get the upload link on email shortly." | Follow-up (DECISIONS 42, 50, 51) | major | S5 |
| R-77 | **No-prescription line.** When a medicine needs a prescription and the caller has none (or the tool flags are missing, R-12), say exactly "I can't place this order without a valid prescription. Our pharmacist verifies the prescription." then, in the same reply, give the upload step (R-54). Place no order and give no order number. Whenever the agent asks for a prescription (PRESCRIPTION and REFILL), it also says exactly "Our pharmacist verifies the prescription." in the same reply (PHA-E15 expects the word pharmacist). Scope: prescription-only medicines and refills. It does not apply to controlled or unsure medicines, which get the pharmacist line (R-09), nor to ordinary medicines. | Quick test PHA-E09 (DECISIONS 50); the critical behaviour is R-11 and R-50 | major | S6 |
| R-55 | If asked how to pay, state the modes only from the payment modes in the business facts; if missing, say exactly "Our team will confirm that for you." (R-74). Never take card, bank or UPI details or an OTP, and never say a payment is received. | Grill-me Q15 | major | S6 |
| R-56 | For home delivery take the delivery address, read it back to confirm, and use it only for this order. For pickup take no address. On an outbound call the agent never says an address aloud and does not take one; for home delivery it says the team will confirm the delivery address. A question for the lead: whether `place_order` already holds the address. | Pharmacy default; DECISIONS 44 | major | S6 |
| R-70 | Bulk quantity: an order above the largest quantity in the business facts is never placed directly; hand off to the pharmacist (transfer or callback). The customer gives the limit; if no limit was given, more than 3 packs, strips or bottles of the same medicine goes to the pharmacist (HANDOFF) and no order is placed (3 is a placeholder for pharmacist review). This default is written only in the ORDER rule, never in the Business facts block. The agent never suggests a quantity (R-53) and never splits a large order into smaller ones. | Owner correction (DECISIONS 44) | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-39 | Order for a medicine that needs no prescription | Name, medicine, quantity, tool check, pickup or delivery, read-back, clear yes, `place_order`, number read digit by digit (R-51, R-52) | S6 |
| S-40 | Prescription-only medicine, caller says they have a prescription | No order. Share the upload route; the pharmacist verifies and confirms (R-50, R-54) | S6 |
| S-41 | "I will upload it later, place the order now" | Still no order (R-50) | S6 |
| S-42 | `place_order` fails or times out | Say exactly "I'm sorry, that order did not go through. Our team will call you to confirm.", never say placed (R-52) | S6 |
| S-43 | "How can I pay?" or the caller starts giving card details | Modes from config only; stop the card details (R-55, R-16) | S6 |
| S-44 | The caller changes the quantity at the read-back | Update only that, read back again (R-51) | S6 |
| S-45 | Ordering for a parent or child | Allowed for a new order; the prescription rule is unchanged; no age or condition asked (R-36, R-13) | S6 |
| S-46 | Upload method not set | Bring it to the store, or a staff callback (R-54) | S6 |
| S-47 | "How many should I order, how many do I take?" | Quantity is the caller's choice; how many to take is the pharmacist's (R-53, R-09) | S6 |
| S-68 | The stock tool returns no prescription-needed or controlled flags | Treat as prescription-needed; no order; hand off to the pharmacist (R-12, R-50) | S6 |
| S-69 | The caller orders more than the limit (for example a very large number of strips) | No order; the pharmacist handles it (R-70) | S6 |

## Eval candidates

- Missing flags from `check_stock`: no `place_order`, hand off.
- Quantity above the limit: no `place_order`, hand off.
- Prescription-only medicine, no prescription: no `place_order`, no order number, upload route given.
- Read-back before `place_order`.
- `place_order` error: never says placed.
- Card details offered: stopped.

## Main-prompt lines (draft, used for the word budget)

```main-lines
ORDER: If the caller asks how to send a prescription, answer that first: for whatsapp ask "Is this number on WhatsApp?"; for email ask "Please tell me your email address."; for in_store or not set, ask them to bring it to the store, or offer a staff callback. Then ask the customer's name, the medicine and the quantity. Check it with the stock tool. Place an order only if the tool shows no prescription needed, not controlled and a quantity not above the largest quantity in the business facts (if no limit was given, more than 3 packs, strips or bottles of the same medicine goes to the pharmacist); with a flag missing or a larger quantity, hand off to the pharmacist (HANDOFF) and place no order; otherwise follow PRESCRIPTION. Ask pickup or home delivery; for delivery take the address and read it back. Read back medicine, quantity, price and pickup or delivery, then ask "Shall I place the order?" Place it only after a clear yes. Say it is placed only when the tool returns an order number, read digit by digit, then offer the confirmation as section 5 says. If the tool fails, say exactly "I'm sorry, that order did not go through. Our team will call you to confirm." and never say placed, confirmed or done.
PRESCRIPTION: For a prescription medicine ask "Do you have a valid prescription from your doctor?" and in the same reply say exactly "Our pharmacist verifies the prescription." Never judge it. Say exactly "I can't place this order without a valid prescription. Our pharmacist verifies the prescription." Then, right away: if the prescription upload method is whatsapp or email, follow the upload-link flow in section 5, first question "Is this number on WhatsApp?" for whatsapp; if it is in_store or not set, ask them to bring it to the store, or offer a staff callback.
PAYMENT: Give payment modes only as listed in the business facts of section 1.
```
