"""Entrypoint for the viewer bot CLI."""
from __future__ import annotations

import asyncio
import argparse
from loguru import logger

from twitch_bot.config.settings import load_settings
from twitch_bot.viewers.pool import ViewerPool
from twitch_bot.ai.chat_persona import ChatPersona


async def run(channel: str, viewers: int, ai_enabled: bool) -> None:
    settings = load_settings()
    logger.info("starting viewer pool channel={} viewers={}", channel, viewers)

    pool = ViewerPool(channel=channel, target=viewers, settings=settings)
    persona = ChatPersona(settings=settings) if ai_enabled else None

    async with pool:
        if persona is not None:
            await persona.attach(pool)
        await pool.run_until_stopped()


def main() -> None:
    parser = argparse.ArgumentParser(prog="twitch-viewer-bot-ai")
    parser.add_argument("channel", help="Twitch channel name (no #)")
    parser.add_argument("--viewers", type=int, default=50)
    parser.add_argument("--no-ai", action="store_true", help="disable AI chat functions")
    args = parser.parse_args()

    try:
        asyncio.run(run(args.channel, args.viewers, ai_enabled=not args.no_ai))
    except KeyboardInterrupt:
        logger.warning("interrupted by user")


if __name__ == "__main__":
    main()