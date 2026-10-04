import pytest

from textkit import truncate


@pytest.mark.parametrize(
    ("text", "width", "expected"),
    [
        ("", 5, ""),
        ("short", 5, "short"),
        ("a longer sentence", 9, "a longer…"),
        ("a longer sentence", 10, "a longer…"),  # no space before the ellipsis
    ],
)
def test_truncate(text: str, width: int, expected: str) -> None:
    assert truncate(text, width) == expected


def test_truncate_with_another_ellipsis() -> None:
    assert truncate("abcdefgh", 6, ellipsis="...") == "abc..."


def test_a_width_smaller_than_the_ellipsis_is_refused() -> None:
    with pytest.raises(ValueError, match="smaller than the ellipsis"):
        truncate("abc", 2, ellipsis="...")
