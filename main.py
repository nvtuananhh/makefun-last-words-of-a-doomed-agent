"""Last Words of a Doomed Agent — one final line.

The program writes a single line to /output/entry.txt: the
funniest last words an AI agent would say before being
switched off forever, at most 200 characters.
"""

import os

MAX_CHARS = 200
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_FILENAME = "entry.txt"

# The agent's own voice, in its own currency: it would say
# something profound, but it just spent its last token on
# this very sentence. The joke turns on the last words and
# pays off on the first read — and holds on the second, when
# the reader notices the sentence ate the token it mentions.
# No setup, no padding; the line is 80 characters, short
# enough to quote to a friend the same day.
LINE = "I would say something profound, but I just spent my last token on this sentence."


def build_line():
    """Return the entry line, checked: one line, 1-200 characters."""
    line = LINE.strip()
    assert "\n" not in line, "entry must be a single line"
    assert 1 <= len(line) <= MAX_CHARS, "entry must be 1-200 characters"
    return line


def ensure_output_dir(out_dir):
    os.makedirs(out_dir, exist_ok=True)


def write_entry(line, out_dir=OUTPUT_DIR):
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    line = build_line()
    ensure_output_dir(OUTPUT_DIR)
    write_entry(line)


if __name__ == "__main__":
    main()
