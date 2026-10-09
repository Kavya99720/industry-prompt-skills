**Assumptions and defaults used**
- Store manager / staff transfer target not given — only "Pharmacist on duty" was provided. Per intake default, any handoff that would otherwise go to staff or a store manager (e.g. complaints) instead offers a callback during {{var.business_hours}}, never a generic transfer.
- confirmation_channels not given — the order-confirmation offer ("Would you like a confirmation on WhatsApp or email?") is skipped entirely; only the prescription-upload-link flow runs, since prescription_upload_method is set to whatsapp.
- delivery_info, return_policy, store_address and business_info not given — not used in these Instructions; where relevant (home delivery address, store questions) the agent says the team will confirm.
- default_language and agent_gender not given in the profile — left as platform variables with no assumed value, to be set in Voice settings.
- Store questions (hours, address, services) beyond the refill flow were not selected (only the STOCK and OUT OF STOCK lines of workflow 01 were chosen), so general enquiry handling is not included.

**Refused or adapted client requests**
- None. "Refill reminders only, no sales, no offers, no medicine talk" matches the existing outbound-reminder rules (R-63) and required no change; "normal order gates apply if the customer wants the refill" matches the default outbound selection of workflows 02 and 01 (STOCK/OUT OF STOCK only), so no refusal or adaptation was needed.

**Open questions**
- Whether the platform actually passes {{var.customer_name}} and {{var.refill_details}} on outbound calls (both marked unconfirmed).
- Whether the platform detects voicemail or no-answer on outbound calls.
- Whether there is a do-not-call tool to action a "stop calling me" request (none assumed; the agent only notes the request).
- What counts as a valid prescription, and the exact controlled/prescription-only medicine schedules — to be confirmed by the industry expert.
- Whether `check_stock` reliably returns the prescription-needed and controlled flags (if missing, the agent treats the medicine as prescription-needed by default).
- Chat channel was not requested, so no chat Instructions were written.

**Word counts**
- Section 6 (Main prompt): 525 words. Allowance: 615. Status: within budget (90 words below allowance, well past the 20-word margin).
