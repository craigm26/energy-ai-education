"""Tests for eadx.package module."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from eadx.package import EADXPackage


def _make_package(root: Path, extra_profile: dict | None = None) -> Path:
    """Write a minimal valid EA-DX package to *root*."""
    profile = {
        "spec_version": "0.1.0",
        "domain": "distribution",
        "tasks": ["forecasting"],
        "sensitivity": "public",
    }
    if extra_profile:
        profile.update(extra_profile)
    descriptor = {
        "name": "test-dataset",
        "title": "Test Dataset",
        "licenses": [{"name": "CC0-1.0"}],
        "eadx_profile": profile,
        "resources": [{"name": "observations", "path": "observations.csv"}],
    }
    (root / "datapackage.json").write_text(json.dumps(descriptor))
    # Write a minimal observations CSV
    (root / "observations.csv").write_text(
        "ts,tz,entity_type,entity_id,measurement,value,unit,quality_flag,source\n"
        "2024-01-01T00:00:00+00:00,UTC,meter,MTR-001,active_power,1.0,kW,measured,sensor\n"
    )
    return root


class TestEADXPackageLoad:
    def test_load_valid_package(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        assert pkg.descriptor["name"] == "test-dataset"

    def test_load_from_string_path(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(str(tmp_path))
        assert isinstance(pkg.root, Path)

    def test_load_missing_descriptor_raises(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="datapackage.json"):
            EADXPackage.load(tmp_path)

    def test_metadata_excludes_resources(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        assert "resources" not in pkg.metadata
        assert "name" in pkg.metadata

    def test_eadx_profile(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        assert pkg.eadx_profile["spec_version"] == "0.1.0"
        assert pkg.eadx_profile["domain"] == "distribution"

    def test_spec_version(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        assert pkg.spec_version == "0.1.0"

    def test_spec_version_unknown_when_missing(self, tmp_path):
        descriptor = {
            "name": "no-profile",
            "licenses": [{"name": "CC0-1.0"}],
            "resources": [],
        }
        (tmp_path / "datapackage.json").write_text(json.dumps(descriptor))
        pkg = EADXPackage.load(tmp_path)
        assert pkg.spec_version == "unknown"

    def test_resources_list(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        assert len(pkg.resources) == 1
        assert pkg.resources[0]["name"] == "observations"

    def test_repr(self, tmp_path):
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        r = repr(pkg)
        assert "test-dataset" in r
        assert "0.1.0" in r

    def test_observations_returns_dataframe(self, tmp_path):
        pytest.importorskip("pandas")
        _make_package(tmp_path)
        pkg = EADXPackage.load(tmp_path)
        df = pkg.observations()
        assert df is not None
        assert len(df) == 1
        assert "ts" in df.columns

    def test_observations_returns_none_when_no_resource(self, tmp_path):
        descriptor = {
            "name": "empty",
            "licenses": [{"name": "CC0-1.0"}],
            "eadx_profile": {
                "spec_version": "0.1.0",
                "domain": "distribution",
                "tasks": ["eda"],
                "sensitivity": "public",
            },
            "resources": [],
        }
        (tmp_path / "datapackage.json").write_text(json.dumps(descriptor))
        pkg = EADXPackage.load(tmp_path)
        result = pkg.observations()
        assert result is None
