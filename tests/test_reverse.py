import pytest

from textkit import reverse_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("one two  three", "three two one"),
        ("", ""),
        ("   ", ""),
        ("Hello, world!", "world! Hello,"),
        ("  single ", "single"),
        ("a\tb\nc", "c b a"),
    ],
)
def test_reverse_words(text: str, expected: str) -> None:
    assert reverse_words(text) == expected
