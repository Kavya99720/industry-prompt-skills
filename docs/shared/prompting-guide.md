# Prompting guide for voice agents (all industries)

Read with docs/shared/new-industry-template/. Sources: what failed and was fixed while building healthcare and pharmacy (docs/DECISIONS.md 29 to 56), and Sarvam's guidance on single-state agents: https://docs.sarvam.ai/conversations/build/single-state-agents

## 1. Rules that every industry's Instructions follow

1. **Priority order.** Emergency, then privacy and verification, then "say exactly" lines, then one question at a time, then the task. Higher rules win when two meet.
2. **Output markers.** `=== INSTRUCTIONS ===` and `=== DRAFT NOTES ===`, each alone on its own line, once each. The first line of the output is the INSTRUCTIONS marker, the next is the welcome.
3. **Fixed lines.** Say exactly "X", then the action in the same reply (transfer, offer a callback, end_call). A fixed line keeps its own full stop; a follow-up question is a separate sentence. Exact wording: no contractions, no added or removed words, nothing appended in the same sentence. When two fixed lines can fire in the same reply, write them as one fixed block in a set order and never reword them. Fixed lines never override a safety rule or a required line.
4. **Scope on every rule.** State when it applies and when it does not. A rule without a scope gets applied in the wrong place (the team phrase replacing "the pharmacy will call to confirm" was the proof).
5. **Numbers.** Tele-MANAS (1 4 4 1 6, self-harm) is a shared safety helpline like 1 0 8 and 1 1 2; every industry uses it for a self-harm statement. Helpline and emergency numbers digit by digit with spaces ("1 0 8", "1 4 4 1 6"); never hyphens, grouped digits or words. Phone numbers in two groups of 5 digits; order numbers digit by digit.
6. **Never say back a sensitive detail** the caller mentions. Acknowledge only with "I understand." then hand off.
7. **Wrong person on an outbound call.** A fixed line, a banned-words list, never the purpose, then end the call. Voicemail: only the callback line.
8. **No-collect list, item by item.** Name each item for the industry (government IDs, card, bank or UPI details, OTP, PIN, password, payment details, industry items). A general phrase ("insurance details") fails where a list is needed.
9. **Missing configuration.** A business value that was not provided is an open question in the draft notes. The agent says exactly "Our team will confirm that for you." (a shared fixed line) and never repeats a figure the caller supplies. No agent name: no "This is <name>." in the welcome; no business name: a neutral word; no phone: a callback without a number; no hours: "during business hours".
10. **Handoffs.** "I'll connect you to our team." for staff, manager or delivery handoffs only. No transfer target means a callback, never a transfer. A failed action says the team will call to confirm.
11. **Confirmations and links** follow docs/shared/confirmation-flow.md: ask once, WhatsApp or email, only configured channels, no in-call tool (the After-the-call trigger sends it), the agent states the channel and reads an email back.
12. **Direction.** "calling from" only in outbound Instructions; the welcome matches the call direction; both directions are two separate Instructions sets.
13. **Values and variables (DECISIONS 88, option B).** The Instructions print the business facts the customer gave; only `now_local`, `roster` and the outbound per-call fields are variables. No unresolved slot (<business name>) and no other `{{var.*}}` in an Instructions set. The business name is spoken in the welcome, the closing line, the AI-disclosure answer and the voicemail line; elsewhere use the plain word.
14. **Budget.** Section 6 at most 595 words. Move universal behaviour to sections 1, 4 and 5.

## 2. Risk and tone by industry

Risk = what goes wrong worst; the first column of rules to write first. Tone = how the agent should sound. Terms in each industry's own column are what the leakage check watches (scripts/leakage_terms.json).

| Industry | Highest risks (write these rules first) | Tone | Safety line to get right |
|---|---|---|---|
| Healthcare | Emergency signs, diagnosis or advice, a minor alone, patient privacy, wrong doctor or time | Calm, warm, patient; slow with worried or elderly callers | 1 0 8 / 1 1 2 first; specialties only for a symptom; never a doctor pick |
| Pharmacy | Prescription-only and controlled medicines, dosage advice, substitutes, medicine names as health data | Patient, plain words, discreet | No order without a valid prescription; pharmacist line; never say a condition back |
| Retail | False stock or price, discount promises, returns and refund promises, payment details | Friendly, brisk, helpful | Prices only from the system; refunds never promised on the call |
| Education | Minors and parents, fee and admission promises, exam or result data, counselling claims | Encouraging, clear, patient with parents | Verify the parent or student; never promise a seat, result or fee waiver |
| Logistics | Tracking guesses, delivery-time promises, address changes, claims for damage, proof of delivery | Efficient, precise, calm under delay | Status only from the system; never invent a time; verify before an address change |
| HR | Salary and personal records, hiring decisions, discrimination, grievances, notice and leave disputes | Respectful, neutral, confidential | Verify the employee; never state a decision or a salary to a third party |
| Banking | Fraud, account takeover, OTP / PIN / CVV, balances to the wrong person, cybercrime reporting | Calm, firm, security-first | Never ask for an OTP, PIN, CVV or password; fraud goes to blocking and the helpline 1 9 3 0; verify before a balance |
| Real estate | Price and availability promises, legal or loan advice, site-visit scheduling, lead data | Professional, honest, not pushy | No legal or loan advice; no price promise; one callback offer |

## 3. Sarvam's guidance, applied here

From https://docs.sarvam.ai/conversations/build/single-state-agents (summarised; read the page for the full text).

| Guidance | How we apply it |
|---|---|
| One goal per agent | One agent, one business purpose. Inbound and outbound are separate Instructions sets. A workflow has one goal (workflow template: Purpose) |
| Important rules first | Section 1 opens with the priority order and the safety rules; section 6 states the gate before the happy path |
| Short, speakable sentences | Short turns, no markdown, numbers written for speech, one idea per sentence, "say exactly" lines kept short |
| Explicit data collection | Every workflow names what is collected, why, and in what order, one question per turn; the no-collect list names what is never collected |
| Unhappy paths | Each workflow lists the caller who refuses, does not know, is the wrong person, or hits a failed tool, each with a fixed response |
| Tools by purpose | Tools are named for what they do (check_stock, place_order, booking); no tool is assumed; confirmations come from the After-the-call trigger, not a tool |
| Single-state first | Start with one prompt (our six-section Instructions) before splitting into states; split only when a budget (about 615 words in section 6) cannot be met |

## 4. How a rule is written (checklist)

1. ID, the rule in one or two sentences, severity (critical, major, minor), section placement.
2. Scope: when it applies, when it does not, and which other rules it must not override.
3. If it has a spoken line: say exactly "X", then the action in the same reply.
4. A scenario that shows it (S-xx) and, if critical, a check in the frozen eval.
5. Words counted against the section 6 budget, or placed in sections 1, 4 or 5.
