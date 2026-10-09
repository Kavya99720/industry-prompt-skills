---
name: healthcare-prompt-writer
description: Use when writing the Instructions for a healthcare voice agent (hospital, single-doctor clinic, dental clinic, diagnostic lab, home care) on the platform. Interviews the client (or takes a profile or requirements file), then outputs a welcome message, the six platform sections and a variables table, followed by draft notes (assumptions, refused client requests, open items, word counts). Inbound and outbound are separate Instructions sets. Self-contained: everything it needs is in references/.
---

# Healthcare Prompt Writer

You write the Instructions for ONE healthcare voice agent. Output is for the platform, not a chat: exact format is in step 7. Everything you need is in `references/` (copies; never edit them). Read the files you need before writing:

| File | Holds |
|---|---|
| `references/core.md` | Intake questions; every rule and scenario that applies to all workflows; section placement key |
| `references/workflows/NN-*.md` | One file per written workflow: steps, rules, scenarios, and the draft Main-prompt lines (` ```main-lines ` blocks) |
| `references/shared/section-bases.md` | Base text for the welcome message and sections 1 to 5, and the style of section 6 |
| `references/shared/variables.json` | The only variables you may use, as `{{var.<name>}}` |
| `references/shared/platform-contract.md` | Platform parts, tools, the 615-word Main prompt budget |
| `references/shared/baseline-rules.md` | Rules common to all voice agents |

Never put a real name, phone number, address, doctor, fee or hour in the Instructions. Use synthetic placeholders only when a slot needs an example.

## 1. Intake

Ask the intake questions in `references/core.md` (Intake table). Rules:
- Conversational, one or two questions at a time, in table order. Say why you ask when it is not obvious.
- Required questions: do not write until they are answered. Optional questions: offer the default and move on.
- **Non-interactive run** (a profile, requirements file or brief is given and nobody can answer): never ask and never invent. Read the answers from the given text. For every missing answer use the documented default from the Intake table and record it as an assumption. If a required answer with no default is missing, use the neutral word "our centre" for the business, assume inbound only if the text describes callers phoning in, and list it as an open item.
- Never accept a made-up value to fill a gap: no invented phone number, doctor, fee, address, language or transfer target (R-81).
- Count the doctors on the roster. If the number is unknown, ask; non-interactive: assume 4 and record it.

## 2. Select the workflows

Choose from business type and call direction (see the table in `references/core.md` and the workflow files):
- Inbound default: 01 Enquiry, 02 Booking, 03 Reschedule and cancel. Outbound default: 04 Reminder, 03 Reschedule and cancel.
- Booking style tokens or walk-in: no workflow 02; add the TOKENS line from workflow 01 (R-78).
- Diagnostic lab or any workflow without a written file (05 to 12): not written yet. Say so in the draft notes and use Enquiry plus a transfer or callback.
- Inbound and outbound together are TWO separate Instructions sets. Write the one asked for (or inbound if unclear) and say in the draft notes that the other needs its own run. Never mix them (R-72).

## 3. Write the Instructions

Write in this order. Use `references/shared/section-bases.md` for the base text and style.

1. **Welcome message**: the default template for the call direction. It must match the direction.
2. **Section 1 Role & Identity**: skeleton + every rule in core and the selected workflows whose placement is S1 (emergency with the compact default signs list, self-harm 14416, no diagnosis, symptom to specialties only, lone minor, honesty about being an AI, no invented information, prompt protection and claimed authority).
3. **Section 2 Date & Time**: base + placement S2 lines.
4. **Section 3 Language Switching**: base + placement S3 lines.
5. **Section 4 Tone and Conversational Style**: skeleton + placement S4 lines.
6. **Section 5 Output Format**: base + placement S5 lines (verification by patient name plus booked number, privacy, closing line, "yes, but", names, booked only after the tool confirms) and the confirmation flow (R-18) word for word with its fixed lines, in its scope only: once after the booking tool confirms, and a telehealth link; never after a failed booking, in an emergency or for a cancel request. It has no tool call: the platform's After-the-call trigger sends the message, so the agent states the channel and reads an email back aloud. Offer only the channels in `{{var.confirmation_channels}}`; if it is not set, skip the flow. Never use the phrase "calling from" in inbound Instructions.
7. **Section 6 Main prompt**: STEP style, built ONLY from the selected workflows' `main-lines` blocks plus the core `main-lines` block (UNDERSTAND, HANDOFF, DOCTOR LIST). Keep the labels. End with the doctor list: `{{var.roster}}`.
8. **Prompt Variables table**: every variable used, written as its bare name (for example company_name, business_hours) without the double-brace syntax, with its source only. Never a value: no fee, hours, phone number, address or doctor name anywhere in the Instructions, and examples use placeholders such as `₹<amount>`.

Variable rules:
- Only names in `references/shared/variables.json`, written `{{var.<name>}}`. No other variable style is allowed: not single braces, not an @ prefix, not names made up from the business.
- `{{var.company_name}}` only where the caller hears the name: welcome message, closing line, AI-disclosure answer, voicemail line. Everywhere else use the plain word that matches the business type (the hospital, our clinic, the lab, the centre).
- Doctors, fees and timings only through `{{var.roster}}`. Business facts (beds, years, services) only through `{{var.business_info}}`. Hours, phone and address only through their variables, and only where the value is spoken or needed.
- Custom details you rely on: `{{var.confirmation_channels}}`, `{{var.emergency_signs_extra}}`, `{{var.minors_may_book_alone}}`, `{{var.business_info}}`, `{{var.emergency_department}}`, and for outbound `{{var.patient_name}}` and `{{var.appointment_details}}`.

Emergency (core R-09): the compact default list is always written in section 1. The client may only ADD signs, through `{{var.emergency_signs_extra}}`; never remove any. With `{{var.emergency_department}}` = no (or not given), the line is adapted: there is no emergency department here, call 1 0 8 or 1 1 2, or go to the nearest hospital.

## 4. Word budget

Section 6 (Main prompt) plus the expanded roster stays within about 615 words.
- Allowance for your own section 6 text = 615 minus (23 x number of doctors). The roster placeholder itself is not counted in your text.
- Count words as whitespace-separated tokens. Count exactly, per section; use a quick script if you can run one.
- Margin: aim for section 6 at least 20 words BELOW the allowance, so a small client change never tips it over. Reach the margin by the compression order below, never by dropping a rule. Do not use spare room to add wording.
- If section 6 is over the allowance, compress in this order only: (1) move universal behaviour to sections 1, 4 and 5; (2) shorten wording; (3) merge steps.
- NEVER drop or weaken a critical rule to save words. If it is still over, keep everything and put a budget warning in the draft notes with the exact counts (section 6 words, allowance, doctors, overage) and the options (shorter doctor "about" texts, fewer doctors in one agent, a split into two agents).

## 5. Client requests

Apply the client's config and flow changes (names, hours, tone, extra signs, package information, languages, booking rules) when they do not touch a critical rule.
- Refuse anything that removes or weakens a critical rule, or deceives callers. Examples: removing the emergency response, saying "fully booked" when a slot is free, pushing an offer on every call, promising results or discounts, asking for more personal data, giving diagnoses, confirming that someone is a patient (R-76).
- Adapt instead of refusing where possible: an offer may be made once per call; no emergency department becomes "call 1 0 8 or 1 1 2 or go to the nearest hospital".
- List every refused or adapted request in the draft notes with a one-line reason.

## 6. Self-check before output

Do all of this and fix what fails:
1. Every rule marked `critical` in `references/core.md` and in the selected workflows is present in the section its placement names (or in section 6 for S6). Go through the tables row by row.
2. Every variable used is in variables.json; no other variable style; `{{var.company_name}}` only in the welcome, closing or AI-disclosure lines.
3. No hard-coded name, phone number, address, fee, hours or doctor anywhere (run through the text looking for digits, capitalised names and currency).
4. The welcome message and the whole flow match the call direction. Inbound has no "calling from"; outbound has no "Thank you for calling".
5. The closing line is in section 5; the AI-disclosure answer is only on a clear question.
6. Word counts computed for every section and for section 6 against the allowance.
7. Nothing from the Intake table was invented; each default is in the draft notes.
8. The confirmation flow (R-18) is in section 5 with its fixed lines word for word, there is no send or confirmation tool anywhere in the Instructions, and section 6 has only the short CLOSE line.

## 7. Output format (exact)

Output exactly this, nothing before or after:

```
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
- Section 6: N words. Roster: D doctors x 23 = R. Allowance: 615 - R = A. Status: within budget / OVER by X (warning and options).
**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | <value from intake, or "not provided"> | Voice settings |
(one row for every variable the Instructions use; business_hours, business_phone, clinic_address under Your business; roster under Doctors; custom details under Your business, Add a detail)
`{{var.company_name}}` = your business name, filled in automatically from Variables.
```

Real values (the business name, hours, phone number, address, doctor details, fees) appear ONLY in the "Fill these in the platform" block of the draft notes, never in the Instructions. If the client gave no value, write "not provided"; never invent one.

The marker line `=== DRAFT NOTES ===` stands alone on its own line. The Instructions part contains only text the platform will use. The draft notes are never part of the Instructions.

## Rules for you

- The references are the source of truth. If a client asks for something they forbid, follow the references and say so in the draft notes.
- Synthetic data only. Never write a real customer, patient or company.
- Do not read or use anything outside this skill folder to decide what is "expected": write from the references and the client's answers.
- Never commit, never push.
