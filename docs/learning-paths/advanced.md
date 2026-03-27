# Advanced

**Level:** Research / Expert  
**Prerequisites:** Strong ML background; familiarity with energy market structures  
**Notebooks:** `notebooks/advanced/`

---

## Curriculum overview

### Grid optimization and RL

The grid is a sequential decision problem. Reinforcement learning agents can learn dispatch schedules, topology switching actions, and storage arbitrage strategies.

- [Grid2Op](https://github.com/rte-france/Grid2Op) — leading RL framework for power grid environments
- [Pandapower](https://pandapower.readthedocs.io/) — power flow simulation
- Safe exploration: hard constraints (thermal limits, voltage limits) must always be satisfied

### Federated learning for energy

Utilities can't always share raw customer or operational data. Federated learning trains models across distributed data owners without centralizing data.

Key references:
- FedAvg in heterogeneous energy contexts
- Privacy-preserving load disaggregation
- Cross-utility load forecasting

### Benchmarking and reproducibility

Research reproducibility in energy ML is poor. Best practices:

- Fixed random seeds and temporal splits
- Versioned datasets with EA-DX packages
- Standardized metrics reported on held-out test sets
- Model cards and result tables with uncertainty estimates

### Model governance

- **Model cards** (Mitchell et al., 2019) — intended use, performance across subgroups, ethical considerations
- **Datasheets for datasets** (Gebru et al., 2021) — motivation, composition, collection, preprocessing
- **NIST AI RMF** — four functions: Govern, Map, Measure, Manage
- **EU AI Act** — energy grid management systems may be classified as high-risk (Annex III)

---

## Notebooks (planned)

| Notebook | Domain | Status |
|----------|--------|--------|
| `01_grid2op_intro.ipynb` | Transmission / Distribution | 📋 Planned |
| `02_storage_arbitrage_rl.ipynb` | Markets / DER | 📋 Planned |
| `03_federated_load_forecasting.ipynb` | Customer | 📋 Planned |
| `04_model_card_template.ipynb` | Governance | 📋 Planned |
| `05_benchmarking_best_practices.ipynb` | Cross-domain | 📋 Planned |
