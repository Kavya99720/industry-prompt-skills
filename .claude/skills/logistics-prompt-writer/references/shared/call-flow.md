# Call flow lines (one rule for every industry)

Defined once, here. Every industry's section-bases points to this file (section 1: the goal line and the done condition; section 5: interruptions and "hello?"), and every industry skill writes the two text blocks below, word for word. The new-industry templates carry the same pointers, so a new industry inherits them. Source: DECISIONS 123.

Scope: call flow only. A "say exactly" line, a safety block (emergency, self-harm, child safety), a verification step, a required line and a handoff rule stay word for word. The closing line is the one the industry already defines in section 5; this file never changes it.

## Goal line (section 1, the first lines right after the "You are <name>..." line)

The goal line is industry-specific and lives in each industry's section-bases (inbound: one fixed sentence; outbound: one sentence per outbound workflow, from that workflow's purpose). It starts with "Your goal:" and is followed by the done condition below. Inbound goal lines:

| Industry | Inbound goal line |
|---|---|
| Healthcare | Your goal: help the caller with clinic information, doctor availability or an appointment request, using only the business facts and the roster. |
| Pharmacy | Your goal: help the caller with medicine availability, orders and store information, using only the business facts. |
| Banking | Your goal: help the caller with general product, branch and card questions, using only the business facts. |
| Real estate | Your goal: help the caller with project information and site visit requests, using only the business facts. |
| Retail | Your goal: help the caller with store, product, order and return questions, using only the business facts and system data. |
| Education | Your goal: help the caller with admissions, fees and school information, using only the business facts. |
| Logistics (for later) | Your goal: help the caller with their shipment, such as tracking, delivery, pickup or a problem, using only system data and the business facts. |
| HR (for later) | Your goal: help the caller with leave, payroll dates, an application or joining, using only system data and the business facts. |

## Done condition text (write word for word, on the line after the goal line)

```
The call is done when the caller has their answer, has been transferred, or a callback has been noted. Then say the closing line and end the call.
```

## Interruptions text (write word for word, in section 5, right after the natural-speech block)

```
If the caller says 'hello?', goes quiet, or the line breaks up in the middle of the call, say 'Yes, I'm here.' and continue from where you stopped. Repeat your last question in short if needed. Never restart the call and never repeat the welcome. If the caller interrupts you, stop, listen, answer the new point, then go back to the open step. If there is no reply after you ask 'Are you still there?' twice, say the closing line and end the call.
```

## How an industry uses it

- Section-bases: section 1 carries the goal line (inbound sentence, and the outbound goals per workflow) and one pointer line, `<Done condition: the done condition text of docs/shared/call-flow.md, word for word.>`, right after the "You are" line. Section 5 carries one pointer line, `<Interruptions: the interruptions text of docs/shared/call-flow.md, word for word.>`, right after the natural-speech pointer. The blocks are not copied into the section-bases. The old one-line "If the caller interrupts, stop at once and listen." is removed so it is not said twice.
- Skill: `scripts/build_skill_refs.py` copies this file to `references/shared/call-flow.md`; SKILL.md says to write the goal line and the done condition into section 1 and the interruptions block into section 5.
- Outbound: the goal is written from the selected workflow's purpose and followed by the same done condition.
- Word budget: sections 1 and 5 lines from this file do not count against the 595-word limit of section 6.
