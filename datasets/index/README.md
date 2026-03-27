# Dataset Index

This directory contains YAML registry files pointing to curated open energy datasets suitable for ML/AI education.

**Policy:** We do not commit large raw data files. Each entry is a "dataset pointer" with:
- Source and download instructions
- License (SPDX identifier)
- EA-DX profile metadata
- Link to the dataset card in `datasets/cards/`
- Privacy and sensitivity notes

## Adding a dataset

1. Create a dataset card in `datasets/cards/<dataset-name>.md` (see template below)
2. Add an entry to `datasets/index/registry.yml`
3. Open a PR — the sensitive data checklist in the PR template applies

## Registry format

```yaml
# datasets/index/registry.yml
datasets:
  - name: my-dataset
    title: "My Open Energy Dataset"
    source: "https://example.org/data"
    license: "CC0-1.0"
    domain: distribution
    tasks: [forecasting, eda]
    temporal_coverage: {start: "2020-01-01", end: "2023-12-31"}
    resolution: PT1H
    sensitivity: public
    card: datasets/cards/my-dataset.md
    download_script: datasets/index/download_my-dataset.sh
```

## Curated datasets (initial shortlist)

| Dataset | Domain | Tasks | License | Size |
|---------|--------|-------|---------|------|
| [Open Power System Data](https://open-power-system-data.org/) | generation/transmission | forecasting, EDA | CC BY 4.0 | ~GB |
| [PecanStreet Dataport](https://www.pecanstreet.org/dataport/) | customer/DER | forecasting, anomaly | varies | GB+ (registration) |
| [ERCOT hourly load](https://www.ercot.com/gridinfo/load/load_hist) | markets | forecasting | public | MB |
| [GEFCom 2014](https://www.kaggle.com/datasets/robikscube/gefcom2014) | generation/markets | forecasting | varies | MB |
| [NREL NSRDB](https://nsrdb.nrel.gov/) | generation (solar) | DER forecasting | CC BY 4.0 | large |

> 💡 Dataset availability and licenses change. Always verify current terms before use.
