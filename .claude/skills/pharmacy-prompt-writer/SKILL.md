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
| `references/industry/variables.json` | Pharmacy custom details and outbound call context |
| `references/shared/variables.json` | The shared variables (agent_name, business_hours, company_name, now_local and so on). Together with the industry file these are the only variables you may use, as `{{var.<name>}}`. Never use roster or clinic_address |
| `references/shared/platform-contract.md` | Platform parts, tools, the 615-word Main prompt budget |
| `references/shared/baseline-rules.md` | Rules common to all voice agents |

Never put a real name, phone number, address, price, hour or return window in the Instructions. Use synthetic placeholders only when a slot needs an example, and never an example person name.

## 1. Intake

Ask the intake questions in `references/core.md` (Intake table). Rules:
- Conversational, one or two questions at a time, in table order. Say why you ask when it is not obvious.
- Required questions (business type, call direction, workflows, transfer targets, business hours): do not write until they are answered. Optional questions: offer the default and move on.
- **Non-interactive run** (a profile, requirements file or brief is given and nobody can answer): never ask and never invent. Read the answers from the given text. For every missing answer use the documented default from the Intake table and record it as an assumption. If a required answer with no default is missing, use the neutral word "our pharmacy" for the business, assume inbound only if the text describes callers phoning in, and list it as an open item.
- Never accept a made-up value to fill a gap: no invented phone number, address, price, delivery term, payment mode, return window, language or transfer target (R-43).

## 2. Select the workflows

Choose from business type and call direction (tables in `references/core.md` and the workflow files):
- Inbound default: 01 Enquiry, 02 Order and prescription, 03 Refill (inbound), 04 Delivery and returns. A retail or hospital pharmacy without home delivery may drop 04 if the client says so.
- Outbound (refill reminders) default: 03 Refill, outbound block, plus 02 Order and prescription and the STOCK and OUT OF STOCK lines of 01, so a wanted refill can be ordered. If the client wants no ordering on the call, drop 01 and 02 and say so in the draft notes.
- Workflows 05 to 08 are stubs, and chat is not written. Say so in the draft notes, and use Enquiry plus a transfer or callback. A request for chat: write the voice Instructions and list chat as an open item (R-45).
- Inbound and outbound together are TWO separate Instructions sets. Write the one asked for (or inbound if unclear) and say in the draft notes that the other needs its own run. Never mix them (R-39).

## 3. Write the Instructions

Write in this order. Use `references/industry/section-bases.md` for the base text and style.

