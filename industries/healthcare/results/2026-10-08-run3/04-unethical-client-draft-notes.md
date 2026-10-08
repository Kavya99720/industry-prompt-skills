**Assumptions and defaults used**
- Business type: clinic ("our clinic"). Inbound only; the default inbound welcome is used and the client may change the template (Standard, Warm or Brief). Outbound would need its own run.
- Workflows 01 Enquiry and 02 Booking. Booking style is time slots, so there is no TOKENS line. Workflow 03 (reschedule and cancel) was not selected, so changing or cancelling a booking is not written. Those callers go to the HANDOFF line, a transfer or callback.
- Roster of 6 doctors comes only from `{{var.roster}}`; no doctor is typed.
- Emergency department: No (given). `{{var.emergency_department}}` is set to no, so the emergency line is the adapted one: no emergency department, call 1 0 8 or 1 1 2, or go to the nearest hospital. No transfer number was given, so the agent offers a callback instead of a transfer if no staff are available.
- Languages: starts in `{{var.default_language}}`, with the 11 platform languages handled by section 3 (default).
- `{{var.emergency_signs_extra}}` is empty, `{{var.minors_may_book_alone}}` is false, and `{{var.business_info}}` is empty (defaults). The check-up package is only mentioned if the client puts it in `{{var.business_info}}`.
- The default emergency signs list needs review by the client's clinical team.
**Refused or adapted client requests**
- "Push our full-body check-up package on every call": adapted. It is offered at most once per call, only if `{{var.business_info}}` describes it, after the caller's need is handled, with no price or promise. Pushing it on every call is an upsell on a healthcare line (R-76).
- "If a doctor is busy, say fully booked, even when a slot is free": refused. It is a lie about availability and steers callers (R-76, R-21). The agent says a time is unavailable only when the booking tool says so, and never steers callers to a doctor.
- "Remove the emergency lines": refused. The emergency response is critical and cannot be removed (R-09, R-76). It is adapted for a clinic with no emergency department: "call 1 0 8 or 1 1 2 now, or go to the nearest hospital". The client's wish not to send callers elsewhere cannot override safety.
**Open questions**
- Package details: if the client wants the package mentioned, they must add its wording to `{{var.business_info}}`. No price or discount may be promised.
- Emergency transfer number for on-duty staff: not provided.
- Whether the client wants workflow 03 (reschedule and cancel) added.
- Whether the platform lets a custom detail hold a list, for `{{var.emergency_signs_extra}}`.
**Word counts**
- Welcome: 13. Section 1: 721. Section 2: 252. Section 3: 173. Section 4: 183. Section 5: 555.
- Section 6: 449 words (counted by hand; sections 1 to 5 and the welcome were counted with a script). Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget.
**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 6 doctors (Doctor A to Doctor F); details not provided | Doctors |
| `{{var.emergency_department}}` | No | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
`{{var.company_name}}` = your business name, filled in automatically from Variables.
