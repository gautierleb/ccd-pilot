"""Tidy the whitespace in text."""


def collapse_whitespace(text: str) -> str:
    """Return ``text`` with every run of whitespace as one space and both ends stripped.

    An empty text, or one of only whitespace, gives an empty string.
    """
    return " ".join(text.split())
