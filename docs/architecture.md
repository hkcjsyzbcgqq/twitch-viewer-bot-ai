# Architecture

```
bootstrap.py
   └── config.settings ── load yaml + env overrides
   └── viewers.pool.ViewerPool ── spawns N drivers
        ├── viewers.http_driver   (HTTP player page + spade ping)
        ├── viewers.ws_driver     (IRC websocket, justinfan nick)
        └── viewers.headless_driver (optional, playwright)
   └── ai.chat_persona ── generates chat lines via PromptRunner
        └── ai.sentiment   ── cheap lexicon filter before sending
   └── services.proxy_rotator ── round-robin from proxies.txt
   └── services.session_store ── cookie persistence per driver
   └── services.analytics_reporter ── periodic pool snapshots
```

**Layers**
- `config/` — schema + loader
- `viewers/` — driver implementations (the actual "bot")
- `ai/` — prompt runners, chat persona, sentiment heuristics
- `services/` — cross-cutting runtime services
- `utils/` — fingerprint, rate-limiter
- `tests/` — unit tests