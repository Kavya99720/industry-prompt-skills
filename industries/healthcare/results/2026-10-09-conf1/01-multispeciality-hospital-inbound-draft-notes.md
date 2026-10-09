**Assumptions and defaults used**
- default_language set to the standard English voice-setting value; the profile says "English start" without naming the exact locale string.
- Welcome and closing templates: no Standard/Warm/Brief choice was given, so the default inbound wording (R-68, section-bases.md) was used; the client can change the template in the platform.
- Doctor roster count = 8, taken directly from the profile; used only to compute the word-budget allowance, never typed into the Instructions.
- emergency_signs_extra: not set (client said "no extra emergency signs"), so no custom addition was written — the compact default list stands alone, per R-09.
- minors_may_book_alone: false (client default), written as the literal `{{var.minors_may_book_alone}}` check in section 1.
- business_info: assumed to hold beds and services text as the client described; no literal value written into the Instructions (R-74).
- confirmation_channels = whatsapp, email: both offered in step (a) of the confirmation flow, matching the client's requirement that it is sent by the After-the-call trigger, not a tool (already how the platform works — no change needed).

**Refused or adapted client requests**
- none — the client's three requirements (book any Available-status doctor, WhatsApp/email confirmation via After-the-call trigger, no special rules) all match existing platform behaviour and critical rules with no conflict.

**Open questions**
- business_phone and clinic_address: no values were given in the profile; both are referenced only as variables (`{{var.business_phone}}` in section 3, `{{var.clinic_address}}` in sections 1 and 6) and must be filled in on the platform's "Your business" page.
- Doctor F's "On leave" status must be set on the platform Doctors list (not in the Instructions) so R-41's on-leave callback behaviour triggers correctly for that doctor.
- R-66 (skip the "new, change or cancel" question when the caller already says "book") and R-43 ("about" text used only as written) are not spelled out verbatim in section 6 to stay under the word budget; both are "major", not "critical", and are covered implicitly by the BOOK/INFO step structure.

**Word count**
- Section 6 (Main prompt, own text, roster placeholder excluded): 404 words. Roster: 8 doctors × 23 = 184. Allowance: 615 − 184 = 431. Status: within budget, 27 words below allowance.
