"""Turn text into Title Case."""

import re

_SEPARATORS = re.compile(r"[^A-Za-z0-9]+")


def title_case(text: str) -> str:
    """Return the words of ``text`` capitalised and joined by a single space.

    Words end at every run of characters other than ASCII letters and digits.
    The first character of each word is upper-cased and the rest are lower-cased.
    Leading and trailing separators are dropped. An empty text, or a text with
    no ASCII letters or digits, gives an empty string.
    """
    return " ".join(word.capitalize() for word in _SEPARATORS.split(text) if word)
