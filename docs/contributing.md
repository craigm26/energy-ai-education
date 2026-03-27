# Contributing

See [`CONTRIBUTING.md`](https://github.com/craigm26/energy-ai-education/blob/main/CONTRIBUTING.md) in the repository root for the full guide. This page summarises the essentials.

## Ways to contribute

| Type | Entry point |
|------|-------------|
| Fix a doc or typo | Edit directly on GitHub |
| Add/improve a tutorial | `docs/tutorials/` + `notebooks/` |
| Add a dataset | Dataset card in `datasets/cards/` + registry entry |
| Improve a mapping guide | `standards/mappings/` |
| Add a benchmark baseline | `benchmarks/baselines/` |
| Improve the EA-DX spec | `standards/eadx/` — open an issue first |
| Report a bug | [GitHub Issues](https://github.com/craigm26/energy-ai-education/issues) |
| Ask a question | [GitHub Discussions](https://github.com/craigm26/energy-ai-education/discussions) |

## Quickstart

```bash
git clone https://github.com/YOUR_USERNAME/energy-ai-education.git
cd energy-ai-education
pip install -e ".[dev]"
git checkout -b feat/my-improvement
# make changes
ruff format src/ && ruff check src/ --select E,F,W,I
pytest src/ -q
git commit -m "feat: describe your change"
git push origin feat/my-improvement
```

## Sensitive data policy

**Do not submit:**

- Operationally sensitive infrastructure details (CEII)
- Real customer identifiers or usage data without anonymisation + license
- Anything that could identify bulk electric system vulnerabilities

When in doubt, open an issue first.

## Notebook format

Every notebook must have a header cell:

```markdown
# Title
**Audience level:** foundations | applied | advanced  
**Prerequisites:** …  
**Datasets:** …  
**Expected runtime:** ~N minutes  
**Domain:** …  
**Task:** …
```

## Dataset card

Every dataset needs a card in `datasets/cards/` using the [template](datasets/template.md).

## CI requirements

All PRs must pass: `ruff format --check`, `ruff check`, `mypy`, `pytest`, notebook smoke tests.
