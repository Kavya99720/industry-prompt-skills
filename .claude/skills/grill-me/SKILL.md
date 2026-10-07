---
name: grill-me
description: 'Interview the user one question at a time before defining an industry agent. Use to clarify the industry, business types, callers, channel, languages, safety limits, escalation, data collection, and scope boundaries. Record decisions only; never start building.'
---

# Grill Me

Interview the user before any work begins on an industry. The goal is to understand enough about the intended agent to inform later planning, not to design or build it.

## Interview Rules

- Use `AskUserQuestion` for every question.
- Ask exactly one question at a time. Wait for the user's answer before asking another.
- Give each question 2-4 distinct options. Put the recommended option first and include the literal label `(Recommended)` in that option. Allow a freeform answer when the tool supports it.
- Ask only questions that resolve meaningful uncertainty. Skip topics already answered or clearly irrelevant, and stop once the agent's intended use, boundaries, and safety expectations are sufficiently clear.
- Do not ask multiple topics in one question just to shorten the interview. A brief acknowledgement between questions is fine; do not turn it into a second question.
- If an answer is unclear or exposes an important ambiguity, ask one focused follow-up before moving on.

## Topics to Cover

Establish the industry and intended agent, then clarify these areas as needed:

- **Businesses:** Which kinds of businesses will use the agent (for example, a clinic or a hospital)? Ask about meaningful differences between business types.
- **Callers and intent:** Who contacts the agent, and what are their common reasons for contacting it?
- **Channel:** Is the agent for voice, chat, or both? Clarify whether channel-specific behavior matters.
- **Languages:** Which languages must it support (for example, English, Hindi, or Kannada)? Clarify any language or handoff requirements that matter.
- **Prohibited behavior:** What must the agent never do? Clarify high-impact safety, compliance, or authority limits.
- **Human escalation:** When must it hand off, to whom, and what should it do if a human is unavailable?
- **Data collection:** What information may it collect, and what must it avoid collecting or retain only with permission?
- **Industry boundaries:** What is in scope and out of scope, especially where industries overlap (for example, banking versus finance)?

Use concrete options tailored to the industry rather than repeating generic choices. Keep the first option the recommended default, but do not imply that the user has accepted it. Capture corrections and exceptions from freeform answers.

## Finish and Record

When enough is known, stop interviewing. Briefly summarize the understood scope and any important unresolved item; do not ask another question unless that item blocks an accurate record.

Append the user's answers to `docs/DECISIONS.md` as one numbered, dated entry titled `<Industry> grill-me` (replace `<Industry>` with the industry name). Use the current date in `YYYY-MM-DD` format and continue the existing entry numbering. Preserve prior entries. If the file does not exist, create it with a suitable heading and start the numbered list. Record only what the user stated or confirmed; mark unanswered details as unspecified rather than inventing them.

Never start building, researching industry rules, drafting a brief or prompt, writing evals, or editing any other file as part of this skill. The decision entry is the only output to the project beyond the interview itself.