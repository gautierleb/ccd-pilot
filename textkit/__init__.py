"""Small text helpers."""

from textkit.reverse import reverse_words
from textkit.slugify import slugify
from textkit.truncate import truncate
from textkit.whitespace import collapse_whitespace

__all__ = ["collapse_whitespace", "reverse_words", "slugify", "truncate"]
