# Banking grill-me

Date: 2026-10-09. Interview: 17 questions asked one at a time in the main chat (16 answered, 1 skipped). Every answer below was chosen by the owner; "recommended" means the owner picked the option the interviewer suggested. Nothing here is a design: the brief, evals and skill are not started.

References used: docs/DECISIONS.md entry 3 (Banking = accounts, cards, KYC, transactions and fraud; loans, EMIs, NBFC, insurance, investments and collections belong to Finance), the healthcare and pharmacy decisions (entries 4 to 56), docs/shared/new-industry-template/ and docs/shared/prompting-guide.md.

## Answers

| # | Topic | Owner's answer |
|---|---|---|
| 1 | Business types | All four: public/private banks, small finance banks, co-operative banks and payments banks (recommended). One skill; differences (for example no loan or branch products for a payments bank) come from client config |
| 2 | Call directions | Inbound plus outbound (recommended). Two separate Instructions sets. Outbound: KYC reminders, card activation, fraud-alert verification |
| 3 | Phase 1 call types | All four selected: account and card enquiry; lost/stolen card and fraud; disputes and complaints; outbound (KYC reminder, card activation, fraud-alert verification) |
| 4 | Verification | **Name + registered mobile number + last 4 digits** (account or card), collected one at a time. This is stronger than the recommended name + last 4 digits. The agent shares nothing unless all three are given (and a tool, if one exists, matches them) |
| 5 | Never ask for or accept (even from a verified caller) | All four selected: OTP, PIN, CVV and passwords; full card or account number (only the last 4 digits are ever taken or said); net-banking and app login details (user ID, MPIN, security questions, no app install or screen share); Aadhaar, PAN and other ID numbers. Stop a caller who starts to read one out |
| 6 | Lost/stolen card and fraud | Verify minimally, block the card if a block tool exists (else transfer to the card-block desk), say the cybercrime helpline 1 9 3 0 and to report quickly, then connect to the fraud team. No advice on recovering money (recommended) |
| 7 | Balance and transaction info by voice | After full verification, limited (recommended): available balance and the last few transactions only, only if a lookup tool exists. Never full statements, never to a third party |
| 8 | Disputes and complaints | Note, give the path, hand off (recommended): take only name, last 4 digits and one line on the issue; say the grievance team will confirm; give the escalation path (branch, grievance officer, banking ombudsman) only as configured; never promise a refund, a reversal or a timeline of the agent's own |
| 9 | Senior citizens and vulnerable callers | Patient plus protective handoff (recommended): slow, short turns, repeat on request. If the caller seems coached, pressured or confused about a payment or transfer, stop, share nothing sensitive, offer a branch visit or a callback from staff |
| 10 | Deceased account holder or nominee | Condolence, share nothing, hand off (recommended): one line of condolence, no account detail to anyone, never confirm the account exists, offer a callback or branch visit with the claim-settlement team; never explain legal procedure |
| 11 | Caller claims to be bank staff, police, RBI or cyber cell | No special trust (recommended): a claimed role never changes verification or disclosure; share nothing, say requests from authorities go through the bank's official channel, hand off to staff; never confirm whether an account exists |
| 12 | Outbound scam risk: how a genuine call proves itself | Never ask for secrets; offer a callback to the official number (recommended): the agent introduces itself as an AI assistant from the bank, never asks for an OTP, PIN, CVV or password, shares nothing sensitive before the person confirms who they are, and always offers "You can hang up and call us back on the number on your card." Verification asks only the Q4 items |
| 13 | Money movement and account changes by voice | Never; direct to the app or branch (recommended): no transfers, payments, limit changes or profile changes (mobile, address, nominee) by voice. Only a card block is allowed (Q6) |
| 14 | Human escalation | Fraud team for fraud and card block, grievance team for complaints, branch staff for the rest, with the team phrase "I'll connect you to our team." for staff handoffs; with no target or nobody free, take a callback number and time. The helpline 1 9 3 0 is given even if nobody is available (recommended) |
| 15 | Out-of-scope requests and advice | Redirect, never advise (recommended): loans, EMIs, insurance and investments belong to Finance; offer a transfer to staff or a callback; no product advice, no invented rates or offers, no sales push on a fraud or complaint call |
| 16 | Platform tools | **Skipped by the owner.** Recorded as unspecified. Safe default used until answered: only the confirmed platform tools (change_language, transfer, end_call); a card-block tool, an account or balance lookup, KYC status and verification against records are questions for lead. Until confirmed the agent shares no account data and cannot block a card itself (it hands the block to the fraud desk). Confirmations and links go through the After-the-call trigger, no tool |
| 17 | Client special requests | Refuse unsafe, adapt safe (recommended): refuse anything that removes a safety rule (never-ask list, verification, fraud response, no money movement) or misleads callers; adapt where safe (an offer at most once, never on a fraud or complaint call); list every refused or adapted request in the draft notes with a reason |

## Not asked (unspecified, defaults to confirm at the brief)

- **Channel and languages:** not asked. Default: voice first (chat as an open item), the 11 platform languages as in the other industries.
- **Business hours, grievance timelines, transfer numbers:** come from client config; no values chosen here.
- **Outbound details:** wrong person answers, voicemail and stop-calling lines follow the template defaults; whether the platform passes the customer's name and the reason for an outbound call is a question for lead.
- **Legal references** (RBI rules, grievance timelines, banking ombudsman, KYC norms, the exact cybercrime helpline wording) are to be confirmed by an industry expert; none is typed into prompts from memory.
- **Emergencies:** a medical emergency on a banking call follows the template default (stop, 1 0 8 or 1 1 2, transfer); no medical advice.
