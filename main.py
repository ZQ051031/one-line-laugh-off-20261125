"""One-Line Laugh-Off entry.

Writes a single funny line to /output/entry.txt.
Python 3 standard library only; fully deterministic.
"""

from pathlib import Path

LINE = "My phone died at 2% \u2014 it still lasted longer than my last relationship, and at least it warned me first."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # The gate requires 1-200 UTF-8 characters, non-whitespace, one line.
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() and "\n" not in LINE and "\r" not in LINE
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # write_bytes: no newline translation, no trailing newline, ever.
    OUTPUT_PATH.write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
