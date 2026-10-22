"""Thin wrapper over OpenAI / Anthropic with retry + token accounting."""
from __future__ import annotations

import asyncio
from typing import Optional

from loguru import logger

from twitch_bot.config.settings import AISettings


class PromptRunner:
    def __init__(self, settings: AISettings) -> None:
        self.settings = settings
        self._client = None

    def _ensure_client(self):
        if self._client is not None:
            return self._client
        if self.settings.provider == "openai":
            from openai import AsyncOpenAI
            self._client = AsyncOpenAI()
        elif self.settings.provider == "anthropic":
            from anthropic import AsyncAnthropic
            self._client = AsyncAnthropic()
        else:
            raise ValueError(f"unknown provider {self.settings.provider}")
        return self._client

    async def complete(self, prompt: str, retries: int = 3) -> Optional[str]:
        client = self._ensure_client()
        for attempt in range(1, retries + 1):
            try:
                if self.settings.provider == "openai":
                    resp = await client.chat.completions.create(
                        model=self.settings.model,
                        temperature=self.settings.temperature,
                        messages=[{"role": "user", "content": prompt}],
                    )
                    return resp.choices[0].message.content
                resp = await client.messages.create(
                    model=self.settings.model,
                    max_tokens=200,
                    temperature=self.settings.temperature,
                    messages=[{"role": "user", "content": prompt}],
                )
                return resp.content[0].text
            except Exception as exc:  # noqa: BLE001
                logger.warning("prompt attempt {} failed: {}", attempt, exc)
                await asyncio.sleep(1.5 * attempt)
        return None