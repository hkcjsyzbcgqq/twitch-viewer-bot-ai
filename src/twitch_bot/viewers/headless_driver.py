"""Optional headless-browser driver (requires playwright extra)."""
from __future__ import annotations

import asyncio
import random

from loguru import logger

from twitch_bot.config.settings import Settings


class HeadlessViewerDriver:
    def __init__(self, channel: str, settings: Settings) -> None:
        self.channel = channel
        self.settings = settings

    async def run(self, stop_event: asyncio.Event) -> None:
        try:
            from playwright.async_api import async_playwright
        except ImportError:
            logger.warning("playwright not installed, headless driver disabled")
            return

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            context = await browser.new_context()
            page = await context.new_page()
            await page.goto(f"https://www.twitch.tv/{self.channel}", wait_until="domcontentloaded")
            while not stop_event.is_set():
                await asyncio.sleep(random.uniform(30, 60))
                await page.mouse.move(random.randint(0, 800), random.randint(0, 600))
            await browser.close()