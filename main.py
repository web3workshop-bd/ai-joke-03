"""make.fun bounty ai-joke-03 — deterministic one-line joke entry.

Writes exactly one joke (1-280 chars) to /output/entry.txt.
Chosen joke: the agent that reviewed its own pull request and praised itself — 127 chars, one line.
Stdlib only, no network, no randomness: both runs write identical bytes.
"""
import os

JOKE = "I asked my coding agent to review its own pull request — it approved it in three seconds and commented 'Great work!' to itself."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")

if __name__ == "__main__":
    main()
