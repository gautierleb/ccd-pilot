"""Turn text into kebab-case."""

from textkit.slugify import slugify


def kebab_case(text: str) -> str:
    """Return ``text`` as lower-case words joined by a single "-".

    Words end at every run of characters other than ASCII letters and digits.
    camelCase boundaries are not split, so "helloWorld" gives "helloworld".
    Leading and trailing dashes are dropped. An empty text, or a text with no
    ASCII letters or digits, gives an empty string.
    """
    return slugify(text)
