#!/usr/bin/env python
"""Fixed-line check for generated Instructions. Standard library only. For the runner and CI only: a skill never runs
this during generation (it would need a tool approval, which cannot be given in a non-interactive run; DECISIONS 63).

Every `say exactly "..."` line (and every fixed block, which is one quoted string) in the skill's references/core.md and
the selected workflows must appear verbatim in the generated output. A line marked `must include "..."` (on any line of
core.md or a selected workflow file) is required text, not a spoken line: it must appear in the output as a normalized
match (case-insensitive, punctuation ignored), so a longer sentence that contains it passes:

  python scripts/check_fixed_lines.py OUTPUT.md --industry banking --workflows 01 02 03 --tool card_block_tool=on --tool balance_lookup_tool=off

  OUTPUT.md        the whole output, starting with the === INSTRUCTIONS === marker (or only the Instructions part)
  --workflows      workflow numbers you selected (default: every written workflow of the output's direction;
                   a workflow whose file name contains "outbound" belongs to the outbound direction)
  --direction      inbound or outbound (default: outbound when the welcome says "calling from")
  --tool name=on|off
                   an optional config tool or setting. A line that only appears in rules mentioning one that is OFF is not
                   required. confirmation_channels is OFF unless you pass --tool confirmation_channels=on
  --industry NAME  use .claude/skills/NAME-prompt-writer/references (default when --references is not given: banking)
  --references DIR the references folder, instead of --industry

  --tool confirmation_channels=whatsapp|email|both
                   the confirmation channels the client gave: only the lines of those channels are required (the
                   combined "WhatsApp or email" question only with both). on/off still works as before.

  --tool lead_source_wording=on|off
                   real estate outbound: on when the client gave lead-source wording (a --profile with a "Lead-source
                   wording" row sets it, or a "Contact-source wording" row for retail); the not-known source line is then
                   not required

  --industry retail or education with --profile
                   the profile's Tools row (retail: order_lookup_tool, stock_check_tool, send_link; education:
                   booking_tool, send_link, callback), Calls recorded, Confirmation channels, Transfer targets and
                   Contact-source wording rows set the settings; --tool overrides them. Education's callback setting
                   (callback_setting) is ON unless the Tools row says "callback OFF"; a rule marked
                   [callback_setting: on] is required only then.

  --tool prescription_upload_method=whatsapp|email|in_store|not_set
                   the prescription upload method the client chose. Rows marked [upload: whatsapp] or [upload: email] are
                   required only for the matching method (none for in_store or not_set). Without this option every marked
                   row is required, as before.

A rule ID such as "R-41" or "S-37" anywhere in the Instructions (the part before the === DRAFT NOTES === marker; the
whole text when there is no marker) is reported as a problem: rule IDs belong to the sources, never to the prompt.

  --profile FILE   a test profile (industries/<x>/test-profiles/NN-*.md) of an industry that prints its business facts
                   (inline_values). The expected welcome is built from the profile's Business name, Assistant and
                   Direction rows ("Thank you for calling <name>. This is <agent>. How can I help you?"; the "This is
                   <agent>." part is dropped when no assistant name is given; no business name gives the neutral
                   word of the Business type row) and must appear word for word.

Exit code 0: nothing missing. Exit code 1: lines are missing; each is printed.
Exit code 2: usage error.
"""
import argparse
import re
import sys
from pathlib import Path

