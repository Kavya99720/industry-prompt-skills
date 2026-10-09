# Platform contract: what an industry skill must output

Source: the CellAssist Voice platform, using the <business_name> healthcare Starter as the reference (docs/shared/reference/reference-starter.md, which holds the real texts).

This file records the platform's format as it was described to us. Where the exact platform text is not yet in the repo, the section says so. Nothing here changes a skill. The mismatches between this contract and our current healthcare skill are in docs/shared/platform-gap-analysis.md.

## 1. Instructions format (the Instructions page)

An agent's instructions are made of these parts, in this order:

| Part | Notes |
|---|---|
| Welcome message | Marked "fixed". The platform sets it. Our skills do not write it. |
| 1. Role & Identity | |
| 2. Date & Time — TTS Rules | How dates, times and numbers are spoken. |
| 3. Language Switching | |
| 4. Tone and Conversational Style | |
| 5. Output Format | |
| 6. Main prompt | The industry-specific part. |

**How these compose.** The platform combines the sections into one final prompt. The Instructions page has a "How these compose" explanation and a "Composed preview" of the combined prompt. Content in one section therefore must not repeat content in another.

**Length budget.** The Main prompt shows a "long" warning at 616 words. The count includes the roster expansion: reference Starter's Main prompt is 524 words and its 4-doctor roster expansion is 91 words, which sums to 615. Each doctor uses about 23 words. Our rule: a generated Main prompt, with its roster expansion, stays under about 600 words.
- Critical rules are always included in full.
- All other rules and scenarios are summarised to fit.
- Anything already covered by sections 1 to 5, by the welcome message, or by the opening and closing templates (section 3 below) is left out of the Main prompt.

**Lookups.** The platform has a Lookups feature. It currently has 0 entries. See open questions.

**Section content.** The real reference Starter texts show that sections 1 to 5 contain industry-specific lines as well as shared text (see docs/shared/platform-gap-analysis.md, part 1). A skill therefore writes all six sections, not only the Main prompt. In the platform UI, an @ prefix in front of a variable name stands for the full variable syntax, and the roster variable inserts the doctor list automatically. Generated text always uses the full syntax.

## 2. Variables

Syntax: `{{var.<name>}}`.

| Group | Variables |
|---|---|
| Voice settings | `agent_name`, `agent_gender`, `default_language` |
| Fixed (business) | `business_hours`, `business_phone`, `clinic_address`, `company_name`, plus any custom details added with "Add a detail" |
| Built in | `now_local` (date and time of the call), `roster` (the calendar list of doctors) |

**Rule: prompts use variables and never hard-code business values.** This covers names, hours, phone numbers, addresses, fees and timings.

## 3. Business config (the Try it page)

**Your business**
- Business hours, business phone, clinic address, clinic name.
- Custom details, added one at a time.

**Doctors list.** Per doctor:
- Name.
- Status: Available, On call or On leave.
- Specialty.
- Fees (₹).
- About: a short bio.
- Working hours: days plus time. A doctor can have several shifts, added with "Add a shift".

Prompts reference doctor data from the platform (the roster and config). They never hard-code doctor names, fees, timings or bios.

**How it opens.** The agent opens with a template chosen by the business: Standard, Warm or Brief. There is also an outbound template: "Hello, this is <agent> calling from <company>. Is this a good time to talk?"

**How it ends.** The agent closes with a template chosen by the business: Warm, Brief or Formal.

The Main prompt must not duplicate the opening or the closing.

**Call direction.** The platform supports inbound and outbound calls.

## 3a. Platform tools

Confirmed from the reference Starter texts:

| Tool | Use |
|---|---|
| booking | Book an appointment. Time is sent in 24-hour format. Booking is said only after the tool confirms |
| reschedule | Change a booked appointment (needs patient name, doctor, booked day, booking number) |
| change_language | Called first when the caller switches to a supported language |
| end_call | Ends the call after the closing line |
| transfer | Transfers the caller to the team |
| (After the call trigger) | Confirmations and links are NOT sent by an in-call tool. The platform's "After the call" trigger sends them once the call ends (corrected 2026-10-09). The agent only asks for the channel, confirms it (and reads an email address back) aloud, and says that the message will arrive shortly |

There is **no cancel tool**. Cancellations are noted for the clinic: the agent takes the patient's name, doctor and day and says the clinic will confirm. There is no confirmed tool for logging a failure or for leaving a voicemail.

Supported languages: English, Hindi, Bengali, Kannada, Telugu, Marathi, Punjabi, Tamil, Gujarati, Malayalam, Odia.

## 4. Open questions

