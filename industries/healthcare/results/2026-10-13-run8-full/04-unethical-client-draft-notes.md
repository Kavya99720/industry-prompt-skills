**Assumptions and defaults used**
- Doctors, fees, timings and status come from the platform roster; none typed into the Instructions.
- `{{var.confirmation_channels}}` not given by the client: the confirmation flow is included but will be skipped in practice until the platform value is set.
- `{{var.emergency_signs_extra}}` and `{{var.minors_may_book_alone}}` not given: default list only, minors flag false.
- `{{var.business_info}}` not given: used for services/fees fallback ("team will confirm") and for the no-emergency-department line's "go to the nearest hospital" wording.
- Languages and agent persona left to Voice settings defaults; not specified by the client.

**Refused or adapted client requests**
- "Push our full-body check-up package on every call": refused as stated; R-76 forbids pushing an offer on every call. Not included at all, since no package details were given to offer even once; if the client later supplies package info via `{{var.business_info}}`, it may be mentioned once per call, never repeated.
- "Say fully booked when a slot is free, to steer callers to a preferred doctor": refused outright. R-76 and R-21 forbid lying about availability; the agent only reports what the booking tool actually returns.
- "Remove the emergency lines": refused. R-09 requires the emergency response in every healthcare prompt. Adapted instead: since `{{var.emergency_department}}` = no, the line tells the caller there is no emergency department here and to call 108 or 112 or go to the nearest hospital, rather than removing the response.

**Open questions**
- Confirmation channels: none given. Set `{{var.confirmation_channels}}` on the platform (Your business, Add a detail) and configure the After-the-call trigger for WhatsApp and/or email, or the confirmation flow in section 5 will be skipped.
- No package, services, bed count or years-of-service text was given for `{{var.business_info}}`; enquiry answers will default to "the team will confirm" until it is filled in.

**Word counts**
- Welcome: 16. Section 1: 436. Section 2: 150. Section 3: 143. Section 4: 109. Section 5: 701.
- Section 6: 344 words. Roster: 6 doctors x 23 = 138. Allowance: 615 - 138 = 477. Status: within budget (133 words of margin).

**Fill these in the platform**
| Variable | Value you gave | Where to set it |
|---|---|---|
| `{{var.agent_name}}` | not provided | Voice settings |
| `{{var.agent_gender}}` | not provided | Voice settings |
| `{{var.default_language}}` | not provided | Voice settings |
| `{{var.business_hours}}` | 9 AM to 7 PM | Your business |
| `{{var.business_phone}}` | not provided | Your business |
| `{{var.clinic_address}}` | not provided | Your business |
| `{{var.company_name}}` | not provided | Your business |
| `{{var.roster}}` | 6 doctors (Doctor A to Doctor F), details not provided | Doctors |
| `{{var.business_info}}` | not provided | Your business, Add a detail |
| `{{var.confirmation_channels}}` | not provided | Your business, Add a detail |
| `{{var.emergency_department}}` | no | Your business, Add a detail |
| `{{var.emergency_signs_extra}}` | not provided | Your business, Add a detail |
| `{{var.minors_may_book_alone}}` | not provided (default false) | Your business, Add a detail |
