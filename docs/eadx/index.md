# EA-DX Package

**Energy AI Data Exchange Package (EA-DX)** — v0.1.0

EA-DX is a lightweight, ML-friendly interchange format for energy data. It is a **profile and mapping layer** on top of existing industry standards — not a replacement — designed to reduce the data engineering friction between energy domain systems and ML workflows.

---

## Why EA-DX?

Energy data lives in many formats: CIM/XML for grid models, Green Button ESPI XML for customer data, ANSI X12 EDI for retail transactions, OpenADR for demand response signals. None of these are ML-friendly out of the box.

EA-DX provides a **tidy, column-oriented canonical form** that:

- Reads directly into pandas, polars, or DuckDB
- Has unambiguous timestamps (ISO 8601 with UTC offset + IANA timezone)
- Uses stable opaque entity IDs (never customer PII)
- Carries quality flags and provenance metadata
- Maps explicitly back to source standards

---

## Package structure

An EA-DX package is a directory with a `datapackage.json` descriptor and one or more CSV resource files:

```
my-dataset/
├── datapackage.json         ← descriptor (required)
├── observations.csv         ← time-series measurements
├── events.csv               ← discrete events (outages, DR, alarms)
├── assets.csv               ← equipment/site metadata (redacted)
└── schemas/
    ├── observations.json    ← Table Schema
    └── events.json
```

---

## The observations resource

The canonical time-series table. One row per (timestamp, entity, measurement) tuple.

| Column | Type | Required | Description |
|--------|------|----------|-------------|
| `ts` | ISO 8601 string | ✅ | Timestamp **with UTC offset** (e.g. `2024-06-15T14:00:00-07:00`) |
| `tz` | IANA string | — | Timezone name (e.g. `America/Los_Angeles`) |
| `entity_type` | enum | ✅ | `meter` · `inverter` · `feeder` · `plant` · `market_node` · `building` · `ev_charger` · `battery` |
| `entity_id` | string | ✅ | Stable opaque ID — **must not be a real customer ID** |
| `measurement` | enum | ✅ | `active_power` · `reactive_power` · `voltage` · `energy` · `price` · `frequency` · `soc` · … |
| `value` | float | ✅ | Numeric measurement value |
| `unit` | enum | ✅ | `kW` · `MW` · `kWh` · `MWh` · `V` · `kV` · `Hz` · `USD/MWh` · … |
| `quality_flag` | enum | ✅ | `measured` · `estimated` · `imputed` · `simulated` · `redacted` |
| `source` | enum | ✅ | `sensor` · `sim` · `market` · `derived` · `manual` |

**Example rows:**

```csv
ts,tz,entity_type,entity_id,measurement,value,unit,quality_flag,source
2024-06-15T14:00:00-07:00,America/Los_Angeles,meter,MTR-0042,active_power,12.4,kW,measured,sensor
2024-06-15T14:15:00-07:00,America/Los_Angeles,meter,MTR-0042,active_power,11.8,kW,measured,sensor
2024-06-15T14:00:00-07:00,America/Los_Angeles,feeder,FDR-001,active_power,4823.0,kW,measured,sensor
2024-06-15T14:00:00+00:00,,market_node,HUB-CAISO-NP15,price,45.72,USD/MWh,measured,market
```

---

## Package descriptor

```json
{
  "name": "example-load-dataset",
  "title": "Example Load Dataset — EA-DX v0.1",
  "licenses": [{"name": "CC0-1.0"}],
  "eadx_profile": {
    "spec_version": "0.1.0",
    "domain": "distribution",
    "tasks": ["forecasting"],
    "sensitivity": "public",
    "anonymization": "synthetic",
    "temporal_coverage": {"start": "2024-01-01", "end": "2024-12-31"},
    "resolution": "PT15M"
  },
  "resources": [
    {"name": "observations", "path": "observations.csv", "schema": {"$ref": "schemas/observations.json"}}
  ]
}
```

---

## Python library

```bash
pip install -e ".[dev]"
```

```python
from eadx import EADXPackage, validate_package

# Load and inspect
pkg = EADXPackage.load("datasets/my-dataset/")
print(pkg.metadata)
df = pkg.observations()   # returns pandas DataFrame

# Validate
result = validate_package("datasets/my-dataset/")
print(result)   # ✅ VALID or ❌ INVALID with errors
```

**CLI:**

```bash
eadx validate datasets/my-dataset/     # validate descriptor + schema
eadx info    datasets/my-dataset/      # show metadata summary
```

---

## Standard mappings

[Full mapping guides →](mappings.md)

| Standard | Key concepts | Mapping guide |
|----------|-------------|---------------|
| IEC CIM 61968/61970 | UsagePoint, IntervalReading, ReadingType | [cim.md](mappings.md#cim) |
| Green Button / ESPI | IntervalBlock, IntervalReading | [green-button.md](mappings.md#green-button) |
| OpenADR 2.0b | oadrEvent, oadrPayload | [openadr.md](mappings.md#openadr) |
| ANSI X12 (814/867) | 867 meter usage transaction | [edi-retail.md](mappings.md#edi) |
| OpenFMB | ReadingMessage, SwitchProfile | [openfmb.md](mappings.md#openfmb) |