SAY_EXACTLY = re.compile(r'say exactly(?: and only)?(?: this block\b[^"]{0,50})?\s*"([^"]+)"', re.I)
MUST_PREFIX = "must include: "
RULE_ID = re.compile(r"\b[RS]-\d+\b")
RULE_ID_PREFIX = "rule ID: "
NOTES_MARKER = "=== DRAFT NOTES ==="
UPLOAD_BRANCH = re.compile(r"\[upload:\s*(whatsapp|email)\]", re.I)
UPLOAD_TOOL = "prescription_upload_method"
UPLOAD_VALUES = ("whatsapp", "email", "in_store", "not_set")
# A row marked "[balance_lookup_tool: off]" or labelled "(lookup off)" / "(block off)" is required only when that tool is not on.
TOOL_OFF_MARK = re.compile(r"\[(\w+):\s*off\]|\((lookup|block) off\)", re.I)
TOOL_OFF_LABELS = {"lookup": "balance_lookup_tool", "block": "card_block_tool"}
TEAM_PHRASE = "I'll connect you to our team."
TRANSFER_TARGET = "transfer_target"  # True when the profile gives at least one transfer target; only set when known (banking)
CHANNELS = "channels"  # the confirmation channels the client gave, a set; only set when known (banking)
LEAD_SOURCE_WORDING = "lead_source_wording"  # True when the profile gives lead-source wording; only set when known (real estate)
SOURCE_NOT_KNOWN = "I don't have that detail with me. Would you like us to stop calling you?"
MUST_INCLUDE = re.compile(r'must include\s*"([^"]+)"', re.I)


def norm(text):
    text = text.replace("`", "").replace("’", "'").replace("‘", "'")
    text = text.replace("“", '"').replace("”", '"')
    return " ".join(text.split())


def norm_text(text):
    """Case-insensitive, punctuation-free form used for must-include lines."""
    return " ".join(re.sub(r"[^\w\s]", "", norm(text).lower()).split())


def profile_value(profile_text, label):
    """The value cell of a `| label | value |` row of a test profile, or None."""
    m = re.search(r"^\|\s*" + re.escape(label) + r"\s*\|\s*(.+?)\s*\|\s*$", profile_text, re.M | re.I)
    return m.group(1).strip() if m else None


def _given(v):
    return v is not None and not re.match(r"(not given|not provided|not stated|none)", v, re.I)


def profile_slots(profile_text):
    """Values a say-exactly line may carry as slots: <agent name>, <business name>, <phone>, from a test profile."""
    slots = {}
    biz = profile_value(profile_text, "Business name")
    if _given(biz):
        slots["business name"] = biz
    agent = profile_value(profile_text, "Assistant")
    if _given(agent):
        slots["agent name"] = re.sub(r"\s*\([^)]*\)\s*$", "", agent).strip()
    phone = profile_value(profile_text, "Business phone")
    if _given(phone):
        slots["phone"] = phone
    return slots


def fill_slots(quote, slots):
    """The quote with its slots filled from the profile; None when a slot has no value (then the line is not required)."""
    if slots is None:
        return quote
    try:
        return re.sub(r"<(agent name|business name|phone)>", lambda m: slots[m.group(1)], quote)
    except KeyError:
        return None


AI_OUTBOUND_INDUSTRIES = ("banking", "real-estate", "retail", "education", "logistics")  # their outbound welcome names the agent as an AI assistant (DECISIONS 100; real estate: DECISIONS 110; retail: DECISIONS 114; education: DECISIONS 118)
RECORDING_IN_WELCOME_INDUSTRIES = ("real-estate", "retail", "education", "logistics")  # calls recorded = yes puts the recording sentence in the outbound welcome (DECISIONS 111, 114)


def profile_tools(profile_text):
    """The banking tool settings and confirmation channels a test profile states: card_block_tool and balance_lookup_tool
    are ON only when the Tools row says so (OFF by default), confirmation_channels is ON when a channel is given."""
    row = profile_value(profile_text, "Tools") or ""
    cell = profile_value(profile_text, "Confirmation channels") or ""
    channels = {c for c in ("whatsapp", "email") if re.search(c, cell, re.I)} if not re.match(r"\s*(not set|none)", cell, re.I) else set()
    tools = {t: bool(re.search(t + r"\s+ON(?![A-Za-z])", row))
             for t in ("card_block_tool", "balance_lookup_tool", "booking_tool", "send_link",
                        "order_lookup_tool", "stock_check_tool",
                        "tracking_lookup_tool", "reschedule_tool", "pickup_request_tool", "address_change_tool")}
    tools["callback_setting"] = not re.search(r"callback(?:_setting)?\s+OFF(?![A-Za-z])", row)  # education: ON unless the row says OFF (DECISIONS 118)
    tools["calls_recorded"] = bool(re.match(r"\s*yes", profile_value(profile_text, "Calls recorded") or "", re.I))
    tools["confirmation_channels"] = bool(channels)
    tools[CHANNELS] = channels
    source = profile_value(profile_text, "Lead-source wording")
    if source is None:  # retail calls it contact-source wording (DECISIONS 114)
        source = profile_value(profile_text, "Contact-source wording")
    if source is not None:  # no row: unknown, the not-known line stays required
        tools[LEAD_SOURCE_WORDING] = _given(source)
    targets = profile_value(profile_text, "Transfer targets")
    if targets:  # no row: unknown, the phrase stays required
        tools[TRANSFER_TARGET] = not re.match(r"\s*(not given|none)", targets, re.I)
    return tools


