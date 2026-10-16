import pytest

import textkit
from textkit import kebab_case, slugify


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello World", "hello-world"),
        ("  spaced  out ", "spaced-out"),
        ("MiXeD CaSe", "mixed-case"),
        ("version 2 beta", "version-2-beta"),
        ("already_snake", "already-snake"),
        ("kebab-case-text", "kebab-case-text"),
        ("--__--", ""),
        ("helloWorld", "helloworld"),  # camelCase is not split
        ("Crème brûlée", "cr-me-br-l-e"),  # only ASCII letters and digits stay
        ("日本語", ""),
    ],
)
def test_kebab_case(text: str, expected: str) -> None:
    assert kebab_case(text) == expected


@pytest.mark.parametrize("text", ["", "Hello World", "a  --  b", "İstanbul", "Kelvin"])
def test_kebab_case_matches_slugify(text: str) -> None:
    assert kebab_case(text) == slugify(text)


def test_kebab_case_is_exported() -> None:
    assert "kebab_case" in textkit.__all__
    assert textkit.__all__ == sorted(textkit.__all__)
    namespace: dict[str, object] = {}
    exec("from textkit import *", namespace)
    assert namespace["kebab_case"] is kebab_case
