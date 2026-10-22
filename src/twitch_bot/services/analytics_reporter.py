"""Periodic status reporter — dumps pool health for the AI layer."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from datetime import datetime, timezone

from loguru import logger


@dataclass
class PoolSnapshot:
    channel: str
    viewers_alive: int
    viewers_target: int
    ts: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())


class AnalyticsReporter:
    def __init__(self, pool, interval: float = 30.0) -> None:
        self.pool = pool
        self.interval = interval
        self._task: asyncio.Task | None = None

    def start(self) -> None:
        self._task = asyncio.create_task(self._loop())

    async def _loop(self) -> None:
        while True:
            snap = PoolSnapshot(
                channel=self.pool.channel,
                viewers_alive=sum(1 for t in self.pool._drivers if not t.done()),
                viewers_target=self.pool.target,
            )
            logger.info("snapshot {} {}/{} alive", snap.channel, snap.viewers_alive, snap.viewers_target)
            await asyncio.sleep(self.interval)