def welcome_from_profile(profile_text, industry=None):
    """The welcome an inline-values Instructions set must start with, from a test profile's own values."""
    def given(v):
        return v is not None and not re.match(r"(not given|not provided|not stated|none)", v, re.I)
    biz = profile_value(profile_text, "Business name")
    if not given(biz):
        kind = profile_value(profile_text, "Business type") or ""
        m = re.search(r'says "([^"]+)"', kind)
        biz = m.group(1) if m else "our clinic"
    agent = profile_value(profile_text, "Assistant")
    agent = re.sub(r"\s*\([^)]*\)\s*$", "", agent).strip() if given(agent) else None
    direction = (profile_value(profile_text, "Direction") or "inbound").lower()
    if direction.startswith("out") and industry in AI_OUTBOUND_INDUSTRIES:
        opening = (f"Hello, this is {agent}, an AI assistant calling from {biz}." if agent
                   else f"Hello, I am an AI assistant calling from {biz}.")
        if industry in RECORDING_IN_WELCOME_INDUSTRIES and re.match(r"\s*yes", profile_value(profile_text, "Calls recorded") or "", re.I):
            opening += " This call may be recorded for quality purposes."  # before the question (DECISIONS 111)
        return opening + " Is this a good time to talk?"
    if direction.startswith("out"):
        return (f"Hello, this is {agent} calling from {biz}. Is this a good time to talk?" if agent
                else f"Hello, I am calling from {biz}. Is this a good time to talk?")
    return (f"Thank you for calling {biz}. This is {agent}. How can I help you?" if agent
            else f"Thank you for calling {biz}. How can I help you?")


def workflow_files(refs, numbers, direction):
    wf = refs / "workflows"
    files = []
    if not wf.is_dir():
        return files
    for f in sorted(wf.glob("*.md")):
        if f.name.lower() == "readme.md":
            continue
        m = re.match(r"(\d+)-", f.name)
        if not m:
            continue
        if numbers:
            if m.group(1) not in numbers:
                continue
        elif ("outbound" in f.name.lower()) != (direction == "outbound"):
            continue
        if "Status: stub" in f.read_text(encoding="utf-8")[:600]:
            continue
        files.append(f)
    return files


def with_defaults(tools):
    """confirmation_channels is OFF unless the client configured a channel: its lines are then required.
    package_offer is OFF unless the business facts or the client name a package or offer (--tool package_offer=on).
    Real estate: booking_tool, send_link and calls_recorded are OFF unless the profile or --tool turns them on (DECISIONS 110).
    Retail: order_lookup_tool and stock_check_tool are OFF too, and its profile's settings are read (DECISIONS 114).
    Education: booking_tool and send_link are OFF by default like real estate; callback_setting is ON by default; its
    profile's settings are read (DECISIONS 118).
    Logistics: tracking_lookup_tool, reschedule_tool, pickup_request_tool and address_change_tool are OFF by default and
    its profile's settings are read (DECISIONS 124)."""
    merged = {"confirmation_channels": False, "package_offer": False,
              "booking_tool": False, "send_link": False, "calls_recorded": False,
              "order_lookup_tool": False, "stock_check_tool": False,
              "tracking_lookup_tool": False, "reschedule_tool": False, "pickup_request_tool": False, "address_change_tool": False,
              "callback_setting": True}
    merged.update(tools or {})
    return merged


