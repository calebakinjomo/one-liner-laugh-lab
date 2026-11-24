"""One-Liner Laugh Lab entry: a robot vacuum's excuse after eating a sock.

Writes the single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3, standard library only.
"""

import os

ENTRY = (
    "In my defence, the sock was alone, it was dark, and it was the only "
    "one of the pair the dryer hadn't already eaten."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
