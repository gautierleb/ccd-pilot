"""Turn text into kebab-case."""

import re

_NOT_WORD = re.compile(r"[^a-z0-9]+")


def kebab_case(text: str) -> str:
    """Return ``text`` as lower-case words joined by a single "-".

    Words end at every run of characters other than ASCII letters and digits;
    camelCase is not split. Leading and trailing "-" are removed. An empty
    text, or a text with no ASCII letters or digits, gives an empty string.
    """
    return _NOT_WORD.sub("-", text.lower()).strip("-")
