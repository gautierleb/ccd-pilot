import pytest

from textkit import title_case


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("hello, WORLD!", "Hello World"),
        ("  the_quick--brown fox ", "The Quick Brown Fox"),
        ("", ""),
        ("   ", ""),
        ("\t\n", ""),
        ("?!...--", ""),
        ("hELLo WoRLD", "Hello World"),
        ("ALL CAPS", "All Caps"),
        ("a,,;;  --b", "A B"),
        ("--leading", "Leading"),
        ("trailing!!", "Trailing"),
        ("  --both--  ", "Both"),
        ("route 66 is 3D", "Route 66 Is 3d"),
        ("42", "42"),
        ("x2y", "X2y"),
        ("café au lait", "Caf Au Lait"),
    ],
)
def test_title_case(text: str, expected: str) -> None:
    assert title_case(text) == expected
