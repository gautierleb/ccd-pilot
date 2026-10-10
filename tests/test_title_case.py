import pytest

import textkit
from textkit import title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("--- !", ""),
        ("   ", ""),
        ("hello, WORLD", "Hello World"),
        ("  the--quick_brown  fox ", "The Quick Brown Fox"),
        ("a - b_c,d", "A B C D"),
        ("3rd place", "3rd Place"),
        ("helloWorld", "Helloworld"),
        ("plato", "Plato"),
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
