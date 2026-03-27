# Benchmarks

Reproducible benchmark tasks for energy ML. Each task defines a dataset, split protocol, and metrics so results are directly comparable across models.

## Design principles

- **Temporal splits only** — no random shuffles; test sets are always the most recent period
- **Versioned datasets** — EA-DX packages with pinned `spec_version`
- **Standard metrics** — defined with units; no ambiguity about normalisation
- **Baselines included** — every task ships at least one naive and one statistical baseline

## Tasks

| Task | Domain | Metric | Baselines | Status |
|------|--------|--------|-----------|--------|
| [Day-ahead load forecasting](load-forecasting-dayahead.md) | Distribution / Markets | MAE, RMSE, MAPE | Naive, Linear regression | 🚧 Draft |
| Short-term solar output forecasting | Generation / DER | MAE, RMSE | Naive, Persistence | 📋 Planned |
| Meter anomaly detection | Customer | F1, AUC-PR | Isolation forest | 📋 Planned |
| Wholesale price forecasting | Markets | MAE, RMSE, CRPS | Naive, ARIMA | 📋 Planned |
| DER flexibility estimation | Distribution / DER | MAE, energy error | Linear model | 📋 Planned |

## Submitting results

Results are tracked as JSON files in `benchmarks/tasks/<task-id>/results/`. See the individual task README for the required format.

## Evaluation harness

```bash
pip install -e ".[dev]"
pytest benchmarks/harness/ -m smoke -q
```
