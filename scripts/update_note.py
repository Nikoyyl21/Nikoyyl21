"""Refresh the auto-managed note block in README.md.

Drop a YYYY-MM-DD.md file into notes/ and write the sentence you want to
show on the first line. The latest file by name wins. No third-party deps.
"""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
NOTES = ROOT / "notes"
START = "<!-- WEEKLY-NOTE:START -->"
END = "<!-- WEEKLY-NOTE:END -->"


def latest_line():
    files = sorted(NOTES.glob("*.md"), reverse=True)
    if not files:
        return None
    for raw in files[0].read_text(encoding="utf-8").splitlines():
        line = raw.strip().lstrip("#").strip()
        if line and not line.startswith("<!--"):
            return files[0].stem, line
    return None


def main():
    picked = latest_line()
    if not picked:
        return
    date, line = picked
    block = f"{START}\n最近更新 {date}　|　{line}\n{END}"
    current = README.read_text(encoding="utf-8")
    pattern = re.escape(START) + r".*?" + re.escape(END)
    if not re.search(pattern, current, flags=re.S):
        return
    updated = re.sub(pattern, lambda _: block, current, flags=re.S)
    if updated != current:
        README.write_text(updated, encoding="utf-8")
        print(f"updated note block from {date}.md")
    else:
        print("no change")


if __name__ == "__main__":
    main()
