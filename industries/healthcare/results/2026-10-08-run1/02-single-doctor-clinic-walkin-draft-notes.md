**Assumptions and defaults used**
- Business type single-doctor clinic: the agent says "our clinic". Inbound only. Workflow 01 Enquiry plus the TOKENS line (R-78). No booking, reschedule or cancel workflow.
- Welcome is the default inbound template in the platform's Standard form. The client may pick the Warm or Brief template. It is spoken in `{{var.default_language}}`, which must be set to Hindi.
- OPD timings come from `{{var.business_hours}}` and the roster shifts. The token system comes only from `{{var.business_info}}`. If `{{var.business_info}}` is empty, the agent says the team will confirm.
- Emergency department is no: the emergency line is adapted (call 1 0 8 or 1 1 2, or go to the nearest hospital). The line is written as a conditional on `{{var.emergency_department}}`.
- No transfer number was given. The agent offers a callback during `{{var.business_hours}}` when no one is available (R-81).
- No extra emergency signs and minors flag false (defaults). The doctor count is 1, so the allowance is 615 − 23 = 592.
- Outbound is not covered. It needs its own run.
- Section 3 uses the default `{{var.default_language}}`. Callers speak Hindi, and the 11-language switching base is kept unchanged.

**Refused or adapted client requests**
- "Never promise a time the patient will be seen": kept and strengthened (TOKENS and WAIT lines). No refusal needed.
- "Tell callers how tokens work": adapted. The agent explains only what `{{var.business_info}}` says and gives no live token status (no lookup tool; R-35).
- A caller asking for a timed visit is told the clinic does not give timed bookings (R-78). No booking is attempted.

**Open questions**
- Please confirm that `{{var.business_info}}` holds the token rules (how tokens are issued, when the counter opens).
- Please confirm a transfer target for on-duty staff and emergencies, or accept callback only.
- The default emergency signs list needs review by the client's clinical team.
- Please confirm that `{{var.roster}}` carries the doctor's fee and morning/evening shifts, so the OPD timings can be said from both.

**Word counts**
- Welcome: 13. Sections 1 to 5 are hand estimates (a count script was blocked): Section 1: about 640. Section 2: about 250. Section 3: about 230. Section 4: about 170. Section 5: about 420.
- Section 6: 276 words (exact). Roster: 1 doctor x 23 = 23. Allowance: 615 - 23 = 592. Status: within budget. The `{{var.roster}}` placeholder is not counted in the 276.
