"""Turn text into Title Case."""

import re

_WORD = re.compile(r"[a-z0-9]+", re.IGNORECASE | re.ASCII)


def title_case(text: str) -> str:
    """Return ``text`` as words joined by a single space, each one capitalised.

    A word is a maximal run of ASCII letters and digits, as in ``slugify``.
    Every other character is a separator and is dropped; camelCase is not
    split. Each word has its first character upper-cased and the rest
    lower-cased. An empty text, or a text with no letters or digits, gives an
    empty string.
    """
    return " ".join(word.capitalize() for word in _WORD.findall(text))
