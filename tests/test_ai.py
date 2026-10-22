from twitch_bot.ai.prompt_runner import PromptRunner
from twitch_bot.ai.sentiment import score_sentiment
from twitch_bot.config.settings import AISettings


def test_sentiment_positive():
    assert score_sentiment("pog nice clutch") > 0


def test_sentiment_negative():
    assert score_sentiment("trash boring fail") < 0


def test_prompt_runner_unknown_provider():
    runner = PromptRunner(AISettings(provider="nope"))
    try:
        runner._ensure_client()
    except ValueError as exc:
        assert "nope" in str(exc)