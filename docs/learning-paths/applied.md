# Applied

**Level:** Intermediate  
**Prerequisites:** Foundations track or equivalent; scikit-learn, regression models  
**Notebooks:** `notebooks/applied/`

---

## Curriculum overview

### Load forecasting

Predicting electricity demand is one of the most established ML applications in energy. Methods range from statistical (ARIMA, exponential smoothing) to modern deep learning (N-BEATS, TFT, PatchTST).

Key challenges:
- Handling holidays and atypical events
- Aggregation level (system, feeder, meter)
- Probabilistic forecasts vs point estimates

See the [day-ahead benchmark](../benchmarks/load-forecasting-dayahead.md) for a reproducible baseline.

### DER output forecasting

Solar PV and wind turbine output depend on weather. Building accurate forecasts requires:

- Numerical weather prediction (NWP) data as input features
- Plant-specific power curves
- Clipping and curtailment detection
- Handling ramp events

### Anomaly detection

Meter data anomalies include outright failures, stuck sensors, drift, and unusual consumption patterns. Techniques: isolation forest, LSTM autoencoders, statistical control charts.

### Demand response event detection

Identifying when a demand response event is active — and whether loads responded — from interval meter data.

---

## Notebooks (planned)

| Notebook | Domain | Status |
|----------|--------|--------|
| `01_load_forecasting_baseline.ipynb` | Distribution / Markets | 📋 Planned |
| `02_solar_forecasting.ipynb` | Generation / DER | 📋 Planned |
| `03_meter_anomaly_detection.ipynb` | Customer / Distribution | 📋 Planned |
| `04_demand_response_detection.ipynb` | Customer | 📋 Planned |
| `05_probabilistic_forecasting.ipynb` | Cross-domain | 📋 Planned |

---

!!! tip "Benchmark-linked"
    The load forecasting notebook links directly to the [day-ahead benchmark](../benchmarks/load-forecasting-dayahead.md) — run your model against the standard split and compare to the baselines.
