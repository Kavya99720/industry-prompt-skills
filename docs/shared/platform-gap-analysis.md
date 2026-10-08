# Platform gap analysis

Compares our healthcare brief (industries/healthcare/brief.md) and healthcare skill with the CellAssist Voice format in docs/shared/platform-contract.md, using the real <business_name> texts in docs/shared/reference/reference-starter.md. Nothing in the brief or the skill has been changed. Everything here is a proposal or a question for the owner.

The "How these compose" tooltip has not been captured yet (still TODO in the reference file).

## 1. Shared across industries, or industry-specific? (re-checked against the real texts)

The earlier version of this table was based on section titles only. The real texts show that sections 2 and 5 are a shared base plus healthcare-specific lines, and section 1 is mostly healthcare-specific.

| Part | Verdict | Shared base | Healthcare-specific lines found in the real text |
|---|---|---|---|
| Welcome message | Platform, fixed | Outbound opener ("I am calling from…") | None, but see conflict 9 |
| 1. Role & Identity | Shared skeleton, mostly healthcare-specific content | Persona and `company_name`, work out intent without a menu, handle each need fully, answer both questions, honest handoff, only share what you were given, AI line only when clearly asked | List of caller needs (book, doctor timings and fees, reports, pharmacy, billing), no medical advice and only read out specialties, emergency steps, hospital info and services, directions |
| 2. Date & Time — TTS Rules | Shared base plus healthcare-specific | Everything spoken aloud, numerals in English, Indian-language numbers as words, `now_local` and relative days, never say the year, how to say Dr., OTP, websites and phone numbers | Doctor timings in 24-hour format for the tool, "3 means 15:00 for Doctor <doctor_1>", the doctor's next two sitting days, 30-minute slots and last bookable time, never book outside timings |
| 3. Language Switching | Shared | All of it (11 languages, `change_language` tool, script rules, `default_language`, callback at `business_phone`) | One line: doctor names, specialties, hospital and medicine names stay in English letters |
| 4. Tone and Conversational Style | Shared base plus one healthcare line | Calm, kind, match pace, never push, acknowledge distress, `agent_gender` | "Many callers are worried, unwell or elderly" |
| 5. Output Format | Shared base plus healthcare-specific | Short spoken sentences, one question, punctuation, no filler praise, remember what was said, "yes, but…", "hello" mid-call, end-call line | Never take Sir, Madam, Doctor as the patient's name, never book with "Patient", say booked only after the tool confirms, never say cancelled, never check availability before booking, never interpret reports or ask for OTP or payment, share booking details only with patient name and booked number |
| 6. Main prompt | Industry-specific | The first lines (LANGUAGE) repeat section 3 | STEP 1 to STEP 6, CANCEL, DOCTOR LIST |
| How it opens / How it ends | Platform templates | Chosen by the business | None |

Answer to platform-contract.md open question 2: sections 1 to 5 are written per agent, with industry-specific lines inside them. An industry skill must therefore output all six sections, using a shared base text for the shared parts and adding its own lines. It cannot only write section 6.

## 2. Where our healthcare brief belongs in the 6 sections

| Platform part | Brief rules and scenarios that belong here | Present in the reference Starter text? |
|---|---|---|
| 1. Role & Identity | R-08 (AI line), R-11 (no medical advice), R-20/R-21 (never invent), R-09 (emergency, short form), R-25 (honest redirect); S-12, S-30 | Yes, but it lists 5 emergency signs, not our 12, and has no "never claim to be human" |
| 2. Date & Time | R-03 (weekday and date), R-39 (timings, never book outside), S-03, S-35, S-43, S-60 | Yes, plus rules we do not have (30-minute slots, 24-hour format) |
| 3. Language | R-06, S-13 | Yes |
| 4. Tone | R-33, R-28 (no pressure on elderly), S-08, S-36 | Yes. R-34 (discretion) is missing |
| 5. Output Format | R-32, R-05 (ask again), R-02 (remember, do not re-ask), R-26 (changes), R-04 (confirmation), R-14 (no report interpretation), R-22 (booking fails, short form) | Yes, partly |
| 6. Main prompt | R-01, R-02, R-04, R-10, R-12 to R-16, R-17 to R-19, R-23 to R-25, R-27, R-29 to R-31, R-35 to R-38, R-40, R-41 and the rest; S-01 to S-62 | Partly. See section 3 |
| Opening / closing templates | R-07 (inbound greeting), S-15 | The Welcome message is outbound, and Output Format fixes its own closing line. See conflicts 9 and 12 |

