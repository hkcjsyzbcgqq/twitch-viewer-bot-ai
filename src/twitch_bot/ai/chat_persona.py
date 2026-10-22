"""Generates chat lines in-character so viewer presence looks human."""
from __future__ import annotations

import asyncio
import random
from typing import TYPE_CHECKING

from loguru import logger

from twitch_bot.ai.prompt_runner import PromptRunner
from twitch_bot.ai.sentiment import score_sentiment
from twitch_bot.config.settings import Settings

if TYPE_CHECKING:
    from twitch_bot.viewers.pool import ViewerPool

SYSTEM_PREAMBLE = (
    "You are a casual Twitch chatter. Reply with one short line, no hashtags, "
    "no emojis at the start, max 90 characters. Never mention being an AI."
)


class ChatPersona:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.runner = PromptRunner(settings.ai)
        self._pool: "ViewerPool | None" = None

    async def attach(self, pool: "ViewerPool") -> None:
        self._pool = pool
        asyncio.create_task(self._loop())

    async def _loop(self) -> None:
        interval = 60.0 / max(1, self.settings.ai.max_chat_per_minute)
        while True:
            await asyncio.sleep(interval * random.uniform(0.6, 1.4))
            line = await self._generate()
            if line and score_sentiment(line) > -0.4:
                logger.info("[chat] {}", line)

    async def _generate(self) -> str | None:
        prompt = f"{SYSTEM_PREAMBLE}\nChannel: #{self.settings.channel_default or 'unknown'}\nSay something."
        return await self.runner.complete(prompt)