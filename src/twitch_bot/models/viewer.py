"""Runtime model for a single simulated viewer."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Viewer:
    viewer_id: str
    channel: str
    proxy: Optional[str] = None
    fingerprint: dict = field(default_factory=dict)
    alive: bool = False
    joined_at: Optional[float] = None