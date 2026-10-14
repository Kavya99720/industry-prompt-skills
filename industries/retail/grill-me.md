# Retail grill-me

Date: 2026-10-14. Interview: 8 questions in the main chat, then the owner's changes after the summary. Every answer below was chosen by the owner; "recommended" means the owner picked the option the interviewer suggested. Nothing here is a design: the brief and skill are the next steps.

References used: docs/DECISIONS.md (entries 108 for the no-evals plan, 109 to 111 for real estate), docs/shared/.

## Answers

| # | Topic | Owner's answer |
|---|---|---|
| 1 | Business types | All four: single store, chain/franchise, e-commerce/online store, electronics/appliance store with service and warranty. One skill; the business type decides the workflows |
| 2 | Callers | Mainly existing customers with an order or purchase; pre-purchase shoppers (stock, price, hours, location) are secondary |
| 3 | Directions | Inbound and outbound, as two separate Instructions sets |
| 4 | Channel | **Voice only in v1** (owner's change; the interview option was voice and chat). Chat is a later option |
| 5 | Inbound scenarios | Product availability and price, order status, delivery, returns/exchange/refund, warranty and repair, store hours and location, complaints, payment problems |
| 6 | Outbound scenarios | Order or delivery update, abandoned cart reminder, feedback call, repair or service-ready update |
| 7 | Refunds and returns | Only that the request is noted until the system confirms. Never "refunded", "approved", "replaced" or "pickup scheduled" before then |
| 8 | Payment problems | Look up status (where the tool is on), never take payment details, route to the payments team. Fake-payment and refund-scam warning |
| 9 | Complaints and legal threats | Log the complaint, give the business's grievance channel (only from business facts), transfer to a human. No argument, no admission of liability, no promise of compensation |
| 10 | Verification | Order lookup tool: order ID plus a match on the registered phone or name. Tool off: no order details, general information only, callback offered (owner's change) |
| 11 | Never invent | Stock, price, discount, offer or delivery date: only from tools or business facts. No Aadhaar, PAN or bank details. No card, UPI, OTP, CVV or PIN on the call |
| 12 | Emergency (owner's change) | A device sparking, smoking or with a burning smell, an electric shock, a fire, a gas leak from an appliance, or an injured person: say exactly "Call 1 1 2 right now." and transfer. No repair or first-aid advice |
| 13 | Transfers (owner's change) | Only targets given at intake (sales, support, payments, complaints). A missing named team uses the main target; with none, a callback. "I'll connect you to our team." in the same reply as every transfer |
| 14 | Tools | Order lookup, stock check, send link (optional, default OFF), transfer; a callback is the agent taking name, number and reason |
| 15 | Intake | Required: business type, call direction, business and branch name, address, phone, hours, assistant name and gender, languages and start language, transfer targets or callback only. Optional: tools on or off, return/exchange/refund policy (printed exactly as given), warranty and repair or service-centre information, delivery areas, charges and timelines, payment modes, grievance officer or complaint contact, other store locations, offers (once, never pushed), confirmation channels, calls recorded, outbound campaign purposes, special rules |
| 16 | Languages | English first in the Supported list; the start language is the business's choice (default English) |
| 17 | Nobody available | Take name, number and reason for a callback during business hours; promise only a time the business gave |
| 18 | Shared rules | All shared rules from healthcare, pharmacy, banking and real estate apply (interactive intake with summary, option B real values, helpline digits in Latin digits, required safety blocks word for word, outbound welcome with AI disclosure and the recording line before the question only if recorded, no rule IDs, plain-word notes) |
| 19 | Evals | None for this industry (DECISIONS 108). Five manual test profiles instead |
