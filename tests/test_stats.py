import pytest

import textkit
from textkit import char_count, word_count


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("hello", 1),
        ("hello world", 2),
        ("one   two    three", 3),
        ("tab\tseparated\twords", 3),
        ("line one\nline two\r\nline three", 6),
        ("  leading and trailing  ", 3),
        ("   ", 0),
        (" \t\n\r\f\v", 0),
        ("non breaking space", 3),
    ],
)
def test_word_count(text: str, expected: int) -> None:
    assert word_count(text) == expected
    assert word_count(text) == len(text.split())


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("hello", 5),
        ("hello world", 11),
        (" a \t b\n", 7),
        ("   ", 3),
    ],
)
def test_char_count_with_spaces(text: str, expected: int) -> None:
    assert char_count(text) == expected
    assert char_count(text, spaces=True) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", 0),
        ("hello", 5),
        ("hello world", 10),
        (" a \t b\n", 2),
        ("   ", 0),
        (" \t\n\r\f\v", 0),
        ("non breaking", 11),
    ],
)
def test_char_count_without_spaces(text: str, expected: int) -> None:
    assert char_count(text, spaces=False) == expected


def test_stats_are_exported() -> None:
    assert "char_count" in textkit.__all__
    assert "word_count" in textkit.__all__
    assert textkit.__all__ == sorted(textkit.__all__)
    namespace: dict[str, object] = {}
    exec("from textkit import *", namespace)
    assert namespace["char_count"] is char_count
    assert namespace["word_count"] is word_count
