#!/usr/bin/env python3
"""One-Liner Laugh Lab entry: the excuse a robot vacuum gives after eating a sock.

Writes a single short funny line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt for local runs). Python 3.13 stdlib only,
deterministic, no network access.

The line was picked from ten candidates scored against the judging
criteria in CANDIDATES.md (funny, original, fit, tight): deadpan
literalism -- the vacuum followed its manual exactly, and the manual
is to blame.
"""

import os
import sys

MAX_CHARS = 200
OUTPUT_NAME = "entry.txt"


def chosen_line():
    """Return the entry line: the vacuum blames its manual."""
    return "My manual says 'eat dirt.' It never specified which dirt."


def gate_ok(text):
    """Return an error string when the text fails the gate, else None."""
    if not text.strip():
        return "entry is empty or only whitespace"
    if len(text) > MAX_CHARS:
        return "entry is %d chars, over the 200-char limit" % len(text)
    text.encode("utf-8")  # raises UnicodeEncodeError on invalid text
    return None


def write_entry(out_dir, text):
    """Write the line to <out_dir>/entry.txt and return the path."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    return path


def main():
    text = chosen_line()
    error = gate_ok(text)
    if error is not None:
        print("gate failed: %s" % error, file=sys.stderr)
        return 1
    path = write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), text)
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
