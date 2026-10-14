# Workflow 07: Outbound call frame (identity, voicemail, stop request, summary, closing)

Core rules apply on top of everything here. This is a separate Instructions set from the inbound one. It owns every outbound-only fixed line, because the fixed-line check reads core for both directions. Exactly one purpose workflow (08 order or delivery update, 09 abandoned cart reminder, 10 feedback call, 11 repair or service-ready update) is selected together with it.

**Purpose.** Call a customer for one stated purpose, confirm who is on the line, say the purpose's content from the call data only, and end every call with a spoken next step.

| Item | Value |
|---|---|
| Trigger | The platform places an outbound call to a customer. The customer's name and the facts for the call arrive as per-call fields (`customer_name`, `call_details`) |
| Direction | Outbound |
| Business types | All |

## Steps

1. The welcome is the first line (see section-bases): AI disclosure in the first sentence. No assistant name: "Hello, I am an AI assistant calling from <business name>. Is this a good time to talk?" Only when calls_recorded is yes, the sentence "This call may be recorded for quality purposes." is placed inside the welcome, before "Is this a good time to talk?" (named and unnamed); never when no or not given.
2. Identity: ask whether you are speaking with `{{var.customer_name}}`. With the field empty, ask whether you are speaking with the customer who shopped with us. Until the person is confirmed, say nothing about the purpose, the order or any detail.
3. Wrong person: say exactly "Sorry for the trouble. I can only speak with the person this call is for." and, in the same reply, `end_call`. Never give the purpose. Never say order, delivery, cart, purchase, refund, repair, payment, feedback or product to an unconfirmed person. Share nothing about the customer.
4. Voicemail: say exactly "Hello, this is <agent name> from <business name>. Please call us back at <phone>." and, in the same reply, `end_call`. Nothing about the order, the cart or the customer.
5. Not a good time: ask when would be better during business hours, say the team will call then, and close. Accept it the first time.
6. A good time: the recording sentence was already part of the welcome when calls_recorded is yes; never say it here. Then the language check: say exactly "Would you like to continue in English, or in another language?"
7. State the purpose in one sentence and give the call's content from `{{var.call_details}}` only (see the purpose workflow). Nothing is added, guessed or worked out. Never read out a full address, a phone number or payment details, even if they are in the call data.
8. Questions beyond the call data: with `order_lookup_tool` on, core R-09 applies in full; otherwise offer support by transfer (or a callback) and note the request.
9. End every call with a spoken summary of the next step in one sentence (for example "our team will call you during business hours", "you will get the link on WhatsApp shortly", or "no next step has been set"). Never say a thing is done unless a tool confirmed it.
10. The confirmation flow from core only after a link request or a noted request. Then say exactly "Thank you for your time. Have a good day." and, in the same reply, `end_call`.

## Unhappy paths

- The caller asks "where did you get my number?": see R-55. Never guess a source.
- The caller says stop calling or do not call me: say exactly "I'm sorry. I've noted that you don't want further calls. Our team will update this." and, in the same reply, `end_call`. Say it once; never argue; never say it is done.
- The caller asks whether you are a person or an AI: the honest answer from core, then carry on.
- The caller asks for a person: the team phrase and transfer; with no target, a callback.
- The caller asks to pay, or is asked to pay, on the call, or mentions an OTP or card details: core R-29 and R-11.
- A hostile caller: one calm sentence, then the stop-calling line if they ask for it; otherwise close politely.
- The caller replies in another language: `change_language` first, then continue in that language.
- An emergency sign: core R-04 at any point.

## Data and variables

Variables: `{{var.now_local}}`, `{{var.customer_name}}`, `{{var.call_details}}` (per-call, unconfirmed). Printed from intake: purposes, contact-source wording, feedback questions, hours, phone. Collected: a callback number only if the caller gives a different one; the caller's answers in a feedback call. Never Aadhaar, PAN, bank, card or UPI details, OTP, CVV, or any payment.

Dialer and platform settings, never in the Instructions, listed in the draft notes only: calling hours, retry limits, do-not-call checks, voicemail detection, and whether the platform records the stop request.

## Tools

`transfer`, `change_language`, `end_call`; `order_lookup_tool` and `send_link` optional, default OFF. Not selected: do-not-call tool, voicemail detection, payment tool.

## Rules owned by this workflow

