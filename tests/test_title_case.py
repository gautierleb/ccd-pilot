import pytest

import textkit
from textkit import title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("hello world", "Hello World"),
        ("hELLO   wORLD", "Hello World"),
        ("hELLO wORLD", "Hello World"),
        ("kebab-case_text", "Kebab Case Text"),
        ("  spaced  out ", "Spaced Out"),
        ("version 2 beta", "Version 2 Beta"),
        ("--__--", ""),
        ("Crème brûlée", "Cr Me Br L E"),  # only ASCII letters and digits stay
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
