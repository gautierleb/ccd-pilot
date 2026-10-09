"""Small text helpers."""

from textkit.initials import initials
from textkit.kebab_case import kebab_case
from textkit.slugify import slugify
from textkit.snake_case import snake_case
from textkit.truncate import truncate
from textkit.whitespace import collapse_whitespace

__all__ = [
    "collapse_whitespace",
    "initials",
    "kebab_case",
    "slugify",
    "snake_case",
    "truncate",
]
