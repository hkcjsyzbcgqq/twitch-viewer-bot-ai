"""Round-robin proxy pool loaded from proxies.txt."""
from __future__ import annotations

import itertools
from pathlib import Path
from typing import Iterator, Optional


class ProxyRotator:
    def __init__(self, pool_file: Optional[Path] = None) -> None:
        self._proxies: list[str] = []
        if pool_file and pool_file.exists():
            self._proxies = [
                line.strip()
                for line in pool_file.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.startswith("#")
            ]
        self._cycle: Iterator[str] = itertools.cycle(self._proxies) if self._proxies else iter(())

    def __len__(self) -> int:
        return len(self._proxies)

    def next(self) -> Optional[str]:
        return next(self._cycle, None)