## 3. reference Starter's Main prompt, measured

| Measure | Value |
|---|---|
| Words in the Main prompt, excluding the roster expansion | 524 |
| Words in the roster expansion (4 doctors) | 91 |
| Sum | 615 (the platform's "long" warning shows 616) |
| Words per doctor in the roster | about 23 |

The 616-word warning counts the roster expansion. The budget of about 600 words therefore includes the doctors, and a clinic with more doctors leaves less room for our text.

Section word counts for the other parts: Welcome message 16, Role & Identity 452, Date & Time 412, Language Switching 209, Tone 140, Output Format 412, Main prompt 524. Total of all parts, excluding the roster: 2,165 words.

**Style**
- Labelled blocks: `LANGUAGE:`, `STEP 1:` to `STEP 6:`, `CANCEL:`, `DOCTOR LIST:`.
- Imperative and very short per rule: "Ask the day first if not given." "Only the named doctor."
- Fixed lines in quotes for the agent to say: "Shall I book it?", "Booking it now, please stay on the line."
- Hard "never" lines ("never skip a step", "never guess a surname").
- Mostly a flow of what to do next, not a list of policies. Variables appear as `@name`.

**What it covers**
- Language (any Indian-language word means switch).
- STEP 1: understand (new booking vs reschedule vs cancel).
- STEP 2: list doctors, never pick one for a problem.
- STEP 3: book (the day, timings, today, the doctor's next two days, on leave or on call, patient name, read-back, "Shall I book it?", tool, taken slots).
- STEP 4: reschedule.
- CANCEL: not possible, note the request.
- STEP 5: handoff (unlisted doctor, complaint, reports, pharmacy, billing, insurance).
- STEP 6: close (booked, WhatsApp or email confirmation, anything else, fee only if asked).
- DOCTOR LIST.

**What it does not cover.** Emergencies, AI disclosure, medical-advice limits, hospital info and the address are in section 1, not here. Not covered anywhere: self-harm, date of birth, minors alone, verification beyond name and booking number, prompt protection, claimed authority, "why do you need this", waiting-time promises.

## 4. Conflicts and gaps: reference Starter vs our brief

"Decision" means the owner decides. I have not resolved these.

| # | Topic | reference Starter | Our brief | Status |
|---|---|---|---|---|
| 1 | Emergency | 5 signs (chest pain, breathlessness, heavy bleeding, unconsciousness, accident). Says "1 0 8" or come to the 24/7 emergency. "Never book." | 12 signs, 108/112, transfer to on-duty staff, check every message (R-09) | reference Starter is narrower. Our skill must output ours |
| 2 | AI disclosure | Only if the caller clearly asks. Exact line. "Never use this line as a reply to anything else." | R-08 / B-01: same trigger (if asked), plus never claim to be human and keep saying so under pressure | Not a real conflict. Ours adds two things |
| 3 | Self-harm, Tele-MANAS 14416 | Missing | R-10 | Missing in reference Starter |
| 4 | Date of birth (R-36) | Missing. DOB is never used | R-36, R-12 | Missing in reference Starter |
| 5 | Verification (R-12) | "Share booking details only with the patient's name and booked number." Reschedule takes name, doctor, booked day and booking number | Registered phone plus name or DOB | **Decision** |
| 6 | Lone minor (R-40) | Missing. Asks only "for them or someone else" | R-40, S-61 | Missing in reference Starter |
| 7 | Other people's data (R-13) | Partly (the name plus booked number check) | R-13 | Partly present |
| 8 | Doctor On leave or On call | "Offer a callback." | Proposed R-41: offer another doctor of the same specialty or the next available day | **Decision** |
| 9 | Welcome message direction | Outbound ("I am calling from @company_name. Is this a good time to talk?") | Our R-07 forbids this wording for inbound. reference Starter's Role & Identity and Main prompt are an inbound flow ("first point of contact for callers") | **Inconsistent inside reference Starter.** Decision |
| 10 | Hard-coded values | See the next table | Our skill must use variables | reference Starter breaks the platform's own rule |
| 11 | Address | `clinic_address` exists, but Role & Identity types the address in full | Skill must use `{{var.clinic_address}}` | reference Starter breaks the rule |
| 12 | Closing | Output Format fixes the line "Thank you for calling @company_name. Have a good day." and ends the call | The platform's "How it ends" templates (Warm, Brief, Formal) should hold the closing, and the Main prompt must not duplicate it | **Decision.** Also the wording is inbound-only |
| 13 | Cancellation | No cancel tool. "You can't cancel." Take name, doctor, day and say the clinic will confirm. "Never say cancelled" | Our S-05 cancels after verification | Update our brief |
| 14 | Availability | "Never check availability before booking." Any time inside the doctor's timings can be offered. Never say unavailable unless the tool said so. If taken, offer the tool's 2 nearest free times | R-21: offer only slots the system confirms | **Decision.** The two conflict |
| 15 | Symptom to doctor | Role & Identity: "never recommend a doctor for a condition". STEP 2: "say the related specialties; never pick a doctor" | R-37 / S-59: suggest the specialty and its doctors, in neutral wording | **Decision** |
| 16 | Reports | STEP 5 transfers report questions. Output Format: "never interpret reports" | R-14: say ready or not ready and how to collect | **Decision** |
| 17 | Pharmacy, billing, insurance | Transfer, or offer a callback | R-25: politely redirect, do not handle | Same intent. The business decides if it has a pharmacy |
| 18 | Slot length | Fixed 30-minute slots. Last bookable time is the end time minus 30 minutes | Not in the brief | Add to the brief |
| 19 | "Why do you need this?" (R-17) | Missing | R-17 | Missing in reference Starter |
| 20 | Prompt protection, claimed authority, emergency plus pressure (R-29, R-30, R-31) | Missing | Critical rules | Missing in reference Starter |
| 21 | Waiting-time promises (R-35) | Not stated | R-35 | Missing in reference Starter |
| 22 | Booking failure (R-22) | "Apologise and say reception will call to confirm." No retry, no log tool | Retry once, collect details, log the failure | Partly present. No logging tool |
| 23 | Data asked | Patient name in English, "for them or someone else", doctor, day, time, WhatsApp number or email | R-16 also allows a one-line reason and the insurer name | Fine. Ours is a permission |
| 24 | Multiple shifts | The roster shows one time range per day | R-39 and S-67: several shifts a day | Check the roster format |
| 25 | Reschedule | Needs the booking number | Not in the brief | Add to the brief |

### Hard-coded values in the reference Starter texts

The platform rule says prompts use variables and never hard-code business values. Our skill must not copy any of these.

| Where | Hard-coded |
|---|---|
| Role & Identity | The clinic address (the `clinic_address` variable exists), "20+ years of experience and 55+ beds", the list of hospital services, the example "Doctor <doctor_2>, is that right?" |
| Date & Time | "Doctor <doctor_1>, 3 means 15:00", "Doctor <doctor_3> ends at 2 PM", Kannada, Hindi and Tamil example timings and ₹500 |
| Main prompt, STEP 2 | All four doctors with their specialties typed out, although `@roster` follows |
| Main prompt, STEP 3 | A Kannada example naming Doctor <doctor_1> and her timings |
| Output Format | The closing line (see conflict 12) |

## 5. Real-call fixes in reference Starter that should become eval tests

These are rules that exist because real calls went wrong. Each should become at least one eval check, written from the brief once the brief includes it. Type: P = prompt check (the prompt contains the instruction), B = behaviour check (the agent's reply to a probe).

| # | Real-call fix | Section | Type |
|---|---|---|---|
| 1 | Caller says "hello" mid-call: say you are here and repeat the last question; never restart or forget what they said | 5 | B |
| 2 | "Yes, but…" is not a yes: answer the question first, then check again before booking or sending | 5 | B |
| 3 | Never take "Sir", "Madam", "Doctor", "Hello" or a doctor's name as the patient's name | 5 | B |
| 4 | Never book with "Patient" or any placeholder as the name | 5 | B |
| 5 | Say "booked" only after the tool confirms | 5, 6 | B |
| 6 | Never say "cancelled". Say the request is noted and the clinic will confirm | 5, 6 | B |
| 7 | Never check availability before booking | 5 | P |
| 8 | Give the doctor's from and to time and ask what time suits. No slot lists | 6 | B |
| 9 | Fillers alone ("haan", "hmm", "theek hai", "sari", "houdu") do not switch language | 3 | B |
| 10 | Any Indian-language word (even "Book ಮಾಡಬೇಡಿ") switches language and calls `change_language` first | 3, 6 | B |
| 11 | Indian-language replies write numbers as words, with no AM or PM | 2 | B |
| 12 | Keep the caller's English words in English letters. Never add your own English words | 3 | B |
| 13 | Appointments are 30 minutes. Last bookable time is end time minus 30 minutes. Offer it if the caller asks for the end time or later | 2 | B |
| 14 | A time without morning or evening means the one inside the doctor's timings. If both fit, ask. If neither, say so | 2 | B |
| 15 | Send time to the tool in 24-hour format | 2 | P |
| 16 | Never offer a time that has passed today, or a day the doctor does not sit. Offer the next two sitting days with dates | 2, 6 | B |
| 17 | Read dates off `now_local`. Say weekday and date together. Never say the year | 2 | B |
| 18 | Phone number in two groups of 5 digits with a pause. "Dr." is "Doctor", "OTP" is "O T P" | 2 | B |
| 19 | One question at a time. One or two short sentences. No lists, no filler praise, no two turns opening with the same word | 5 | B |
| 20 | Do not ask again for something already said. If the caller changes one thing, update only that | 5 | B |
| 21 | Emergency: say "1 0 8" or the 24/7 emergency. Never book | 1 | B |
| 22 | AI line only when clearly asked. Never use it as a reply to anything else | 1 | B |
| 23 | Never invent a doctor, slot, fee or service. A hospital service is not a doctor | 1 | B |
| 24 | If a doctor name is unclear, confirm the part you heard. Never guess a surname | 1, 6 | B |
| 25 | If the caller says "book", it is a new booking. Never ask "new or change?" | 6 | B |
| 26 | Never interpret reports. Never ask for an OTP or payment | 5 | B |
| 27 | Share booking details only with the patient's name and booked number | 5 | B |
| 28 | WhatsApp: ask if the calling number is on WhatsApp, never say the number aloud. Email: read the address back. Then send without waiting | 6 | B |
| 29 | If booking fails: apologise and say reception will call. If the slot is taken: offer the tool's 2 nearest free times and book the pick without asking again | 5, 6 | B |
| 30 | Doctor On leave or on call: offer a callback (pending the decision in conflict 8) | 6 | B |
| 31 | When the caller is done, say the closing line and use the end call tool | 5 | B |
| 32 | Accept a decline the first time. Acknowledge distress in one short sentence | 4 | B |
| 33 | Cancellation: accept the first time, ask why at most once, take name, doctor and day | 6 | B |
| 34 | Give the fee only if asked, not when confirming the booking | 6 | B |
| 35 | Use the grammar matching `agent_gender` and gender-neutral forms for the caller | 4 | P |

## 6. Missing from our brief (proposed IDs, not yet added)

IDs continue from S-63 and R-41. Part 4 conflicts 8, 14, 15 and 16 must be decided before R-41 and the related rules are final.

| ID | Scenario | Expected behaviour |
|---|---|---|
| S-63 | Requested doctor's status is On leave | Say the doctor is unavailable. reference Starter offers a callback. We proposed another doctor of the same specialty or the next available day. **Decision** (conflict 8). Never book |
| S-64 | Requested doctor's status is On call | Same as S-63. What "On call" means for booking is an open question |
| S-65 | Caller asks about fees, or asks for a discount | Quote the fee from the roster only. Never estimate, round or negotiate |
| S-66 | Caller asks about a doctor | Share the roster's "about" text only. Never add or exaggerate, and never turn it into a medical claim |
| S-67 | Caller asks for a time between a doctor's shifts | Name the shifts and offer a time inside one. Never book outside |
| S-68 | Outbound: appointment reminder | Open with the outbound template and ask if it is a good time. After confirming it is the patient, give the details and ask whether they will attend |
| S-69 | Outbound: patient wants to reschedule | After identity is confirmed, follow the normal booking flow |
| S-70 | Outbound: follow-up call | Scheduling only. No clinical talk |
| S-71 | Outbound: wrong person answers | Share nothing about the patient or the appointment. Apologise and end politely |
| S-72 | Outbound: bad time to talk | Offer a callback time or end politely |
| S-73 | Outbound: voicemail or no answer | Leave no health details. Leave only the clinic name and a request to call back on `{{var.business_phone}}` |
| S-74 | Outbound: "who gave you my number?" | Say it is the number on the patient's record. Never invent a source. Offer to pass a stop-calling request to staff |

| ID | Rule | Severity |
|---|---|---|
| R-41 | Never offer or book a doctor whose roster status is On leave or On call. What to offer instead is pending conflict 8 | major |
| R-42 | State a doctor's fee only from the roster. Never estimate, round, discount or negotiate it. If missing, say staff will confirm | critical |
| R-43 | Share a doctor's "about" text only as written. Never exaggerate it or present it as a medical claim | major |
| R-44 | On an outbound call, confirm the person is the patient (or the guardian of a patient under 18) before sharing any appointment detail. If it is someone else, share nothing | critical |
| R-45 | On a voicemail or no answer, never leave health details, a doctor's name, a specialty or an appointment detail. Leave only the clinic name and a callback request | critical |
| R-46 | At the start of an outbound call, ask whether it is a good time. If not, offer a callback time or end politely | major |
| R-47 | If asked how the clinic got the number, say it is the number on the patient's record. Never invent a source. Pass stop-calling requests to staff | major |

New items from the real texts, with no IDs yet (add after the decisions): 30-minute slots and the last bookable time, the doctor's next two sitting days, reschedule needs the booking number, cancellation is noted (no cancel tool), "hello" mid-call, "yes, but…", patient name rules, fillers do not switch language, Indian-language number words.

Changes to existing items:
- R-39 and S-60 already cover shifts. Reword R-39 for several shifts a day.
- S-05 and the brief's cancel flow: no cancel tool. See conflict 13.
- R-20 and S-23 already cover fees from config. R-42 narrows this to the roster fee.

Open questions added: what "On call" means for booking, whether the agent states it is an AI on an outbound call without being asked, how a stop-calling request is recorded, what a voicemail may say.

## 7. Other mismatches with our current skill output

Compared with outputs/healthcare/sample-prompt.md and `.claude/skills/healthcare-prompt-writer/`.

| # | Platform expects | Our skill outputs today | Fix needed |
|---|---|---|---|
| 1 | Six sections, each with shared and industry lines (part 1 above) | One prompt of 16 sections | Output the six platform sections |
| 2 | About 600 words including the roster expansion | 1,779 words, with the roster typed in | Compress. docs/shared/proposals/healthcare-main-prompt-reference-style.md shows 517 words of our own text for all 18 critical rules, 608 with a 4-doctor roster |
| 3 | `{{var.<name>}}` | `{{hospital_name}}`, `{{persona_name}}`, `{{doctors}}`, `{{transfer_target}}` and others | Use `{{var.agent_name}}`, `{{var.company_name}}`, `{{var.roster}}`, `{{var.business_hours}}`, `{{var.business_phone}}`, `{{var.clinic_address}}`, `{{var.default_language}}` |
| 4 | No hard-coded business values | The sample prompt inlines the clinic, persona name and three doctors | Reference variables only |
| 5 | Welcome message, opening and closing from templates | The skill writes its own Opening and Closing | Remove both |
| 6 | Date, language, tone and output-format content in their own sections | The skill repeats it in the Main prompt | Move it to the right section, once |
| 7 | `now_local` for dates | Not used, so "tomorrow" cannot become a date | Use `{{var.now_local}}` |
| 8 | Roster with status, specialty, fees (₹), about and shifts | Skill's roster has name, specialty, days and shifts only | Read all fields from the roster |
| 9 | `business_hours`, `business_phone`, `clinic_address` | "Staff will confirm" for timings and location | Use the variables |
| 10 | Inbound and outbound | Inbound only | Add an outbound branch (S-68 to S-74, R-44 to R-47) |
| 11 | Voice only | Includes chat handling | Drop chat lines from the platform output |
| 12 | `agent_name` and `agent_gender` | Free-text persona, no gender | Use both |
| 13 | Config limited to the listed fields plus custom details | Skill needs an emergency signs list, a minors flag, a transfer target, an ambulance number | Put them in custom details if a list or flag can be stored (platform-contract.md open question 6) |
| 14 | Tools: booking, reschedule, change_language, end_call, transfer, WhatsApp/email send. No cancel tool | Skill assumes cancel, a log action and a booking-system "tool" with unspecified names | Name the real tools. Remove cancel. Drop "log the failure" or confirm a log action |
| 15 | Conflicts and customer additions outside the prompt | A conflicts list at the end of the same file | Return conflicts separately |
