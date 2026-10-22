"""Configuration loader with env-var override."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field


class ProxySettings(BaseModel):
    enabled: bool = False
    pool_file: Optional[Path] = None
    rotate_every: int = Field(default=25, ge=1)


class AISettings(BaseModel):
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    temperature: float = 0.7
    max_chat_per_minute: int = 6


class Settings(BaseModel):
    channel_default: str = ""
    viewer_concurrency: int = 20
    user_agent_rotation: bool = True
    proxy: ProxySettings = ProxySettings()
    ai: AISettings = AISettings()


def _read_yaml(path: Path) -> dict:
    if not path.exists():
        return {}
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def load_settings(root: Path | None = None) -> Settings:
    root = root or Path.cwd()
    data = _read_yaml(root / "config.yaml")
    local = _read_yaml(root / "config.local.yaml")
    data.update(local)

    if os.getenv("TWITCH_BOT_VIEWERS"):
        data["viewer_concurrency"] = int(os.environ["TWITCH_BOT_VIEWERS"])
    return Settings(**data)