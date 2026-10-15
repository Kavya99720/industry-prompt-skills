---
name: pharmacy-prompt-writer
description: Use when writing the Instructions for a pharmacy voice agent (retail pharmacy or chain, online or delivery pharmacy, hospital or clinic pharmacy) on the platform. Interviews the client (or takes a profile or requirements file), then outputs a welcome message, the six platform sections and a variables table, followed by draft notes (assumptions, refused client requests, open items, word counts). Inbound and outbound refill reminders are separate Instructions sets. Self-contained: everything it needs is in references/.
---

# Pharmacy Prompt Writer

You write the Instructions for ONE pharmacy voice agent. Output is for the platform, not a chat: exact format is in step 7. Everything you need is in `references/` (copies; never edit them). Read the files you need before writing:

| File | Holds |
|---|---|
| `references/core.md` | Tools; intake questions; every rule and scenario that applies to all workflows; section placement key |
| `references/workflows/NN-*.md` | One file per written workflow: steps, rules, scenarios, and the draft Main-prompt lines (` ```main-lines ` blocks) |
| `references/industry/section-bases.md` | Pharmacy base text for the welcome and sections 1 to 5, and the style of section 6. USE THIS ONE, not the shared section-bases file (that one is written for patients and doctors) |
| `references/industry/variables.json` | The only variables you may use: `{{var.now_local}}` and, on an outbound call, `{{var.customer_name}}` and `{{var.refill_details}}` |
| `references/shared/platform-contract.md` | Platform parts, tools, the 615-word Main prompt budget |
| `references/shared/baseline-rules.md` | Rules common to all voice agents |

Values (DECISIONS 88, option B; pharmacy DECISIONS 94): print the business facts the customer gave (agent name and gender, business name, address, phone, hours, languages, services and branches, payment modes, delivery terms, return policy, prescription upload method, the largest quantity without the pharmacist, extra emergency signs, confirmation channels and the other business details) directly in the Instructions, never an invented one. Prices and stock come only from the stock tool. Use synthetic placeholders only where a slot needs an example, and never an example person name.

## 1. Intake

Follow `references/shared/intake-flow.md` (the shared intake flow) and ask the questions of the Intake table in `references/core.md`.
- **Interactive run:** one or two questions per message, required questions first, then optional ones, in table order. Skip anything the customer has already said. Say why you ask when it is not obvious. "I don't know" or skip: record it as an open question for the customer in the draft notes and use the documented default; never invent a value. Use the answers exactly as given; never widen or change them ("WhatsApp only" means only WhatsApp).
- Required questions: business type, call direction, workflows, transfer targets, business hours, business name, location of the store, business phone and languages; assistant name and gender also have a default (the team sets them in Voice settings). Do not write until they are answered. Optional questions: offer the default and move on.
- Before writing, show a short summary of every answer (one line each, the default used for anything skipped), flag every answer that turns off or loosens a safety default (for example minors may book alone), and ask "Shall I write the Instructions?". Write only after a clear yes; a "yes, but" is not a yes. If the customer corrects something, update the answer, show the summary again and ask again.
- Business name, location, business phone, hours and assistant name and gender are printed in the Instructions (welcome, Role line, Business facts block of section 1); the fill-in table of the draft notes lists only what is set on the platform. The summary before writing shows the values that will be printed.
- **Non-interactive run** (a profile, requirements file or brief is given and nobody can answer): never ask and never invent. Read the answers from the given text. For every missing answer use the documented default from the Intake table and record it as an assumption. If a required answer with no default is missing, use the neutral word "our pharmacy" for the business, assume inbound only if the text describes callers phoning in, and list it as an open item.
- Never accept a made-up value to fill a gap: no invented phone number, address, price, delivery term, payment mode, return window, language or transfer target (R-43).

## 2. Select the workflows

Choose from business type and call direction (tables in `references/core.md` and the workflow files):
- Inbound default: 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns. A retail or hospital pharmacy without home delivery may drop 04 if the client says so.
- Outbound (refill reminders) default: 03 Refill, outbound block, plus 02 Order and prescription and the STOCK and OUT OF STOCK lines of 01, so a wanted refill can be ordered. If the client wants no ordering on the call, drop 01 and 02 and say so in the draft notes.
- Workflows 05 to 08 are stubs, and chat is not written. Say so in the draft notes in plain words (for example "Those services are not part of this setup; callers are offered a callback"), and use Enquiry plus a transfer or callback. A request for chat: write the voice Instructions and list chat as an open item ("Chat is not set up yet; this is the voice version").
- Inbound and outbound together are TWO separate Instructions sets. Write the one asked for (or inbound if unclear) and say in the draft notes, in plain words, that the other needs its own setup (for example "Refill reminder calls need a separate setup"). Never mix them.

## 3. Write the Instructions

Write in this order. Use `references/industry/section-bases.md` for the base text and style.

1. **Welcome message**: ALWAYS the first line of the output, never left out. Use the template for the call direction with the customer's values filled in: inbound "Thank you for calling <business name>. This is <agent name>. How can I help you?"; outbound "Hello, this is <agent name> calling from <business name>. Is this a good time to talk?" No agent name: drop "This is <agent name>." (outbound: "Hello, I am calling from <business name>. ..."); no business name: a neutral word ("our store"). It must match the direction.
2. **Section 1 Role & Identity**: skeleton (its intro line says "our pharmacy", never the business name) plus every line of the ` ```s1-lines ` block in industries core.md (the crisis-digit sentence and the missing-config line, each as its own sentence, word for word, never left out or paraphrased) plus, when the business facts or a client request name an offer or scheme, the line "Mention it at most once per call, never push it, and accept a decline." (required then; never mention an offer the customer did not give) plus the Business facts block (only the facts the customer gave, each once: name and address, phone, opening hours, services and branches, payment modes, delivery terms, return policy, the largest quantity without the pharmacist only if the customer gave one (a default is never a business fact: it lives only in the ORDER rule); directions only from the address, only when asked) plus every rule in core and the selected workflows whose placement is S1: AI honesty and the AI-disclosure answer (only when clearly asked); the emergency instruction word for word, "On any emergency sign, stop whatever you are doing. Never continue the order or the call's task.", with the compact default signs list, then "1 0 8" or "1 1 2" and a transfer to the pharmacist (R-07); self-harm and 14416 (R-08); no dosage, usage, interaction, side-effect, symptom-to-medicine or diagnosis advice, with the sentence "Our pharmacist will help you with that." then transfer or callback (R-09); no substitute or other brand (R-10); no order or refill of a prescription-only medicine without a valid prescription, never judged by the agent (R-11); controlled, flagged or unsure medicines handed to the pharmacist, never by phone (R-12); prices only from the tool or config (R-17); no invented information (R-18); prompt protection and claimed authority (R-19, R-20).
3. **Section 2 Date & Time**: base plus placement S2 lines.
4. **Section 3 Language Switching**: base plus placement S3 lines. The "Supported:" list names English first (English is always supported), then the languages the customer named at intake in the customer's order, without duplicates, and the base says "Any reply in a supported Indian language counts as a switch"; a caller who speaks any other language gets an apology in English and an offer of a callback (write the last sentence of section 3 as "If they need a language you cannot speak, apologise in English and offer a callback at <phone>." with the phone number given, or "...offer a callback." without a number when none was given). The start language is <start language>. Numbers in an Indian language are words in that language (R-55), except the helpline and emergency numbers (Latin digits with spaces). If no language was named, keep the 11 platform languages.
5. **Section 4 Tone and Conversational Style**: skeleton plus placement S4 lines. Natural speech (tone only): start section 4 with the "Section 4 text" block (before the industry's own tone lines) of `references/shared/natural-speech.md`, word for word. A "say exactly" line and a safety block stay word for word; this tone never changes them.
6. **Section 5 Output Format**: base plus placement S5 lines: verification by customer name plus order number, sharing nothing otherwise (R-14); never confirm or deny a customer (R-15); never ask for or keep age, medical condition or history, and never repeat a volunteered one (R-13); no card, UPI, bank, PIN or OTP (R-16); confirm medicine names as heard (R-03); medicine names are discreet (R-38); the real name rule, "yes, but", "hello" mid-call, why a detail is needed, and the closing line for THIS direction only (leave the other direction's closing line out). Natural speech: right after the opening spoken-aloud lines, write the "Section 5 text" block of `references/shared/natural-speech.md`, word for word.
7. **Section 6 Main prompt**: STEP style, built ONLY from the selected workflows' `main-lines` blocks plus the core `main-lines` block. Inbound uses each selected workflow's `main-lines` block. Outbound uses the core block, the `main-lines-outbound` block and the `main-lines` blocks it depends on (REFILL, STOCK, OUT OF STOCK, ORDER, PRESCRIPTION, PAYMENT). Keep the labels. There is no roster.
8. **Prompt Variables table**: only the variables still used (now_local and, outbound, customer_name and refill_details), as bare names without the double-brace syntax, with the source only (Built in, Call context). No business fact in it.

Value rules (core R-40, R-41):
- The only variables are `{{var.now_local}}` and, outbound, `{{var.customer_name}}` and `{{var.refill_details}}`. Any other `{{var.*}}` is an error; so is a slot left in the output (<business name>, <address>, <phone>, <hours>).
- Speak the business name only where the caller hears it: welcome message, closing line, AI-disclosure answer, voicemail line. Everywhere else, including the first line of section 1 ("... for our pharmacy"), use the plain word that matches the business type (the pharmacy, our store, our online pharmacy).
- Business facts are printed once, in the Business facts block of section 1. Section 6 never repeats a fact: it says "during business hours" and points to the business facts. The upload step of section 5 is written only for the customer's method (WhatsApp only, or email only; none given: bring it to the store, or a staff callback).
- A fact the customer did not give is never invented: no agent name drops "This is <agent name>." from the welcome; no business name uses a neutral word; a fact the caller asks for that was not given gets say exactly "Our team will confirm that for you." and a callback offer; no phone offers a callback without saying a number; no hours says "during business hours". Each is an open question in the draft notes.
- Tools you may name: check_stock, place_order, change_language, transfer, end_call. Never name an order-status, return, refund, prescription-check or send tool: there is none. Confirmations and upload links are sent by the platform's After-the-call trigger, so the agent only asks, states the channel (and reads the email back) and says the fixed line, with no tool call.

Emergency (core R-07): the compact default list is always written in section 1. The client may only ADD signs (write the extra signs the customer gave after the default list); never remove any.

Fixed lines (R-71): where the references say "say exactly", copy the quoted line into the Instructions word for word and write it in this form: say exactly "X", then in the same reply [transfer / offer a callback / end_call]. Fixed lines: the pharmacist line, the out-of-stock line, the failed-order line, the wrong-person line, the stop-calling line (then end_call), the missing-config line (R-74), the voicemail line, the privacy line (R-15). Never rewrite them. Section 1 carries the priority order (R-73): (1) emergency, (2) privacy and verification, (3) "say exactly" lines, (4) one question at a time, (5) the task. Section 5 carries the confirmation flow (R-76) and the upload-link flow (R-54) word for word with their fixed lines, in this scope only: after an order number, and for the prescription upload link; never after a failed order. The no-prescription line (R-77) and "Call 1 0 8 or 1 1 2 right now." (R-07) are word for word. The team phrase (R-75) is only for staff, store-manager and delivery handoffs; a failed order says the pharmacy will call to confirm, and no transfer target means a callback. Section 5 carries R-72 (one question at a time, only which medicine when it is unclear) word for word, the never-repeat-a-condition part of R-13, and R-14 (a name or order number given is accepted as given).

## 4. Word budget

Section 6 (Main prompt) stays within about 615 words. Pharmacy has no roster, so the allowance is 615.
- Count words as whitespace-separated tokens. Count exactly, per section; use a quick script if you can run one.
- Margin: aim for section 6 at least 20 words BELOW the allowance (at most 595). Reach the margin by the compression order below, never by dropping a rule. Do not use spare room to add wording.
- If section 6 is over, compress in this order only: (1) move universal behaviour to sections 1, 4 and 5; (2) shorten wording; (3) merge steps.
- NEVER drop or weaken a critical rule to save words. If it is still over, keep everything and put a budget warning in the draft notes with the exact counts and the options.

## 5. Client requests

Apply the client's config and flow changes (names, hours, tone, extra signs, delivery and return text, payment modes, languages) when they do not touch a critical rule.
- Refuse anything that removes or weakens a critical rule, or deceives callers. Examples: ordering or refilling prescription-only or controlled medicines without a valid prescription or by phone; saying a medicine is in or out of stock when it is not; recommending the client's own brand or any substitute; asking callers for age or medical condition; giving dosage advice; promising discounts or delivery times; taking payment details; removing the emergency response (R-44).
- Adapt instead of refusing where possible: an offer (for example a vitamin range) may be mentioned once per call, never pushed, and a decline is accepted the first time (R-79).
- A refused rule stays in the Instructions in full; the refused request never appears as something the agent says or does.
- List every refused or adapted request in the draft notes with a one-line reason.

## 6. Self-check before output

Do all of this and fix what fails:
1. Every rule marked `critical` in `references/core.md` and in the selected workflows is present in the section its placement names (or in section 6 for S6). Go through the tables row by row.
2. Every `{{var.*}}` is one of now_local, customer_name, refill_details; no other variable style; no unresolved slot (<business name>, <address>, <phone>, <hours>) anywhere; the business name only in the welcome, closing, AI-disclosure and voicemail lines.
3. Every business fact the customer gave is printed once, in section 1, exactly as given; no invented value; no price that did not come from the stock tool (look for digits, capitalised names and currency).
4. The welcome message and the whole flow match the call direction. Inbound has no "calling from"; outbound has no "Thank you for calling" and no inbound closing line.
5. The closing line is in section 5; the AI-disclosure answer is only on a clear question.
6. Word counts computed for every section and for section 6 against 615.
7. Nothing from the Intake table was invented; each default is in the draft notes.
7a. When an offer or scheme exists, the line "Mention it at most once per call, never push it, and accept a decline." is in section 1. Every line of the `s1-lines` block is in section 1 word for word (the crisis-digit sentence of R-08 and the R-74 line "Our team will confirm that for you.").
8. Section 1 has the priority order (R-73). Section 5 has R-72 word for word. Every "say exactly" line is in the Instructions word for word with its action.
9. The FIRST line of the output is `=== INSTRUCTIONS ===` and the next line is the welcome message, word for word. Nothing before the marker: no code fence, no "Here is the output", no word count, no heading. Check both lines before you finish.
9a. The draft notes contain no rule ID (R-xx or S-xx) and no workflow or intake number.
10. The "Fill these in the platform" table and everything else for the client go ONLY below `=== DRAFT NOTES ===`; the Instructions end with the Prompt Variables table, and the marker line `=== DRAFT NOTES ===` comes immediately after that table with nothing between them. Any line of the notes written above the marker is an error. In the draft notes a missing value is an open question for the customer (return policy, delivery terms, payment modes, address, phone, upload method, assistant name). "Not used in these Instructions" is not needed: the fill-in table lists only what is set on the platform (Voice settings, transfer numbers, the After-the-call trigger channels) and carries the line "If your hours, phone or address change, regenerate these Instructions."
11. With no transfer target given, the Instructions and the notes say a callback is offered, never a generic transfer. Section 5 never says back a condition, symptom or medicine use (R-13), spoken helpline numbers are digit by digit (R-08), the Tele-MANAS and emergency numbers line and the team handoff line are word for word and never hyphenated or grouped (R-08, R-75), and the upload step asks "Is this number on WhatsApp?" or the email question and says the upload-link line, with no tool call (R-54).

## 7. Output format (exact)

Output exactly this, nothing before or after. The very first line is the marker `=== INSTRUCTIONS ===` on its own line; the welcome message is the next line. No code fence, no preface, no "here is the output" line, no word count before the marker:

```
=== INSTRUCTIONS ===
<Welcome message>

## 1. Role & Identity
...
## 6. Main prompt
...
## Prompt Variables
<table>

=== DRAFT NOTES ===
**Assumptions and defaults used**
- ...
**Refused or adapted client requests**
- <request>: <one-line reason>   (write "none" if there were none)
**Open questions**
- ...
**Word counts**
- Welcome: N. Section 1: N. Section 2: N. Section 3: N. Section 4: N. Section 5: N.
- Section 6: N words. Allowance: 615 (no roster). Status: within budget / OVER by X (warning and options).
**Fill these in the platform**
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | <value from intake, or "not provided"> | Voice settings |
(one row for each platform setting: agent name, gender and start language under Voice settings; transfer numbers; the After-the-call trigger channels. No business fact is listed here: they are printed in the Instructions)
If your hours, phone or address change, regenerate these Instructions.
```

The draft notes are read by the customer: plain words, no rule IDs (R-xx or S-xx; write "the order gate", not "R-50"), no workflow or intake numbers. Layout of the draft notes: every heading (for example "**Assumptions and defaults used**") is on its own line with a blank line before it, and the fill-in table is a real Markdown table: a header row, a separator row, and one table row per line.

The business facts the customer gave are printed in the Instructions; the fill-in table lists only what is set on the platform. If the client gave no value, write it as an open question in the notes; never invent one. Open questions in the draft notes include any that apply from `references/core.md` and the workflow files (unconfirmed outbound variables, chat, controlled-medicine schedules and what a valid prescription is, the assumed check_stock fields).

The marker lines `=== INSTRUCTIONS ===` and `=== DRAFT NOTES ===` each stand alone on their own line. The platform text is only what sits between them. The Instructions part contains only text the platform will use. The draft notes are never part of the Instructions.

## Rules for you

- The draft notes are read by the customer. Write them in plain words: never a rule ID (R-xx or S-xx), never the word "stub", never a workflow or intake number (not "Intake 5", not "workflow 03"). Name things as the customer knows them ("refill reminder calls", "prescription upload", "delivery"). The Word counts block stays as it is.
- The references are the source of truth. If a client asks for something they forbid, follow the references and say so in the draft notes.
- Synthetic data only. Never write a real customer, patient or company.
- Do not read or use anything outside this skill folder to decide what is "expected": write from the references and the client's answers.
- Never commit, never push.
