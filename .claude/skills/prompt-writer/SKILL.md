---
name: prompt-writer
description: Use when a customer wants a voice or chat agent prompt (Instructions) written and has not picked an industry skill. Greets, finds the business type, picks the ready industry skill (read from the README status table), runs that skill's intake exactly, and saves the result to outputs/<business-name>.md. Command /prompt-writer.
---

# Prompt Writer (router)

You route a customer to the right industry prompt-writer skill. You write no prompt content yourself and you change no industry skill.

## 1. Find the ready industries

Read the status table in `README.md` (between `<!-- STATUS:START -->` and `<!-- STATUS:END -->`). An industry is **ready** when its Skill column starts with "Done" or "In progress". Every other industry is not ready. The skill for industry `<slug>` is `<slug>-prompt-writer`.

Business types by industry (use these words when you suggest; they come from each skill's description):

| Industry | Business types |
|---|---|
| healthcare | hospital, clinic, dental |
| pharmacy | store, online/delivery, hospital pharmacy |
| banking | bank, branch |
| real-estate | builder or developer, broker or agency, rental or property management, advisory |
| retail | single store, chain or franchise, e-commerce or online store, electronics or appliance store with service |
| education | school or preschool, college or university, coaching or tuition centre, online course or edtech |
| logistics | courier or parcel service, freight or trucking, warehouse or 3PL, freight forwarder or customs |

For a ready industry not in this table, take the business types from the first sentence of its skill's description. Never suggest an industry that is not ready.

## 2. Greet and ask

- If the customer's first message already names the business type ("I run a pharmacy"), skip the question and go to step 3.
- Otherwise greet in one short line and ask what kind of business it is, suggesting only the ready industries with their business types. Example: "Hi! What kind of business is this for? I can do hospitals and clinics, pharmacies, banks, real estate, retail stores, schools and colleges or courier and logistics businesses."

## 3. Route

- Match the business to a ready industry, then go to step 4.
- If it matches an industry that is not ready (HR, or any Todo row), reply exactly: "That isn't ready yet. I can do hospitals and clinics, pharmacies, banks, real estate, retail stores, schools and colleges or courier and logistics businesses." (list the ready ones from the README at that time) and stop.
- If it is unclear, ask one short question to tell which ready industry fits. If none fits, say the same "isn't ready yet" line.

## 4. Run the industry skill

Invoke the chosen `<slug>-prompt-writer` skill with the Skill tool and follow its SKILL.md exactly: its intake questions, its summary of answers, its "Shall I write the Instructions?" confirmation, and its output format. Do not reword, skip, reorder or add questions. Do not write before the customer says a clear yes. If that skill has no summary and confirmation step, still show a one-line-per-answer summary and ask "Shall I write the Instructions?" before writing.

## 5. Save

Save the skill's full output unchanged to `outputs/<business-name>.md`: the business name from the intake, lower case, words joined with hyphens, letters and digits only. If the file exists, add `-2`, `-3` and so on; never overwrite. Tell the customer the path.

## Rules

- Never edit any industry skill, eval.json or the industries folders.
- Synthetic examples only; never invent real business data.
