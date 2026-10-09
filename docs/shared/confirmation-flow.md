# Confirmation flow (starter template for all industries)

Status: pharmacy uses it from 2026-10-09 (DECISIONS 50, corrected by 51: no in-call tool). New industries start from it. Healthcare adopts it later, with a targeted rerun, not before. Each industry keeps its own copy of the rule in its core.md (so a skill stays self-contained) and fills in the scope below.

Scope. It applies once, right after the industry's main action succeeded (for example an order number or a booking was returned by the tool), and for sending a document link. It does NOT apply when the action failed, in an emergency, on a handoff, on a voicemail, or when the caller is done. Fixed phrases never override a safety rule or a required line.

Channels. Only channels enabled in the business config are offered (for example whatsapp, email). With one channel enabled, offer only that one. With none enabled, skip the whole flow. There is NO in-call tool: the platform's After-the-call trigger sends the message once the call has ended, so the agent must make the chosen channel (and the email address) clear in the conversation. Never say a message has been sent, only that the caller will get it shortly.

1. Ask once, say exactly: "Would you like a confirmation on WhatsApp or email?"
2. WhatsApp: say exactly "Is this number on WhatsApp?" Yes: say exactly "You will get a confirmation on WhatsApp shortly." No: offer email instead. Never read the number aloud.
3. Email: say exactly "Please tell me your email address." Read it back once, spelled out, with "at" and "dot", and get a yes (the read-back is how the address is stated for the trigger). Then say exactly "You will get a confirmation on email shortly."
4. The caller does not want one: do not send, do not ask again, and say exactly "Is there anything else I can help with?"

For a document link (for example a prescription upload link) use the same flow with "upload link" in place of "confirmation", and no channel question when the business config names the one channel.

Inbound Instructions never contain the phrase "calling from".
