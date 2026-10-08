"""Turn text into snake_case."""

import re

_NOT_SNAKE = re.compile(r"[^a-z0-9]+")


def snake_case(text: str) -> str:
    """Return ``text`` lower-cased, with every run of other characters as one "_".

    Leading and trailing "_" are removed. An empty text gives an empty string.
    """
    return _NOT_SNAKE.sub("_", text.lower()).strip("_")
