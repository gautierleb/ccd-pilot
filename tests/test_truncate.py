import pytest

from textkit import truncate


@pytest.mark.parametrize(
    ("text", "width", "expected"),
    [
        ("", 5, ""),
        ("heron", 10, "heron"),
        ("short", 5, "short"),
        ("kingfisher", 5, "king…"),
        ("a longer sentence", 10, "a longer …"),  # spaces before the ellipsis stay
        ("abc", 1, "…"),
    ],
)
def test_truncate(text: str, width: int, expected: str) -> None:
    assert truncate(text, width) == expected


def test_truncate_with_another_ellipsis() -> None:
    assert truncate("abcdefgh", 6, ellipsis="...") == "abc..."


@pytest.mark.parametrize("width", [0, -1])
def test_a_width_below_one_is_refused(width: int) -> None:
    with pytest.raises(ValueError, match="at least 1"):
        truncate("a", width)


def test_a_width_smaller_than_the_ellipsis_is_refused() -> None:
    with pytest.raises(ValueError, match="smaller than the ellipsis"):
        truncate("abc", 2, ellipsis="...")
