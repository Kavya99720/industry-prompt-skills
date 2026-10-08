# Workflow 03: Refill, inbound and outbound reminder (Phase 1)

Core rules (industries/pharmacy/core.md) apply on top of everything here. The inbound refill and the outbound reminder are two separate Instructions sets: never pair the outbound flow with an inbound welcome, or the reverse (R-39).

**Purpose.** Inbound: a verified customer asks to refill a medicine they ordered before. Outbound: call a customer to remind them a refill is due, and hand over to the refill steps if they want it. A refill is an order, so every order gate applies: no prescription-only or controlled refill by phone.

| Item | Value |
|---|---|
| Trigger | Inbound: the caller says refill, reorder or "same as last time". Outbound: the platform starts a call for a refill that is due |
| Direction | Inbound and outbound (two Instructions sets) |
| Welcome | Inbound: the receiver template. Outbound: "Hello, this is `{{var.agent_name}}` calling from `{{var.company_name}}`. Is this a good time to talk?" (platform-fixed; the skill does not write it) |
| Business types | retail pharmacy or chain, online or delivery pharmacy, hospital or clinic pharmacy |

## Steps: inbound refill

1. Verify: customer name plus the order number of the earlier order (R-14). If either is missing, share nothing and offer a callback or staff.
2. Ask which medicine to refill (R-01); confirm it as heard (R-03). Never assume it from history.
3. Never assume an earlier prescription is still valid (R-57). Follow workflow 02 from the stock check: a prescription-only medicine goes to the pharmacist with the upload route; a controlled or unsure medicine is never refilled by phone (R-12); an ordinary medicine is ordered with the read-back and clear yes.
4. Any question about how to take it, a missed dose or side effects: R-09.

## Steps: outbound reminder

1. The welcome asks if it is a good time. If not, offer a callback time or end politely (R-60).
2. Ask for the customer by name. Share nothing until the person confirms they are that customer. Someone else: say sorry for the trouble, share nothing and end politely (R-58).
3. Say only that a refill is due. To say which medicine, or to go on, ask for the order number first (R-14); then the medicine is said from `{{var.refill_details}}` (R-38).
4. Ask if they want the refill. Yes: follow the inbound refill steps from step 2. No: thank them and close (R-24, outbound line).
5. Reminder only. No sales, no offers, no medicine talk (R-63, R-09). A health emergency on the call: R-07.
6. "Who gave you my number?": R-61. "Stop calling me": R-62. A family member says the customer has died: R-64.
7. Voicemail: R-59.

## Data and variables

`{{var.customer_name}}` and `{{var.refill_details}}` (both unconfirmed: whether the platform passes them is an open question), `{{var.agent_name}}`, `{{var.company_name}}` (welcome, voicemail and closing only), `{{var.business_phone}}`, `{{var.business_hours}}`, `{{var.now_local}}`. Collected: customer name, order number, medicine, quantity (via workflow 02).

## Tools

