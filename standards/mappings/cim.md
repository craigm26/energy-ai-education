# EA-DX → IEC CIM Mapping Guide

**Standard:** IEC 61968 / IEC 61970 (Common Information Model)  
**EA-DX spec version:** 0.1.0

This guide shows how EA-DX `observations` and `assets` resource fields map to CIM concepts used in utility enterprise systems and network models.

## Key CIM classes

| CIM Class | Package | Relevance |
|-----------|---------|-----------|
| `UsagePoint` | 61968-9 | Maps to EA-DX `entity_type: meter` |
| `MeterReading` | 61968-9 | Container for interval readings |
| `IntervalReading` | 61968-9 | Single time-stamped value — maps to EA-DX observation row |
| `ReadingType` | 61968-9 | Describes measurement type, unit, multiplier |
| `EnergyConsumer` | 61970-302 | Load element — maps to `entity_type: building` or `feeder` |
| `GeneratingUnit` | 61970-302 | Generator — maps to `entity_type: plant` |
| `PowerTransformer` | 61970-302 | Transformer — maps to `entity_type: feeder` (simplified) |
| `Terminal` | 61970-302 | Connection point on a conducting equipment |

## Field mappings

### `observations` → CIM

| EA-DX field | CIM mapping | Notes |
|-------------|-------------|-------|
| `ts` | `IntervalReading.timeStamp` or `MeterReading.valuesInterval.start` | ISO 8601; CIM uses xsd:dateTime |
| `entity_type: meter` | `UsagePoint` | Each UsagePoint has a serviceDeliveryPoint |
| `entity_id` | `UsagePoint.mRID` or `Meter.serialNumber` (anonymized) | Must be opaque in EA-DX |
| `measurement: active_power` | `ReadingType` with `kind=power`, `phase=AN` | |
| `measurement: energy` | `ReadingType` with `kind=energy`, `accumulation=deltaData` | |
| `value` | `IntervalReading.value` | Numeric string in CIM XML |
| `unit: kW` | `ReadingType.unit=W`, `ReadingType.multiplier=k` | CIM separates unit and multiplier |
| `quality_flag` | `IntervalReading.ReadingQuality.quality` | CIM has rich quality code hierarchy |

### `assets` → CIM

| EA-DX field | CIM mapping |
|-------------|-------------|
| `entity_type: feeder` | `Feeder` (part of `VoltageLevel`) |
| `entity_type: plant` | `GeneratingUnit` → `PowerSystemResource` |
| `entity_type: building` | `EnergyConsumer` |
| `voltage_level` | `BaseVoltage.nominalVoltage` |
| `capacity_kw` | `GeneratingUnit.maxOperatingP` (in MW) |

## Simplification rationale

EA-DX deliberately uses simpler field names than CIM to reduce onboarding friction for ML practitioners. The above mappings allow round-tripping between EA-DX and CIM-based systems without semantic loss.

## Further reading

- IEC 61968-9: Metering domain package
- IEC 61970-302: Dynamics package (generating units)
- [CIM Users Group](https://cimug.ucaiug.org/)
