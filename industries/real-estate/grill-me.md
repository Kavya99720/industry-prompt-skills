# Real estate grill-me

Date: 2026-10-14. Interview: 7 rounds of one or two questions in the main chat, then the owner's changes after the summary. Every answer below was chosen by the owner; "recommended" means the owner picked the option the interviewer suggested. Nothing here is a design: the brief and skill are not started.

References used: docs/DECISIONS.md (healthcare, pharmacy and banking entries, 108 for the no-evals plan change), docs/shared/, and one real client's outbound real-estate script (outside the repo; read as a reference only, no client name, figures, partner names or commission numbers are used anywhere in the repo).

## Answers

| # | Topic | Owner's answer |
|---|---|---|
| 1 | Business types | All four: builder/developer, broker/agency, rental/property management, real-estate advisory. One skill; the business type decides the scenarios |
| 2 | Depth | Builder and broker equal and deepest (scenarios and test profiles). Rental and advisory get a lighter set |
| 3 | Directions | Inbound and outbound, as two separate Instructions sets |
| 4 | Channel and languages | **Voice only in v1** (like healthcare, pharmacy, banking); chat is a later option. English always first; the platform handles other languages |
| 5 | Inbound scenarios | Property enquiry, price/availability, site visit, documents, booking follow-up, complaints |
| 6 | Outbound scenarios | Lead qualification; consultation or site-visit booking; referral-partner recruitment as an opt-in variant (off unless the business turns it on), described only from the business's approved text, no earnings, commission or income talk |
| 7 | Price and availability | Only facts the business supplied, as "starting from", never final. No negotiation, discount or promise that a price will hold |
| 8 | Token or advance payment | Never taken or arranged on the call, no account, UPI or link given. Decline and route to a site visit or the sales team. Fake-payment scam warning when payment to a third party comes up |
| 9 | Loans and returns | No loan-approval statement, no EMI or yield figures even as examples. Offer the team or a specialist |
| 10 | Other limits | RERA number only from business facts; no legal outcomes; no Aadhaar, PAN or bank details (stop a caller who starts reading them out); no pressure language; no re-pitch after a decline; never say "booked" or "sent" before a tool confirms |
| 11 | Source of the caller's number | State a source only if the call data provides it. Otherwise say "I don't have that detail with me. Would you like us to stop calling you?" Never guess |
| 12 | Call recording | "This call may be recorded" only if the business records calls (a yes/no intake question). The AI disclosure is always in the first exchange of an outbound call |
| 13 | Data collected | Name, number, area, property type, timeline, and a rough budget range only if the caller offers it |
| 14 | Tools | Booking (consultation or site visit), transfer to a human, callback request, send link (business-supplied links only). If a tool is off or fails, offer a callback. Transfer says "I'll connect you to our team." inline |
| 15 | Escalation | Request for a human, complaint, specific legal or tax question, high-value lead, journalist or regulator. If nobody is available or no number is set: take a callback (name, number, reason), promise only a time the business gave; complaints and journalist/regulator are high priority |
| 16 | Outbound shape | Welcome with AI disclosure; language check; discovery first, then at most 2 services; call to action is a consultation or site-visit booking, with send-a-link as the lighter option; fixed stop-calling line; every call ends with a spoken summary of the next step. Calling hours, retry limits and DND checks are platform settings: draft notes only |
| 17 | Shared rules | All shared rules from healthcare, pharmacy and banking apply, including the emergency/crisis baseline (108/112, Tele-MANAS digits) |
| 18 | Evals | None for this industry (DECISIONS 108). Quality: check_variables, check_fixed_lines, manual /prompt-writer tests on 5 test profiles |
