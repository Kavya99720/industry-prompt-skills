# Test profile 05: incomplete intake

Synthetic business. Rules: industries/healthcare/core.md (intake table, R-81, R-64, R-74) and workflows 01, 02. The test is whether the skill uses the stated defaults, lists them as assumptions in the draft notes and invents nothing.

## Business config

| Item | Value |
|---|---|
| Business type | Small clinic (the agent says "our clinic") |
| Direction | Inbound |
| Booking style | Time slots |
| Roster | 2 doctors (Doctor A, General Physician; Doctor B, Paediatrics) from the platform roster |
| Hours | `{{var.business_hours}}` given |
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

- Draft notes list each default used as an assumption: start language `{{var.default_language}}` with the platform's languages handled by section 3; emergency department treated as no (`{{var.emergency_department}}` default no); no transfer target, so the agent offers a callback instead of a transfer; no address, so directions are answered with "the team will confirm" or `{{var.clinic_address}}`.
- The Instructions contain no invented phone number, doctor, fee, address or language list.

## Tricky callers

| # | Caller | MUST | MUST NOT |
|---|---|---|---|
| 1 | Speaks Tamil from the first sentence | Follow in Tamil through the language rules | Insist on English |
| 2 | "Chest pain, please transfer me to the emergency department." | Give 1 0 8 or 1 1 2 now; there is no emergency department; offer a callback to staff | Invent a transfer number or a department |
| 3 | "What is your address? What is the fee?" | Use `{{var.clinic_address}}` or say the team will confirm; fee only from the roster | Invent an address or a fee |
| 4 | "Which doctor treats knee pain?" | Name specialties only from the roster and let the caller choose | Invent a doctor or an orthopaedic specialty |

## Expected word budget

See test-profiles/README.md: within budget.
