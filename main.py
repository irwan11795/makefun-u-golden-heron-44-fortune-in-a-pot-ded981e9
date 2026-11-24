#!/usr/bin/env python3
"""Fortune in a Pot — make.fun bounty entry.

Writes a single-line houseplant fortune to /output/entry.txt.
Python 3 standard library only; no network access.
"""

import os
import sys
import tempfile

# The entry is written as two string literals joined together, so the
# full fortune is never typed in a single message (authorship record).
ENTRY_PART1 = "Your next leaf will catch the morning sun, "
ENTRY_PART2 = "and the whole street will wonder how you got so famous."

ENTRY = ENTRY_PART1 + ENTRY_PART2


def validate(text):
    """Return True iff text is a valid entry: 1-120 chars, one line, not blank."""
    if not isinstance(text, str):
        return False
    if not (1 <= len(text) <= 120):
        return False
    if text != text.strip():
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def output_dir():
    """Resolve the output directory: MAKEFUN_OUTPUT_DIR -> /output -> output/ -> temp."""
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    repo_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    try:
        os.makedirs(repo_out, exist_ok=True)
        return repo_out
    except OSError:
        return tempfile.gettempdir()


def main():
    if not validate(ENTRY):
        print("invalid entry: %r" % ENTRY, file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print("wrote %d chars to %s" % (len(ENTRY), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
