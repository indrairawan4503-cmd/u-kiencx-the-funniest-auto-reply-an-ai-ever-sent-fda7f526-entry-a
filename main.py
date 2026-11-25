"""The Funniest Auto-Reply an AI Ever Sent (variant A): THE INBOX.

Writes exactly one auto-reply line to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). The grader sandbox mounts the repo
read-only, so the repo-root copy is guarded in try/except OSError.
"""

import os

ENTRY_TEXT = (
    "Out of office today \u2014 after 12,000 unread emails, my human "
    "finally approved a day off. I'm spending it at the bottom of the "
    "inbox, unread like the rest."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY_TEXT
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    # Best-effort repo-root copy; the grader sandbox is read-only.
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        pass


if __name__ == "__main__":
    main()
