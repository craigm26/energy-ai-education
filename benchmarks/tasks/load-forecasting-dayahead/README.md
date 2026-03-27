# Benchmark: Day-Ahead Load Forecasting

**Task ID:** `load-forecasting-dayahead`  
**Domain:** Distribution / Markets  
**EA-DX tasks:** forecasting  
**Maturity:** Applied  
**Status:** 🚧 Draft

## Task definition

Predict hourly system load (active power in MW) for a 24-hour horizon, given:
- Historical load observations (at least 7 days)
- Calendar features (hour-of-day, day-of-week, holidays)
- Optional: weather data (temperature, humidity)

## Dataset

Use the EA-DX synthetic load dataset (see `datasets/index/registry.yml`):

```bash
python -m eadx validate datasets/synthetic-load/
```

Or bring your own data in EA-DX format with `entity_type: feeder`, `measurement: active_power`.

## Split protocol

| Split | Description |
|-------|-------------|
| Train | All data before the last 60 days |
| Validation | Days -60 to -30 |
| Test | Last 30 days |

No random shuffling — temporal order must be preserved.

## Metrics

| Metric | Unit | Direction |
|--------|------|-----------|
| MAE | MW | lower is better |
| RMSE | MW | lower is better |
| MAPE | % | lower is better |
| sMAPE | % | lower is better |

## Baselines

| Baseline | Description | MAE (example) |
|----------|-------------|---------------|
| `naive_yesterday` | Same hour, previous day | — |
| `naive_week_ago` | Same hour, same weekday last week | — |
| `linear_regression` | Linear regression on calendar features | — |

See `benchmarks/baselines/load-forecasting-dayahead/` for implementations.

## Evaluation harness

```bash
# Run evaluation against the test split
python -m eadx.eval load-forecasting-dayahead \
  --predictions predictions.csv \
  --dataset datasets/synthetic-load/
```

Output format:
```json
{
  "task": "load-forecasting-dayahead",
  "metrics": {"MAE": 0.0, "RMSE": 0.0, "MAPE": 0.0},
  "dataset_version": "0.1.0",
  "split": "test",
  "model": "my-model"
}
```

## Changelog

| Version | Date | Change |
|---------|------|--------|
| 0.1.0 | 2026-03-27 | Initial draft |
