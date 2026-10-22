"""Cheap lexicon-based sentiment so we don't burn tokens on every filter."""
from __future__ import annotations

POSITIVE = {"pog", "poggers", "nice", "love", "gg", "hype", "clean", "clutch"}
NEGATIVE = {"bad", "trash", "boring", "cringe", "fail", "lag", "dead"}


def score_sentiment(text: str) -> float:
    words = text.lower().split()
    if not words:
        return 0.0
    pos = sum(1 for w in words if w.strip("!?.,") in POSITIVE)
    neg = sum(1 for w in words if w.strip("!?.,") in NEGATIVE)
    return (pos - neg) / len(words)