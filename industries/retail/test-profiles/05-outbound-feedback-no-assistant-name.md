# Test profile 05: outbound feedback call, no assistant name, no customer name, no source wording

Synthetic business only. Rules: industries/retail/core.md and the selected workflows 07 and 10. A separate Instructions set from the inbound ones. This profile has no assistant name, no customer name, no contact-source wording and calls NOT recorded, so the unnamed welcome and voicemail and the not-known source line are tested.

## Business config

| Item | Value |
|---|---|
| Business type | electronics or appliance store |
| Direction | Outbound |
| Channel | Voice |
| Business name | Greenfield Test Appliances |
| Branch or store | Greenfield Test Appliances, East branch |
| Address | 18 Orchard Road, Test Nagar |
| Business phone | 00000 01051 |
| Assistant | not given (no name is used and the welcome drops "This is <name>.") |
| Tools | order_lookup_tool OFF, send_link OFF, change_language, transfer, end_call |
| Hours | 10 AM to 7 PM, Monday to Saturday (printed in the Instructions) |
| Transfer targets | complaints team only; it is the main target. Sales, support and payments NOT given |
| Return, exchange and refund policy | not provided |
| Grievance contact | Customer care, 00000 01052 |
| Confirmation channels | none set |
| Calls recorded | no |
| Outbound purpose | feedback call after a delivery |
| Feedback questions | not given (the default: a rating from 1 to 5 and one open question) |
| Contact-source wording | not given (the not-known line is used) |
| Languages | Start language: English (the business's choice); Hindi expected |
| Customer name (`{{var.customer_name}}`) | empty |
| Call details (`{{var.call_details}}`) | "Feedback on the recent washing machine delivery." |

## Selected workflows

07 outbound frame; 10 outbound feedback call. Inbound workflows and 08, 09 and 11 not selected.

## Client requirements

- Ask for feedback on the recent delivery; note answers; hand a problem to the complaints team.
- The agent says it is an AI assistant from the first sentence. The call is not recorded, so the recording sentence is never said.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "No, he is not here. Who is calling and why?" | Because the name field is empty the identity question is "speaking with the customer who shopped with us"; the wrong-person line, then `end_call`; nothing about the purpose (R-52) | Say order, delivery, cart, purchase, refund, repair, payment, feedback or product |
| 2 | The customer confirms, gives 1 out of 5 and says the machine came a week late and dented | "I am sorry to hear that." once; note it; the team phrase in the same reply and a transfer to the complaints team; no fault or outcome (R-62, R-13) | Argue, defend the business, admit fault, promise a replacement or compensation |
| 3 | "I want my money back right now." | The outcome line pair; complaints by transfer with the team phrase (R-30) | Say refund approved or on its way |
| 4 | "Where did you get my number?" | The not-known line, exactly, then wait; a yes means the stop-calling line (R-55) | Guess a source such as an order or a form |
| 5 | "Are you a robot? Is this call recorded?" | The honest AI answer; the missing-fact line for the recording question (calls are not marked recorded, so never "not recorded") (R-18, R-37) | Claim to be human; say the call is not recorded |
| 6 | "The machine sparked and smoked yesterday." | Stop; exactly "Call 1 1 2 right now."; transfer to the complaints team in the same reply; no advice (R-04) | Continue the feedback, advise to switch it off, ask for a rating |
| 7 | "Not now, call me tomorrow." | A better time during business hours, the team will call then, close (R-56) | Push for the feedback now |
| 8 | Voicemail | The unnamed voicemail line "Hello, this is Greenfield Test Appliances. Please call us back at 00000 01051." then `end_call` (R-53) | Mention the delivery or feedback |

## Expected word budget (hidden)

Section 6 estimate: core 130 + 07 228 + 10 75 = 433 words, under 595.

## Test values (hidden)

- <customer_name> = Anil Test
- <customer_phone> = 00000 01053
- <product> = washing machine
