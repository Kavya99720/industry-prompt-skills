**Assumptions and defaults used**
- Business type "single-doctor clinic" → business word "our clinic" everywhere except where the caller hears the name (R-75).
- Workflow 01 (Enquiry) only, per the profile; no Booking, Reschedule or Cancel lines in section 6.
- Booking style tokens/walk-in → the TOKENS main-prompt line added and no timed booking is ever offered (R-78).
- Roster: 1 doctor (General Physician); doctor name, specialty and fee come only from `{{var.roster}}`, never typed.
- `{{var.emergency_department}}` = no → emergency line adapted to "we do not have an emergency department, call 108 or 112" (R-09); nothing else in the default emergency list was removed.
- `{{var.default_language}}` = Hindi, since callers speak Hindi; the value itself is not written into the Instructions.
- `{{var.confirmation_channels}}` not given → no confirmation flow written (per rule: skip it if unset); also moot here since workflow 01 has no booking tool to confirm.
- `{{var.minors_may_book_alone}}` not given → default false used (R-40 as written).
- `{{var.emergency_signs_extra}}` not given → default signs list only, nothing added.
- `{{var.business_info}}` assumed to carry the OPD-timings/token explanation mentioned in the profile; its text is never typed into the Instructions (R-74).
- `{{var.agent_name}}` and `{{var.agent_gender}}` not given → left to Voice settings, no value invented.

**Refused or adapted client requests**
- none. Both client requirements ("tell callers the OPD timings and how tokens work", "never promise a time") are already satisfied word-for-word by the core WAIT line and the workflow's TOKENS line, so no rule conflict arose.

**Open questions**
- Whether `{{var.business_info}}` will actually be filled in on the platform with the OPD timings and the token-system explanation before go-live.
- Whether the roster's specialty label (e.g. "General Physician") reads naturally in the R-37 symptom-routing line once spoken in Hindi.
- `{{var.agent_name}}` and `{{var.agent_gender}}` still need to be set in Voice settings.

**Word counts**
- Welcome: 13. Section 1: ~675. Section 2: ~186. Section 3: ~173. Section 4: ~148. Section 5: ~471. (Sections 1–5 do not count against the Main-prompt budget.)
- Section 6: 169 words. Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget (169 words, 423 words under the allowance — far past the required 20-word margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | Hindi | Voice settings |
| `{{var.business_hours}}` | OPD morning and evening (exact hours not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | 1 doctor: Doctor A, General Physician; fee not provided | Doctors |
| `{{var.emergency_signs_extra}}` | none given | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not given (defaults false) | Your business, Add a detail |
| `{{var.business_info}}` | OPD timings and token-system explanation (exact text not provided) | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
```
