"""HTTP-based viewer driver — opens the player page and pings presence."""
from __future__ import annotations

import asyncio
import random

import aiohttp
from fake_useragent import UserAgent
from loguru import logger

from twitch_bot.config.settings import Settings

SPADE_URL = "https://spade.twitch.tv/track"


class HttpViewerDriver:
    def __init__(self, channel: str, settings: Settings) -> None:
        self.channel = channel
        self.settings = settings
        self.ua = UserAgent() if settings.user_agent_rotation else None

    def _headers(self) -> dict:
        return {
            "User-Agent": self.ua.random if self.ua else "Mozilla/5.0",
            "Referer": f"https://www.twitch.tv/{self.channel}",
            "Client-ID": "kimne78kx3ncx6brgo4mv6wki5h1ko",
        }

    async def run(self, stop_event: asyncio.Event) -> None:
        timeout = aiohttp.ClientTimeout(total=30)
        async with aiohttp.ClientSession(timeout=timeout, headers=self._headers()) as session:
            player_url = f"https://www.twitch.tv/{self.channel}"
            while not stop_event.is_set():
                try:
                    async with session.get(player_url) as resp:
                        logger.trace("http viewer {} -> {}", self.channel, resp.status)
                    await asyncio.sleep(random.uniform(20, 45))
                    await session.post(SPADE_URL, json={"event": "minute-watched"})
                except (aiohttp.ClientError, asyncio.TimeoutError) as exc:
                    logger.debug("http driver retry: {}", exc)
                    await asyncio.sleep(5)