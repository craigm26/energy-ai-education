"""EA-DX Package — Energy AI Data Exchange Package library.

Provides:
- Package loading and validation
- Schema discovery
- datapackage.json descriptor generation
"""

from __future__ import annotations

__version__ = "0.1.0"
__spec_version__ = "0.1.0"

from .package import EADXPackage
from .validator import validate_package

__all__ = ["EADXPackage", "validate_package", "__version__", "__spec_version__"]
