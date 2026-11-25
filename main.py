"""Notes From a Passive-Aggressive Fridge — make.fun entry.

Writes the fridge's one-line passive-aggressive note to entry.txt in the
output directory and exits 0.
"""

import os

ENTRY = "I kept your yogurt at 3 degrees while you ate takeout four nights running. You're welcome. I'm not."

MAX_CHARS = 200


def output_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} characters, over the {MAX_CHARS}-character limit"
        )
    if not ENTRY.strip() or "\n" in ENTRY:
        raise SystemExit("entry must be one non-blank line")
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
