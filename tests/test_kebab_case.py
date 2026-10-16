import pytest

import textkit
from textkit import kebab_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello World", "hello-world"),
        ("helloWorld", "hello-world"),
        ("HelloWorld", "hello-world"),
        ("HTTPServer", "http-server"),
        ("snake_case_text", "snake-case-text"),
        ("already-kebab", "already-kebab"),
        ("  spaced__out- ", "spaced-out"),
        ("a---b", "a-b"),
        ("-leading", "leading"),
        ("trailing-", "trailing"),
        ("--__--", ""),
        ("version 2 beta", "version-2-beta"),
        ("version2Beta", "version2-beta"),
        ("parseHTTP", "parse-http"),
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
