# Pharmacy grill-me

Date: 2026-10-08. Interview: 18 questions, one at a time. Every answer below was chosen by the owner; "recommended" means the owner picked the option the interviewer suggested. Nothing here is a design: the brief, evals and skill are not started.

References used: docs/DECISIONS.md entry 3 (Pharmacy owns medicine orders, refills, prescriptions and delivery; appointments, doctors and emergencies belong to healthcare; no dosage advice) and the healthcare decisions (entries 4 to 40).

## Answers

| # | Topic | Owner's answer |
|---|---|---|
| 1 | Business types | Retail pharmacy and chains, online/delivery pharmacy, and hospital/clinic pharmacy (all three; recommended plus two more) |
| 2 | Call directions | Inbound plus outbound refill reminders (recommended). Two separate Instructions sets |
| 3 | Phase 1 call types | Medicine enquiry (availability, price, substitutes); order plus prescription upload; refill (inbound and outbound reminder); delivery status and returns. All four selected |
| 4 | Channel and languages | Voice plus chat |
| 5 | Chat handling (follow-up) | Voice Instructions now; chat noted as an open question until the platform supports chat (recommended) |
| 6 | Prescription-only medicines | Never confirm an order without a valid prescription (recommended). The agent asks for the prescription; the pharmacist verifies |
| 7 | Controlled / habit-forming medicines | Never order or refill by phone; transfer to the pharmacist (recommended). Exact schedules to be confirmed by an industry expert |
| 8 | Substitutes | Never substitute; offer a pharmacist callback or transfer (recommended) |
| 9 | Dosage and usage questions | No advice at all; pharmacist or doctor (recommended) |
| 10 | Emergencies (overdose, poisoning, wrong medicine, child swallowed medicine, severe allergic reaction) | Stop everything, 108/112 now, transfer to the pharmacist (recommended). Same universal stop line as healthcare |
| 11 | Verification | Customer name plus order number before any detail (recommended) |
| 12 | Data the agent may collect | **Changed in the follow-up (2026-10-08): the agent does NOT collect age or medical condition.** For medicine or usage questions it says "Our pharmacist will help you with that." and transfers, or offers a callback. The pharmacist asks any clinical questions. Consistent with healthcare. (The first answer, "also age and condition", is withdrawn.) |
| 13 | Age and condition limits (follow-up) | Superseded by the change to Q12: no age and no condition are collected by the agent at all |
| 14 | Human escalation | Pharmacist for medicine questions; store manager for complaints (recommended). Callback if nobody is available |
| 15 | Payments and prices | Prices and discounts only from the system or config; payment modes only; never take payment details (recommended) |
| 16 | Returns and refunds | Only per the configured policy; wrong, damaged or expired item goes to staff (recommended) |
| 17 | Platform tools | Stock/price check and place order (recommended). Order status lookup and a send-link/confirmation tool were NOT selected |
| 18 | Client special requests | Same as healthcare: refuse unsafe or deceptive requests, adapt where possible, list in the draft notes (recommended) |

## What the answers imply (as stated by the owner, not new decisions)

- **Scope:** medicine orders, refills, prescriptions, delivery and returns over voice, for retail/chain, online and hospital pharmacies. Appointments, doctors and emergencies belong to healthcare.
- **Safety limits:** no dosage, usage, interaction, side-effect or substitute advice; no order of a prescription-only medicine without a valid prescription; no phone order or refill of controlled medicines; emergencies go to 108/112 first; never take payment details.
- **Privacy:** no order or prescription details without customer name plus order number; the agent never collects age or medical condition (the pharmacist asks clinical questions).
- **Escalation:** pharmacist (medicine questions), store manager (complaints and returns problems); callback when nobody is available; emergencies always get 108/112.
- **Client requests:** refuse unsafe or deceptive requests; list every refusal in the draft notes.

## Gap defaults (follow-up, 2026-10-08)

Decided by the owner after the interview, for the items first left unspecified:

- **Order status:** there is no lookup tool, so the agent never guesses a status. It offers a callback or a transfer to staff.
- **Prescription upload:** if the client enables it (custom detail `prescription_upload_method`: whatsapp, email or in_store), the agent uses the platform send tool to share the upload instructions. Otherwise it asks the customer to bring the prescription to the store, or offers a staff callback.
- **Out of stock:** "That medicine isn't in stock right now. Our pharmacist can help, or we can call you when it's back." The agent never suggests another brand or a substitute.
- **Controlled or prescription status:** if the stock tool flags a medicine as controlled or prescription-only, or the agent is unsure, it hands off to the pharmacist. The exact schedules are an open question for an industry expert.
- **Medicine or usage questions:** "Our pharmacist will help you with that." Then transfer, or offer a callback. No age, no condition asked.

## Open questions (Phase 2 or for an expert)

- **Chat channel:** voice first; chat behaviour (image upload, no TTS rules) is open.
- **Hospital-pharmacy specifics:** collection counter, discharge medicines, queue questions. Phase 2.
- **Other outbound call types** beyond refill reminders (delivery updates, payment reminders, promotions). Phase 2.
- **Controlled-medicine schedules** and what counts as a valid prescription: to be confirmed by an industry expert.
- **Languages:** assumed to follow healthcare's 11 platform languages; not confirmed.
- **Poison-control helpline:** not discussed; only 108/112 and, for self-harm, Tele-MANAS 14416, as in healthcare.
- **Returns policy values** (window, refund rules): come from client configuration.
- **Tools not selected:** an order-status lookup and a send-link tool for confirmations were not selected. The send tool is used only for prescription-upload instructions when the client enables it.
