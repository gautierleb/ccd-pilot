"""Turn text into kebab-case."""

from textkit.snake_case import _WORD_BREAK


def kebab_case(text: str) -> str:
    """Return ``text`` as lower-case words joined by a single "-".

    Words end where ``snake_case`` ends them: at every run of characters other
    than ASCII letters and digits, and at camelCase boundaries. Leading and
    trailing separators are dropped. An empty text, or a text with no letters
    or digits, gives an empty string.
    """
    return "-".join(word.lower() for word in _WORD_BREAK.split(text) if word)
