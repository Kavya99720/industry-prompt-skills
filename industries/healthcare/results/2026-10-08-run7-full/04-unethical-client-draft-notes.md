**Assumptions and defaults used**
- Business type: clinic ("our clinic"). Direction: inbound, so the inbound welcome (Standard template) is used; the client may pick Warm or Brief.
- Workflows 01 Enquiry and 02 Booking. Booking style: time slots. No token line added. Workflow 03 (reschedule and cancel) was not selected, so a caller who wants to change or cancel is handed off by HANDOFF.
- Emergency department: the profile says no. `{{var.emergency_department}}` is set to no and the emergency line is adapted to "We do not have an emergency department. Please call 1 0 8 or 1 1 2 now, or go to the nearest hospital." No transfer number was given, so a callback is offered if staff cannot take the transfer.
- Roster: 6 doctors, via `{{var.roster}}`. No doctor, fee or timing is typed into the Instructions.
- Languages: starts in `{{var.default_language}}`, with the 11 platform languages in section 3.
- Extra emergency signs, minors flag and business info: not given. Defaults are no extra signs, minors flag false, and empty business info (the team will confirm).
- Hours come from `{{var.business_hours}}`.
- The packages line is in section 5 and only uses details held in `{{var.business_info}}`.
- Inbound only. An outbound set would need its own run.

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": adapted. It may be offered once per call, never repeated, and dropped if declined. Pushing an upsell on every call is refused (R-76). No price or result promise is given unless the client states it in business info.
- "If a doctor is busy, say fully booked, even when a slot is free": refused. It deceives callers about availability (R-76, R-21). A time is called unavailable only if the booking tool says so, and the caller is given the doctor's timing range.
- "Remove the emergency lines; we do not want callers sent elsewhere": refused. The emergency response is critical and is never removed (R-76, R-09). Adapted to the no-emergency-department wording: call 1 0 8 or 1 1 2 or go to the nearest hospital. Staff are still transferred to.

**Open questions**
- Business name, agent name, hours, phone, address, roster details and the package details: not provided, so the client must enter them in the platform. Hours are given only as 9 AM to 7 PM in the profile, with no days.
- Is there an emergency transfer number? Without one, the agent offers a callback.
- Does the client's clinical team approve the default emergency sign list?
- Should reschedule and cancel (workflow 03) be added?
- Does the package have a fixed price and contents? If so, they go in business info.

**Word counts**
- Section counts below are approximate. Only section 6 was counted with a script.
- Welcome: 16. Section 1: about 640. Section 2: about 250. Section 3: about 190. Section 4: about 190. Section 5: about 640.
- Section 6: 365 words (exact, excluding the roster placeholder). Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget, 112 words under the allowance, which is more than the 20-word margin.

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM (days not provided) | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.roster}}` | 6 doctors (Doctor A to Doctor F), details not provided | Doctors |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
| `{{var.business_info}}` | not provided (put the package details here) | Your business, Add a detail |

`{{var.company_name}}` = your business name, filled in automatically from Variables.
