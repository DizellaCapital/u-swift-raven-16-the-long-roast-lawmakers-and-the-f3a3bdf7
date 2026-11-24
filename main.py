"""One satirical sentence for the make.fun bounty
"The Long Roast: Lawmakers and the File They Cannot Convert".

Writes a single satirical sentence roasting lawmakers who want to
regulate AI, crypto and the internet but cannot convert a file to PDF.
Stdlib only, deterministic, no network access.
"""

import os
import re
import sys

MAX_CHARS = 320

SENTENCE = (
    "The lawmaker who wants to write the rules for AI spent this morning "
    "asking his intern to print the PDF so he could fax it to the "
    "committee that regulates the internet."
)


def fail(message):
    print("ERROR: " + message, file=sys.stderr)
    raise SystemExit(1)


def check_sentence(text):
    if not text or not text.strip():
        fail("sentence is empty or whitespace only")
    if len(text) > MAX_CHARS:
        fail("sentence is %d characters, over the %d limit" % (len(text), MAX_CHARS))
    if any(ord(ch) < 0x20 and ch not in "\t" for ch in text):
        fail("sentence contains control characters")
    if "\n" in text or "\r" in text:
        fail("sentence spans more than one line")
    if text != text.strip():
        fail("sentence has leading or trailing whitespace")
    if text[-1] not in ".!?":
        fail("sentence does not end with terminal punctuation")
    if len(re.findall(r"[.!?](\s|$)", text)) != 1:
        fail("text is not exactly one sentence")
    if "PDF" not in text:
        fail("sentence does not mention the file format")


def main():
    check_sentence(SENTENCE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != SENTENCE:
        fail("read-back mismatch after writing entry.txt")
    print("Wrote %d characters to %s" % (len(SENTENCE), path))
    print(SENTENCE)


if __name__ == "__main__":
    main()
