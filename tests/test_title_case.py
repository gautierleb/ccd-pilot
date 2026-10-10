import pytest

from textkit import title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("   ", ""),
        ("\t\n", ""),
        ("!?,.--__", ""),
        ("hello, WORLD!", "Hello World"),
        ("hELLO wORLD", "Hello World"),
        ("  foo--bar_baz ", "Foo Bar Baz"),
        ("foo \t\n  bar", "Foo Bar"),
        ("__init__", "Init"),
        ("!!hello!!", "Hello"),
        ("3rd place", "3rd Place"),
        ("route 66 north", "Route 66 North"),
        ("helloWorld", "Helloworld"),
        ("café au lait", "Caf Au Lait"),
        ("plato", "Plato"),
    ],
)
def test_title_case(text: str, expected: str) -> None:
    assert title_case(text) == expected
