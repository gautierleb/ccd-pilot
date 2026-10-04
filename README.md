# ccd-pilot

The pilot repository of claude-controller (`ccd`): a small Python library, `textkit`, that
Claude Code workers extend under the controller's supervision.
Changes arrive as pull requests that the controller opens, checks and merges.

It is a test bed. Do not depend on it.

## Layout

- `textkit/`: the library, standard library only
- `tests/`: pytest tests, one file per module
- `.github/workflows/ci.yml`: lint and tests on every pull request

## Checks

```
python -m pip install pytest ruff
ruff check .
python -m pytest -q
```
