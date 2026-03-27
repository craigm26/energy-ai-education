# Energy AI Education Hub

> A curated, reproducible collection of ML/AI educational materials for the energy industry — built on open standards, designed for broad reuse.

[![CI](https://github.com/craigm26/energy-ai-education/actions/workflows/ci.yml/badge.svg)](https://github.com/craigm26/energy-ai-education/actions/workflows/ci.yml)
[![License: Apache-2.0](https://img.shields.io/badge/Code-Apache--2.0-blue.svg)](LICENSES/LICENSE-CODE)
[![License: CC BY 4.0](https://img.shields.io/badge/Docs-CC%20BY%204.0-lightgrey.svg)](LICENSES/LICENSE-DOCS)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/craigm26/energy-ai-education/badge)](https://securityscorecards.dev/viewer/?uri=github.com/craigm26/energy-ai-education)

## What this is

A learning hub *and* reproducible reference implementation for ML/AI in the energy sector. You can:

- **Find** trustworthy learning materials organized by domain and skill level
- **Run** end-to-end examples with pinned, tested dependencies
- **Reuse** standardized datasets and evaluation harnesses under clear open licenses
- **Interchange** energy data using the [EA-DX Package](#ea-dx-package) format

## Who it's for

| Audience | Entry point |
|----------|-------------|
| Students & newcomers | `docs/concepts/` + `notebooks/foundations/` |
| Data scientists | `notebooks/applied/` + `benchmarks/` |
| Researchers | `benchmarks/` + `standards/eadx/` |
| Engineers & architects | `standards/mappings/` + `src/` |
| Managers | `docs/case-studies/` + `docs/governance/` |

## Repository layout

```
energy-ai-education/
├── docs/                  # Conceptual guides, tutorials, case studies
│   ├── concepts/          # Energy domain + ML/AI primers
│   ├── tutorials/         # Step-by-step guides (link to notebooks)
│   ├── case-studies/      # Real-world applications (redacted appropriately)
│   └── governance/        # Model governance, responsible AI
├── notebooks/             # Executable notebooks (Jupyter)
│   ├── foundations/       # Intro: time-series, energy basics, EDA
│   ├── applied/           # Forecasting, anomaly detection, DER, markets
│   └── advanced/          # Optimization, RL, benchmarking, reproducibility
├── datasets/              # Dataset index + dataset cards (no large raw data)
│   ├── index/             # Curated dataset registry (YAML)
│   └── cards/             # Per-dataset datasheets
├── benchmarks/            # Benchmark task definitions + evaluation harness
│   ├── tasks/             # Per-task spec (dataset, split, metrics)
│   ├── baselines/         # Reference baseline models
│   └── harness/           # Shared evaluation CLI/API
├── standards/             # Energy data standards and EA-DX spec
│   ├── eadx/              # EA-DX Package specification + JSON schemas
│   │   └── schemas/       # JSON Schema + Table Schema files
│   └── mappings/          # Mappings to CIM, Green Button, OpenADR, EDI
├── src/                   # Shared Python library
│   ├── eadx/              # EA-DX package loader + validator
│   ├── loaders/           # Dataset connectors and download helpers
│   └── eval/              # Evaluation metrics and reporting
├── governance/            # Maintainers, ADRs, contributor ladder
├── .github/               # CI workflows, issue templates, CODEOWNERS
├── LICENSES/              # Separate license files per artifact type
├── CITATION.cff           # How to cite this repository
├── CONTRIBUTING.md        # Contribution guide
├── CODE_OF_CONDUCT.md     # Community standards
└── SECURITY.md            # Vulnerability reporting
```

## Quickstart

```bash
# 1. Clone
git clone https://github.com/craigm26/energy-ai-education.git
cd energy-ai-education

# 2. Install Python dependencies
pip install -e ".[dev]"

# 3. Run the hello-energy-ml notebook
jupyter lab notebooks/foundations/01_hello_energy_ml.ipynb

# 4. Run benchmark smoke tests
pytest benchmarks/harness/ -m smoke
```

## Learning paths

### 🟢 Foundations
- Energy systems primer: generation, transmission, distribution, markets
- Time-series fundamentals for energy data
- Exploratory data analysis with the EA-DX Package format

### 🟡 Applied
- Load forecasting (short-term, day-ahead)
- Price forecasting and volatility
- DER output forecasting (solar, wind)
- Anomaly detection in meter and SCADA data
- Demand response event detection

### 🔴 Advanced
- Grid topology optimization and RL agents (Grid2Op compatible)
- Federated learning for privacy-preserving energy analytics
- Benchmarking and reproducibility practices
- Governance: model cards, datasheets, AI RMF alignment

## EA-DX Package

**Energy AI Data Exchange Package (EA-DX)** is a thin ML-friendly interchange format built on open standards. It is designed to reduce friction for ML workflows while staying semantically compatible with existing energy standards.

See [`standards/eadx/`](standards/eadx/) for the full specification.

### Quick format sketch

```yaml
# observations.csv — canonical time-series resource
ts:           "ISO 8601 timestamp with UTC offset"
tz:           "IANA timezone name (optional if ts includes offset)"
entity_type:  "meter | inverter | feeder | plant | market_node | building"
entity_id:    "stable opaque ID (never a real customer ID)"
measurement:  "active_power | reactive_power | voltage | price | frequency"
value:        float
unit:         "kW | MW | kWh | V | Hz | USD/MWh"
quality_flag: "measured | estimated | imputed | simulated | redacted"
source:       "sensor | sim | market | derived"
```

### Standard mappings

| Standard | Mapping guide |
|----------|---------------|
| IEC CIM (61968/61970) | [`standards/mappings/cim.md`](standards/mappings/cim.md) |
| IEC 62325 (market comms) | [`standards/mappings/cim-markets.md`](standards/mappings/cim-markets.md) |
| Green Button / ESPI | [`standards/mappings/green-button.md`](standards/mappings/green-button.md) |
| ANSI X12 retail EDI (814/867) | [`standards/mappings/edi-retail.md`](standards/mappings/edi-retail.md) |
| OpenADR 2.0b | [`standards/mappings/openadr.md`](standards/mappings/openadr.md) |
| OpenFMB | [`standards/mappings/openfmb.md`](standards/mappings/openfmb.md) |

## License

This repository uses separate licenses by artifact type:

| Artifact | License |
|----------|---------|
| Code (`src/`, `benchmarks/harness/`, notebooks) | Apache-2.0 |
| Documentation, tutorials, diagrams | CC BY 4.0 |
| Datasets and data packages | CC0 1.0 or ODC-By (per dataset card) |

See [`LICENSES/`](LICENSES/) for full license texts and [`CITATION.cff`](CITATION.cff) for citation metadata.

## Contributing

Read [`CONTRIBUTING.md`](CONTRIBUTING.md) and [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).

**Security / sensitive data:** See [`SECURITY.md`](SECURITY.md). Do not submit operationally sensitive infrastructure details in public issues or PRs.

## How to cite

See [`CITATION.cff`](CITATION.cff). GitHub renders a "Cite this repository" button in the About sidebar.
