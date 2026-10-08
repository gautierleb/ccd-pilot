from html.parser import HTMLParser
from pathlib import Path

import textkit

PAGE = Path(__file__).resolve().parent.parent / "docs" / "index.html"


class _Collector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()
        self.viewport: str | None = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.add(values["id"] or "")
        if tag == "meta" and values.get("name") == "viewport":
            self.viewport = values.get("content")


def _parse() -> _Collector:
    collector = _Collector()
    collector.feed(PAGE.read_text(encoding="utf-8"))
    return collector


def test_every_public_function_has_a_section() -> None:
    missing = set(textkit.__all__) - _parse().ids
    assert not missing, f"no element with these ids: {sorted(missing)}"


def test_viewport_meta_tag_is_present() -> None:
    viewport = _parse().viewport
    assert viewport is not None
    assert "width=device-width" in viewport
