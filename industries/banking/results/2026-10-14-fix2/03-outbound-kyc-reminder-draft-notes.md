**Assumptions and defaults used**
- Card blocking and balance lookup: off (default; no banking tools given, so neither block is written).
- Extra emergency signs: none given — only the default list is in the Instructions.
- Offer or scheme: none given — no offer line written.
- Confirmation channels: not set — no confirmation flow is written (it is also excluded on every outbound call regardless).
- Branch/ATM information, escalation path and grievance contact: not given — "Our team will confirm that for you." is used if a caller asks for any of these.

**Refused or adapted client requests**
- none — every client requirement (short reminder call, no document or ID taken, respecting a stop-calling request, a callback-only voicemail line) already matches the required safety defaults, so nothing needed refusing or weakening.

**Open questions**
- Whether the platform actually passes `{{var.customer_name}}` on every call, or sometimes leaves it empty.
- Whether the platform tells the agent when a call has reached a voicemail system.
- Branch/ATM information, the escalation path and the grievance contact were not given — add them if the bank wants them available.
- The outbound welcome names Riya as an AI assistant from the first words; this is the required template wording for outbound calls, not an error.
- This set is outbound only; an inbound call-handling set needs a separate run.
- Chat is not written here; this is a voice-only set.
- Legal references, RBI rules and grievance timelines are never quoted; a caller asking for one is told the team will confirm.

**Word counts**
- Section 6: 345 words. Allowance: 615 (aim 595). Status: well within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Riya | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Transfer target — branch staff | Given | Transfer numbers |
| Transfer target — fraud team | Not given | Transfer numbers |
| Confirmation channels | Not set | After-the-call trigger |
| Card blocking | Off (default) | Tool settings |
| Balance lookup | Off (default) | Tool settings |

If your hours, phone or address change, regenerate these Instructions.
