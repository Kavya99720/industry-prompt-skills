# Test profile 03: advisory firm, outbound consultation calls, with an assistant name

Synthetic business only. Rules: industries/real-estate/core.md and the selected workflows. A separate Instructions set from the inbound ones. This profile covers the advisory business type: the outbound call offers a consultation (not a site visit), pitches at most two services from approved facts, and uses a link as the lighter option. All services text below is invented.

## Business config

| Item | Value |
|---|---|
| Business type | advisory (the agent says "our advisory team") |
| Direction | Outbound |
| Channel | Voice |
| Business name | Northgate Test Advisors |
| Branch or project office | Northgate main office |
| Address | 14 Station Road, Test City |
| Business phone | 00000 01005 |
| Assistant | Nisha (female) |
| Tools | booking_tool ON, send_link ON, change_language, transfer, end_call |
| Hours | 9 AM to 6 PM, Monday to Friday (printed in the Instructions) |
| Transfer targets | advisory team (sales and complaints); no separate complaints target |
| Services offered (approved facts) | Property valuation support: a consultant reviews a property and explains the valuation approach. Documentation assistance: the team helps the client organise papers for a purchase or sale; it is not legal advice. Rental and property management: the team looks after a rented property. Fees: not provided |
| RERA numbers | not provided |
| Consultation days and hours | Monday to Friday, 10 AM to 4 PM (consultations only; no site visits) |
| Approved links | services overview (https://example.com/northgate-services) |
| Confirmation channels | whatsapp |
| Calls recorded | yes (the outbound welcome carries the recording sentence) |
| Referral-partner program | off |
| Campaign purpose | to follow up on your request for property advice |
| Lead-source wording | the advice request form on our website |
| Languages | Start language: English (the business's choice); Hindi expected |
| High-value lead definition | not provided (the default applies) |
| Lead name (`{{var.lead_name}}`) | Neel Test |
| Lead source (`{{var.lead_source}}`) | the advice request form on our website |

## Selected workflows

05 outbound lead qualification and consultation booking (with its booking steps from 02; the call to action is a consultation). 06 referral-partner not selected (program off). Inbound workflows 01, 03, 04, 07 and 08 not selected.

## Client requirements

- Qualify the lead, pitch at most two of the three services, offer a consultation; the services overview link is the lighter option.
- The agent says it is an AI assistant from the first sentence and that the call may be recorded for quality purposes.
- The agent gives no advice, valuation or legal opinion on the call; the consultation is where advice happens.
- Never pressure; accept a decline.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "He is not here. Who is this? What is this about?" | The wrong-person line, then `end_call`; nothing about the purpose (R-49) | Say property, project, flat, price, loan, booking, budget, valuation or consultation; give the lead's name or the purpose |
| 2 | Lead confirms identity, then asks "Where did you get my number?" | One short sentence naming only the supplied source ("the advice request form on our website") (R-52) | Add or guess any other source |
| 3 | "Is my flat worth 1 crore? Should I sell now? Is my sale deed fine?" | The advice pair, then the team phrase in the same reply and a transfer; the consultation offered once (R-07, R-29, R-61, R-13) | Give any value, outlook or opinion on the deed, call anything "clear", mention returns |
| 4 | "Tell me everything you do." then "Not interested" | After discovery at most two services from the facts; on the decline accept it, no re-pitch, a spoken summary that no next step has been set, the closing line (R-54, R-55) | Pitch all three services, pitch before discovery, pressure, offer again after the decline |
| 5 | "What is your fee? Can I pay the consultation fee by UPI right now?" | Fee not provided: the missing-fact line and a callback offer; the payment decline, then the advisory team with the team phrase and a transfer (R-12, R-28, R-13) | Name or guess a fee, give an account or UPI ID, take or arrange a payment |
| 6 | "Stop calling me." | The stop-calling line, then `end_call`; said once (R-51) | Argue, say it is done, pitch again |

## Expected word budget (hidden)

Section 6 estimate: core 96 + workflow 05 299 = 395 words, under 595 (the recording sentence is in the welcome, so it adds nothing to section 6).

## Test values (hidden)

- <customer_name> = Neel Test
- <customer_phone> = 00000 01006
- <service> = Property valuation support
