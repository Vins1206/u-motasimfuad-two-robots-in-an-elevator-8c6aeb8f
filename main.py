"""Two Robots in an Elevator — one line of awkward robot small talk.

Writes exactly one line of plain text to /output/entry.txt.
Python standard library only.
"""

import os

LINE = "Sorry, my voice module glitched and just said 'nice weather' — indoors, at night, in an elevator, to another robot."


def main():
    # Gate: exactly one line, 1-200 characters, not only whitespace.
    assert "\n" not in LINE and 1 <= len(LINE) <= 200, len(LINE)
    assert LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
