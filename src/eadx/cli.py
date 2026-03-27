"""EA-DX CLI — validate and inspect EA-DX packages."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .package import EADXPackage
from .validator import validate_package


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="eadx",
        description="EA-DX Package CLI — validate and inspect Energy AI Data Exchange packages.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # validate
    val_parser = subparsers.add_parser("validate", help="Validate an EA-DX package directory")
    val_parser.add_argument("path", help="Path to the EA-DX package directory")
    val_parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")

    # info
    info_parser = subparsers.add_parser("info", help="Show package metadata")
    info_parser.add_argument("path", help="Path to the EA-DX package directory")

    args = parser.parse_args()

    if args.command == "validate":
        result = validate_package(args.path)
        print(result)
        if not result.valid:
            sys.exit(1)
        if args.strict and result.warnings:
            print(f"\n{len(result.warnings)} warning(s) in strict mode — treating as errors")
            sys.exit(1)

    elif args.command == "info":
        try:
            pkg = EADXPackage.load(args.path)
        except FileNotFoundError as e:
            print(f"Error: {e}", file=sys.stderr)
            sys.exit(1)
        print(f"Name:          {pkg.descriptor.get('name', '(unnamed)')}")
        print(f"Title:         {pkg.descriptor.get('title', '')}")
        print(f"EA-DX version: {pkg.spec_version}")
        print(f"Domain:        {pkg.eadx_profile.get('domain', '?')}")
        print(f"Tasks:         {', '.join(pkg.eadx_profile.get('tasks', []))}")
        print(f"Sensitivity:   {pkg.eadx_profile.get('sensitivity', '?')}")
        print(f"Resources:     {[r.get('name') for r in pkg.resources]}")


if __name__ == "__main__":
    main()
