# textkit

A small library of text helpers. Standard library only: no runtime dependencies.

## Rules for changes

- Python 3.11 or later, full type hints, one public function per concern.
- Every public function has a docstring that states its behaviour on empty input.
- Tests live in `tests/test_<module>.py` and use pytest. A change to behaviour comes with a test.
- Before you commit: `ruff check .` and `python -m pytest -q` both pass.
- Do not add dependencies, change the CI workflow or edit this file. If the task needs one of
  these, say so in your result and stop.
