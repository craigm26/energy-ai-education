# EA-DX Package Specification

**Energy AI Data Exchange Package (EA-DX)** — v0.1.0

EA-DX is a lightweight, ML-friendly interchange format for energy data. It is designed as a **profile/mapping layer** on top of existing energy standards — not a replacement — to reduce friction for ML workflows while staying semantically compatible.

## Design goals

1. **Simple:** tidy, column-oriented data that pandas/polars/DuckDB can read directly
2. **Unambiguous:** timestamps with offsets, IANA timezones, UCUM/OM units
3. **Interoperable:** explicit mappings to CIM, Green Button, OpenADR, retail EDI
4. **Safe:** entity IDs are always opaque; no customer PII; sensitivity metadata required
5. **Portable:** JSON Schema + Table Schema for validation; `datapackage.json` as envelope

## Package structure

```
my-dataset/
├── datapackage.json         ← EA-DX package descriptor (required)
├── observations.csv         ← time-series measurements (optional)
├── events.csv               ← discrete events (outages, DR, alarms) (optional)
├── assets.csv               ← equipment/site metadata (optional, redacted)
├── topology.json            ← simplified network structure (optional)
├── labels.csv               ← supervised learning labels (optional)
└── schemas/
    ├── observations.json    ← Table Schema for observations.csv
    └── events.json          ← Table Schema for events.csv
```

## Package descriptor (`datapackage.json`)

```json
{
  "name": "example-load-dataset",
  "title": "Example Load Dataset — EA-DX v0.1",
  "description": "Synthetic residential load measurements for load forecasting tutorials.",
  "licenses": [
    {"name": "CC0-1.0", "path": "LICENSE", "title": "Creative Commons Zero"}
  ],
  "sources": [
    {"title": "Synthetic generator", "path": "notebooks/generate_synthetic.ipynb"}
  ],
  "eadx_profile": {
    "spec_version": "0.1.0",
    "domain": "distribution",
    "tasks": ["forecasting"],
    "sensitivity": "public",
    "anonymization": "synthetic",
    "temporal_coverage": {"start": "2024-01-01", "end": "2024-12-31"},
    "resolution": "PT15M",
    "cim_mapping": "standards/mappings/cim.md#usage-meter",
    "green_button_mapping": "standards/mappings/green-button.md"
  },
  "resources": [
    {
      "name": "observations",
      "path": "observations.csv",
      "schema": {"$ref": "schemas/observations.json"}
    }
  ]
}
```

## Canonical schemas

See [`schemas/`](schemas/) for JSON Schema and Table Schema definitions.

### `observations` columns

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `ts` | string (ISO 8601) | ✅ | Timestamp with UTC offset (e.g. `2024-06-15T14:00:00-07:00`) |
| `tz` | string (IANA) | — | IANA timezone name (e.g. `America/Los_Angeles`) |
| `entity_type` | string | ✅ | `meter` \| `inverter` \| `feeder` \| `plant` \| `market_node` \| `building` |
| `entity_id` | string | ✅ | Stable opaque identifier (never a real customer ID) |
| `measurement` | string | ✅ | `active_power` \| `reactive_power` \| `voltage` \| `price` \| `frequency` \| `energy` |
| `value` | number | ✅ | Numeric measurement value |
| `unit` | string | ✅ | `kW` \| `MW` \| `kWh` \| `MWh` \| `V` \| `kV` \| `Hz` \| `USD/MWh` |
| `quality_flag` | string | ✅ | `measured` \| `estimated` \| `imputed` \| `simulated` \| `redacted` |
| `source` | string | ✅ | `sensor` \| `sim` \| `market` \| `derived` |

### `events` columns

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `ts_start` | string (ISO 8601) | ✅ | Event start timestamp |
| `ts_end` | string (ISO 8601) | — | Event end timestamp (null = ongoing) |
| `entity_type` | string | ✅ | Affected entity type |
| `entity_id` | string | ✅ | Opaque entity identifier |
| `event_type` | string | ✅ | `outage` \| `dr_event` \| `switching` \| `alarm` \| `fault` \| `curtailment` |
| `severity` | string | — | `info` \| `warning` \| `critical` |
| `source` | string | ✅ | `sensor` \| `operator` \| `market` \| `sim` |
| `notes` | string | — | Free-text (no PII) |

## Standard mappings

| Standard | Mapping guide | Key concepts |
|----------|---------------|--------------|
| IEC CIM 61968/61970 | [cim.md](../mappings/cim.md) | UsagePoint, Meter, EnergyConsumer |
| IEC 62325 (market comms) | [cim-markets.md](../mappings/cim-markets.md) | MarketDocument, TimeSeries |
| Green Button / ESPI | [green-button.md](../mappings/green-button.md) | UsagePoint, IntervalBlock |
| ANSI X12 (814/867) | [edi-retail.md](../mappings/edi-retail.md) | 867 meter usage, 814 request |
| OpenADR 2.0b | [openadr.md](../mappings/openadr.md) | oadrEvent, oadrPayload |
| OpenFMB | [openfmb.md](../mappings/openfmb.md) | ReadingMessage, SwitchDiscreteControlProfile |

## Versioning

EA-DX follows [Semantic Versioning](https://semver.org/). The `spec_version` field in `datapackage.json` declares compatibility. Breaking changes increment the major version.

## Validation

```bash
# Install
pip install -e "../../[dev]"

# Validate a package
python -m eadx validate /path/to/my-dataset/

# Generate a package descriptor from a CSV
python -m eadx init /path/to/my-dataset/ --domain distribution --task forecasting
```
