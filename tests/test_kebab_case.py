import pytest

import textkit
from textkit import kebab_case, slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello World", "hello-world"),
        ("helloWorld", "helloworld"),  # camelCase is not split
        ("HTTPServer", "httpserver"),
        ("already-kebab", "already-kebab"),
        ("snake_case_text", "snake-case-text"),
        ("  spaced  out ", "spaced-out"),
        ("a, b; c...  d!?", "a-b-c-d"),  # runs of spaces and punctuation
        ("--Leading and trailing__", "leading-and-trailing"),
        ("version 2 beta", "version-2-beta"),
        ("--__--", ""),
        ("!!!", ""),
        ("Crème brûlée", "cr-me-br-l-e"),  # only ASCII letters and digits stay
    ],
)
def test_kebab_case(text: str, expected: str) -> None:
    assert kebab_case(text) == expected
    assert kebab_case(text) == slugify(text)


def test_kebab_case_is_exported() -> None:
    assert "kebab_case" in textkit.__all__
    assert textkit.__all__ == sorted(textkit.__all__)
    namespace: dict[str, object] = {}
    exec("from textkit import *", namespace)
    assert namespace["kebab_case"] is kebab_case