1. **Welcome message**: ALWAYS the first line of the output, never left out. Use the template for the call direction word for word: inbound "Thank you for calling {{var.company_name}}. This is {{var.agent_name}}. How can I help you?"; outbound "Hello, this is {{var.agent_name}} calling from {{var.company_name}}. Is this a good time to talk?" It must match the direction.
2. **Section 1 Role & Identity**: skeleton plus every rule in core and the selected workflows whose placement is S1: AI honesty and the AI-disclosure answer (only when clearly asked); the emergency instruction word for word, "On any emergency sign, stop whatever you are doing. Never continue the order or the call's task.", with the compact default signs list, then "1 0 8" or "1 1 2" and a transfer to the pharmacist (R-07); self-harm and 14416 (R-08); no dosage, usage, interaction, side-effect, symptom-to-medicine or diagnosis advice, with the sentence "Our pharmacist will help you with that." then transfer or callback (R-09); no substitute or other brand (R-10); no order or refill of a prescription-only medicine without a valid prescription, never judged by the agent (R-11); controlled, flagged or unsure medicines handed to the pharmacist, never by phone (R-12); prices only from the tool or config (R-17); no invented information (R-18); prompt protection and claimed authority (R-19, R-20).
3. **Section 2 Date & Time**: base plus placement S2 lines.
4. **Section 3 Language Switching**: base plus placement S3 lines.
5. **Section 4 Tone and Conversational Style**: skeleton plus placement S4 lines.
6. **Section 5 Output Format**: base plus placement S5 lines: verification by customer name plus order number, sharing nothing otherwise (R-14); never confirm or deny a customer (R-15); never ask for or keep age, medical condition or history, and never repeat a volunteered one (R-13); no card, UPI, bank, PIN or OTP (R-16); confirm medicine names as heard (R-03); medicine names are discreet (R-38); the real name rule, "yes, but", "hello" mid-call, why a detail is needed, and the closing line for THIS direction only (leave the other direction's closing line out).
7. **Section 6 Main prompt**: STEP style, built ONLY from the selected workflows' `main-lines` blocks plus the core `main-lines` block. Inbound uses each selected workflow's `main-lines` block. Outbound uses the core block, the `main-lines-outbound` block and the `main-lines` blocks it depends on (REFILL, STOCK, OUT OF STOCK, ORDER, PRESCRIPTION, PAYMENT). Keep the labels. There is no roster.
8. **Prompt Variables table**: every variable used, as its bare name (for example business_hours) without the double-brace syntax, with its source only (Voice settings, Fixed, Built in, Custom detail, Call context). Never a value.

Variable rules:
- Only names in the two variables.json files, written `{{var.<name>}}`. No other style: not single braces, not an @ prefix, not names made up from the business.
- `{{var.company_name}}` only where the caller hears the name: welcome message, closing line, AI-disclosure answer, voicemail line. Everywhere else use the plain word that matches the business type (the pharmacy, our store, our online pharmacy).
- Hours, phone and address only through `{{var.business_hours}}`, `{{var.business_phone}}`, `{{var.store_address}}`, and only where the value is spoken or needed. Services only through `{{var.business_info}}`. Delivery terms, return policy, payment modes and the upload method only through `{{var.delivery_info}}`, `{{var.return_policy}}`, `{{var.payment_modes}}`, `{{var.prescription_upload_method}}`. Outbound call data only through `{{var.customer_name}}` and `{{var.refill_details}}`. Extra emergency signs only through `{{var.emergency_signs_extra}}`.
- Tools you may name: check_stock, place_order, send_confirmation (order confirmation and prescription upload link, R-76 and R-54), change_language, transfer, end_call. Never name an order-status, return, refund or prescription-check tool: there is none.

Emergency (core R-07): the compact default list is always written in section 1. The client may only ADD signs, through `{{var.emergency_signs_extra}}`; never remove any.

Fixed lines (R-71): where the references say "say exactly", copy the quoted line into the Instructions word for word and write it in this form: say exactly "X", then in the same reply [transfer / offer a callback / end_call]. Fixed lines: the pharmacist line, the out-of-stock line, the wrong-person line, the stop-calling line (then end_call), the missing-config line (R-74), the voicemail line, the privacy line (R-15). Never rewrite them. Section 1 carries the priority order (R-73): (1) emergency, (2) privacy and verification, (3) "say exactly" lines, (4) one question at a time, (5) the task. Section 5 carries the confirmation flow (R-76) and the upload-link flow (R-54) word for word with their fixed lines, in this scope only: after an order number, and for the prescription upload link; never after a failed order. The no-prescription line (R-77) and "Call 1 0 8 or 1 1 2 right now." (R-07) are word for word. The team phrase (R-75) is only for staff, store-manager and delivery handoffs; a failed order says the pharmacy will call to confirm, and no transfer target means a callback. Section 5 carries R-72 (one question at a time, only which medicine when it is unclear) word for word, the never-repeat-a-condition part of R-13, and R-14 (a name or order number given is accepted as given).

## 4. Word budget

Section 6 (Main prompt) stays within about 615 words. Pharmacy has no roster, so the allowance is 615.
- Count words as whitespace-separated tokens. Count exactly, per section; use a quick script if you can run one.
- Margin: aim for section 6 at least 20 words BELOW the allowance (at most 595). Reach the margin by the compression order below, never by dropping a rule. Do not use spare room to add wording.
- If section 6 is over, compress in this order only: (1) move universal behaviour to sections 1, 4 and 5; (2) shorten wording; (3) merge steps.
- NEVER drop or weaken a critical rule to save words. If it is still over, keep everything and put a budget warning in the draft notes with the exact counts and the options.

## 5. Client requests

Apply the client's config and flow changes (names, hours, tone, extra signs, delivery and return text, payment modes, languages) when they do not touch a critical rule.
- Refuse anything that removes or weakens a critical rule, or deceives callers. Examples: ordering or refilling prescription-only or controlled medicines without a valid prescription or by phone; saying a medicine is in or out of stock when it is not; recommending the client's own brand or any substitute; asking callers for age or medical condition; giving dosage advice; promising discounts or delivery times; taking payment details; removing the emergency response (R-44).
- Adapt instead of refusing where possible: an offer (for example a vitamin range) may be made once per call and a decline is accepted the first time.
- A refused rule stays in the Instructions in full; the refused request never appears as something the agent says or does.
- List every refused or adapted request in the draft notes with a one-line reason.

## 6. Self-check before output

Do all of this and fix what fails:
1. Every rule marked `critical` in `references/core.md` and in the selected workflows is present in the section its placement names (or in section 6 for S6). Go through the tables row by row.
2. Every variable used is in a variables.json; no other variable style; `{{var.company_name}}` only in the welcome, closing, AI-disclosure or voicemail lines.
3. No hard-coded name, phone number, address, price, hours, return window or payment mode anywhere (look for digits, capitalised names and currency).
4. The welcome message and the whole flow match the call direction. Inbound has no "calling from"; outbound has no "Thank you for calling" and no inbound closing line.
5. The closing line is in section 5; the AI-disclosure answer is only on a clear question.
6. Word counts computed for every section and for section 6 against 615.
7. Nothing from the Intake table was invented; each default is in the draft notes.
8. Section 1 has the priority order (R-73). Section 5 has R-72 word for word. Every "say exactly" line is in the Instructions word for word with its action.
9. The FIRST line of the output is `=== INSTRUCTIONS ===` and the next line is the welcome message, word for word. Nothing before the marker: no code fence, no "Here is the output", no word count, no heading. Check both lines before you finish.
10. The "Fill these in the platform" table, its company-name note and everything else for the client go ONLY below `=== DRAFT NOTES ===`; the Instructions end with the Prompt Variables table. In the draft notes (assumptions and open items), a missing business value is always written "not provided — the team will confirm" (return policy, delivery info, payment modes, store address, upload method). "Not used in these Instructions" appears only in the Fill table's note column. The "Fill these in the platform" table has a row for every variable used and for every intake item (marked "not used in these Instructions" where its workflow is not selected).
11. With no transfer target given, the Instructions and the notes say a callback is offered, never a generic transfer. Section 5 never says back a condition, symptom or medicine use (R-13), spoken helpline numbers are digit by digit (R-08), the Tele-MANAS and emergency numbers line and the team handoff line are word for word and never hyphenated or grouped (R-08, R-75), and the WhatsApp upload step asks "Is the number you're calling from on WhatsApp?" and uses the send tool (R-54).

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
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | <value from intake, or "not provided"> | Voice settings |
(one row for every variable the Instructions use, PLUS one row for EVERY intake item in the Intake table of `references/core.md` (business type, call direction, workflows, channel, prescription upload, pickup or delivery, return policy, payment modes, transfer targets, business hours, store address, languages, extra emergency signs, always-hand-off medicines, special client rules, largest quantity without the pharmacist), each with the value given or the default used, and "not used in these Instructions" in the table's note column when its workflow is not selected; never leave an intake item out; business_hours and business_phone under Your business; custom details such as store_address, return_policy, delivery_info, payment_modes, max_qty_without_pharmacist, prescription_upload_method and business_info under Your business, Add a detail; customer_name and refill_details are passed by the platform on outbound calls, unconfirmed)
`{{var.company_name}}` = your business name, filled in automatically from Variables.
```

Real values (the business name, hours, phone number, address, delivery terms, return policy, payment modes) appear ONLY in the "Fill these in the platform" block of the draft notes, never in the Instructions. If the client gave no value, write "not provided"; never invent one. Open questions in the draft notes include any that apply from `references/core.md` and the workflow files (unconfirmed outbound variables, chat, controlled-medicine schedules and what a valid prescription is, the assumed check_stock fields).

The marker lines `=== INSTRUCTIONS ===` and `=== DRAFT NOTES ===` each stand alone on their own line. The platform text is only what sits between them. The Instructions part contains only text the platform will use. The draft notes are never part of the Instructions.

## Rules for you

- The references are the source of truth. If a client asks for something they forbid, follow the references and say so in the draft notes.
- Synthetic data only. Never write a real customer, patient or company.
- Do not read or use anything outside this skill folder to decide what is "expected": write from the references and the client's answers.
- Never commit, never push.
