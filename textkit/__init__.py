"""Small text helpers."""

from textkit.initials import initials
from textkit.slugify import slugify
from textkit.snake_case import snake_case
from textkit.stats import char_count, word_count
from textkit.truncate import truncate
from textkit.whitespace import collapse_whitespace

__all__ = [
    "char_count",
    "collapse_whitespace",
    "initials",
    "slugify",
    "snake_case",
    "truncate",
    "word_count",
]
