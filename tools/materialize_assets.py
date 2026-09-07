#!/usr/bin/env python3
"""Decode the included thumbnail reference; no network, Pillow or credentials required."""
from __future__ import annotations
import base64
import hashlib
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = '81b44adda8892d8947bb2581df0e27c25bda9d6bf3d797e6e4df805a22e70516'


def main() -> int:
    try:
        source = ROOT / 'assets/encoded/character_reference_preview'
        encoded = ''.join((source / f'part{i}.txt').read_text(encoding='ascii').strip() for i in range(4))
        data = base64.b64decode(encoded, validate=True)
        if hashlib.sha256(data).hexdigest() != EXPECTED:
            raise ValueError('Character reference checksum mismatch; refuse to generate image')
        target = ROOT / 'assets/approved/character_reference_preview.jpg'
        if target.exists():
            if target.read_bytes() != data:
                raise ValueError('Existing character reference differs; refuse to overwrite')
        else:
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_suffix('.tmp')
            temporary.write_bytes(data)
            os.replace(temporary, target)
        restaurant = ROOT / 'assets/approved/restaurant_reference_preview.jpg'
        if hashlib.sha256(restaurant.read_bytes()).hexdigest() != '2bcd80cabc43982fe5e01a087204e4fe4e9910815a16e90383b7fdde87dde17a':
            raise ValueError('Restaurant reference checksum mismatch')
        print('PASS: two 320px reference thumbnails verified. These are NOT production sprites.')
        return 0
    except (OSError, ValueError) as exc:
        print(f'FAIL: {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
