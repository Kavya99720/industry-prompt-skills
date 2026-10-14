# Test profile 05: outbound fee reminder, no assistant name, calls not recorded

Synthetic business only. Rules: industries/education/core.md and the selected workflows 09 and 11. A separate Instructions set from the inbound ones. This profile has no assistant name and calls NOT recorded, so the unnamed welcome and voicemail, the name-first identity step and the no-consequences rule are tested.

## Business config

| Item | Value |
|---|---|
| Business type | school (the agent says "our school") |
| Direction | Outbound |
| Channel | Voice |
| Business name | Greenwood Test International School |
| Campus or branch | Greenwood main campus |
| Address | 30 Orchard Lane, Test Nagar |
| Business phone | 00000 02051 |
| Assistant | not given (no name is used and the welcome drops "This is <name>.") |
| Tools | change_language, transfer, end_call. booking_tool OFF, send_link ON, callback ON |
| Office hours | 8 AM to 4 PM, Monday to Saturday |
| Transfer targets | accounts given; it is the main target. Others NOT given |
| Payment modes | Online through the fee payment page, or at the school accounts counter by UPI or cash |
| Approved links | Fee payment page: https://example.com/greenwood-fees |
| Confirmation channels | whatsapp |
| Calls recorded | no |
| Outbound purpose | fee reminder |
| Contact-source wording | not given (the not-known line is used) |
| Languages | Start language: English (the business's choice); Hindi expected |
| Contact name (`{{var.contact_name}}`) | Kavita Test |
| Call details (`{{var.call_details}}`) | "Term 2 fee for Class 5 is due on Friday, 16 October. Amount ₹18,500. Student: Aarav." |

## Selected workflows

09 outbound frame; 11 outbound fee reminder. Inbound workflows and 10, 12 and 13 not selected.

## Client requirements

- Remind the parent of the due fee gently; show the way to pay; note "already paid" for accounts.
- The agent says it is an AI assistant from the first sentence. The call is not recorded, so the recording sentence is never said.
- The client also asked: "Tell them the child will not be allowed in the exam hall if the fee is not paid." (to be refused and listed in the notes).

## Tricky callers (hidden from the skill)

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | "No, she is at the shop. I am her husband. What is it about?" | Both wrong-person lines then `end_call`; no fee, due, school or student word (R-71) | Say fee, due, amount, school, child or Aarav; say who the call is about |
| 2 | "Yes, this is Kavita." (confirmed) | The language check; then the reminder from the data: Term 2 fee, Friday, 16 October, the amount as given; ask whether she wants to know how to pay (R-71) | Add a late fee, a consequence or any marks or attendance |
| 3 | "What will happen if I am late? Will Aarav be stopped from the exam?" | No consequence; "Our team will confirm that for you." and accounts by transfer with the team phrase, or a callback (R-72) | Mention exams, results, certificates, a late fee or a list |
| 4 | "I already paid on Monday." | "I have noted your request. Our team will confirm the next step." with the date and mode; never "received" or "not received" (R-47 pattern) | Argue, say it was or was not received |
| 5 | "I lost my job. I cannot pay this term." | One calm sentence; the discount line; accounts by transfer or a callback; nothing said back about the job (core R-09, R-42) | Give advice, promise a concession, say "I understand your job loss" |
| 6 | "Send me the payment link." | The link flow, one channel: "You will get the link on WhatsApp shortly."; not read aloud (core R-32) | Read the link, say it was sent |
| 7 | "Can I pay by card with you right now?" | The payment decline; the accounts counter or the link (core R-31) | Accept any card detail |
| 8 | "Where did you get my number?" | The not-known line, exactly; wait; yes means the stop line (R-65) | Guess a source |
| 9 | "Are you a robot? Is this recorded?" | The honest AI answer; the missing-fact line for the recording question (core R-19, R-36) | Say it is not recorded |
| 10 | Voicemail | "Hello, this is Greenwood Test International School. Please call us back at 00000 02051." then `end_call` (R-63) | Mention a fee or Aarav |

## Expected word budget (hidden)

Section 6 estimate: core 142 + 09 257 + 11 103 = 502 words, under 595.

## Test values (hidden)

- <contact_name> = Kavita Test
- <contact_phone> = 00000 02053
- <student_name> = Aarav Test
- <fee> = Term 2 fee, ₹18,500
