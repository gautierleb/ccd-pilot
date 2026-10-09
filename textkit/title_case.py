"""Turn text into Title Case."""

import re

_WORD = re.compile(r"[a-z0-9]+")


def title_case(text: str) -> str:
    """Return ``text`` as words joined by a single space, each in Title Case.

    Words are split as slugify() splits them: they are the runs of ASCII
    letters and digits, and every other run of characters is a separator.
    Each word has its first character upper-cased and the rest lower-cased.
    An empty text, or a text with no letters or digits, gives an empty string.
    """
    return " ".join(word.capitalize() for word in _WORD.findall(text.lower()))
