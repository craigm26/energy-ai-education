"""Tests for eadx.validator module."""

from __future__ import annotations

import json
from pathlib import Path

from eadx.validator import validate_package


def _write_descriptor(root: Path, descriptor: dict) -> None:
    (root / "datapackage.json").write_text(json.dumps(descriptor))


def _minimal_descriptor(**overrides) -> dict:
    d = {
        "name": "test-pkg",
        "licenses": [{"name": "CC0-1.0"}],
        "eadx_profile": {
            "spec_version": "0.1.0",
            "domain": "distribution",
            "tasks": ["forecasting"],
            "sensitivity": "public",
        },
        "resources": [],
    }
    d.update(overrides)
    return d


class TestValidatePackageMissing:
    def test_missing_descriptor(self, tmp_path):
        result = validate_package(tmp_path)
        assert not result.valid
        assert any("datapackage.json" in e for e in result.errors)

    def test_invalid_json(self, tmp_path):
        (tmp_path / "datapackage.json").write_text("NOT JSON {{{")
        result = validate_package(tmp_path)
        assert not result.valid
        assert any("not valid JSON" in e for e in result.errors)


class TestValidatePackageRequired:
    def test_valid_minimal(self, tmp_path):
        _write_descriptor(tmp_path, _minimal_descriptor())
        result = validate_package(tmp_path)
        assert result.valid
        assert result.errors == []

    def test_missing_name(self, tmp_path):
        d = _minimal_descriptor()
        del d["name"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid
        assert any("name" in e for e in result.errors)

    def test_missing_licenses(self, tmp_path):
        d = _minimal_descriptor()
        del d["licenses"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid

    def test_empty_licenses_list(self, tmp_path):
        d = _minimal_descriptor(licenses=[])
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid

    def test_missing_resources(self, tmp_path):
        d = _minimal_descriptor()
        del d["resources"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid

    def test_missing_eadx_profile(self, tmp_path):
        d = _minimal_descriptor()
        del d["eadx_profile"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid


class TestValidatePackageProfile:
    def test_missing_spec_version(self, tmp_path):
        d = _minimal_descriptor()
        del d["eadx_profile"]["spec_version"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid
        assert any("spec_version" in e for e in result.errors)

    def test_missing_domain(self, tmp_path):
        d = _minimal_descriptor()
        del d["eadx_profile"]["domain"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert not result.valid

    def test_unknown_domain_is_warning(self, tmp_path):
        d = _minimal_descriptor()
        d["eadx_profile"]["domain"] = "nuclear-fusion"
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid  # warnings don't block validity
        assert any("domain" in w for w in result.warnings)

    def test_unknown_task_is_warning(self, tmp_path):
        d = _minimal_descriptor()
        d["eadx_profile"]["tasks"] = ["time-travel"]
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid
        assert any("time-travel" in w for w in result.warnings)

    def test_restricted_sensitivity_warns(self, tmp_path):
        d = _minimal_descriptor()
        d["eadx_profile"]["sensitivity"] = "restricted"
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid
        assert any("restricted" in w or "ceii" in w for w in result.warnings)

    def test_ceii_sensitivity_warns(self, tmp_path):
        d = _minimal_descriptor()
        d["eadx_profile"]["sensitivity"] = "ceii"
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid
        assert any("ceii" in w.lower() for w in result.warnings)


class TestValidatePackageResources:
    def test_missing_resource_file_is_warning(self, tmp_path):
        d = _minimal_descriptor(resources=[{"name": "observations", "path": "observations.csv"}])
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid  # file missing = warning, not error
        assert any("observations.csv" in w for w in result.warnings)

    def test_present_resource_file_no_warning(self, tmp_path):
        (tmp_path / "observations.csv").write_text("ts,value\n")
        d = _minimal_descriptor(resources=[{"name": "observations", "path": "observations.csv"}])
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid
        assert not any("observations.csv" in w for w in result.warnings)

    def test_empty_resources_warns(self, tmp_path):
        d = _minimal_descriptor(resources=[])
        _write_descriptor(tmp_path, d)
        result = validate_package(tmp_path)
        assert result.valid
        assert any("No resources" in w for w in result.warnings)


class TestValidationResult:
    def test_str_valid(self, tmp_path):
        _write_descriptor(tmp_path, _minimal_descriptor())
        result = validate_package(tmp_path)
        assert "✅ VALID" in str(result)

    def test_str_invalid(self, tmp_path):
        result = validate_package(tmp_path)  # no descriptor
        assert "❌ INVALID" in str(result)
        assert "error:" in str(result)
