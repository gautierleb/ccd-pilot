"""Reverse the order of words."""


def reverse_words(text: str) -> str:
    """Return the words of ``text`` in reverse order, joined by single spaces.

    Words are separated by whitespace, and punctuation stays attached to its
    word. An empty text, or one with only whitespace, gives an empty string.
    """
    return " ".join(reversed(text.split()))
