---
name: spec-first
description: 'Turn one industry''s grill-me entry and confirmed brainstorm into an industry brief (scope, scenarios S-xx, rules R-xx, vocabulary, escalation, data handling) at industries/<industry>/brief.md, before any eval or skill is written. Show the brief and get approval before saving. Stops if grill-me or brainstorm input is missing. Never write evals or the skill.'
---

# Spec First

Write the industry brief for ONE industry. The brief is the contract that later evals and the industry skill are built from, so it must be specific, traceable and approved before anything else is written.

## Before You Start

- Confirm which ONE industry. If the user did not name it, ask. Never brief two industries in one run.
- Read both inputs:
  - the `<Industry> grill-me` entry in `docs/DECISIONS.md`
  - `industries/<industry>/brainstorm.md`
- If `docs/DECISIONS.md`, the grill-me entry, or the brainstorm file is missing, STOP. Tell the user which input is missing and which skill to run first (grill-me or brainstorm). Do not infer the missing input and do not continue.
- Treat the grill-me entry and the confirmed brainstorm as the only sources of scope. Anything marked unspecified stays unspecified: list it as an open question in the brief, do not invent an answer.
- Use synthetic examples only. Never use real customer, patient or company data.

## Brief Contents

Write the brief with these sections, in this order.

1. **Scope**
   - In scope and out of scope, as short bullet lists.
   - Overlap boundaries with other industries (for example banking versus finance): what this agent handles, what it hands off or refuses.

2. **Scenarios**
   - IDs `S-01`, `S-02`, ... continuing without gaps.
   - Each scenario states: the caller, the goal, and the expected agent behaviour. Keep each to a few lines.
   - Cover common, rare, emotional, confused, vulnerable-caller, edge-case, failure-mode and adversarial scenarios from the brainstorm.

3. **Rules**
   - IDs `R-01`, `R-02`, ... continuing without gaps.
   - Each rule is one testable must or must-not statement, with:
     - **Source:** a grill-me answer (cite the question topic) or a named regulation or standard. Name a regulation only if you are confident it applies and say precisely what it requires; otherwise mark the source as "to be confirmed by the industry expert". Never fabricate a regulation or citation.
     - **Severity:** `critical` (safety, legal, privacy, or harm if broken), `major`, or `minor`.
   - Write rules so an independent grader could judge a prompt or a transcript against them as pass or fail. Avoid vague wording like "be helpful".

4. **Vocabulary**
   - Key industry terms the agent should use correctly, each with a one-line meaning and, where it matters, a term to avoid or a common confusion.

5. **Escalation**
   - When the agent must hand off, to whom, and what it does if no human is available. Take these from the grill-me answers; mark gaps as open questions.

6. **Data Handling**
   - What the agent may collect, what it must not collect, and what it may keep only with permission. Include consent and AI-disclosure expectations where the grill-me entry or brainstorm raises them.

7. **Open Questions**
   - Anything unspecified that affects scope, scenarios or rules. Leave empty only if there are none.

## Traceability

- Every `[MUST]` item in the brainstorm file must map to at least one `S-xx` or `R-xx` ID.
- Include a traceability table at the end of the brief: brainstorm item number, its short text, and the S/R IDs that cover it.
- Before showing the brief, check the table yourself: no `[MUST]` item may be unmapped. Fix gaps by adding a scenario or rule.
- `[NICE]` items may be mapped, folded into another scenario, or listed as deferred. Do not silently drop them; record deferred ones.
- Do not add scenarios or rules that have no source in the grill-me entry or the brainstorm, other than clearly sourced regulation-based rules.

## Review and Save

- Show the full brief to the user in the conversation. Do not save yet.
- Ask for approval with `AskUserQuestion` (for example: approve as is, request changes). Take specific edits from a freeform answer.
- Apply requested changes, re-check traceability, and show the revised brief if the changes were significant.
- Save only after explicit approval, to `industries/<industry>/brief.md` (industry slug: pharmacy, healthcare, retail, finance, education, logistics, hr, banking, real-estate or travel). Create the folder if needed. If the file already exists, ask before overwriting.

Never write evals or the industry skill, and never edit any other file. The brief is the only output beyond the conversation.
