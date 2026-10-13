**Assumptions and defaults used**
- Languages not given: call starts in `{{var.default_language}}`; the 11 platform languages are handled by section 3 (intake default).
- Emergency department not given: `{{var.emergency_department}}` defaulted to "no"; section 1 uses the adapted line "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now." (R-09).
- Emergency transfer number not given: instead of transferring to on-duty staff, the emergency and self-harm lines offer a callback during `{{var.business_hours}}` (R-81).
- Address not given: `{{var.clinic_address}}` is referenced only for directions when asked; no value was invented, and the client fills it in later.
- No custom details given: `{{var.emergency_signs_extra}}` left empty (default sign list only, never removed), `{{var.minors_may_book_alone}}` defaulted to false (R-40 as written), `{{var.business_info}}` left empty (agent says "the team will confirm" for services, beds or years of service).
- Confirmation channels not given: the confirmation flow (R-18) is skipped entirely; section 5 offers no WhatsApp or email confirmation.
- Booking style (time slots) and roster size (2 doctors) were given explicitly, not assumed.

**Refused or adapted client requests**
- none — the client gave no specific requests beyond "book appointments and answer questions"; every unspecified item used the intake table's documented default instead of an invented value.

**Open questions**
- Business hours: `{{var.business_hours}}` is referenced throughout but the actual hours must still be set in the platform's business config.
- Whether this clinic will have an emergency department and a transfer number needs a decision; defaults above apply until then.
- Clinic address not given — add `{{var.clinic_address}}` under Your business if directions should be offered.
- The default emergency signs list still needs review by the client's clinical team (standing note, R-09).

**Word counts**
- Welcome: 13. Section 1: 746. Section 2: 243. Section 3: 173. Section 4: 150. Section 5: 925.
- Section 6: 336 words. Roster: 2 doctors x 23 = 46. Allowance: 615 - 46 = 569. Status: within budget (margin 233 words below the allowance).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | given as a variable only, no value stated | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided (small clinic) | automatically from Variables |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| Doctors | 2 doctors stated: Doctor A (General Physician), Doctor B (Paediatrics) | Doctors |

No `{{var.confirmation_channels}}` was given, so the confirmation flow was left out of the Instructions; the customer can still set up the After-the-call trigger for WhatsApp and email on the platform if they later add this detail.
