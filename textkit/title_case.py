"""Title-case text."""

from textkit.slugify import slugify


def title_case(text: str) -> str:
    """Return ``text`` with each word capitalized and the words joined by one space.

    Words are split as in ``slugify``: the text is lower-cased and every run of
    characters other than a-z and 0-9 separates words. An empty text, or one
    with no letters or digits, gives an empty string.
    """
    return " ".join(word.capitalize() for word in slugify(text).split("-") if word)
