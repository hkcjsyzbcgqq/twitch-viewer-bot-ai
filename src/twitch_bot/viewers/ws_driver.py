"""WebSocket driver — joins the IRC chat anonymously to keep presence alive."""
from __future__ import annotations

import asyncio
import random

import websockets
from loguru import logger

from twitch_bot.config.settings import Settings

IRC_URL = "wss://irc-ws.chat.twitch.tv:443"


class WebSocketViewerDriver:
    def __init__(self, channel: str, settings: Settings) -> None:
        self.channel = channel
        self.settings = settings

    def _nick(self) -> str:
        return f"justinfan{random.randint(10000, 99999)}"

    async def run(self, stop_event: asyncio.Event) -> None:
        while not stop_event.is_set():
            try:
                async with websockets.connect(IRC_URL, ping_interval=30) as ws:
                    await ws.send("PASS SCHMOOPIIE")
                    await ws.send(f"NICK {self._nick()}")
                    await ws.send(f"JOIN #{self.channel}")
                    logger.trace("ws viewer joined #{}", self.channel)
                    async for raw in ws:
                        if stop_event.is_set():
                            break
                        if raw.startswith("PING"):
                            await ws.send("PONG :tmi.twitch.tv")
            except (websockets.WebSocketException, OSError) as exc:
                logger.debug("ws driver retry: {}", exc)
                await asyncio.sleep(8)