def channel_needed(quote, channels):
    """A confirmation-flow quote is required only for the channels the client gave: the combined question needs both,
    an email line needs email, a WhatsApp line needs WhatsApp. channels is a set of "whatsapp" / "email"."""
    low = quote.lower()
    if "whatsapp or email" in low:
        return {"whatsapp", "email"} <= channels
    if "email" in low:
        return "email" in channels
    if "whatsapp" in low:
        return "whatsapp" in channels
    return True


def quote_needed(row, quote, tools):
    """Whether one quote of one rule row is required under the profile's real tool settings and channels."""
    mentioned = [t for t in tools if t in row and isinstance(tools[t], bool)]
    needed = (not mentioned) or all(tools[t] for t in mentioned)  # a row naming several settings needs ALL of them on (DECISIONS 111)
    branch = UPLOAD_BRANCH.search(row)
    if branch and isinstance(tools.get(UPLOAD_TOOL), str):
        needed = needed and tools[UPLOAD_TOOL] == branch.group(1).lower()
    off = TOOL_OFF_MARK.search(row)
    if off:
        name = off.group(1) or TOOL_OFF_LABELS[off.group(2).lower()]
        needed = tools.get(name) is not True
    if tools.get(TRANSFER_TARGET) is False and norm(quote) == norm(TEAM_PHRASE):
        needed = False  # with no transfer target every handoff is a callback offer (R-17)
    if tools.get(LEAD_SOURCE_WORDING) is True and norm(quote) == norm(SOURCE_NOT_KNOWN):
        needed = False  # the business gave lead-source wording: the not-known line never fires (DECISIONS 111)
    channels = tools.get(CHANNELS)
    if needed and isinstance(channels, (set, frozenset)) and "confirmation_channels" in row:
        needed = channel_needed(quote, channels)
    return needed


def required_lines(refs, numbers, direction, tools, slots=None):
    """Quotes that must be present, as a list of (source file name, quote)."""
    files = [refs / "core.md"] + workflow_files(refs, numbers, direction)
    found = {}
    for f in files:
        if not f.is_file():
            continue
        for row in f.read_text(encoding="utf-8").splitlines():
            for q in SAY_EXACTLY.findall(row):
                if q.strip() == "X":
                    continue  # the format example, not a real line
                needed = quote_needed(row, q, tools)
                q = fill_slots(q, slots)
                if q is None:
                    continue
                key = norm(q)
                if key not in found:
                    found[key] = [f.name, q, needed]
                elif needed:
                    found[key][2] = True
    return [(v[0], v[1]) for v in found.values() if v[2]]


def required_text(refs, numbers, direction, tools):
    """Quotes marked must include, as a list of (source file name, quote)."""
    files = [refs / "core.md"] + workflow_files(refs, numbers, direction)
    found = {}
    for f in files:
        if not f.is_file():
            continue
        for row in f.read_text(encoding="utf-8").splitlines():
            for q in MUST_INCLUDE.findall(row):
                mentioned = [t for t in tools if t in row and isinstance(tools[t], bool)]
                needed = (not mentioned) or all(tools[t] for t in mentioned)
                key = norm_text(q)
                if key not in found:
                    found[key] = [f.name, q, needed]
                elif needed:
                    found[key][2] = True
    return [(v[0], v[1]) for v in found.values() if v[2]]


def check(output_text, refs, numbers=(), direction=None, tools=None, welcome=None, slots=None):
    tools = with_defaults(tools)
    head = output_text.split("\n", 12)
    if direction is None:
        direction = "outbound" if any("calling from" in l for l in head) else "inbound"
    body = norm(output_text)
    missing = [(src, q) for src, q in required_lines(Path(refs), set(numbers), direction, tools, slots) if norm(q) not in body]
    text = norm_text(output_text)
    missing += [(src, MUST_PREFIX + q) for src, q in required_text(Path(refs), set(numbers), direction, tools)
                if norm_text(q) not in text]
    if welcome and norm(welcome) not in body:
        missing.append(("welcome (profile)", welcome))
    missing += rule_id_problems(output_text)
    return missing


