import pytest

from textkit import snake_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", ""),
        ("Hello, World!", "hello_world"),
        ("  A  b ", "a_b"),
        ("  leading", "leading"),
        ("trailing!!", "trailing"),
        ("a --- b", "a_b"),
        ("a,,,b...c", "a_b_c"),
        ("!!!", ""),
        ("already_snake_case", "already_snake_case"),
        ("kebab-case-text", "kebab_case_text"),
        ("Crème brûlée", "cr_me_br_l_e"),  # only a-z and 0-9 stay
    ],
)
def test_snake_case(text: str, expected: str) -> None:
    assert snake_case(text) == expected
