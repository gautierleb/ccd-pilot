import pytest

from textkit import slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello, World!", "hello-world"),
        ("  A  b ", "a-b"),
        ("already-a-slug", "already-a-slug"),
        ("Crème brûlée", "cr-me-br-l-e"),  # only a-z and 0-9 stay
    ],
)
def test_slugify(text: str, expected: str) -> None:
    assert slugify(text) == expected
