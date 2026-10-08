import pytest

from textkit import snake_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello, World!", "hello_world"),
        ("  A  b ", "a_b"),
        ("already_snake_case", "already_snake_case"),
        ("__lead_and_trail__", "lead_and_trail"),
        ("Version 2 Of HTTP11", "version_2_of_http11"),
        ("Crème brûlée", "cr_me_br_l_e"),  # only a-z and 0-9 stay
    ],
)
def test_snake_case(text: str, expected: str) -> None:
    assert snake_case(text) == expected
