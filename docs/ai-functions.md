# AI functions

The AI layer is deliberately small. It exists so the viewer bot can emit
plausible chat lines and so the harness can classify chat sentiment.

## Components

- `ai.prompt_runner.PromptRunner` — async wrapper over OpenAI and Anthropic clients.
  Retries 3× with linear backoff, returns `None` on total failure.
- `ai.chat_persona.ChatPersona` — drives a background loop that produces a line
  every `60 / max_chat_per_minute` seconds. Lines are filtered by `score_sentiment`.
- `ai.sentiment.score_sentiment` — lexicon-based, no token cost.

## Why not stream everything to an LLM?

Cost and rate-limits. The persona uses a small prompt every time; the sentiment
filter is a local pre-screen so obviously toxic or negative lines are dropped
before they hit the IRC layer.

## Provider config

```yaml
ai:
  provider: openai        # or anthropic
  model: gpt-4o-mini
  temperature: 0.7
  max_chat_per_minute: 6
```