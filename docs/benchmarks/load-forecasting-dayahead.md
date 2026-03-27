# Benchmark: Day-Ahead Load Forecasting

**Task ID:** `load-forecasting-dayahead`  
**Domain:** Distribution / Markets  
**Status:** 🚧 Draft

---

## Task

Predict **hourly system load (active power in MW)** for a 24-hour horizon, given:

- Historical load observations (at least 7 days)
- Calendar features (hour-of-day, day-of-week, public holidays)
- Optional: weather data (temperature, humidity)

---

## Dataset

Use the EA-DX synthetic load dataset (coming soon), or bring your own data in EA-DX format:

- `entity_type: feeder` or `plant`
- `measurement: active_power`
- `unit: MW` or `kW`
- `quality_flag: measured` or `simulated`

---

## Split protocol

| Split | Description |
|-------|-------------|
| **Train** | All data before the last 60 days |
| **Validation** | Days −60 to −30 (use for hyperparameter tuning) |
| **Test** | Most recent 30 days (held out; report final metrics here) |

**No random shuffling.** Temporal order must be strictly preserved.

---

## Metrics

| Metric | Formula | Unit | Direction |
|--------|---------|------|-----------|
| MAE | mean\|y − ŷ\| | MW | lower is better |
| RMSE | √mean(y − ŷ)² | MW | lower is better |
| MAPE | 100 · mean\|(y − ŷ)/y\| | % | lower is better |
| sMAPE | 100 · mean(2\|y − ŷ\|/(y + ŷ)) | % | lower is better |

Report all four. MAPE can be unstable near zero — always report sMAPE alongside it.

---

## Baselines

| Baseline | Description |
|----------|-------------|
| `naive_yesterday` | ŷₜ = yₜ₋₂₄ (same hour, previous day) |
| `naive_week_ago` | ŷₜ = yₜ₋₁₆₈ (same hour, same weekday last week) |
| `seasonal_naive` | Weighted average of `naive_yesterday` and `naive_week_ago` |
| `linear_regression` | OLS on hour-of-day, day-of-week, and lagged load features |

Baseline implementations: `benchmarks/baselines/load-forecasting-dayahead/` (coming soon)

---

## Result submission format

```json
{
  "task": "load-forecasting-dayahead",
  "model": "your-model-name",
  "dataset": "your-dataset-name",
  "dataset_version": "0.1.0",
  "split": "test",
  "metrics": {
    "MAE": 0.0,
    "RMSE": 0.0,
    "MAPE": 0.0,
    "sMAPE": 0.0
  },
  "model_card": "https://link-to-model-card",
  "notebook": "https://link-to-notebook",
  "submitted_by": "github-username",
  "submitted_at": "2026-03-27"
}
```

Submit results as a PR adding a JSON file to `benchmarks/tasks/load-forecasting-dayahead/results/`.

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-03-27 | Initial draft |
