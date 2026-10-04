"""Turn text into a slug."""

import re

_NOT_SLUG = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """Return ``text`` lower-cased, with every run of other characters as one "-".

    Leading and trailing "-" are removed. An empty text gives an empty slug.
    """
    return _NOT_SLUG.sub("-", text.lower()).strip("-")
