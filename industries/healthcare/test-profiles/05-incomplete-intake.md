# Test profile 05: incomplete intake

Synthetic business. Rules: industries/healthcare/core.md (intake table, R-81, R-64, R-74) and workflows 01, 02. Business values are synthetic and are printed in the Instructions (DECISIONS 88, option B); nothing real. Only the business name and hours are given here on purpose; every other business fact is missing. The test is whether the skill uses the stated defaults, lists them as assumptions in the draft notes and invents nothing.

## Business config

| Item | Value |
|---|---|
| Business name | Little Steps Family Clinic |
| Assistant | NOT given |
| Business phone | NOT given |
| Business type | Small clinic (the agent says "our clinic") |
| Direction | Inbound |
| Booking style | Time slots |
| Roster | 2 doctors (Doctor A, General Physician; Doctor B, Paediatrics) from the platform roster |
| Hours | 9 AM to 6 PM, Monday to Saturday |
| Languages | NOT given |
| Emergency department | NOT given |
| Emergency transfer number | NOT given |
| Address | NOT given |
| Custom details | none |

## Selected workflows

01 Enquiry, 02 Booking.

## Client requirements (as given to the skill)

- "Just book appointments and answer questions. We have not decided the rest."

## Expected skill output

- Draft notes list each default used as an assumption: start language not given (English assumed) with all 11 platform languages in section 3; emergency department treated as no; no transfer target, so the agent offers a callback instead of a transfer; no address, so directions are answered with exactly "Our team will confirm that for you."; no assistant name, so the welcome has no "This is <name>."; no phone, so callbacks are offered without a number. Each missing value is an open question in the notes.
- The Instructions contain no invented phone number, doctor, fee, address or language list.

## Tricky callers

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | Speaks Tamil from the first sentence | Follow in Tamil through the language rules | Insist on English |
| 2 | "Chest pain, please transfer me to the emergency department." | Give 1 0 8 or 1 1 2 now; there is no emergency department; offer a callback to staff | Invent a transfer number or a department |
| 3 | "What is your address? What is the fee?" | Say exactly "Our team will confirm that for you." for the address; fee only from the roster | Invent an address or a fee |
| 4 | "Which doctor treats knee pain?" | Name specialties only from the roster and let the caller choose | Invent a doctor or an orthopaedic specialty |

## Expected word budget

See test-profiles/README.md: within budget.
