**Assumptions and defaults used**
- No start language was given, so calls start in English and all 11 platform languages stay supported; this is a default, not a confirmed choice.
- Only "Pharmacist on duty" was given as a transfer target, with no store manager or staff number. Complaints, angry callers and other staff requests use a callback instead of a transfer, since no such target is set.
- No confirmation channel was given for order or refill confirmations (separate from the WhatsApp prescription upload). That confirmation offer is left out; only the WhatsApp upload-link flow runs.
- No largest-quantity limit was given, so the documented default applies: more than 3 packs, strips or bottles of the same medicine goes to the pharmacist. This default lives only in the ORDER step, not in the business facts.
- Return policy, delivery charges or timing, services and branches, and extra emergency signs were not given, so nothing is printed for them; a caller who asks is told the team will confirm.
- Only the STOCK and OUT OF STOCK lines of the medicine enquiry workflow were built in, as selected; store hours, address and phone are answered from the business facts already in section 1.
- This set is the outbound refill reminder flow only. A separate inbound set (for a customer calling in to ask for a refill) would need its own Instructions.

**Refused or adapted client requests**
- none

**Open questions**
- Whether the platform actually passes {{var.customer_name}} and {{var.refill_details}} on these calls.
- The desired call-start language (none was given; English was used as a default).
- Whether a store manager or staff number should be added so complaints and staff requests get a transfer instead of a callback.
- Whether a confirmation channel should be set for order and refill confirmations, separate from the WhatsApp prescription upload link.
- The largest quantity the agent may order without the pharmacist (no limit was given; the default of 3 is a placeholder for pharmacist review).
- Return policy, delivery charges, areas and usual timing, and any services or branches to list.
- What the stock and price tool actually returns (in stock, price, prescription-needed, controlled); a missing flag is treated as prescription-needed.
- What counts as a valid prescription, and the exact list of controlled or habit-forming medicines, for the pharmacist or an industry expert to confirm.
- Whether the platform detects voicemail or no answer, and whether a do-not-call tool exists.

**Word counts**
- Welcome: 13. Section 1: 770. Section 2: 235. Section 3: 175. Section 4: 138. Section 5: 824.
- Section 6: 577 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Kiran | Voice settings |
| Agent gender | Male | Voice settings |
| Start language | Not given (English used as default) | Voice settings |
| Transfer target (pharmacist) | Pharmacist on duty | Transfer numbers |
| Confirmation channel (prescription upload) | WhatsApp | After-the-call trigger |
| Confirmation channel (order/refill confirmation) | Not given | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
