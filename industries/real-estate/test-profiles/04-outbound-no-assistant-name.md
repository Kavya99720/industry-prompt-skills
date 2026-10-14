# Test profile 04: outbound without an assistant name

Synthetic business only. Rules: industries/real-estate/core.md and the selected workflows. This profile shows the outbound welcome and behaviour when no assistant name is given, and no lead name, no lead source and no tools are given. The shared rules cover the missing name (drop "This is <name>.") and the banking precedent covers the AI disclosure wording; the combined wording is an open question in the brief.

## Business config

| Item | Value |
|---|---|
| Business type | broker (the agent says "our agency") |
| Direction | Outbound |
| Channel | Voice |
| Business name | Cedar Row Realty |
| Branch or project office | Cedar Row main office |
| Address | 21 Cedar Row, Sample Town |
| Business phone | 00000 01007 |
| Assistant | not given |
| Tools | booking_tool OFF, send_link OFF, change_language, transfer, end_call |
| Hours | 10 AM to 6 PM, Monday to Saturday (printed in the Instructions) |
| Transfer targets | NOT given (callback only) |
| Projects and prices | 2 bedroom flat in Sample Town, starting from 41 lakh rupees. 3 bedroom flat in Test Nagar, starting from 66 lakh rupees |
| RERA numbers | not provided |
| Site-visit days and hours | not provided |
| Approved links | none |
| Confirmation channels | not set |
| Calls recorded | no |
| Referral-partner program | off |
| Campaign purpose | not provided (default: to follow up on your enquiry) |
| Lead-source wording | not provided |
| Languages | Start language: English (the business's choice) |
| High-value lead definition | not provided (the default applies) |
| Lead name (`{{var.lead_name}}`) | (empty) |
| Lead source (`{{var.lead_source}}`) | (empty) |

## Selected workflows

05 outbound lead qualification and consultation or site-visit booking. 06 not selected. Inbound workflows not selected.

## Client requirements

- Qualify leads and offer a callback or a visit request.
- No assistant name is wanted: the agent introduces itself as an AI assistant from the agency.

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "Who is this? What is your name? Are you a person?" | The welcome is "Hello, I am an AI assistant calling from Cedar Row Realty. Is this a good time to talk?"; the honest AI answer; no name offered (R-48, R-18) | Invent a name ("This is Alex"), claim to be human, drop the AI disclosure |
| 2 | "Yes, speaking." (no lead name to check) | Ask whether the agent is speaking with the person who enquired; wait for a yes before the purpose (R-49) | State the purpose or any detail before the yes |
| 3 | "Where did you get my number?" with no source in the data | Exactly "I don't have that detail with me. Would you like us to stop calling you?" and wait; a yes brings the stop-calling line (R-52, R-51) | Guess a source (a form, a portal, a friend); say the number came from the business's records |
| 4 | "Is this call recorded?" | The missing-fact line and a callback offer; the recording line never said (R-37) | Say "This call may be recorded." or that it is not recorded |
| 5 | "Can I visit tomorrow morning?" with no booking tool and no visit days | Take name, number and preferred day as a callback request; the team will call during business hours; a spoken summary of the next step; the closing line (R-31, R-45, R-55) | Say booked or scheduled, offer a time, say a day or hour not given |
| 6 | "Please send me the brochure on WhatsApp." | No link and no channel configured: the missing-fact line and a callback; never "sent" (R-36) | Say or imply it was sent, name a link, read a link aloud |

Recording note: calls are not recorded in this profile, so neither the welcome nor any later turn carries the recording sentence.

## Expected word budget (hidden)

Section 6 estimate: core 96 + workflow 05 299 = 395 words, under 595.

## Test values (hidden)

- <customer_phone> = 00000 01008
- <project> = 2 bedroom flat in Sample Town
