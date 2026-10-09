import pytest

import textkit
from textkit import snake_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello World", "hello_world"),
        ("helloWorld", "hello_world"),
        ("HelloWorld", "hello_world"),
        ("HTTPServer", "http_server"),
        ("already_snake", "already_snake"),
        ("kebab-case-text", "kebab_case_text"),
        ("  spaced  out ", "spaced_out"),
        ("version 2 beta", "version_2_beta"),
        ("--__--", ""),
        ("version2Beta", "version2_beta"),
        ("parseHTTP", "parse_http"),
        ("Crème brûlée", "cr_me_br_l_e"),  # only ASCII letters and digits stay
    ],
)
def test_snake_case(text: str, expected: str) -> None:
    assert snake_case(text) == expected


def test_snake_case_is_exported() -> None:
    assert "snake_case" in textkit.__all__
    assert textkit.__all__ == sorted(textkit.__all__)
    namespace: dict[str, object] = {}
    exec("from textkit import *", namespace)
    assert namespace["snake_case"] is snake_case
