# Contributing to twitch-viewer-bot-ai

Thanks for your interest in improving the Twitch viewer bot + AI functions toolkit.

## Ground rules

- **Educational use only.** This project exists to study how Twitch viewer counts, chat presence, and AI-driven engagement heuristics work under load. Do not use it against channels you do not own, and do not violate the Twitch Terms of Service. You are responsible for how you run this code.
- Do not open PRs that add paid proxy resellers, credential harvesters, or anything that scrapes private user data.
- Keep AI prompts deterministic where possible — LLM-as-a-feature, not LLM-as-a-black-box.

## Development setup

```bash
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest -q
```

## Project layout

- `src/twitch_bot/` — main package (viewer engine, AI layer, session handling)
- `src/twitch_bot/viewers/` — viewer pool drivers (http, websocket, headless)
- `src/twitch_bot/ai/` — prompt runners, chat persona, sentiment heuristics
- `src/twitch_bot/config/` — settings loader and schema
- `tests/` — unit tests and stub drivers

## Style

- `ruff` for linting, `mypy` for types.
- Prefer `async def` for anything touching the network.
- Public functions get a short docstring; internal helpers may skip it.

## PR checklist

- [ ] `pytest -q` passes
- [ ] `ruff check src tests` clean
- [ ] New behaviour covered by a test in `tests/`
- [ ] No hardcoded tokens, cookies, or proxy credentials