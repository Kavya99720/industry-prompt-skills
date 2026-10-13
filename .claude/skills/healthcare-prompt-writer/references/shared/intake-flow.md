# Intake flow (shared by every industry skill)

How a prompt-writer skill collects the customer's answers before it writes the Instructions. The questions themselves live in each industry's core.md (Intake table). This file is the way they are asked. Each skill gets a copy in references/shared/ (scripts/build_skill_refs.py) and follows it.

## Interactive run (the customer is talking to the skill)

1. **One or two questions per message.** Ask the required questions first, in table order, then the optional ones. Say why you ask when it is not obvious. Skip anything the customer has already said, including in the first message.
2. **"I don't know" or skip.** Record it as an open question for the customer in the draft notes and use the documented default. Never invent a value (no name, phone number, address, fee, doctor, price, language or transfer target).
3. **Use the answers exactly as given.** Never widen or change them. "WhatsApp only" means only WhatsApp; "Hindi and Kannada" means those two languages plus English, which is always supported, and no others. If an answer is unclear, ask again in one short line.
4. **Summary before writing.** When the questions are done, show a short summary of every answer (one line each, with the default used for anything skipped). Flag every answer that turns off or loosens a safety default, for example "minors may book alone", an emergency department answer that changes the emergency line, or a payment or prescription setting. Then ask: "Shall I write the Instructions?" Write only after a clear yes. A "yes, but" is not a yes. If the customer corrects something, update the answer, show the summary again and ask again.
5. **Where answers go (DECISIONS 88, option B).** The Instructions print the business facts the customer gave directly: agent name and gender, business name, location, phone, hours, languages, services, emergency department answer and the other business details. Only `now_local`, `roster` and the outbound per-call fields stay variables. The fill-in table of the draft notes lists only what is set on the platform (Voice settings, the Doctors setup, transfer numbers).
6. **Missing values.** Never invent one, and list each as an open question in the draft notes. No agent name: the welcome drops "This is <agent name>." No business name: a neutral word ("our clinic"). A fact the caller asks for that was not given: say exactly "Our team will confirm that for you." and offer a callback (a shared fixed line). No phone: offer a callback without saying a number. No hours: say "during business hours".
7. **Summary shows the values.** The summary before writing lists the values that will be printed in the Instructions, so the customer can correct a name, number or hour before anything is written.

## Non-interactive run (a profile, requirements file or brief is given)

Skip every question and the summary. Read the answers from the given text, use the documented default for anything missing, and record each default as an assumption and each missing required answer as an open item, as the skill's Intake section says. Nothing here changes how those runs worked before.

## Draft notes layout (all skills)

- Every heading of the draft notes (for example "Assumptions and defaults used") is on its own line, with a blank line before it.
- The fill-in table is a real Markdown table: a header row, a separator row, and exactly one row per line.
- The notes are read by the customer: plain words, no rule IDs, no workflow or intake numbers.
- The notes carry the line: "If your hours, phone or address change, regenerate these Instructions."
