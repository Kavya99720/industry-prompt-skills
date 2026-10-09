#!/usr/bin/env python
"""PreToolUse hook (Edit|Write|MultiEdit): industry isolation and locks.

1. Scope. An industry SUBAGENT (agent type "<industry>-agent") may write only inside
   industries/<its-industry>/ and .claude/skills/<its-industry>-prompt-writer/. The main session is never
   blocked by this rule.
2. Lock. Industries listed in .claude/locked-industries.json (finished ones) cannot be edited by anyone,
   main session included, until the owner says "unlock <industry>" and the entry is removed from that file.

Every event with a file path is logged as one line to .claude/logs/hook-events.log (gitignored) so the agent_type field
can be checked on real subagent writes. The hook reads the tool event from stdin. Subagent calls carry agent_type (and agent_id); a call from the main
session carries neither. Exit code 2 blocks the call and shows the message to Claude.
"""
import datetime
import json
import os
import re
import sys
from pathlib import Path

INDUSTRIES = (
    "healthcare", "pharmacy", "retail", "finance", "banking",
    "education", "logistics", "hr", "real-estate", "travel",
)
LOCK_FILE = ".claude/locked-industries.json"
LOG_FILE = ".claude/logs/hook-events.log"
AGENT_RE = re.compile(r"^([a-z][a-z-]*)-agent$")


def repo_root(event):
    return Path(os.environ.get("CLAUDE_PROJECT_DIR") or event.get("cwd") or Path.cwd())


def relative_path(file_path, root):
    """Path relative to the repo root in posix form, or None when the file is outside the repo."""
    p = Path(file_path)
    if not p.is_absolute():
        p = Path(root) / p
    try:
        return p.resolve().relative_to(Path(root).resolve()).as_posix()
    except (ValueError, OSError):
        return None


def industry_of_path(rel):
    """The industry whose industries/<x>/ or skill folder holds this path, else None."""
    m = re.match(r"^industries/([^/]+)(/|$)", rel)
    if m:
        return m.group(1)
    m = re.match(r"^\.claude/skills/([^/]+)-prompt-writer(/|$)", rel)
    if m:
        return m.group(1)
    return None


def locked_industries(root):
    try:
        data = json.loads((Path(root) / LOCK_FILE).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    return set(data.get("locked", []))


def agent_industry(event):
    """The industry of a subagent named <industry>-agent, else None (main session or another kind of agent)."""
    agent = event.get("agent_type") or event.get("subagent_type") or ""
    m = AGENT_RE.match(agent)
    if m and m.group(1) in INDUSTRIES:
        return m.group(1)
    return None


def decide(event, root):
    """Return None to allow, or a message to block."""
    path = (event.get("tool_input") or {}).get("file_path")
    if not isinstance(path, str):
        return None
    rel = relative_path(path, root)
    if rel is None:
        return None
    owner = industry_of_path(rel)
    if owner and owner in locked_industries(root):
        return (f"{owner} is locked (finished, Done v1): {rel} cannot be edited. "
                f"Ask the owner; edits are allowed only after they say \"unlock {owner}\" "
                f"(then remove {owner} from {LOCK_FILE}).")
    mine = agent_industry(event)
    if mine and owner != mine:
        return (f"The {mine} agent may write only inside industries/{mine}/ and "
                f".claude/skills/{mine}-prompt-writer/. Blocked: {rel}. "
                "If a shared file needs a change, stop and tell the owner what and why.")
    return None


def log_event(event, root, message):
    """Append one line: time, tool, path, agent_type (or "missing"), decision. Never raises."""
    try:
        path = (event.get("tool_input") or {}).get("file_path")
        if not isinstance(path, str):
            return
        agent = event.get("agent_type") or event.get("subagent_type") or "missing"
        rel = relative_path(path, root) or path
        line = " | ".join([
            datetime.datetime.now().isoformat(timespec="seconds"),
            str(event.get("tool_name") or "?"),
            rel,
            f"agent_type={agent}",
            "block" if message else "allow",
        ])
        log = Path(root) / LOG_FILE
        log.parent.mkdir(parents=True, exist_ok=True)
        with log.open("a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def main():
    try:
        event = json.load(sys.stdin)
    except ValueError:
        return 0
    root = repo_root(event)
    message = decide(event, root)
    log_event(event, root, message)
    if message:
        print(message, file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
