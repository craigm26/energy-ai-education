---
hide:
  - navigation
  - toc
---

# Energy AI Education Hub

<div class="hero" markdown>

**Curated, reproducible ML/AI learning materials for the energy industry — built on open standards.**

[:fontawesome-solid-bolt: Get started](#get-started){ .md-button .md-button--primary }
[:fontawesome-brands-github: View on GitHub](https://github.com/craigm26/energy-ai-education){ .md-button }

</div>

---

## What this is

A learning hub *and* reproducible reference implementation for ML/AI in the energy sector. Three surfaces in one place:

<div class="grid cards" markdown>

-   :material-book-open-variant:{ .lg .middle } **Learning surface**

    ---

    Concept guides, tutorials, and case studies organized by domain and skill level. From "what is a feeder?" to benchmarking production models.

    [:octicons-arrow-right-24: Browse docs](learning-paths/overview.md)

-   :material-play-box-multiple:{ .lg .middle } **Reproducibility surface**

    ---

    Jupyter notebooks with pinned, tested dependencies. Every example runs in CI. Baselines, metrics, and split protocols are versioned alongside the code.

    [:octicons-arrow-right-24: View learning paths](learning-paths/foundations.md)

-   :material-swap-horizontal:{ .lg .middle } **Interoperability surface**

    ---

    EA-DX Package — a thin ML-friendly data interchange format with explicit mappings to CIM, Green Button, OpenADR, ANSI X12, and OpenFMB.

    [:octicons-arrow-right-24: EA-DX format](eadx/index.md)

</div>

---

## Who it's for

| Audience | Where to start |
|----------|---------------|
| 🎓 Students & newcomers | [Foundations path](learning-paths/foundations.md) |
| 📊 Data scientists | [Applied path](learning-paths/applied.md) + [Benchmarks](benchmarks/index.md) |
| 🔬 Researchers | [Advanced path](learning-paths/advanced.md) + [EA-DX spec](eadx/index.md) |
| ⚙️ Engineers & architects | [EA-DX mappings](eadx/mappings.md) + [GitHub source](https://github.com/craigm26/energy-ai-education/tree/main/src) |
| 📋 Managers & policy leads | Case studies (coming soon) + [Model governance](learning-paths/advanced.md) |

---

## Get started

=== "Explore docs"
    Browse the learning paths in the left navigation, or jump to:

    - [Foundations — energy time-series basics](learning-paths/foundations.md)
    - [Applied — load forecasting end-to-end](learning-paths/applied.md)
    - [EA-DX Package format](eadx/index.md)

=== "Run locally"
    ```bash
    git clone https://github.com/craigm26/energy-ai-education.git
    cd energy-ai-education
    pip install -e ".[dev]"
    jupyter lab notebooks/foundations/
    ```

=== "Validate an EA-DX package"
    ```bash
    pip install -e ".[dev]"
    eadx validate /path/to/my-dataset/
    eadx info    /path/to/my-dataset/
    ```

=== "Run benchmarks"
    ```bash
    pip install -e ".[dev]"
    pytest benchmarks/harness/ -m smoke -q
    ```

---

## EA-DX Package — quick look

**Energy AI Data Exchange Package (EA-DX)** reduces friction between energy domain systems and ML workflows — without replacing existing standards.

```yaml
# observations.csv — the canonical time-series resource
ts:           "2024-06-15T14:00:00-07:00"   # ISO 8601 with UTC offset
tz:           "America/Los_Angeles"           # IANA timezone
entity_type:  "meter"                         # meter | feeder | plant | ...
entity_id:    "MTR-0042"                      # stable opaque ID (no PII)
measurement:  "active_power"
value:        12.4
unit:         "kW"
quality_flag: "measured"                      # measured | estimated | simulated | ...
source:       "sensor"
```

Maps to CIM `IntervalReading`, Green Button `IntervalBlock`, OpenADR signals, ANSI X12 867, and OpenFMB `ReadingMessage`.

[Full EA-DX specification →](eadx/index.md)

---

## Benchmarks

| Benchmark | Domain | Metric | Status |
|-----------|--------|--------|--------|
| [Day-ahead load forecasting](benchmarks/load-forecasting-dayahead.md) | Distribution / Markets | MAE, RMSE, MAPE | 🚧 Draft |
| Short-term solar output forecasting | Generation / DER | MAE, RMSE | 📋 Planned |
| Meter anomaly detection | Customer / Distribution | F1, AUC-PR | 📋 Planned |
| Wholesale price forecasting | Markets | MAE, RMSE, CRPS | 📋 Planned |

---

## Principles

!!! tip "Reproducible by default"
    Every notebook and benchmark runs in CI with pinned dependencies. If it's in this repo, it runs.

!!! info "Open and interoperable"
    Code is Apache-2.0. Docs are CC BY 4.0. Data defaults to CC0. All three licensing layers are machine-readable via SPDX.

!!! warning "Sensitive data policy"
    No operationally sensitive infrastructure details (CEII), customer PII, or live operational data. Synthetic datasets are preferred. See [SECURITY.md](https://github.com/craigm26/energy-ai-education/blob/main/SECURITY.md).

---

## Contributing

Read [CONTRIBUTING.md](contributing.md). Short version:

1. Fork → branch → PR
2. New notebooks need a header cell (audience level, prerequisites, expected runtime)
3. New datasets need a [dataset card](datasets/template.md)
4. CI must pass: `ruff`, `mypy`, `pytest`, notebook smoke tests

[![CI](https://github.com/craigm26/energy-ai-education/actions/workflows/ci.yml/badge.svg)](https://github.com/craigm26/energy-ai-education/actions/workflows/ci.yml)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/craigm26/energy-ai-education/badge)](https://securityscorecards.dev/viewer/?uri=github.com/craigm26/energy-ai-education)
