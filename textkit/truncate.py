"""Shorten text to a width."""


def truncate(text: str, width: int, *, ellipsis: str = "…") -> str:
    """Return ``text`` unchanged if it has at most ``width`` characters.

    Otherwise return its first ``width - len(ellipsis)`` characters followed by
    ``ellipsis``, so the result has exactly ``width`` characters. With the default
    ellipsis that is the first ``width - 1`` characters and "…". An empty text stays
    empty. ``width`` must be at least 1 and at least the length of ``ellipsis``, else
    ValueError is raised.
    """
    if width < 1:
        raise ValueError("width must be at least 1")
    if width < len(ellipsis):
        raise ValueError("width is smaller than the ellipsis")
    if len(text) <= width:
        return text
    return text[: width - len(ellipsis)] + ellipsis
