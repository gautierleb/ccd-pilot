import pytest

import textkit
from textkit import title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("  ,.-!  ", ""),  # only separators
        ("hello, WORLD", "Hello World"),
        ("  a  b ", "A B"),
        ("already-a-slug", "Already A Slug"),
        ("Crème brûlée", "Cr Me Br L E"),  # only a-z and 0-9 stay
        ("3rd place", "3rd Place"),
    ],
)
def test_title_case(text: str, expected: str) -> None:
    assert title_case(text) == expected


def test_title_case_is_exported() -> None:
    assert "title_case" in textkit.__all__
    assert textkit.__all__ == sorted(textkit.__all__)
    namespace: dict[str, object] = {}
    exec("from textkit import *", namespace)
    assert namespace["title_case"] is title_case
