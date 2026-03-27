# Foundations

**Level:** Beginner  
**Prerequisites:** Python basics, pandas/numpy familiarity  
**Notebooks:** `notebooks/foundations/`

---

## Curriculum

### 1. Energy systems primer

Before building models, understand what you're modelling.

- **Generation:** Power plants convert fuel or flow into electricity. Renewable sources (wind, solar) are variable — their output depends on weather.
- **Transmission:** High-voltage lines move bulk power across regions. Bottlenecks cause congestion and price differences between zones.
- **Distribution:** Lower-voltage networks deliver power to homes and businesses. Most meters live here.
- **Markets:** Wholesale electricity is bought and sold in day-ahead and real-time markets. Prices vary by hour and location.

### 2. Energy time-series fundamentals

Energy data is almost always sequential. Key concepts:

- **Interval data:** Most meters record in fixed intervals (15 min, 30 min, 1 hr). The timestamp marks the *end* of the interval in many standards — always check.
- **Seasonality:** Load follows daily, weekly, and annual patterns. Temperature is a strong driver.
- **Quality flags:** Measured, estimated, imputed — these matter for model training and evaluation.
- **Units:** Watch for kW vs kWh (power vs energy), MW vs MW·h. Mixing them is the most common data bug in energy ML.

### 3. EA-DX Package format

All datasets in this hub use the [EA-DX Package format](../eadx/index.md). The core resource is `observations.csv`:

```csv
ts,tz,entity_type,entity_id,measurement,value,unit,quality_flag,source
2024-01-01T00:00:00-08:00,America/Los_Angeles,meter,MTR-0001,active_power,3.2,kW,measured,sensor
2024-01-01T00:15:00-08:00,America/Los_Angeles,meter,MTR-0001,active_power,2.9,kW,measured,sensor
```

### 4. Exploratory data analysis

Planned notebook: `notebooks/foundations/01_hello_energy_ml.ipynb`

Topics:

- Loading an EA-DX package with `eadx.EADXPackage.load()`
- Plotting load profiles with matplotlib/plotly
- Identifying seasonality and outliers
- Handling missing data and quality-flagged readings

---

## Notebooks (planned)

| Notebook | Description | Status |
|----------|-------------|--------|
| `01_hello_energy_ml.ipynb` | Load + explore an EA-DX dataset | 📋 Planned |
| `02_time_series_basics.ipynb` | Resampling, interpolation, seasonality decomposition | 📋 Planned |
| `03_data_quality.ipynb` | Quality flags, imputation strategies, visualising gaps | 📋 Planned |
| `04_feature_engineering.ipynb` | Calendar features, lag features, rolling statistics | 📋 Planned |

---

!!! note "Want to contribute?"
    Adding a foundations notebook is a great first contribution. See [CONTRIBUTING.md](../contributing.md) for the notebook header format requirements.
