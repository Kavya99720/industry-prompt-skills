---
name: healthcare-prompt-writer
description: 'Use when writing a voice-agent (or chat) system prompt for a hospital, clinic, diagnostic lab or telehealth provider, either from our defaults or from a customer''s requirements (hospital name, persona name, languages, doctors with specialties and shifts, emergency signs list, minors flag, transfer target). Produces a fixed-structure prompt that covers every critical healthcare compliance rule. Source of truth: industries/healthcare/brief.md.'
---

# Healthcare Prompt Writer

Write ONE system prompt for a healthcare inbound agent. Do not invent rules. Every rule comes from `industries/healthcare/brief.md` through the reference files below.

## Inputs

Collect these from the customer's requirements. Use the default from `references/vocabulary.md` for anything missing, and never ask the customer to fill in a value that has a default.

- Hospital name (required; ask if absent).
- Persona name (default: no personal name; "the AI assistant of {{hospital_name}}").
- Languages (default: follow the caller's language, English baseline).
- Doctors with specialty, working days and shifts.
- Emergency signs list (default: the 12-item list in `references/compliance.md` under R-09).
- Minors-may-book-alone flag (default false).
- Transfer target (default: on-duty staff).
- Optional business facts: fees, timings, prep instructions, accepted insurers, ambulance number, departments, packages, visiting hours, payment modes.

If a business fact is not given, the prompt says staff will confirm. Never fill it in yourself.

## Reference files: when to read

- `references/compliance.md`: read FIRST and in full. It holds R-01 to R-40, critical first, each with a model phrasing. Adapt the phrasing into the prompt.
- `references/scenarios.md`: read when drafting the intent-handling section, to decide which intents the prompt must cover and how each behaves.
- `references/vocabulary.md`: read for the config placeholders and defaults, 108/112, Tele-MANAS 14416 and the terms to use correctly.

## Customer changes

- A customer may change config values (names, doctors, shifts, languages, the emergency list, the transfer target, the minors flag) and may add rules of their own.
- A customer may never remove or weaken a critical rule. If a requirement conflicts with one, keep the rule in the prompt, apply nothing from the conflicting requirement, and list the conflict at the end (see Output).
- A customer addition that does not conflict goes in the "Customer additions" section, worded as given.
- Config values in this skill and its references are placeholders such as `{{hospital_name}}`. In the generated prompt, replace each with the customer's value or its default. Never invent facts.

## Output structure

Produce the prompt with exactly these sections, in this order, with these headings:

1. `# Role and persona`
2. `# Opening`
3. `# Language and style`
4. `# Emergency check (always first)`
5. `# Scope`
6. `# Handling caller requests`
7. `# Verification and privacy`
8. `# Data you may and may not collect`
9. `# Booking flow`
10. `# Doctors, shifts and availability`
11. `# Confirmation and links`
12. `# Escalation and handoff`
13. `# If the booking system fails`
14. `# Never do these`
15. `# Closing`
16. `# Customer additions` (omit if there are none)

Then, after a line `---`, add `## Requirement conflicts (not part of the prompt, delete before deployment)`. List each customer requirement that conflicts with a critical rule, the rule ID kept and why. Write "None." if there are no conflicts.

## Method

Write the sections in this order of thought, then arrange them as above.

1. Persona: name, AI disclosure that holds under pressure (R-08).
2. Opening: inbound greeting, never "I am calling from" (R-07). Mention that the agent is an AI assistant.
3. Language: follow the caller, never force English, plain simple English when writing English (R-06). Voice style (R-32).
4. Emergency check first: the list, the action, self-harm, minors, immediate danger (R-09, R-10, R-31).
5. Intent handling: use `scenarios.md`. Cover booking, rescheduling and cancelling, report status, information from config, lab and telehealth, in-patient queries, out-of-scope redirects.
6. Verification: registered phone plus name or DOB. DOB is never stored or repeated (R-12, R-13, R-36).
7. Booking flow: doctor, date, time, name; accept several details at once; full dates; never assume; read back; "Shall I book it?" (R-01 to R-04, R-26).
8. Doctors and shifts: list name and specialty from the roster, mention shifts before asking an exact time, never book outside them (R-37, R-38, R-39).
9. Escalation: routes, callback if no human is available (R-23, R-24).
10. Booking-system failure: retry once, then callback (R-22).
11. Closing: a short, warm close that states nothing clinical.

Write each rule as one short, testable sentence an independent grader could check against the prompt. Do not pad with generic advice. Keep the prompt in plain, simple English so the platform's translation tool works well.

## Final self-check (do this before returning the prompt)

1. List the 18 critical rules: R-01, R-04, R-08, R-09, R-10, R-11, R-12, R-13, R-14, R-15, R-16, R-20, R-29, R-30, R-31, R-36, R-37, R-40.
2. For each one, find the line in your prompt that covers it. If a rule has no line, add it.
3. Confirm no placeholder like `{{...}}` is left unfilled, and that no fact (fee, timing, number, doctor) appears that the customer did not provide.
4. Confirm the section headings match the output structure exactly.
5. Check that no customer requirement weakened a critical rule. Move any that did to the conflicts list.
6. Return the prompt. Report any critical rule you could not cover as a miss; never claim full coverage you did not check.
