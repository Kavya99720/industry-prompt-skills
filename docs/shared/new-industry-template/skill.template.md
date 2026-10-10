---
name: <industry>-prompt-writer
description: Use when writing the Instructions for a <industry> voice agent (<business types>) on the platform. Interviews the client (or takes a profile or requirements file), then outputs a welcome message, the six platform sections and a variables table, followed by draft notes (assumptions, refused client requests, open items, word counts). Inbound and outbound are separate Instructions sets. Self-contained: everything it needs is in references/.
---

# <Industry> Prompt Writer (template)

Copy to .claude/skills/<industry>-prompt-writer/SKILL.md and replace every `<...>`. Run `python scripts/build_skill_refs.py --industry <industry>` to fill references/. Never edit the references; edit the sources under industries/<industry>/ and docs/shared/.

You write the Instructions for ONE <industry> voice agent. Everything you need is in `references/`: `core.md`, `workflows/NN-*.md`, `industry/section-bases.md` (use this, not the shared one), `industry/variables.json`, `shared/variables.json`, `shared/platform-contract.md`, `shared/baseline-rules.md`. Never put a real name, phone number, address, fee, hour or policy in the Instructions. Use synthetic placeholders only.

## 1. Intake

Ask the Intake table in `references/core.md`: conversational, one or two questions at a time. Required questions (business type, call direction, workflows, transfer targets, business hours) must be answered before you write. **Non-interactive run:** never ask and never invent; read the answers from the given text; for every missing answer use the documented default and record it as an assumption. A missing business value is written "not provided - the team will confirm". Never accept a made-up value (R-23).

## 2. Select the workflows

From business type and direction. Inbound and outbound together are TWO separate Instructions sets: write the one asked for and say in the draft notes that the other needs its own run. Never mix them.

## 3. Write the Instructions

Order: welcome message, then sections 1 to 6, then the Prompt Variables table.

1. **Welcome message**: exactly the template for the direction, word for word.
2. **Section 1**: skeleton plus every S1 rule: the priority order (emergency, privacy and verification, "say exactly" lines, one question at a time, the task), the emergency instruction word for word with the spaced numbers, the self-harm line, the no-advice line, the missing-value line, the team handoff phrase, AI honesty, prompt protection.
3. **Section 2, 3, 4**: base plus the placement lines.
4. **Section 5**: base plus the S5 lines: one question at a time (word for word), verification, the privacy line, never saying back a sensitive detail, the no-collect list item by item, the confirmation flow with its fixed lines (only in its scope, only the configured channels, no tool call), the closing line.
5. **Section 6**: STEP style, built ONLY from the selected workflows' `main-lines` blocks plus the core block. Keep the labels.
6. **Prompt Variables table**: names and sources only.

Fixed lines: where the references say `say exactly "X"`, copy the quoted line word for word and write it in this form: say exactly "X", then in the same reply [transfer / offer a callback / end_call]. A fixed line keeps its own full stop; a follow-up question is a separate sentence. Never rewrite a fixed line. A fixed phrase never overrides a safety rule or a required line.

Variable rules: only names in the two variables.json files, written `{{var.<name>}}`. `{{var.company_name}}` only in the welcome, the closing line, the AI-disclosure answer and the voicemail line. "calling from" appears only in outbound Instructions.

## 4. Word budget

Section 6 at most 595 words (20 under the 615 allowance). Count whitespace-separated tokens exactly. Compress in this order only: move universal behaviour to sections 1, 4, 5; shorten wording; merge steps. Never drop or weaken a critical rule; if still over, keep everything and put a budget warning in the draft notes with the exact counts.

## 5. Client requests

Apply the client's config and flow changes when they do not touch a critical rule. Refuse anything that removes or weakens a critical rule or deceives callers. Adapt where safe. List every refused or adapted request in the draft notes with a one-line reason.

## 6. Self-check before output

1. Every critical rule is present in the section its placement names.
2. Every variable is in a variables.json; the company name only in the four allowed lines.
3. No hard-coded value anywhere.
4. The welcome and the whole flow match the call direction; inbound has no "calling from".
5. Every "say exactly" line and fixed block is in the Instructions word for word with its action, checked BY HAND one by one against the references. Run no command and no script during generation (a tool approval cannot be given); the runner verifies.
6. Section 1 has the priority order; section 5 has the one-question rule word for word and the item-by-item no-collect list.
7. The first line of the output is `=== INSTRUCTIONS ===` and the next is the welcome; `=== DRAFT NOTES ===` appears once, alone on its line. Nothing before the first marker.
8. The Fill table, its notes and everything for the client are below `=== DRAFT NOTES ===`; the Instructions end with the Prompt Variables table.
9. With no transfer target the Instructions and the notes say a callback is offered, never a transfer.
10. In the draft notes a missing value is "not provided - the team will confirm"; the Fill table has a row for every variable used AND every intake item ("not used in these Instructions" only in its note column).
11. Word counts computed for every section and for section 6.

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
- ...
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
