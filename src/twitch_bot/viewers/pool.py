"""Viewer pool — spawns N drivers against a channel and keeps them alive."""
from __future__ import annotations

import asyncio
from typing import List

from loguru import logger

from twitch_bot.config.settings import Settings
from twitch_bot.viewers.http_driver import HttpViewerDriver
from twitch_bot.viewers.ws_driver import WebSocketViewerDriver


class ViewerPool:
    def __init__(self, channel: str, target: int, settings: Settings) -> None:
        self.channel = channel
        self.target = target
        self.settings = settings
        self._drivers: List[asyncio.Task] = []
        self._stop = asyncio.Event()

    async def _spawn(self, index: int) -> None:
        # alternate HTTP and WebSocket drivers so the pool looks organic
        if index % 3 == 0:
            driver = WebSocketViewerDriver(channel=self.channel, settings=self.settings)
        else:
            driver = HttpViewerDriver(channel=self.channel, settings=self.settings)
        try:
            await driver.run(stop_event=self._stop)
        except Exception as exc:  # noqa: BLE001
            logger.debug("driver {} died: {}", index, exc)

    async def __aenter__(self) -> "ViewerPool":
        sem = asyncio.Semaphore(self.settings.viewer_concurrency)

        async def guarded(i: int) -> None:
            async with sem:
                await self._spawn(i)

        self._drivers = [asyncio.create_task(guarded(i)) for i in range(self.target)]
        logger.info("pool online: {} drivers", len(self._drivers))
        return self

    async def __aexit__(self, *exc) -> None:
        self._stop.set()
        for task in self._drivers:
            task.cancel()
        await asyncio.gather(*self._drivers, return_exceptions=True)

    async def run_until_stopped(self) -> None:
        try:
            await self._stop.wait()
        except asyncio.CancelledError:
            pass