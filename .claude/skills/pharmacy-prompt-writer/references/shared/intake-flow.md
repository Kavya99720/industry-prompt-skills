# Intake flow (shared by every industry skill)

How a prompt-writer skill collects the customer's answers before it writes the Instructions. The questions themselves live in each industry's core.md (Intake table). This file is the way they are asked. Each skill gets a copy in references/shared/ (scripts/build_skill_refs.py) and follows it.

## Interactive run (the customer is talking to the skill)

1. **One or two questions per message.** Ask the required questions first, in table order, then the optional ones. Say why you ask when it is not obvious. Skip anything the customer has already said, including in the first message.
2. **"I don't know" or skip.** Record it as an open question for the customer in the draft notes and use the documented default. Never invent a value (no name, phone number, address, fee, doctor, price, language or transfer target).
3. **Use the answers exactly as given.** Never widen or change them. "WhatsApp only" means only WhatsApp; "Hindi and Kannada" means those two languages plus English, which is always supported, and no others. If an answer is unclear, ask again in one short line.
4. **Summary before writing.** When the questions are done, show a short summary of every answer (one line each, with the default used for anything skipped). Flag every answer that turns off or loosens a safety default, for example "minors may book alone", an emergency department answer that changes the emergency line, or a payment or prescription setting. Then ask: "Shall I write the Instructions?" Write only after a clear yes. A "yes, but" is not a yes. If the customer corrects something, update the answer, show the summary again and ask again.
5. **Where answers go.** Business name, location, phone number, assistant name and gender go ONLY into the fill-in table of the draft notes. The Instructions keep the `{{var.<name>}}` variables (platform contract, R-74). Never put a real value in the Instructions.

## Non-interactive run (a profile, requirements file or brief is given)

Skip every question and the summary. Read the answers from the given text, use the documented default for anything missing, and record each default as an assumption and each missing required answer as an open item, as the skill's Intake section says. Nothing here changes how those runs worked before.

## Draft notes layout (all skills)

- Every heading of the draft notes (for example "Assumptions and defaults used") is on its own line, with a blank line before it.
- The fill-in table is a real Markdown table: a header row, a separator row, and exactly one row per line.
- The notes are read by the customer: plain words, no rule IDs, no workflow or intake numbers.
