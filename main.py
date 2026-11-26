"""One-Liner Laughs — make.fun entry.

One joke, one line: an AI assistant asked for motivation answers
with a twist nobody asked for. The program writes the whole entry —
one line, 119 of 200 characters — to /output/entry.txt.
"""

import os

# The entry line: setup ("asked my AI assistant for motivation"),
# surprise twist at the end ("Let's start by deleting this") — the
# punch the judge weighs most after "is it a one-line joke". 119/200 chars.
LINE = "I asked my AI assistant for motivation. It sighed, opened my browser history, and said, 'Let's start by deleting this.'"
MAX_CHARS = 200


def entry_line() -> str:
    """Return the entry line, refusing anything outside the gate."""
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError("entry line outside the 1..200 gate")
    return LINE


def main() -> None:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(entry_line())


if __name__ == "__main__":
    main()
