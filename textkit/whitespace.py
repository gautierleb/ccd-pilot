"""Collapse runs of whitespace."""

import re

_WHITESPACE = re.compile(r"\s+")


def collapse_whitespace(text: str) -> str:
    """Return ``text`` with every run of whitespace as one space.

    Whitespace at both ends is removed. An empty text gives an empty string.
    """
    return _WHITESPACE.sub(" ", text).strip()
