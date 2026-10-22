"""Persist per-driver cookies so restarts don't re-fingerprint from scratch."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class SessionStore:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def path_for(self, key: str) -> Path:
        return self.root / f"{key}.session"

    def save(self, key: str, data: dict[str, Any]) -> None:
        self.path_for(key).write_text(json.dumps(data), encoding="utf-8")

    def load(self, key: str) -> dict[str, Any]:
        p = self.path_for(key)
        if not p.exists():
            return {}
        return json.loads(p.read_text(encoding="utf-8"))