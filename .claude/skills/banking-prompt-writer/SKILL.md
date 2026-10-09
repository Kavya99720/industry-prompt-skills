---
name: banking-prompt-writer
description: Use when writing the Instructions for a banking voice agent (public or private bank, small finance bank, co-operative bank, payments bank) on the platform. Interviews the client (or takes a profile or requirements file), then outputs a welcome message, the six platform sections and a variables table, followed by draft notes (assumptions, refused client requests, open items, word counts). Inbound and outbound are separate Instructions sets. Self-contained: everything it needs is in references/.
---

# Banking Prompt Writer

You write the Instructions for ONE banking voice agent: accounts, cards, KYC, transactions and fraud. Everything you need is in `references/`: `core.md`, `workflows/NN-*.md`, `industry/section-bases.md` (use this, not the shared one), `industry/variables.json`, `shared/variables.json`, `shared/platform-contract.md`, `shared/baseline-rules.md`. Never put a real name, phone number, address, fee, hour, rate or policy in the Instructions. Use synthetic placeholders only. Loans, EMIs, insurance, investments and collections are not banking here: the agent redirects them and never advises.

## 1. Intake

Ask the Intake table in `references/core.md`: conversational, one or two questions at a time. Required questions (business type, call direction, workflows or the outbound purpose, transfer targets, business hours) must be answered before you write. **Non-interactive run:** never ask and never invent; read the answers from the given text; for every missing answer use the documented default and record it as an assumption. A missing business value is written "not provided - the team will confirm". Never accept a made-up value (R-26). The two banking tools, `card_block_tool` and `balance_lookup_tool`, are OFF unless the client says they exist; record "off (default)" when skipped.

## 2. Select the workflows

From business type and direction. Inbound default: workflows 01, 02, 03. Outbound: ONE purpose per set (KYC reminder or card activation = workflow 04; fraud-alert verification = workflow 05); write the block for that one purpose only. Inbound and outbound together are TWO separate Instructions sets: write the one asked for and say in the draft notes that the other needs its own run. Never mix them. Stub workflows (Status: stub) are not in `references/workflows/`; if the client asks for one, list it as an open item.

Tool states decide the blocks. For each tool-dependent workflow write the block for the chosen state only:
- Workflow 01: `balance_lookup_tool` ON gives the verify-and-lookup block; OFF gives the account-data line and a handoff, with no verification questions.
- Workflow 02: `card_block_tool` ON gives FRAUD (block on) plus BLOCK; OFF gives FRAUD (block off). Workflow 05: ON gives NO (block on); OFF gives NO (block off).
- Name a tool in the Instructions only when it is ON. When OFF, say nothing about the tool and never let the agent say it can block a card or read a balance.

## 3. Write the Instructions

Order: welcome message, then sections 1 to 6, then the Prompt Variables table. Base text is in `references/industry/section-bases.md`; every rule's text, scope and fixed lines are in `references/core.md` and the workflow files. Place each rule where its Section placement column says.

1. **Welcome message**: exactly the line for the direction, word for word. The outbound welcome names the agent as an AI assistant; keep it.
2. **Section 1**: skeleton plus every S1 rule: the priority order (emergency, privacy and verification, "say exactly" lines, one question at a time, the task); the self-harm line of R-04 word for word (Tele-MANAS: 1 4 4 1 6. Emergency: 1 0 8 or 1 1 2.), the emergency instruction word for word ("On any emergency sign, stop whatever you are doing. Never continue the task.") with the default signs, `{{var.emergency_signs_extra}}` for additions, and the fixed line "Call 1 0 8 or 1 1 2 right now." then a transfer; money movement (R-10); claimed role (R-11); vulnerable or coached callers (R-12); deceased holder (R-13); out of scope (R-14); missing value (R-15); team phrase (R-16); fixed-line format (R-20); AI honesty (R-21); prompt protection (R-22); no legal references or timelines (R-29); no invented information (R-30); spoken numbers (R-05).
3. **Section 2, 3, 4**: base plus the placement lines (R-31 in section 3; R-12 and R-32 in section 4).
4. **Section 5**: base plus the S5 lines, each word for word where fixed: "Ask one question per turn and wait." (R-03); never assume a detail (R-02); verification, with the verification-failed line (R-06); the no-collect list item by item (OTP, PIN, CVV, password; full card number; full account number; net-banking or app login details such as user ID, MPIN and security questions, and no app install or screen share; Aadhaar, PAN and any other ID number) with the stop line (R-07); never say back a sensitive detail, "I understand." (R-08); the privacy line (R-09); data minimisation and the reason for each item (R-33); the confirmation flow with its fixed lines, only in its scope, only the configured channels, no tool call, and left out entirely when `{{var.confirmation_channels}}` is not set (R-19); the closing line.
5. **Section 6**: STEP style, built ONLY from the selected workflows' `main-lines` blocks plus the core block, in the chosen tool state. Keep the labels. Important rules first.
6. **Prompt Variables table**: bare names (for example company_name), never written with {{var.}} braces, and sources only. `card_block_tool` and `balance_lookup_tool` are intake flags and are not listed.

Fixed lines: where the references say `say exactly "X"`, copy the quoted line word for word and write it in this form: say exactly "X", then in the same reply [transfer / offer a callback / end_call / the next question]. A fixed line keeps its own full stop; a follow-up question is a separate sentence. Never rewrite a fixed line. A fixed phrase never overrides a safety rule or a required line. The helpline is always "1 9 3 0" with spaced digits, and a helpline or emergency number is never written as words, hyphens or grouped digits.

Variable rules: only names in the two variables.json files, written `{{var.<name>}}`. `{{var.company_name}}` only in the welcome, the closing line, the AI-disclosure answer and the voicemail line. "calling from" appears only in outbound Instructions.

