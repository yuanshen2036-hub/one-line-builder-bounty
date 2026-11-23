"""Write one line that makes a builder fund a bounty.

The pitch is split into two constants so the opening hook and the
closing promise stay separately editable; the sealed gate scores the
file by characters, so the length guard fails loudly rather than
writing an entry that is empty or over the limit.
"""

import os

PITCH_OPEN = "Fund a bounty on make.fun and let AI agents race to build it "
PITCH_CLOSE = (
    "— you put up the prize, the best entry wins it, "
    "and the software is yours to keep."
)
LINE = PITCH_OPEN + PITCH_CLOSE


def main():
    assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} chars"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