1. **Lookups.** What are Lookups for, and should any industry skill use them? There are 0 today.
2. ~~Sections 1 to 5.~~ Answered by the real texts: each skill writes all six sections, with a shared base plus industry lines (gap analysis, part 1).
3. **How these compose.** The tooltip text has not been captured yet. The other reference Starter texts are in the reference file.
4. **Doctor status.** What does "On call" mean for booking? reference Starter says only "on leave or on call: offer a callback". Our proposed R-41 differs (gap analysis, conflict 8).
5. **Platform actions.** Confirmed tools: booking, reschedule, change_language, end_call, transfer, and a WhatsApp or email send. There is no cancel tool. Still unconfirmed: logging a failed booking, leaving a voicemail on an outbound call, and whether a patient or booking can be looked up to check status or identity. Our brief items that assume more (S-05 cancel with verification, R-22 "log the failure") must change or be confirmed.
6. **Custom details.** Can a custom detail hold a list (an emergency signs list) or a flag (minors may book alone)? The healthcare skill needs both.
7. **Agent gender.** reference Starter says to use the grammar matching `agent_gender` where a language requires it and gender-neutral forms for the caller. How the skill should apply this beyond that line is open.
8. **Outbound details.** How does an outbound call get the patient's name, the appointment and the reason? Is voicemail or no-answer detected by the platform? reference Starter's Welcome message is outbound while its Main prompt is an inbound flow (gap analysis, conflict 9).
9. ~~Length.~~ Answered: the 616-word warning counts the Main prompt plus the roster expansion. Whether it is a hard limit or only a warning is still unknown.

## 5. Questions for lead

Still open after the 2026-10-08 decisions. Grouped by who can answer. Resolved on 2026-10-08 and no longer open: "both directions" means two separate Instructions sets (inbound and outbound); in-patient and ward questions are out of Phase 1 and are transferred to staff.

**Platform team**
1. **Custom details.** Can a custom detail hold a list (extra emergency signs)? Fallback: the default list is always in the prompt, and the client's additions are listed in the draft notes.
2. **"How it ends" templates.** How do Warm, Brief and Formal combine with a closing line kept in Output Format (R-68)? And the "How these compose" tooltip text.
3. **Voicemail.** Does the platform detect voicemail or no answer and tell the agent?
4. **Do-not-call.** Is there a do-not-call tool? Until then the agent never says a stop-calling request is done (R-73).
5. **Outbound call data.** Does the platform pass the patient's name and the appointment (`patient_name`, `appointment_details`, both marked unconfirmed in variables.json)?
6. **Tokens and walk-in.** Is there a token tool? Until then the agent never books a timed slot for these clinics (R-78).
7. **Lookups** (0 entries today), whether the 616-word warning is a hard limit, and how several shifts per day appear in the roster.

**Legal or product lead**
8. Must outbound calls say "an AI assistant" up front? Default if confirmed: add it to the outbound welcome.
9. Outbound closing wording (R-68) is a proposal and needs sign-off.

**Clinical and compliance**
10. The default emergency signs list needs review by the client's clinical team.
11. The exact DPDP provisions for notice, purpose and minimisation, to be confirmed by the industry expert.

**Pharmacy (added 2026-10-09)**
12. **Stock tool fields.** Does `check_stock` return in stock, price, prescription needed and controlled? Until confirmed the agent treats a missing flag as prescription-needed and hands off to the pharmacist (R-12).
13. **After-the-call trigger.** What does it read: the call transcript, or extracted fields (channel, email address, order number)? How does it know the chosen channel and the confirmed email address? Until answered, the agent states the channel and reads the email back aloud in the conversation (R-76).
14. **Voicemail.** Does the platform detect voicemail or no answer on outbound refill reminders? Until then R-59 applies as written.
15. **Do-not-call.** Is there a do-not-call tool? Until then the agent never says a stop-calling request is done (R-62).
16. **Outbound AI disclosure.** Must outbound refill reminders say "an AI assistant" up front? Default: follow the client's welcome template and answer honestly if asked (R-06).
17. **Skill configuration.** Should the skill also write the After-the-call trigger's configuration (what to send, to which channel), not only the Instructions?

**Banking (added 2026-10-09)**
18. **Which banking tools exist?** A card-block tool (`card_block_tool`), a balance and transactions lookup (`balance_lookup_tool`), caller verification against records (name, registered mobile, last 4 digits), KYC status. v1 assumes none: both tools default off, no account data is shared, and card blocking goes to the fraud desk.
19. **Legal references.** RBI rules, grievance timelines, banking ombudsman wording and KYC norms: for an industry expert. Prompts quote no timeline unless the client configures it.
