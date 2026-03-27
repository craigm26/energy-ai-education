"""EA-DX Package loader."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class EADXPackage:
    """Represents a loaded EA-DX data package.

    Usage::

        pkg = EADXPackage.load("/path/to/my-dataset/")
        obs = pkg.observations()   # returns pandas DataFrame
        print(pkg.metadata)
    """

    def __init__(self, root: Path, descriptor: dict[str, Any]) -> None:
        self.root = root
        self.descriptor = descriptor

    @classmethod
    def load(cls, path: str | Path) -> "EADXPackage":
        """Load an EA-DX package from a directory.

        Args:
            path: Path to the package directory (must contain datapackage.json).

        Returns:
            Loaded EADXPackage.

        Raises:
            FileNotFoundError: If datapackage.json is not found.
            ValueError: If the descriptor is not valid JSON.
        """
        root = Path(path)
        descriptor_path = root / "datapackage.json"
        if not descriptor_path.exists():
            raise FileNotFoundError(f"datapackage.json not found in {root}")
        with open(descriptor_path) as f:
            descriptor = json.load(f)
        return cls(root, descriptor)

    @property
    def metadata(self) -> dict[str, Any]:
        """Return package-level metadata (excludes resources)."""
        return {k: v for k, v in self.descriptor.items() if k != "resources"}

    @property
    def eadx_profile(self) -> dict[str, Any]:
        """Return the eadx_profile block from the descriptor."""
        return self.descriptor.get("eadx_profile", {})

    @property
    def spec_version(self) -> str:
        """Return the declared EA-DX spec version."""
        return self.eadx_profile.get("spec_version", "unknown")

    @property
    def resources(self) -> list[dict[str, Any]]:
        """Return the list of resource descriptors."""
        return self.descriptor.get("resources", [])

    def observations(self) -> Any:
        """Load the canonical observations resource as a pandas DataFrame.

        Returns:
            pandas.DataFrame with observations data, or None if not present.
        """
        import pandas as pd  # optional at runtime

        for resource in self.resources:
            if resource.get("name") == "observations":
                csv_path = self.root / resource["path"]
                if csv_path.exists():
                    return pd.read_csv(csv_path, parse_dates=["ts"])
        return None

    def __repr__(self) -> str:
        name = self.descriptor.get("name", "unnamed")
        return f"EADXPackage(name={name!r}, spec_version={self.spec_version!r}, root={self.root})"
