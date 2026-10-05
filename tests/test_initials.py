import pytest

from textkit import initials


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("ada lovelace", "AL"),
        ("  grace   brewster\thopper ", "GBH"),
        ("", ""),
        ("   ", ""),
        ("plato", "P"),
        ("Jean\nLuc", "JL"),
    ],
)
def test_initials(name: str, expected: str) -> None:
    assert initials(name) == expected
