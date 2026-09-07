#!/usr/bin/env python3
"""Import the optional original PNG source bundle. Never download or overwrite."""
from __future__ import annotations
import argparse
import hashlib
import shutil
from pathlib import Path

SOURCES = {
    'restaurant_demo_benchmark_v1.png': 'ce7e32cf95c35dd9a87433440497b600b7240f10ac4ac71d4fdd0378a4454690',
    'character_demo_benchmark_v1.png': '2d90e72964c4faa4975472f18b23005dbbbdd9eff9b1e934048a3d3867318aa6',
}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path, help='Directory containing the two original PNGs')
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    destination = args.root / 'assets/approved/source'
    try:
        # Check the whole batch before writing anything.
        for name, expected in SOURCES.items():
            data = (args.source / name).read_bytes()
            if hashlib.sha256(data).hexdigest() != expected:
                raise ValueError(f'Unexpected source hash: {name}')
            target = destination / name
            if target.exists() and target.read_bytes() != data:
                raise ValueError(f'Refuse to overwrite existing asset: {name}')
        destination.mkdir(parents=True, exist_ok=True)
        for name in SOURCES:
            target = destination / name
            if not target.exists():
                shutil.copyfile(args.source / name, target)
        print('PASS: original PNG benchmarks imported. Still reference sheets, not animation atlases.')
        return 0
    except (OSError, ValueError) as exc:
        print(f'FAIL: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
