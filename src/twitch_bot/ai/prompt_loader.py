"""Load prompt templates from the prompts/ directory."""
from __future__ import annotations

from pathlib import Path

_PROMPT_DIR = Path(__file__).parent / "prompts"


def load(name: str) -> str:
    path = _PROMPT_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"prompt template not found: {name}")
    return path.read_text(encoding="utf-8")