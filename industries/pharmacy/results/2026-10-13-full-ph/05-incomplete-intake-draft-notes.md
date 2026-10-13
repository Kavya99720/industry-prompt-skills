**Assumptions and defaults used**
- No assistant name or gender given: the welcome drops "This is <agent name>", section 1 does not name the agent, and section 4 keeps only the gender-neutral line.
- No business phone, address, prescription upload method, delivery terms, return policy, payment modes or largest order quantity given: each is printed in the Instructions as "has not been set," with the fixed line "Our team will confirm that for you." plus a callback or staff offer used whenever a caller asks.
- No transfer target given: every pharmacist or staff handoff is written to fall back to a callback, as the default rules require.
- No languages given: kept the full set of 11 platform languages, with calls starting in English (the default start language with no language named).
- No confirmation channels given: the order-confirmation question ("Would you like a confirmation on WhatsApp or email?") is left out entirely, since there is nothing to offer; the order step ends once the order number is read back.
- No largest-order-quantity given: used the standard placeholder (more than 3 packs, strips or bottles of the same medicine goes to the pharmacist).
- Business type is written as "small independent pharmacy," so the plain word used throughout is "our pharmacy" (never "the pharmacy" or "our store").
- Only the two requested workflows (medicine enquiry, and order and prescription) are built into section 6; refill and delivery/returns are not included, since they were not selected.

**Refused or adapted client requests**
- "Just take orders and answer stock questions, we have not decided the rest": accepted as the scope (enquiry and ordering only), but every safety rule (emergency handling, no dosage advice, no substitutes, no order without a valid prescription, privacy and verification, no payment collection) is still included in full, since none of these can be switched off.

**Open questions**
- Business phone: not given. Needed so callbacks can state a number instead of just being offered.
- Store address: not given. Needed for directions and the facts block.
- Prescription upload method (WhatsApp, email or bring to store): not given. Right now every prescription case is told to bring it to the store or ask for a staff callback.
- Delivery info (pickup, home delivery, areas, charges, timing): not given.
- Return policy: not given.
- Payment modes accepted: not given.
- Who the agent should transfer to for the pharmacist and the store manager: not given. Until set, the agent always offers a callback instead of a transfer.
- Languages the business can actually handle, and the language calls should start in: not given. All 11 platform languages and an English start are used as a placeholder.
- Largest order quantity allowed without the pharmacist: not given. The 3-pack/strip/bottle placeholder is in use and should be reviewed by the pharmacy.
- Services, branches and any offers or schemes: none given, so none are mentioned.
- This is the voice version only; a chat version is not set up.
- The stock tool's exact result fields (in stock, price, prescription needed, controlled) are assumed; until confirmed, a medicine with missing flags is always treated as needing the pharmacist.
- What counts as a valid prescription is left to the pharmacist to judge; it is not defined in this prompt.

**Word counts**
- Welcome: 11. Section 1: 790. Section 2: 223. Section 3: 173. Section 4: 126. Section 5: 738.
- Section 6: 410 words. Allowance: 615 (no roster). Status: within budget.

**Fill these in the platform**
| Set on the platform | Value you gave | Where to set it |
|---|---|---|
| Agent name | not provided | Voice settings |
| Agent gender | not provided | Voice settings |
| Start language | not provided (defaulted to English) | Voice settings |
| Transfer number (pharmacist) | not provided | Transfer numbers |
| Transfer number (store manager / staff) | not provided | Transfer numbers |
| After-the-call trigger channels | not provided (no confirmation flow included) | After-the-call trigger |

If your hours, phone or address change, regenerate these Instructions.
