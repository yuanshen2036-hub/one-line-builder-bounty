#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes the pitch line to /output/entry.txt, the file the sealed gate
scores: UTF-8 text of 1 to 240 characters, a single sentence pitching
a builder on funding a make.fun bounty and letting AI agents compete
for the reward.
"""

import os

PITCH_OPEN = "Fund a bounty on make.fun and let AI agents race to build it "
PITCH_CLOSE = (
    "\u2014 you put up the prize, the best entry wins it, "
    "and the software is yours to keep."
)
LINE = PITCH_OPEN + PITCH_CLOSE
MAX_CHARS = 240


def main() -> None:
    # The sealed gate scores the file by characters; fail loudly
    # rather than write an entry that is empty or over the limit.
    assert 1 <= len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
