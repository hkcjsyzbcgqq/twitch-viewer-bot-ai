# Security Policy

## Scope

`twitch-viewer-bot-ai` is a research/hobbyist toolkit. It ships **no** authentication bypasses, credential stealers, or Twitch-internal exploits. "Viewer bot" here means a controlled, opt-in simulation harness for channels you own, used to study analytics and chat-AI behaviour.

## Reporting a vulnerability

If you find a real security issue (e.g. cookie leakage in logs, proxy credential exposure, prompt-injection in the AI chat module), open a private security advisory on GitHub or email `security@twitch-viewer-bot-ai.dev` with:

- Affected module and version
- Reproduction steps
- Impact assessment

Please do **not** open a public issue for exploitable bugs.

## Hardening notes for users

- Run against your own channel only. The Twitch ToS treats artificial view inflation as abuse.
- Store proxy credentials in `.env`, never in `config.yaml`.
- AI provider keys (`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`) should be scoped and rotated.
- The `sessions/` directory may contain Twitch IRC cookies — treat it as sensitive and keep it out of git (already in `.gitignore`).

## Out of scope

- Issues caused by misusing the toolkit against channels you don't own.
- Rate-limit bans from Twitch (expected behaviour when running a viewer bot).
- Third-party proxy quality.

## Disclosure policy

We aim to acknowledge reports within 72 hours and patch high-severity issues within 14 days.