import pytest

from textkit import snake_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello, World!", "hello_world"),
        ("  A  b ", "a_b"),
        ("a \t\n b", "a_b"),  # repeated whitespace of any kind
        ("__init__", "init"),  # leading and trailing separators
        ("--a--", "a"),
        ("already_snake_case", "already_snake_case"),
        ("Crème brûlée", "cr_me_br_l_e"),  # only a-z and 0-9 stay
    ],
)
def test_snake_case(text: str, expected: str) -> None:
    assert snake_case(text) == expected
