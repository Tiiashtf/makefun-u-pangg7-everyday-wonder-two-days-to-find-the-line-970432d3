#!/usr/bin/env python3
"""Write one sentence of everyday wonder to /output/entry.txt.

Deterministic, no network, no input: the sentence is a constant string.
Its turn lands in the last words: a bird that wandered in by accident
is suddenly a shopper with errands, and the automatic door -- built to
welcome paying customers -- has let in the one visitor who will never pay.
The output step never removes the output directory itself -- it only
clears the directory's contents, then writes entry.txt -- so the program
also works when /output is root-owned inside a sticky parent.
"""

import os
import shutil

SENTENCE = (
    "The supermarket door slid open for a pigeon, "
    "and the pigeon strolled in like it had a shopping list."
)

OUTPUT_DIR = "/output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as fh:
        fh.write(SENTENCE)


if __name__ == "__main__":
    main()