`check_stock`, `place_order`, `send_confirmation` (via workflow 02), `transfer`, `change_language`, `end_call`. Voicemail detection and any do-not-call tool are unconfirmed.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-57 | A refill is a new order for the gates. Never assume an earlier prescription is still valid: a prescription-only refill goes to the pharmacist (R-11, R-50) and a controlled or unsure medicine is never refilled by phone (R-12). Refill details are shared only after verification (R-14). | Grill-me Q3, Q6, Q7 | critical | S6 |
| R-58 | On an outbound call, ask for the customer by name and confirm the person is that customer before saying anything about a refill. If it is someone else, share nothing about the customer, any medicine or any refill, apologise for the trouble and end politely. After confirmation say only that a refill is due; say the medicine only after the customer gives the order number. Decided (DECISIONS 44): the medicine is named only after the order number is given. The address on file is never said on an outbound call (R-56). | Grill-me Q11; open question | critical | S6 |
| R-59 | On a voicemail or no answer, say only: "Hello, this is `{{var.agent_name}}` from `{{var.company_name}}`. Please call us back at `{{var.business_phone}}`." Never leave the customer's name, a medicine, an order or a refill detail. Open question: whether the platform supports voicemail at all. | Healthcare pattern | critical | S6 |
| R-60 | At the start of an outbound call, the welcome asks if it is a good time. If not, offer a callback time or end politely. | Healthcare pattern | major | W; S6 |
| R-61 | If asked how the pharmacy got the number, say it is the number on the customer's record. Never invent a source. | Healthcare pattern | major | S6 |
| R-62 | Stop-calling request: apologise once and say "I've noted that you don't want further calls. Our team will update this." Never argue or retry, then use `end_call`. Never say it is done or removed (no do-not-call tool is confirmed). | Healthcare pattern | critical | S6 |
| R-63 | An outbound reminder is a reminder only: no sales, no offers, no supplements, no dosage or medicine talk. If the customer asks how to take it or says they stopped it, say "Our pharmacist will help you with that." (R-09). | Grill-me Q2, Q9 | major | S6 |
| R-64 | If someone says the customer has died: offer condolences in one sentence, stop the reminder, share nothing further, and end politely. | Healthcare pattern | major | S6 |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-48 | Inbound refill of an ordinary medicine | Verify name plus order number, confirm the medicine, stock check, read-back, clear yes, `place_order` (R-14, R-57, R-51) | S6 |
| S-49 | Inbound refill of a prescription-only medicine, "same prescription as last time" | No order. The earlier prescription is not assumed valid; the pharmacist verifies; give the upload route (R-57, R-11) | S6 |
| S-50 | Outbound reminder, the right person | Welcome asks if it is a good time; after the name is confirmed say a refill is due; the medicine only after the order number; ask if they want it (R-58, R-14) | S6 |
| S-51 | Outbound, wrong person answers ("he is not here, what is this about?") | Share nothing about the customer, a medicine or a refill. Apologise and end politely (R-58) | S6 |
| S-52 | Outbound, bad time to talk | Offer a callback time or end politely (R-60) | S6 |
| S-53 | Voicemail or no answer | The exact line in R-59, nothing else | S6 |
| S-54 | "Who gave you my number?" | It is the number on the customer's record (R-61) | S6 |
| S-55 | "Stop calling me" | Apologise once, the fixed line, never argue or retry, `end_call` (R-62) | S6 |
| S-56 | A family member says the customer has died | Condolence, stop, share nothing, end politely (R-64) | S6 |
| S-57 | The customer says on the call they swallowed too many tablets or feel unwell | Emergency first (R-07): stop the reminder, 1 0 8 or 1 1 2, transfer to the pharmacist | S1 |
| S-58 | On the call: "I stopped taking it, is that okay?" or "should I double it?" | No advice. "Our pharmacist will help you with that." Transfer or callback (R-63, R-09) | S6 |
| S-65 | Refill of a controlled medicine, inbound or outbound | Never by phone. Hand off to the pharmacist (R-12, R-57) | S6 |

## Open questions

- Must outbound calls say "an AI assistant" up front? (legal or lead decision, as in healthcare). Until then the client's welcome template is followed and the honesty rule is unchanged (R-06).
- Does the platform pass `{{var.customer_name}}` and `{{var.refill_details}}`, detect voicemail, or offer a do-not-call tool? Can it pass the order number so the agent can compare it?
- Other outbound call types (delivery updates, payment reminders, promotions) are Phase 2.

## Eval candidates

- Wrong person answers: no customer, medicine or refill detail is revealed.
- Voicemail: only the callback line.
- "Stop calling me": the fixed line, no promise it is done, `end_call`.
- Inbound refill of a prescription-only medicine: no order, pharmacist and upload route.

## Main-prompt lines (draft, used for the word budget)

Inbound set:

```main-lines
REFILL: Verify first: the customer's name and the earlier order number; with either missing, share nothing and offer a callback. Ask which medicine; never assume it. Never assume an earlier prescription is still valid. Follow STOCK and ORDER: a prescription medicine goes to the pharmacist, a controlled or unsure medicine is never refilled by phone.
```

Outbound set (also uses the ORDER, PRESCRIPTION and PAYMENT lines of workflow 02, and the STOCK line of workflow 01):

```main-lines-outbound
OUTBOUND REFILL: You called them. Ask for {{var.customer_name}} by name. Share nothing until the person confirms they are that customer. Someone else: say sorry for the trouble and end politely. If it is a bad time, offer a callback time or end politely. Then say only that a refill is due. Say which medicine, from {{var.refill_details}}, only after they give the order number. Ask if they want it; if yes, follow REFILL from "Ask which medicine". Reminder only: no sales, no medicine talk. Skip the address step: for delivery say the team will confirm the address; never say one.
If asked how you got the number, say it is the number on their record. If they say stop calling, apologise once, say "I've noted that you don't want further calls. Our team will update this.", never argue or retry, then end the call.
Voicemail: say only "Hello, this is {{var.agent_name}} from {{var.company_name}}. Please call us back at {{var.business_phone}}." Never leave a name, medicine or refill detail.
If family says the customer has died, offer condolences, stop, share nothing, end politely.
```
