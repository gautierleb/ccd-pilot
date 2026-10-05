"""Initials of a name."""


def initials(name: str) -> str:
    """Return the upper-cased first character of each word in ``name``.

    Words are separated by whitespace. An empty name, or one with only
    whitespace, gives an empty string.
    """
    return "".join(word[0] for word in name.split()).upper()
