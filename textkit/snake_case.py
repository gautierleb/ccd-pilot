"""Turn text into snake_case."""

import re

_WORD_BREAK = re.compile(
    r"[^A-Za-z0-9]+"  # any run of other characters
    r"|(?<=[a-z0-9])(?=[A-Z])"  # helloWorld
    r"|(?<=[A-Z])(?=[A-Z][a-z])"  # HTTPServer
)


def snake_case(text: str) -> str:
    """Return ``text`` as lower-case words joined by a single "_".

    Words end at every run of characters other than ASCII letters and digits,
    and at camelCase boundaries. Leading and trailing separators are dropped.
    An empty text, or a text with no letters or digits, gives an empty string.
    """
    return "_".join(word.lower() for word in _WORD_BREAK.split(text) if word)
