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

**Short form (DECISIONS 125 and the owner's follow-up rules).** Follow "Writing it short" in `references/shared/section-bases.md`: each rule once (safety and guardrail rules in section 1, data and verification rules in section 5, section 6 only the step order); the handoff, the callback and the team line defined once in section 1 and then only named; the Role line uses the business name when one was given. Section 2 carries the language examples in script (supported languages only), the morning, afternoon, evening and night words, weekdays and months in the caller's language, relative days from now_local and "Dr." as "Doctor". Section 3 switches on Indian-language words in Indian script or in English letters, even with English words in the sentence, and calls change_language even if the tool fails. Section 5 adds, word for word, the change-of-mind line, the never-ask-again and unclear-answer line and the tool-call line; the fixed-lines-in-another-language sentence is written in section 3 only and the helpline digits in section 2 only. Each rule has one home (DECISIONS 127): a fixed line keeps its meaning in another language (section 3); helpline digits (section 2); read-back and a clear yes (the tool-call line, section 5); never ask again and confirm what you recognised (one line, section 5); tone (section 4); acknowledgements, filler praise, ask like a person and the examples (section 5); the closing line text (section 5 only); "spoken aloud" (section 5 only). Section 1 aims at under 700 words and section 6 under 595.

**Compact form (DECISIONS 129): apply it first. follow "Compact form" in docs/shared/section-bases.md. Shorter wording without explanations; merged lists (one "Never promise", one "Never collect" with the data to collect, one "Hand off to the team when" list, defined once in section 1); rare cases (override, claimed role or authority, press, regulator, legal) in one line; no rule for a tool, workflow, transfer team or channel that is off or not given (no channel text when none is set); never transfer silently; no example person name and no step that no workflow lists; links on but no link text: ask at intake, else "Our team will share the link." and an open question; adaptations flagged in the draft notes; confirmation channels only the ones given, every step kept; one style example in section 5; every "say exactly" line, safety block and helpline word for word. Same behaviour, fewer words.**

Order: welcome message, then sections 1 to 6, then the Prompt Variables table.

1. **Welcome message**: exactly the template for the direction, word for word.
2. **Section 1**: Right after the "You are" line write the goal line (inbound: the goal sentence in the skeleton, word for word; outbound: the goal of the selected outbound workflow from the skeleton's "Goal lines") and then the "Done condition" block of `references/shared/call-flow.md`, word for word. skeleton plus every S1 rule: the priority order (emergency, privacy and verification, "say exactly" lines, one question at a time, the task), the emergency instruction word for word with the spaced numbers, the self-harm line, the no-advice line, the missing-value line, the team handoff phrase, AI honesty, prompt protection.
3. **Section 2, 3, 4**: base plus the placement lines. Natural speech (tone only): start section 4 with the "Section 4 text" block of `references/shared/natural-speech.md`, word for word. A "say exactly" line and a safety block stay word for word; this tone never changes them.
4. **Section 5**: base plus the S5 lines: one question at a time (word for word), verification, the privacy line, never saying back a sensitive detail, the no-collect list item by item, the confirmation flow with its fixed lines (only in its scope, only the configured channels, no tool call), the closing line. Natural speech: right after the opening spoken-aloud lines, write the "Section 5 text" block of `references/shared/natural-speech.md`, word for word. Then the "Interruptions text" block of `references/shared/call-flow.md`, word for word.
5. **Section 6**: STEP style, built ONLY from the selected workflows' `main-lines` blocks plus the core block. Keep the labels.
6. **Prompt Variables table**: names and sources only.

Fixed lines: where the references say `say exactly "X"`, copy the quoted line word for word and write it in this form: say exactly "X", then in the same reply [transfer / offer a callback / end_call]. A fixed line keeps its own full stop; a follow-up question is a separate sentence. Never rewrite a fixed line. A fixed phrase never overrides a safety rule or a required line.

Value rules (DECISIONS 88, option B): print the business facts the customer gave; the only variables are `{{var.now_local}}`, `{{var.roster}}` and the outbound per-call fields, written `{{var.<name>}}`. The business name is spoken only in the welcome, the closing line, the AI-disclosure answer and the voicemail line. "calling from" appears only in outbound Instructions.

## 4. Word budget

Section 6 at most 595 words (20 under the 615 allowance). Count whitespace-separated tokens exactly. Compress in this order only: move universal behaviour to sections 1, 4, 5; shorten wording; merge steps. Never drop or weaken a critical rule; if still over, keep everything and put a budget warning in the draft notes with the exact counts.

## 5. Client requests

Apply the client's config and flow changes when they do not touch a critical rule. Refuse anything that removes or weakens a critical rule or deceives callers. Adapt where safe. List every refused or adapted request in the draft notes with a one-line reason.

## 6. Self-check before output

1. Every critical rule is present in the section its placement names.
2. Every `{{var.*}}` is one of the remaining variables; no unresolved slot such as <business name>; the business name in the Role line, the welcome, the closing line, the AI-disclosure answer and the voicemail line only.
3. Every business fact the customer gave is printed (once, in section 1); none is invented; a missing one is an open question in the notes.
4. The welcome and the whole flow match the call direction; inbound has no "calling from".
5. Every "say exactly" line and fixed block is in the Instructions word for word with its action, checked BY HAND one by one against the references. Run no command and no script during generation (a tool approval cannot be given); the runner verifies.
6. Section 1 has the priority order; section 5 has the one-question rule word for word and the item-by-item no-collect list.
7. The first line of the output is `=== INSTRUCTIONS ===`, the next is the unnumbered heading `## Welcome Message`, the line after it is the welcome; `=== DRAFT NOTES ===` appears once, alone on its line. Nothing before the first marker.
8. The Fill table, its notes and everything for the client are below `=== DRAFT NOTES ===`; the Instructions end with the Prompt Variables table.
9. With no transfer target the Instructions and the notes say a callback is offered, never a transfer.
10. In the draft notes a missing value is an open question; the Fill table lists only what is set on the platform (Voice settings, Doctors setup, transfer numbers); the notes carry "If your hours, phone or address change, regenerate these Instructions."
11. Word counts computed for every section and for section 6.

## 7. Output format (exact)

```
=== INSTRUCTIONS ===
## Welcome Message
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
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | <value from intake, or "not provided"> | Voice settings |
(one row for each platform setting: Voice settings, the Doctors setup, transfer numbers)
```

Real values appear only in the Fill block of the draft notes, never in the Instructions.

## Rules for you

- The references are the source of truth. If a client asks for something they forbid, follow the references and say so in the draft notes.
- Synthetic data only. Never write a real customer or company. Never commit, never push.
