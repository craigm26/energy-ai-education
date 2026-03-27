"""EA-DX Package validator."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class ValidationResult:
    """Result of validating an EA-DX package."""

    valid: bool
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        status = "✅ VALID" if self.valid else "❌ INVALID"
        lines = [status]
        for e in self.errors:
            lines.append(f"  error: {e}")
        for w in self.warnings:
            lines.append(f"  warn:  {w}")
        return "\n".join(lines)


REQUIRED_TOP_LEVEL = ["name", "licenses", "resources", "eadx_profile"]
REQUIRED_EADX_PROFILE = ["spec_version", "domain", "tasks", "sensitivity"]
VALID_DOMAINS = {"generation", "transmission", "distribution", "markets", "customer", "der", "other"}
VALID_TASKS = {"forecasting", "anomaly-detection", "optimization", "rl", "eda", "classification", "other"}
VALID_SENSITIVITY = {"public", "internal", "restricted", "ceii"}


def validate_package(path: str | Path) -> ValidationResult:
    """Validate an EA-DX package directory.

    Args:
        path: Path to the package directory.

    Returns:
        ValidationResult with errors and warnings.
    """
    root = Path(path)
    errors: list[str] = []
    warnings: list[str] = []

    # 1. Check descriptor exists
    descriptor_path = root / "datapackage.json"
    if not descriptor_path.exists():
        return ValidationResult(valid=False, errors=["datapackage.json not found"])

    # 2. Parse JSON
    try:
        with open(descriptor_path) as f:
            descriptor: dict[str, Any] = json.load(f)
    except json.JSONDecodeError as e:
        return ValidationResult(valid=False, errors=[f"datapackage.json is not valid JSON: {e}"])

    # 3. Required top-level keys
    for key in REQUIRED_TOP_LEVEL:
        if key not in descriptor:
            errors.append(f"Missing required top-level key: '{key}'")

    # 4. Licenses: must be a non-empty list with SPDX identifiers
    licenses = descriptor.get("licenses", [])
    if not isinstance(licenses, list) or len(licenses) == 0:
        errors.append("'licenses' must be a non-empty list")
    else:
        for lic in licenses:
            if not lic.get("name"):
                warnings.append("A license entry is missing 'name' (SPDX identifier recommended)")

    # 5. eadx_profile block
    profile = descriptor.get("eadx_profile", {})
    if isinstance(profile, dict):
        for key in REQUIRED_EADX_PROFILE:
            if key not in profile:
                errors.append(f"Missing required eadx_profile key: '{key}'")

        domain = profile.get("domain", "")
        if domain and domain not in VALID_DOMAINS:
            warnings.append(f"eadx_profile.domain '{domain}' is not in the known set {sorted(VALID_DOMAINS)}")

        tasks = profile.get("tasks", [])
        if isinstance(tasks, list):
            for task in tasks:
                if task not in VALID_TASKS:
                    warnings.append(f"eadx_profile.tasks entry '{task}' is not in the known set")

        sensitivity = profile.get("sensitivity", "")
        if sensitivity and sensitivity not in VALID_SENSITIVITY:
            warnings.append(f"eadx_profile.sensitivity '{sensitivity}' is not in the known set {sorted(VALID_SENSITIVITY)}")

        if sensitivity in ("restricted", "ceii"):
            warnings.append(
                "Package marked as 'restricted' or 'ceii' — verify this is appropriate for public distribution"
            )

    # 6. Resources: check files exist
    resources = descriptor.get("resources", [])
    if not isinstance(resources, list) or len(resources) == 0:
        warnings.append("No resources declared in 'resources'")
    else:
        for resource in resources:
            rpath = resource.get("path", "")
            if rpath and not (root / rpath).exists():
                warnings.append(f"Resource file not found: '{rpath}'")

    valid = len(errors) == 0
    return ValidationResult(valid=valid, errors=errors, warnings=warnings)
