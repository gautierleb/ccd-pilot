import pytest

import textkit
from textkit import kebab_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello World", "hello-world"),
        ("Hello, World! How are you?", "hello-world-how-are-you"),
        ("helloWorld", "hello-world"),
        ("HelloWorld", "hello-world"),
        ("HTTPServer", "http-server"),
        ("parseHTTP", "parse-http"),
        ("version 2 beta", "version-2-beta"),
        ("version2Beta", "version2-beta"),
        ("already-kebab-case", "already-kebab-case"),
        ("snake_case_text", "snake-case-text"),
        ("  spaced  out ", "spaced-out"),
        ("--leading and trailing__", "leading-and-trailing"),
        ("--__--", ""),
        ("   ", ""),
        ("Crème brûlée", "cr-me-br-l-e"),  # only ASCII letters and digits stay
    ],
)
def test_kebab_case(text: str, expected: str) -> None:
    assert kebab_case(text) == expected


def test_kebab_case_is_exported() -> None:
    assert "kebab_case" in textkit.__all__
    assert textkit.__all__ == sorted(textkit.__all__)
    namespace: dict[str, object] = {}
    exec("from textkit import *", namespace)
    assert namespace["kebab_case"] is kebab_case
