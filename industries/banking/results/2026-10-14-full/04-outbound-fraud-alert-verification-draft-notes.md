**Assumptions and defaults used**
- Only one workflow (fraud-alert verification) was selected, matching an outbound purpose set.
- Balance lookup is off, so no balance or lookup language is used anywhere.
- No extra emergency signs were given, so only the default list is used.
- No offer or scheme was given, so no offer line was added.
- Branch staff was not given as a transfer target. The fraud team was given, so fraud-related handoffs (the coached-caller block and the "no/not sure" outcome) transfer there. All other handoffs in this call (emergency, authority caller, deceased holder, out-of-scope, prompt-level team handoff) have no configured target, so they offer a callback instead of a transfer, per the no-target default.
- Confirmation channels were not set, so the confirmation flow is left out entirely (it is also never used on outbound calls).
- The address given (Orchid House, 18 Ocean Drive, Mumbai) is treated as the single business address; no separate branch name was given.
- The business phone is a landline-style number; it is printed exactly as given rather than split into mobile-style digit groups.

**Refused or adapted client requests**
- None. The two requirements given (check whether recent transactions are theirs; never say what the flagged transaction was; block only after asking, then connect to the fraud team) all match the required fraud-alert-verification flow and were applied directly.

**Open questions**
- The outbound welcome names Nisha as an AI assistant on purpose; this differs from a plain introduction, and that wording should be kept.
- No legal references or resolution timelines are quoted anywhere; a caller asking about RBI timelines is told the team will confirm.
- This covers outbound calls only. Any inbound Instructions for this bank need their own separate run.
- Chat was not requested, so only voice Instructions were written.
- Whether the platform actually passes the customer's name into the call is unconfirmed; if it does not, the agent falls back to asking "Am I speaking with the customer?"
- No escalation path, grievance contact, or branch/ATM information was given; these were not needed for this fraud-only call, so none was asked for or printed.

**Word counts**
- Welcome: 19. Section 1: not counted (outside the budget). Section 2: not counted. Section 3: not counted. Section 4: not counted. Section 5: not counted. Section 6: 541 words. Allowance: 615 (aim 595). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Nisha | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Fraud team transfer number | Given (fraud team) | Transfer numbers |
| Branch staff transfer number | Not provided | Transfer numbers |
| Confirmation channels | Not set (no confirmation offered) | After-the-call trigger |
| Card blocking | On | Banking tools |
| Balance lookup | Off (default) | Banking tools |

If your hours, phone or address change, regenerate these Instructions.
