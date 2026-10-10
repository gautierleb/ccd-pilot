"""Small text helpers."""

from textkit.initials import initials
from textkit.slugify import slugify
from textkit.snake_case import snake_case
from textkit.title_case import title_case
from textkit.truncate import truncate
from textkit.whitespace import collapse_whitespace

__all__ = [
    "collapse_whitespace",
    "initials",
    "slugify",
    "snake_case",
    "title_case",
    "truncate",
]
