"""Sends generated chat lines into the IRC connection of a ws driver."""
from __future__ import annotations

from loguru import logger


class ChatSender:
    def __init__(self, ws) -> None:
        self.ws = ws

    async def send(self, channel: str, line: str) -> None:
        payload = f"PRIVMSG #{channel} :{line}\r\n"
        try:
            await self.ws.send(payload)
            logger.debug("sent chat to #{}", channel)
        except Exception as exc:  # noqa: BLE001
            logger.warning("chat send failed: {}", exc)