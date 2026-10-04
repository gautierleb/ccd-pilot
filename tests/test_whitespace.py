import pytest

from textkit import collapse_whitespace


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("  a \t b\n\nc ", "a b c"),
        (" \t\n ", ""),
        ("already clean", "already clean"),
        ("one", "one"),
    ],
)
def test_collapse_whitespace(text: str, expected: str) -> None:
    assert collapse_whitespace(text) == expected
