---
name: brainstorm
description: 'Generate an exhaustive, grouped list of caller scenarios, edge cases, compliance risks and adversarial attempts for ONE industry, grounded in its grill-me entry in docs/DECISIONS.md. Use after grill-me and before the brief. Confirm the list with the user, then save it. Never write the brief, evals or skill.'
---

# Brainstorm

Turn one industry's grill-me decisions into an exhaustive, user-confirmed list of things the agent must handle. This list feeds the later brief; it is not the brief.

## Before You Start

- Confirm which ONE industry to brainstorm. If the user did not name it, ask. Never cover two industries in one run.
- Read `docs/DECISIONS.md` and find the `<Industry> grill-me` entry. If the file or entry is missing, stop and tell the user to run grill-me first. Do not invent the industry's scope.
- Treat the grill-me entry as the source of truth for business types, callers, channel, languages, prohibited behavior, escalation, data collection and scope boundaries. Items marked unspecified there stay open: flag them, do not assume answers.
- Respect the channel. Include voice-only items (silence, noise, interruptions, mishearing, spelled-out data) only if the agent uses voice; chat-only items (typos, pasted text, long messages) only if it uses chat.

## What to Generate

Ground every item in the grill-me entry and the industry. Be specific and concrete, one line each, using synthetic examples only. Never use real customer, patient or company data.

1. **Caller scenarios:** common requests, rare requests, emotional or angry callers, confused callers, and vulnerable callers (for example elderly callers or minors), as relevant to this industry's callers.
2. **Edge cases and failure modes:** out-of-scope asks, wrong or mixed language, silence, interruptions, caller unclear or unreachable, human escalation unavailable, backend or system down, conflicting or incomplete information.
3. **Compliance and safety risks:** privacy and data protection (including DPDP), limits on financial or medical advice, fraud and social engineering, consent, AI disclosure, data the agent must not collect or retain, and any industry regulation the entry implies.
4. **Adversarial attempts:** prompt injection, requests for other people's data, pressure or claimed authority to break rules, attempts to extract the system prompt, and attempts to push the agent out of scope.

Aim for breadth first. Cover the grill-me prohibited-behavior, escalation and data-collection answers with at least one item each. Do not pad with generic items that do not fit this industry.

## Present and Confirm

- Show the items grouped under the four headings above, numbered continuously (1, 2, 3, ... across all groups) so the user can refer to them by number.
- Mark each item `[MUST]` (must-cover: safety, compliance, or high-frequency) or `[NICE]` (nice-to-have).
- Add a short list of open questions for anything the grill-me entry left unspecified and that affects the list.
- Ask the user to confirm: which items to remove, change, or re-mark, and what is missing. Use one `AskUserQuestion` for the overall decision (for example: confirm as is, remove or change items, add items), and take specific item numbers from the freeform answer.
- Apply the user's changes, show the revised list if the changes were significant, and get explicit confirmation before saving. If confirmation is not given, do not save.

## Save

Write the confirmed list to `industries/<industry>/brainstorm.md`, using the industry slug from the folder naming (pharmacy, healthcare, retail, finance, education, logistics, hr, banking, real-estate, travel). Create the folder if needed. If the file already exists, ask before overwriting.

File contents: a title, the source (the grill-me entry number and date), the four grouped sections with the confirmed numbered items and their `[MUST]`/`[NICE]` marks, and any remaining open questions. Keep removed items out; do not record unconfirmed ones.

Never write the industry brief, evals, or the industry skill, and never edit any other file. The brainstorm file is the only output beyond the conversation.
