**Assumptions and defaults used**
- Channel: voice (as given); this is a voice-only setup.
- Largest quantity without the pharmacist: not given, so the default applies — orders above 3 packs, strips or bottles of the same medicine go to the pharmacist. This default is a placeholder, not a clinical limit.
- Medicines that should always go to the pharmacist beyond what the stock tool flags: none given, so the agent relies only on the stock tool's prescription and controlled flags.
- Delivery areas, charges and usual timing: not given. The agent says the team will confirm these.
- Return policy: not given. The agent says the team will confirm it.
- Confirmation channels for order confirmations: not given, so no confirmation offer is made after an order is placed; the caller is simply asked if there is anything else.
- Extra emergency signs: none given, so only the standard list is used.
- Stock tool result fields (in stock, price, prescription needed, controlled) are assumed as described; if a flag is missing, the medicine is treated as prescription-only and sent to the pharmacist.

**Refused or adapted client requests**
- none

**Open questions**
- What is the actual return policy text to read to callers?
- Which stores offer home delivery, and what are the delivery areas, charges and usual timing?
- Is 3 packs, strips or bottles the right cutoff for sending an order to the pharmacist, or should the owner set a different number?
- Should order confirmations be offered to callers, and if so on WhatsApp, email or both?
- What exactly counts as a valid prescription for the pharmacist to verify?
- Does the stock and price check tool reliably return whether a medicine needs a prescription and whether it is controlled?

**Word counts**
- Welcome: 14. Section 1: 915. Section 2: 235. Section 3: 167. Section 4: 138. Section 5: 814.
- Section 6: 594 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**

| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | Asha | Voice settings |
| Agent gender | Female | Voice settings |
| Start language | English | Voice settings |
| Transfer target: pharmacist on duty | Pharmacist on duty (number not given) | Transfer numbers |
| Transfer target: store manager | Store manager (number not given) | Transfer numbers |
| After-the-call trigger channels | Not given (no confirmation channel set) | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