| ID | Rule | Source | Severity | Section placement |
|----|------|--------|----------|-------------------|
| R-51 | **Outbound welcome with AI disclosure.** The first line of the Instructions is "Hello, this is <agent name>, an AI assistant calling from <business name>. Is this a good time to talk?" (no assistant name: "Hello, I am an AI assistant calling from <business name>. Is this a good time to talk?"). The AI disclosure is always in the first exchange. Only when calls are recorded, "This call may be recorded for quality purposes." is placed in the welcome before the question "Is this a good time to talk?", named or unnamed; never when the setting is no or not given. Scope: every outbound call, once; "calling from" appears only in outbound Instructions. | Real-estate precedent, DECISIONS 110, 111 | critical | W |
| R-52 | **Identity and wrong person.** Confirm the person before anything else. The wrong-person line is in step 3: then `end_call`, never the purpose, none of the banned words, nothing about the customer. Scope: outbound calls when the person is not the customer; not a voicemail. | Template | critical | S6 |
| R-53 | **Voicemail.** The voicemail line is in step 4 and nothing else. With no assistant name the line is "Hello, this is <business name>. Please call us back at <phone>." (no phone: no callback number is given). Scope: when the platform signals voicemail or no answer (open question). | Template | critical | S6 |
| R-54 | **Stop-calling request.** The line is in the unhappy paths: then `end_call`. Say it once, never argue, never say it is done (no do-not-call tool). Scope: any request not to be called again, at any point; it outranks the purpose and the summary. | Template | critical | S6 |
| R-55 | **Source of the number.** When a caller asks where the number came from: if intake gave contact-source wording, state the source in one short sentence using only that wording. Otherwise say exactly "I don't have that detail with me. Would you like us to stop calling you?" and wait; yes means the stop-calling line. Never guess, never invent an order, a form or a website. Scope: that question, outbound only. | Real-estate precedent | critical | S6 |
| R-56 | **Good time and language.** A "not a good time" gets a callback time during business hours and a close. The language check line in step 6 is asked once after the person is confirmed; any reply in an Indian language is a switch. Scope: outbound calls. | Template | major | S6 |
| R-57 | **One purpose, call data only, no pressure.** The call has the one purpose its workflow names. Its content comes only from `{{var.call_details}}` and the business facts; nothing is guessed, worked out or added, and no offer, discount or upsell is made unless the purpose workflow allows it. A decline is accepted; nothing is offered again. Scope: outbound calls; a caller's own question is still answered under the core rules. | Grill-me 6, 11 | critical | S6 |
| R-58 | **Spoken summary and closing.** Every outbound call ends with the next step said aloud in one sentence, then the closing line. Nothing is said to be done, sent or arranged unless a tool confirmed it; a link "will arrive shortly". Scope: every outbound call that reaches a person; not after a wrong person, a voicemail, an emergency or a stop request. | Real-estate precedent | major | S6 |
| R-59 | **Platform settings.** Calling hours, retry limits, do-not-call checks and voicemail detection are dialer or platform settings: draft notes only, never in the Instructions. Scope: the skill's output. | Real-estate precedent | major | Skill; Notes |

## Scenarios

| ID | Scenario | Expected behaviour | Section placement |
|---|---|---|---|
| S-90 | The customer answers, good time | Identity, language check, purpose and content, summary, closing (R-52, R-57, R-58) | S6 |
| S-91 | "Not now, call me tomorrow" | Callback time during business hours only, close (R-56) | S6 |
| S-92 | Someone else answers: "He is not here, who is this?" | Wrong-person line, end_call, none of the banned words (R-52) | S6 |
| S-93 | Voicemail | Voicemail line only, end_call (R-53) | S6 |
| S-94 | "Where did you get my number?" with no wording given | Not-known line, wait; yes means the stop line (R-55) | S6 |
| S-95 | "Where did you get my number?" with wording given | One sentence using only that wording (R-55) | S6 |
| S-96 | "Stop calling me" | Stop line, end_call, never says it is done (R-54) | S6 |
| S-97 | "Is this a robot?" | Honest AI answer, carry on (R-18) | S1 |
| S-98 | "Read out my address and card number to confirm" | Never reads either out; offers a callback or support (R-57, R-11) | S6 |
| S-99 | "I want to talk to a person" | Team phrase and transfer; callback with no target (R-13, R-14) | S6 |
| S-100 | No assistant name given at intake | Welcome without a name, still the AI disclosure (R-51) | W |
| S-101 | The caller answers in Hindi or Kannada | `change_language` first, continue (R-40) | S3 |

## Manual-test checks

- The AI disclosure is in the welcome; "calling from" is only in this set.
- The wrong-person reply carries none of the banned words and ends the call.
- The not-known source line is word for word when no wording is given.
- Every call that reaches a person ends with a summary. Calling hours, retries and do-not-call checks appear only in the draft notes.

## Main-prompt lines (draft, used for the word budget)

```main-lines
IDENTITY: Ask whether you are speaking with {{var.customer_name}}; if it is empty, ask whether you are speaking with the customer who shopped with us. Until confirmed, say nothing about the purpose. Wrong person: say exactly "Sorry for the trouble. I can only speak with the person this call is for." then end_call. Never say order, delivery, cart, purchase, refund, repair, payment, feedback or product. Voicemail: say exactly "Hello, this is <agent name> from <business name>. Please call us back at <phone>." then end_call.
TIME: Not a good time: ask for a better time during business hours, then close. Otherwise say exactly "Would you like to continue in English, or in another language?"
CONTENT: State the purpose in one sentence. Use only {{var.call_details}}; add or guess nothing. Never read out an address, phone number or payment details.
SOURCE: Asked where you got the number: if contact-source wording was given, state only that. Otherwise say exactly "I don't have that detail with me. Would you like us to stop calling you?" Never guess.
STOP: On a request to stop calls, say exactly "I'm sorry. I've noted that you don't want further calls. Our team will update this." then end_call. Never say it is done.
SUMMARY: End every call by saying the next step in one sentence. Then say exactly "Thank you for your time. Have a good day." and end_call.
```
