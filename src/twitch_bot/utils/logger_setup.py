"""Central loguru config."""
from __future__ import annotations

import sys
from loguru import logger

from twitch_bot.config.settings import Settings


def configure(settings: Settings) -> None:
    logger.remove()
    logger.add(sys.stderr, level="INFO", enqueue=True)
    logger.add("logs/bot_{time}.log", rotation="10 MB", retention=5, level="DEBUG")