import pytest

from twitch_bot.config.settings import Settings
from twitch_bot.viewers.pool import ViewerPool


@pytest.mark.asyncio
async def test_pool_spawns_target(monkeypatch):
    spawned = []

    class FakeDriver:
        def __init__(self, channel, settings):
            self.channel = channel

        async def run(self, stop_event):
            spawned.append(self.channel)
            await stop_event.wait()

    monkeypatch.setattr("twitch_bot.viewers.pool.HttpViewerDriver", FakeDriver)
    monkeypatch.setattr("twitch_bot.viewers.pool.WebSocketViewerDriver", FakeDriver)

    settings = Settings(viewer_concurrency=4)
    async with ViewerPool(channel="demo", target=6, settings=settings):
        await __import__("asyncio").sleep(0.05)

    assert len(spawned) == 6
    assert all(c == "demo" for c in spawned)