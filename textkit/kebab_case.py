"""Turn text into kebab-case."""

from textkit.slugify import slugify


def kebab_case(text: str) -> str:
    """Return ``text`` lower-cased, with every run of other characters as one "-".

    Characters other than ASCII letters and digits (after lower-casing) separate
    words; camelCase boundaries are not split. Leading and trailing "-" are
    removed. The result is the same as ``slugify(text)``. An empty text, or a
    text with no letters or digits, gives an empty string.
    """
    return slugify(text)
