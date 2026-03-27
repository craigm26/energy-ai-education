# Standard mappings

EA-DX is designed to sit **alongside** existing energy standards, not replace them. This page summarises how EA-DX fields map to the major standards used in utility operations.

---

## CIM (IEC 61968 / 61970) { #cim }

The IEC Common Information Model is the dominant standard for utility enterprise systems and grid models.

| EA-DX field | CIM class / attribute | Notes |
|-------------|----------------------|-------|
| `entity_type: meter` | `UsagePoint` | Each UsagePoint has a serviceDeliveryPoint |
| `entity_id` | `UsagePoint.mRID` or `Meter.serialNumber` | Must be anonymised in EA-DX |
| `ts` | `IntervalReading.timeStamp` | CIM uses xsd:dateTime |
| `measurement: active_power` | `ReadingType` with `kind=power` | |
| `measurement: energy` | `ReadingType` with `kind=energy`, `accumulation=deltaData` | |
| `value` | `IntervalReading.value` | Numeric string in CIM XML |
| `unit: kW` | `ReadingType.unit=W`, `ReadingType.multiplier=k` | CIM separates unit and multiplier |
| `quality_flag` | `IntervalReading.ReadingQuality.quality` | CIM has a rich quality code hierarchy |
| `entity_type: feeder` | `Feeder` (part of `VoltageLevel`) | |
| `entity_type: plant` | `GeneratingUnit` | |
| `entity_type: building` | `EnergyConsumer` | |

Full guide: [`standards/mappings/cim.md`](https://github.com/craigm26/energy-ai-education/blob/main/standards/mappings/cim.md)

---

## Green Button / ESPI { #green-button }

Green Button (NAESB ESPI) is the standard for sharing retail customer energy data.

| EA-DX field | ESPI element | Notes |
|-------------|-------------|-------|
| `entity_type: meter` | `UsagePoint` | |
| `entity_id` | `UsagePoint/UUID` | Pseudonymise before use |
| `ts` | `IntervalBlock/IntervalReading/timePeriod/start` | Unix epoch in ESPI; convert to ISO 8601 |
| `measurement: energy` | `IntervalReading/value` with `ReadingType/uom=72` (Wh) | |
| `quality_flag: estimated` | `IntervalReading/ReadingQuality/quality=14` | ESPI quality codes |

!!! note "Timestamp convention"
    Green Button intervals use `start` + `duration`. EA-DX `ts` convention should be documented in the dataset card (typically end-of-interval).

Full guide: [`standards/mappings/green-button.md`](https://github.com/craigm26/energy-ai-education/blob/main/standards/mappings/green-button.md) *(stub — contributions welcome)*

---

## OpenADR 2.0b { #openadr }

OpenADR is the standard for demand response signal exchange between utilities and facilities.

| EA-DX concept | OpenADR element | Notes |
|--------------|----------------|-------|
| `entity_type: market_node` | `oadrEvent/venID` or `marketContext` | |
| `measurement: active_power` (target) | `oadrPayload/oadrSignal/signalPayload` | EA-DX represents DR targets, not raw OpenADR messages |
| `source: market` | `oadrEvent/eventStatus` | |
| Events resource | `oadrEvent` start/end times | Use EA-DX `events.csv` for DR event intervals |

Full guide: [`standards/mappings/openadr.md`](https://github.com/craigm26/energy-ai-education/blob/main/standards/mappings/openadr.md) *(stub)*

---

## ANSI X12 retail EDI { #edi }

ANSI X12 transaction sets 814 (request) and 867 (meter usage) are used in deregulated retail energy markets.

| EA-DX field | X12 867 element | Notes |
|-------------|----------------|-------|
| `entity_id` | `MG01` (meter number) | Pseudonymise |
| `ts` | `MG06` (period start date/time) | Convert to ISO 8601 |
| `measurement: energy` | `QTY02` quantity | |
| `unit: kWh` | `QTY03 = KH` (kilowatt-hour) | |
| `quality_flag` | `PWK` segment qualifier | Maps vary by market |

Full guide: [`standards/mappings/edi-retail.md`](https://github.com/craigm26/energy-ai-education/blob/main/standards/mappings/edi-retail.md) *(stub)*

---

## OpenFMB { #openfmb }

OpenFMB is a field-device messaging standard for DER, substation automation, and microgrid control.

| EA-DX concept | OpenFMB profile | Notes |
|--------------|----------------|-------|
| `measurement: active_power` | `ReadingMessageProfile` → `Reading.value` | |
| `entity_type: inverter` | `SolarInverterEventProfile` or `ESSEventProfile` | |
| `entity_type: battery` | `ESSReadingProfile` | |
| Switch status | `SwitchDiscreteControlProfile` | Maps to EA-DX `events.csv` |

Full guide: [`standards/mappings/openfmb.md`](https://github.com/craigm26/energy-ai-education/blob/main/standards/mappings/openfmb.md) *(stub)*

---

!!! tip "Contributing mappings"
    The stub mapping guides are ideal contributions. See [CONTRIBUTING.md](../contributing.md) for how to submit a mapping guide PR.
