"""Build a plausible browser fingerprint per viewer."""
from __future__ import annotations

import random
import hashlib

RESOLUTIONS = [(1920, 1080), (1366, 768), (2560, 1440), (1440, 900), (1536, 864)]
TIMEZONES = ["Europe/Berlin", "America/New_York", "America/Los_Angeles", "Asia/Tokyo"]


def build_fingerprint(seed: str) -> dict:
    rng = random.Random(seed)
    w, h = rng.choice(RESOLUTIONS)
    return {
        "id": hashlib.sha1(seed.encode()).hexdigest()[:16],
        "screen": f"{w}x{h}",
        "timezone": rng.choice(TIMEZONES),
        "lang": rng.choice(["en-US", "en-GB", "de-DE"]),
        "hardware_concurrency": rng.choice([4, 8, 12, 16]),
    }