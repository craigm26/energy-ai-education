# Learning Paths

Three tracks organized by prerequisite level. Each track has a corresponding notebooks directory.

## Choose your path

=== "🟢 Foundations"
    **Best for:** Students, newcomers to energy ML, data scientists exploring a new domain.

    **Prerequisites:** Basic Python, familiarity with pandas/numpy.

    **You'll learn:**

    - How electricity grids work: generation, transmission, distribution, markets
    - Energy time-series data: intervals, quality flags, seasonality
    - Exploratory data analysis with EA-DX packages
    - Data quality: imputation, resampling, outlier handling

    [Start foundations →](foundations.md)

=== "🟡 Applied"
    **Best for:** Practising data scientists, ML engineers entering the energy sector.

    **Prerequisites:** Foundations track or equivalent; comfortable with scikit-learn and regression.

    **You'll learn:**

    - Short-term and day-ahead load forecasting
    - Solar/wind output forecasting for DER integration
    - Anomaly detection in meter and SCADA data
    - Demand response event detection
    - Model evaluation with energy-specific metrics (MAPE, sMAPE, CRPS)

    [Start applied →](applied.md)

=== "🔴 Advanced"
    **Best for:** ML researchers, energy systems engineers, PhD students.

    **Prerequisites:** Applied track or strong ML background; familiarity with energy market structures.

    **You'll learn:**

    - Grid topology optimization and RL agents (Grid2Op compatible)
    - Federated learning for privacy-preserving energy analytics
    - Benchmarking methodology and reproducibility practices
    - Model governance: model cards, datasheets, NIST AI RMF alignment
    - EU AI Act considerations for energy AI systems

    [Start advanced →](advanced.md)

---

## Domain map

| Domain | Description | Relevant tracks |
|--------|-------------|-----------------|
| **Generation** | Power plants, renewables, dispatch | Applied, Advanced |
| **Transmission** | High-voltage grid, congestion, scheduling | Advanced |
| **Distribution** | Feeders, meters, DER integration | Foundations, Applied |
| **Markets** | Wholesale prices, ancillary services | Applied, Advanced |
| **Customer** | Retail energy, demand-side management | Foundations, Applied |
| **DER** | Solar, wind, batteries, EVs | Applied, Advanced |