def rule_id_problems(output_text):
    """Rule IDs (R-12, S-37) inside the Instructions part of an output, as (where, RULE_ID_PREFIX + text) pairs."""
    instructions = output_text.split(NOTES_MARKER, 1)[0] if re.search(r"(?m)^" + re.escape(NOTES_MARKER) + r"\s*$", output_text) else output_text
    found = []
    for n, line in enumerate(instructions.splitlines(), 1):
        for m in RULE_ID.finditer(line):
            found.append((f"Instructions line {n}", RULE_ID_PREFIX + m.group(0) + " in: " + line.strip()[:70]))
    return found


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("output")
    ap.add_argument("--workflows", nargs="*", default=[])
    ap.add_argument("--direction", choices=("inbound", "outbound"))
    ap.add_argument("--tool", action="append", default=[], help="name=on|off")
    ap.add_argument("--industry", default="banking")
    ap.add_argument("--references")
    ap.add_argument("--profile")
    args = ap.parse_args(argv)
    if not args.references:
        args.references = str(Path(__file__).resolve().parent.parent / ".claude" / "skills" / f"{args.industry}-prompt-writer" / "references")
    path = Path(args.output)
    if not path.is_file():
        print(f"cannot read {path}", file=sys.stderr)
        return 2
    tools = {}
    for item in args.tool:
        name, _, state = item.partition("=")
        if name == UPLOAD_TOOL and state.lower() in UPLOAD_VALUES:
            tools[name] = state.lower()
            continue
        if name == "confirmation_channels" and state.lower() in ("whatsapp", "email", "both"):
            tools[name] = True
            tools[CHANNELS] = {"whatsapp", "email"} if state.lower() == "both" else {state.lower()}
            continue
        if state.lower() not in ("on", "off"):
            print(f"--tool needs name=on or name=off, got {item}", file=sys.stderr)
            return 2
        tools[name] = state.lower() == "on"
    profile_text = Path(args.profile).read_text(encoding="utf-8") if args.profile else None
    if profile_text is not None and args.industry in ("retail", "education", "logistics"):
        # retail and education read every setting its profile states (tools, recording, channels, transfer targets, source wording);
        # an explicit --tool wins. Other industries keep passing their settings with --tool (DECISIONS 114).
        for key, value in profile_tools(profile_text).items():
            tools.setdefault(key, value)
    if profile_text is not None and LEAD_SOURCE_WORDING not in tools:
        known = profile_tools(profile_text).get(LEAD_SOURCE_WORDING)
        if known is not None:
            tools[LEAD_SOURCE_WORDING] = known
    welcome = welcome_from_profile(profile_text, args.industry) if profile_text else None
    slots = profile_slots(profile_text) if profile_text else None
    missing = check(path.read_text(encoding="utf-8"), args.references, args.workflows, args.direction, tools, welcome, slots)
    for src, q in missing:
        if q.startswith(RULE_ID_PREFIX):
            print(f"RULE ID in the Instructions ({src}): {q[len(RULE_ID_PREFIX):]}")
        elif q.startswith(MUST_PREFIX):
            print(f'MISSING (from {src}): must include "{q[len(MUST_PREFIX):]}"')
        else:
            print(f'MISSING (from {src}): "{q}"')
    direction = args.direction or ("outbound" if "calling from" in path.read_text(encoding="utf-8")[:900] else "inbound")
    required = (len(required_lines(Path(args.references), set(args.workflows), direction, with_defaults(tools), slots))
                + len(required_text(Path(args.references), set(args.workflows), direction, with_defaults(tools)))
                + (1 if welcome else 0))
    print(f"fixed lines: {required} required, {len(missing)} missing")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
