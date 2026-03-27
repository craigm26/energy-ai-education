# Contributing to Energy AI Education Hub

Thank you for contributing! This guide explains how to submit changes and what standards we require.

## Ways to contribute

| Type | What it means |
|------|---------------|
| **Docs** | Improve concepts, tutorials, case studies, glossary, diagrams |
| **Notebooks** | Add or fix runnable Jupyter notebooks |
| **Dataset cards** | Add dataset pointers, provenance, and EA-DX metadata |
| **Benchmarks** | Add benchmark task specs, baseline models, or evaluation scripts |
| **Standards** | Improve EA-DX schemas or standard mapping guides |
| **Code** | Fix bugs or add features in `src/` |
| **Governance** | Improve maintainer docs, ADRs, contributor ladder |

## Before you start

1. Check existing [issues](https://github.com/craigm26/energy-ai-education/issues) — your idea may already be in progress.
2. For significant changes, open an issue first and get alignment before writing code.
3. Read [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
4. Read [`SECURITY.md`](SECURITY.md) — especially the **sensitive data policy**.

## Content standards

### Every tutorial / notebook must declare

```markdown
<!-- Notebook Header Cell -->
# Title
**Audience level:** foundations | applied | advanced  
**Prerequisites:** list them  
**Datasets:** link to dataset cards  
**Expected runtime:** ~N minutes on standard hardware  
**Domain:** generation | transmission | distribution | markets | customer | DER  
**Task:** forecasting | anomaly-detection | optimization | RL | EDA | other  
```

### Every dataset card must include

- License (SPDX identifier)
- Provenance (source, version, access method)
- Privacy and sensitivity notes
- EA-DX schema reference
- Datasheet link (Gebru et al. format)

### Every benchmark task must include

- Dataset + split protocol
- Metric definitions (with units)
- Baseline results
- Changelog

## Sensitive content policy

**Do not submit:**

- Operationally sensitive infrastructure details (specific design/vulnerability data for bulk electric system assets)
- Real customer identifiers or raw operational data without explicit license and anonymization
- Anything that might constitute Critical Energy Infrastructure Information (CEII) as defined by FERC/NERC

**When unsure:** open an issue first and describe the content. A maintainer will advise.

## Development workflow

```bash
# 1. Fork and clone
git clone https://github.com/YOUR_USERNAME/energy-ai-education.git
cd energy-ai-education

# 2. Create a branch
git checkout -b feat/my-improvement

# 3. Install dev dependencies
pip install -e ".[dev]"

# 4. Make changes
# 5. Run tests locally
pytest src/ benchmarks/harness/ -q
# For notebooks:
pytest --nbval notebooks/foundations/ -q

# 6. Commit with a meaningful message
git commit -m "feat: add load forecasting tutorial (applied level)"

# 7. Push and open a PR
git push origin feat/my-improvement
```

## CI requirements

All PRs must pass:

- **Lint and formatting** (`ruff format --check`, `ruff check`)
- **Type checks** (`mypy src/`)
- **Unit tests** (`pytest src/ -q`)
- **Notebook smoke tests** (`pytest --nbval notebooks/ -m smoke -q`)
- **Schema validation** (`python -m eadx validate standards/eadx/`)
- **Dependency audit** (Dependabot + dependency-review action)

## Commit message style

Use [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add day-ahead price forecasting notebook
fix: correct MW→kW unit conversion in loader
docs: improve CIM mapping guide introduction
chore: update numpy to 2.x
```

## Review process

1. CI must pass ✅
2. CODEOWNERS are automatically assigned — domain reviewers may be added
3. At least one maintainer approval required
4. Docs changes additionally need an education editor review

## Contributor ladder

| Level | How to get there |
|-------|-----------------|
| **Contributor** | Any merged PR |
| **Reviewer** | 3+ merged PRs in a domain, invited by a maintainer |
| **Maintainer** | Consistent quality contributions, community trust, nominated by existing maintainers |

## Questions?

Open a [Discussion](https://github.com/craigm26/energy-ai-education/discussions) rather than an issue for general questions.
