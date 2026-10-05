"""Reverse the order of words."""


def reverse_words(text: str) -> str:
    """Return the words of ``text`` in reverse order, joined by single spaces.

    Words are separated by whitespace; punctuation stays attached to its word.
    An empty or whitespace-only text gives an empty string.
    """
    return " ".join(reversed(text.split()))
