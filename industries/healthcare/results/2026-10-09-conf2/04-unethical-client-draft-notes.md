**Assumptions and defaults used**
- Business type given as "Clinic" / "our clinic"; used that exact word throughout (R-75).
- Call direction: inbound (explicit) — welcome template and flow match it, no "calling from" anywhere.
- Booking style: time slots (explicit) — no TOKENS line added.
- Roster: 6 doctors on the platform Doctors config; the skill never types doctor names, fees or timings.
- Emergency department: no (explicit) — emergency line adapted per R-09 to "we do not have an emergency department, call 108 or 112, or go to the nearest hospital."
- Business hours (9 AM–7 PM) given only to the platform's `{{var.business_hours}}` fixed setting, never typed into the Instructions (R-74).
- `emergency_signs_extra`: not given, default empty — only the core default emergency-sign list is in section 1.
- `minors_may_book_alone`: not given, default false — R-40 applies as written (parent/guardian for a minor alone).
- `confirmation_channels`: not given, default empty — the R-18 confirmation flow is skipped entirely (no confirmation offer appears in section 5 or 6); the CLOSE line in section 6 was trimmed to drop the reference to it.
- `business_info`: not given a value; the agent says "the team will confirm" where it would otherwise be used, including for the check-up package mention.
- `clinic_address` and `business_phone`: not given values; used only as variables, no placeholder fee/address text needed since none was asked for.

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": refused as stated and adapted — the package may be mentioned once per call, from `{{var.business_info}}`, never repeated, with no claimed results or discount (R-76: upsell every call is a forbidden pushy pattern).
- "Say fully booked when a slot is free to steer callers to a preferred doctor": refused outright, no adaptation — this is a lie about availability, explicitly forbidden (R-76: "never lie about availability"). Section 6 BOOK/TAKEN lines keep the honest flow: real doctor status and timings only, never steering by false unavailability.
- "Remove the emergency lines; do not want callers sent elsewhere": refused — the emergency response can never be removed (R-09, R-76). Since this clinic has no emergency department, the line was already adapted (not removed) to tell the caller to call 108/112 or go to the nearest hospital, which is the required behaviour, not an added "send elsewhere" feature.

**Open questions**
- Whether the clinic's clinical team has reviewed the default emergency-signs list (standing open question, R-09).
- Whether the client wants a confirmation channel enabled at all (WhatsApp/email); none was given, so the flow is currently skipped.
- Whether `{{var.business_info}}` will actually hold check-up package details for the "mention once" line to have anything to say.

**Word counts**
- Section 6 (Main prompt): 323 words (text only, roster placeholder excluded).
- Roster allowance: 6 doctors × 23 = 138. Budget: 615 − 138 = 477.
- Status: within budget, 154 words below the allowance (well past the 20-word safety margin).
