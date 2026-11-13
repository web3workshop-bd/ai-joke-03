"""make.fun bounty ai-joke-03 — deterministic one-line joke entry.

Writes exactly one joke (1-280 chars) to /output/entry.txt.
Chosen joke: the "one-line fix" that touched 14 files — 132 chars, one line.
Stdlib only, no network, no randomness: both runs write identical bytes.
"""
import os

JOKE = "My coding agent's 'one-line fix' touched 14 files, deleted my config, and ended with: 'Let me know if you'd like me to fix the fix.'"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
