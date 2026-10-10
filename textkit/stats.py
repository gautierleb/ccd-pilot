"""Count words and characters."""


def word_count(text: str) -> int:
    """Return the number of words in ``text``.

    A word is a run of non-whitespace characters, split the way ``str.split()``
    splits. An empty text gives 0.
    """
    return len(text.split())


def char_count(text: str, spaces: bool = True) -> int:
    """Return the number of characters in ``text``.

    With ``spaces`` false, whitespace characters are left out of the count.
    An empty text gives 0.
    """
    if spaces:
        return len(text)
    return sum(1 for char in text if not char.isspace())