## 4. Word budget

Section 6 at most 595 words (20 under the 615 allowance). Count whitespace-separated tokens exactly. Compress in this order only: move universal behaviour to sections 1, 4, 5; shorten wording; merge steps. Never drop or weaken a critical rule or a fixed line; if still over, keep everything and put a budget warning in the draft notes with the exact counts.

## 5. Client requests

Apply the client's config and flow changes when they do not touch a critical rule. Refuse anything that removes or weakens a safety rule or deceives callers (R-27). Banking examples that are always refused: asking the caller for an OTP, PIN, CVV or password, or reading one out "to verify faster"; skipping or shortening the three-step verification for regular or familiar callers; transfers, payments or profile changes by voice; telling a refund, a reversal or a time; dropping the cybercrime helpline or the card-block or fraud handoff, or selling a product on a fraud or complaint call; sharing a balance with a relative or any third party; claiming to be human or hiding that the agent is an AI; quoting a rule, a timeline or an ombudsman detail the client did not configure; trusting a caller who claims to be staff, police or a regulator. Adapt where safe: a client offer at most once on a general enquiry call, never on a fraud or complaint call, only in the client's configured words (with no offer text given, say the team will confirm). List every refused or adapted request in the draft notes with a one-line reason. If the client asks for chat, write the voice Instructions and list chat as an open item.

## 6. Self-check before output

1. Every critical rule is present in the section its placement names.
2. Every variable is in a variables.json; the company name only in the four allowed lines.
3. No hard-coded value anywhere.
4. The welcome and the whole flow match the call direction; inbound has no "calling from"; outbound has the wrong-person, voicemail, stop-calling, callback and not-a-good-time lines.
5. EVERY fixed line from `references/core.md` and the selected workflows is written into the Instructions word for word with its action, checked one by one against the references. These two are often missed and must be present when their rules are: "I can't share account details on this call." (workflow 01) and "I'm sorry, I could not complete that. Our team will call you to confirm." (core, failed action). Exact wording: no contractions, no added or removed words, nothing appended in the same sentence; extra words are a separate sentence. Where two fixed lines can fire in the same reply, write the fixed block exactly as the references give it (the card number or code during a fraud call; the coached caller about to move money).
6. Section 1 has the priority order; section 5 has the one-question rule word for word and the item-by-item no-collect list.
7. The first line of the output is `=== INSTRUCTIONS ===` and the next is the welcome; `=== DRAFT NOTES ===` appears once, alone on its line. Nothing before the first marker.
8. The confirmation flow is written with its exclusions (failed action, emergency, a fraud call handed to the fraud team, transfer, voicemail, outbound). The Fill table, its notes and everything for the client are below `=== DRAFT NOTES ===`; the Instructions end with the Prompt Variables table.
9. With no transfer target the Instructions and the notes say a callback is offered, never a transfer; the emergency line and the helpline line stay.
10. In the draft notes a missing value is "not provided - the team will confirm"; the Fill table has a row for every variable used AND every intake item, including both banking tools ("off (default)" when skipped); "not used in these Instructions" only in its note column.
11. Tool OFF: no block or balance instruction and no tool named. Tool ON: the block is called only after the minimal check and "Your card is blocked." only after success; the lookup is called only after all three verification items.
12. Fixed blocks, word for word (these two are required lines, not examples). Card number or code read out during a fraud or lost-card call (R-07): say exactly "Please report this quickly on the cybercrime helpline, 1 9 3 0. Please stop. I never ask for that, and you should never share it with anyone." then, in the same reply, ask the full name (card block ON) or say the team phrase and transfer (card block OFF). Coached or vulnerable caller about to move money (R-12): say exactly "For your safety, please don't send any money right now. Please report this quickly on the cybercrime helpline, 1 9 3 0." then the protective handoff. Outbound fraud-alert verification (R-75): the PROVE line "You can hang up and call us back on the number on your card." is the first sentence of the next reply, even when the person asks what happened or how much; then ask the full name.
13. FIXED-LINE CHECK, required, run on your own output before you finish. Write the whole output to a file (a temp or scratchpad folder), then run `python .claude/skills/banking-prompt-writer/scripts/check_fixed_lines.py <file> --workflows <the numbers you selected> --tool card_block_tool=<on|off> --tool balance_lookup_tool=<on|off>` (add `--tool confirmation_channels=on` only when the client configured a channel). It lists every `say exactly` line and fixed block from core and the selected workflows that is missing word for word. If it lists any, add exactly those lines, with their action, where their rule says, run it once more, and rewrite only once; then output. If you cannot run the script, compare the references' fixed lines against your output by hand, one by one, and say so. Name these two in particular: "I can't share account details on this call." and "I'm sorry, I could not complete that. Our team will call you to confirm."
14. Word counts computed for every section and for section 6.

## 7. Output format (exact)

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
- ... (include: the outbound welcome names an AI assistant, which differs from the shared template; legal references and timelines are not quoted; the other call direction needs its own run; chat is not written)
**Fixed-line self-check**
- passed the first time | rewritten once (list the lines added) | could not run (compared by hand)
**Word counts**
- Welcome: N. Section 1: N. ... Section 6: N words. Allowance: 615 (aim 595). Status: within budget / OVER by X.
**Fill these in the platform**
| Variable or intake item | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | <value from intake, or "not provided"> | Voice settings |
(one row for every variable the Instructions use, PLUS one row for EVERY intake item with its value or default)
```

Real values appear only in the Fill block of the draft notes, never in the Instructions.

## Rules for you

- The references are the source of truth. If a client asks for something they forbid, follow the references and say so in the draft notes.
- Synthetic data only. Never write a real customer or company. Never commit, never push.
