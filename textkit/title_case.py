"""Turn text into Title Case."""

import re

_WORD = re.compile(r"[a-z0-9]+")


def title_case(text: str) -> str:
    """Return the words of ``text`` capitalised and joined by single spaces.

    Words are the runs of ASCII letters and digits, split as in ``slugify``.
    Every other character separates words and is dropped. An empty text, or a
    text with no letters or digits, gives an empty string.
    """
    return " ".join(word.capitalize() for word in _WORD.findall(text.lower()))
