#!/usr/bin/env python3
"""track.py - keep this repo's memory files up to date. Standard library only.

Usage (run from the repo root):
    python scripts/track.py status                 # where am I?
    python scripts/track.py next "task"            # queue a next action
    python scripts/track.py done 2                 # finish next action #2 (also logs it)
    python scripts/track.py log "what I did"       # add to today's session log
    python scripts/track.py focus "new focus"      # change current focus
    python scripts/track.py block "reason"         # add a blocker ("none" clears them)
    python scripts/track.py decide "title" --why "reason" [--alt "..."] [--revisit "..."]
    python scripts/track.py learn "concept: explanation"
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MEM = ROOT / "memory"
STATUS = MEM / "STATUS.md"
LOG = MEM / "SESSION_LOG.md"
DECISIONS = MEM / "DECISIONS.md"
LEARN = MEM / "LEARNINGS.md"
ROADMAP = ROOT / "ROADMAP.md"

LOG_MARKER = "<!-- entries below, newest first -->"
LEARN_MARKER = "<!-- entries below -->"
EMPTY = "_(empty - add one with: python scripts/track.py next \"...\")_"


def today() -> str:
    return dt.date.today().isoformat()


def read(path: Path) -> str:
    if not path.exists():
        sys.exit(f"Missing {path.relative_to(ROOT)}. Is the repo kit installed?")
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


# ---------- STATUS.md helpers ----------

def find_section(text: str, name: str) -> re.Match:
    m = re.search(rf"^## {re.escape(name)}[ \t]*\n(.*?)(?=^## |\Z)", text, re.S | re.M)
    if not m:
        sys.exit(f"STATUS.md has no '## {name}' section.")
    return m


def replace_section(text: str, name: str, body: str) -> str:
    m = find_section(text, name)
    return text[: m.start(1)] + body.rstrip() + "\n\n" + text[m.end(1):].lstrip("\n")


def touch(text: str) -> str:
    return re.sub(r"^_Last updated: .*_$", f"_Last updated: {today()}_", text, count=1, flags=re.M)


def get_actions(text: str) -> list[str]:
    body = find_section(text, "Next actions").group(1)
    return [line[6:].strip() for line in body.splitlines() if line.startswith("- [ ] ")]


def set_actions(text: str, items: list[str]) -> str:
    body = "\n".join(f"- [ ] {i}" for i in items) if items else EMPTY
    return replace_section(text, "Next actions", body)


def bullet_lines(text: str, name: str) -> list[str]:
    body = find_section(text, name).group(1)
    return [line[2:].strip() for line in body.splitlines() if line.startswith("- ")]


# ---------- commands ----------

def cmd_log(entry: str) -> None:
    text = read(LOG)
    heading = f"### {today()}\n"
    if heading in text:
        text = text.replace(heading, f"{heading}- {entry}\n", 1)
    elif LOG_MARKER in text:
        text = text.replace(LOG_MARKER, f"{LOG_MARKER}\n\n{heading}- {entry}", 1)
    else:
        text = text.rstrip() + f"\n\n{heading}- {entry}\n"
    write(LOG, text)
    print(f"Logged: {entry}")


def cmd_next(task: str) -> None:
    text = read(STATUS)
    items = get_actions(text) + [task]
    write(STATUS, touch(set_actions(text, items)))
    print(f"Queued as #{len(items)}: {task}")


def cmd_done(n: int) -> None:
    text = read(STATUS)
    items = get_actions(text)
    if not 1 <= n <= len(items):
        sys.exit(f"No next action #{n}. There are {len(items)}.")
    task = items.pop(n - 1)
    write(STATUS, touch(set_actions(text, items)))
    cmd_log(f"DONE: {task}")


def cmd_focus(focus: str) -> None:
    text = read(STATUS)
    write(STATUS, touch(replace_section(text, "Current focus", focus)))
    cmd_log(f"Focus -> {focus}")


def cmd_block(reason: str) -> None:
    text = read(STATUS)
    if reason.strip().lower() == "none":
        lines = ["none"]
    else:
        lines = [b for b in bullet_lines(text, "Blockers") if b.lower() != "none"] + [reason]
    body = "\n".join(f"- {b}" for b in lines)
    write(STATUS, touch(replace_section(text, "Blockers", body)))
    print("Blockers updated.")


def cmd_decide(title: str, why: str, alt: str = "", revisit: str = "") -> None:
    text = read(DECISIONS)
    n = len(re.findall(r"^## D-\d+", text, re.M)) + 1
    entry = (
        f"\n## D-{n:03d} - {today()} - {title}\n"
        f"- **Why:** {why}\n"
        f"- **Alternatives rejected:** {alt or 'not recorded'}\n"
        f"- **Revisit if:** {revisit or 'not set'}\n"
    )
    write(DECISIONS, text.rstrip() + "\n" + entry)
    cmd_log(f"Decision D-{n:03d}: {title}")


def cmd_learn(note: str) -> None:
    text = read(LEARN)
    line = f"- {today()} - {note}"
    if LEARN_MARKER in text:
        text = text.rstrip() + "\n" + line + "\n"
    else:
        text = text.rstrip() + "\n\n" + line + "\n"
    write(LEARN, text)
    print(f"Learned: {note}")


def cmd_status() -> None:
    text = read(STATUS)
    updated = re.search(r"_Last updated: (.*)_", text)
    focus = find_section(text, "Current focus").group(1).strip()
    print("=" * 60)
    print(f"STATUS  (last updated {updated.group(1) if updated else '?'})")
    print("=" * 60)
    print(f"Focus:    {focus}")

    print("\nNext actions:")
    items = get_actions(text)
    for i, t in enumerate(items, 1):
        print(f"  {i}. {t}")
    if not items:
        print("  (none queued)")

    blockers = [b for b in bullet_lines(text, "Blockers") if b.lower() != "none"]
    print("\nBlockers: " + ("; ".join(blockers) if blockers else "none"))

    if ROADMAP.exists():
        rm = ROADMAP.read_text(encoding="utf-8")
        done = len(re.findall(r"^- \[[xX]\]", rm, re.M))
        total = done + len(re.findall(r"^- \[ \]", rm, re.M))
        pct = 100 * done / total if total else 0
        print(f"Roadmap:  {done}/{total} done ({pct:.0f}%)")

    if LOG.exists():
        lines = [ln for ln in LOG.read_text(encoding="utf-8").splitlines()
                 if ln.startswith(("### ", "- "))]
        print("\nRecent log:")
        for ln in lines[:6]:
            print(f"  {ln}")

    if updated:
        try:
            age = (dt.date.today() - dt.date.fromisoformat(updated.group(1))).days
            if age > 7:
                print(f"\n! STATUS.md is {age} days old. Update it before coding.")
        except ValueError:
            pass
    print()


def main(argv: list[str] | None = None) -> None:
    p = argparse.ArgumentParser(description="Keep repo memory files current.")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("status")
    sub.add_parser("next").add_argument("task")
    sub.add_parser("done").add_argument("n", type=int)
    sub.add_parser("log").add_argument("entry")
    sub.add_parser("focus").add_argument("focus")
    sub.add_parser("block").add_argument("reason")
    d = sub.add_parser("decide")
    d.add_argument("title")
    d.add_argument("--why", required=True)
    d.add_argument("--alt", default="")
    d.add_argument("--revisit", default="")
    sub.add_parser("learn").add_argument("note")
    a = p.parse_args(argv)

    if a.cmd == "status":
        cmd_status()
    elif a.cmd == "next":
        cmd_next(a.task)
    elif a.cmd == "done":
        cmd_done(a.n)
    elif a.cmd == "log":
        cmd_log(a.entry)
    elif a.cmd == "focus":
        cmd_focus(a.focus)
    elif a.cmd == "block":
        cmd_block(a.reason)
    elif a.cmd == "decide":
        cmd_decide(a.title, a.why, a.alt, a.revisit)
    elif a.cmd == "learn":
        cmd_learn(a.note)


if __name__ == "__main__":
    main()
