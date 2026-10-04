"""Shorten text to a width."""


def truncate(text: str, width: int, *, ellipsis: str = "…") -> str:
    """Return ``text`` cut to at most ``width`` characters, ending in ``ellipsis`` when it was cut.

    An empty text stays empty. ``width`` must be at least the length of ``ellipsis``.
    """
    if width < len(ellipsis):
        raise ValueError("width is smaller than the ellipsis")
    if len(text) <= width:
        return text
    return text[: width - len(ellipsis)].rstrip() + ellipsis
