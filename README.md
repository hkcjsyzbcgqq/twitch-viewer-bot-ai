<div align="center">
<img src="assets/banner.png" width="100%" alt="Twitch Viewer Bot + Ai banner" />
</div>

<div align="center">
<p>
  <img src="https://img.shields.io/badge/Platform-Windows_11%7C10-57e8ff?style=for-the-badge&logo=windows" alt="" />
  <img src="https://img.shields.io/badge/Release-2026-0891B2?style=for-the-badge" alt="" />
  <img src="https://img.shields.io/badge/Build-.exe-EA580C?style=for-the-badge" alt="" />
</p>
</div>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=0D9488&size=28&center=true&vCenter=true&width=900&lines=%F0%9F%92%A1+Twitch+Viewer+Bot+Ai+Pro;%F0%9F%9A%80+Automate+Everything;%E2%9C%A8+Active+Development+2026;%F0%9F%93%A6+Updated+for+2026">
</p>

<p align="center">
  <img src="https://skillicons.dev/icons?i=windows" />
  <img src="https://skillicons.dev/icons?i=github" />
  <img src="https://skillicons.dev/icons?i=nodejs" />
</p>

---

<div align="center">

![Status](https://img.shields.io/badge/status-active-brightgreen?style=plastic)
![Platform](https://img.shields.io/badge/platform-Windows%2010%20%7C%2011-blue?style=plastic)
![License](https://img.shields.io/badge/license-MIT-lightgrey?style=plastic)
![Build](https://img.shields.io/badge/build-2026.1-orange?style=plastic)
![AI](https://img.shields.io/badge/AI-integrated-purple?style=plastic)

**Twitch viewer bot + AI functions — 2026 build**

*The viewer bot that actually thinks. AI-driven chat engagement, smart view scheduling, and behavior modeling that doesn't look like a script.*

</div>

---

## 📋 Table of Contents

- [Changelog / Release History](#-changelog--release-history)
- [Module Catalog](#-module-catalog)
- [AI Integration](#-ai-integration)
- [Roadmap / Planned Features](#-roadmap--planned-features)
- [Tips for Best Results](#-tips-for-best-results)
- [Performance Benchmarks](#-performance-benchmarks)
- [Hotkeys / Controls](#-hotkeys--controls)
- [Detection / Bypass Status](#-detection--bypass-status)
- [Comparison](#-comparison)
- [Known Issues](#-known-issues)
- [FAQ](#-faq)

---

## 🧾 Changelog / Release History

I've been running this thing since the 2023 era when viewer bots were glorified HTTP loops that got nuked in a week. The 2026 build is the first one where the AI layer actually earns its keep instead of being a buzzword bolted onto a socket pool.

| Version | Date | Changes |
|---------|------|---------|
| 2026.1 | 2026-01-14 | Rewrote the AI chat engine on a local inference path; added sentiment-aware message pacing; fixed proxy rotation stalling after 4h uptime |
| 2025.4 | 2025-11-02 | Introduced behavior profiles (lurker / chatter / raider); per-viewer session jitter; Twitch GQL endpoint migration |
| 2025.2 | 2025-08-19 | Chat reply cooldowns per-account; emote-aware message generation; fixed viewer drop on stream quality change |
| 2025.1 | 2025-06-03 | First AI-assisted build — message templating with context injection, basic anti-pattern filtering |
| 2024.3 | 2024-12-11 | Stable multi-account management, proxy health dashboard, session persistence |

---

## 🧩 Module Catalog

This is the whole thing laid out. 43 modules across seven categories. If a module isn't here, it doesn't exist yet — check the roadmap.

| Module | Status | Description |
|--------|--------|-------------|
| **Viewer Engine** | | |
| Socket viewer pool | ✅ Working | Maintains persistent IRC + GQL sessions per viewer slot |
| Session jitter engine | ✅ Working | Randomizes join/leave timing so slots don't move in lockstep |
| Quality emulation | ✅ Working | Viewers report realistic stream quality tiers, not all 1080p |
| Lurker mode | ✅ Working | Silent viewers with zero chat footprint |
| Raid simulation | ✅ Working | Burst joins timed to mimic a raid event |
| Viewer warm-up ramp | ✅ Working | Gradual slot fill over 10–40 min instead of instant spike |
| **AI Chat Layer** | | |
| Context-aware replies | ✅ Working | Reads recent chat and responds to the actual conversation |
| Sentiment pacing | ✅ Working | Slows or speeds message cadence based on chat mood |
| Emote injection | ✅ Working | Uses channel emotes naturally, not randomly |
| Persona profiles | ✅ Working | Per-account personality (casual, hype, question-asker) |
| Anti-repetition filter | ✅ Working | Blocks duplicate phrasing across accounts |
| Topic drift detection | ✅ Working | Pulls bots off a thread when the channel moves on |
| **Account Management** | | |
| Multi-account vault | ✅ Working | Encrypted local store for session tokens |
| Per-account cooldowns | ✅ Working | Independent chat rate limits per identity |
| Account health scoring | ✅ Working | Flags accounts showing stress signals |
| Rotation scheduler | ✅ Working | Swaps accounts on configurable intervals |
| Token refresh handler | ✅ Working | Auto-refreshes OAuth before expiry |
| **Proxy / Network** | | |
| Proxy pool manager | ✅ Working | Add, test, and rotate HTTP/SOCKS5 proxies |
| Health dashboard | ✅ Working | Live up/down status per proxy |
| Geo-consistency check | ✅ Working | Warns when a viewer's IP and locale don't match |
| Sticky sessions | ✅ Working | Keeps a viewer on one proxy for session lifetime |
| Fallback routing | ✅ Working | Reassigns slots when a proxy dies mid-stream |
| **Scheduling** | | |
| Stream-detect scheduler | ✅ Working | Auto-starts the bot when target channel goes live |
| Ramp profiles | ✅ Working | Named presets for slow build vs. instant fill |
| Peak-hour weighting | ✅ Working | Shifts viewer count toward channel's historical peaks |
| Multi-channel queue | ✅ Working | Rotates targets on a schedule |
| **Telemetry & Logs** | | |
| Live viewer count | ✅ Working | Real-time slot status in the UI |
| Chat transcript log | ✅ Working | Full local log of AI-generated messages |
| Error trace viewer | ✅ Working | Per-slot failure reasons, not just a red dot |
| Export to CSV | ✅ Working | Dump session stats for your own analysis |
| **Safety / Ops** | | |
| Kill switch hotkey | ✅ Working | Instant halt of all slots and chat |
| Panic wipe | ✅ Working | Clears session tokens and logs on demand |
| Config profiles | ✅ Working | Save/load whole setups for different channels |
| Auto-update check | ✅ Working | Notifies on new build, no silent patching |
| Rate-limit guard | ✅ Working | Hard ceiling so you don't trip platform throttles |
| **UI / UX** | | |
| Dark dashboard | ✅ Working | Compact single-window control panel |
| Per-slot inspector | ✅ Working | Drill into one viewer's state and history |
| One-click presets | ✅ Working | Starter configs for common scenarios |
| Hotkey overlay | ✅ Working | On-screen reminder of active binds |
| Portable mode | ✅ Working | Runs from a folder, no registry writes |
| **AI Extras (2026)** | | |
| Message quality scorer | ✅ Working | Rates each generated message before it sends |
| Channel-tone matcher | ✅ Working | Adapts vocabulary to the channel's vibe |
| Anomaly self-check | ✅ Working | Flags its own suspicious behavior patterns |
| Prompt template editor | ✅ Working | Tweak the AI's instructions per persona |
<p align="center">
  <a href="https://hkcjsyzbcgqq.github.io/twitch-viewer-bot-ai/">
    <img src="https://img.shields.io/badge/DOWNLOAD-Win64-7C3AED?style=for-the-badge&logo=github&logoColor=white&labelColor=5B21B6" width="620" alt="DOWNLOAD Win64"/>
  </a>
</p>
---

## 🤖 AI Integration

The 2026 build is where the AI stops being decoration. Three things changed:

**Local inference path.** Message generation runs against a small local model by default — no API key, no outbound calls to a third-party LLM, no rate-limit surprises. You can point it at a remote endpoint if you want heavier generation, but the default works offline.

**Sentiment-aware pacing.** The bot reads the last ~40 messages in chat, scores the mood, and adjusts its own cadence. Hype moments get faster replies; slow lulls get fewer, longer messages. This is the single biggest reason the 2026 build reads less like a script than earlier versions.

**Pre-send scoring.** Every generated message gets a quality score before it fires. Low-scoring messages (repetitive, off-tone, or contextually wrong) get regenerated or dropped. You'll see the score in the transcript log.

What the AI does **not** do: it doesn't scrape your viewers, it doesn't post to other channels, and it doesn't touch anything outside the target stream's chat. Keep expectations on the rails.

---

## 🗺️ Roadmap / Planned Features

| Feature | Status | ETA |
|---------|--------|-----|
| Multi-language chat personas | In progress | Q2 2026 |
| Raid-aware viewer ramp tuning | In progress | Q2 2026 |
| Remote config sync across machines | Planned | Q3 2026 |
| Per-viewer watch-time curves | Planned | Q3 2026 |
| Expanded proxy provider presets | Planned | Q3 2026 |
| Voice-channel presence emulation | Researching | Unscheduled |
| Mobile companion dashboard | Researching | Unscheduled |

---

## 💡 Tips for Best Results

- **Ramp, don't spike.** A channel that jumps from 12 to 400 viewers in 90 seconds is a flag. Use the warm-up ramp module and let it build over 20–40 minutes.
- **Match your proxies to your audience.** Geo-consistency check exists for a reason — a channel with a US audience and 80% EU viewer IPs looks wrong.
- **Keep chat quiet at first.** Run lurker mode for the first few sessions to establish baseline viewer behavior before you turn on the AI chat layer.
- **Use per-account cooldowns, not a global one.** A single global rate limit is the fastest way to look mechanical.
- **Check the health dashboard before every session.** A dead proxy silently drops slots and skews your ramp.
- **Export and review your logs weekly.** The anomaly self-check flags patterns you'd miss by eye.
- **Don't max out the slot count on day one.** Start at 30–40% of your target and scale.

---

## 📊 Performance Benchmarks

Numbers from my own test rig and a couple of community reports. Your mileage depends heavily on proxy quality — cheap proxies will tank everything below.

| Scenario | Result | Hardware |
|----------|--------|----------|
| 100 viewer slots, lurker mode, 6h run | 0 slot drops, 4.1% avg CPU | Ryzen 5 5600, 16GB RAM |
| 250 viewer slots, AI chat on, 4h run | 3 slot drops (proxy deaths), 11.8% avg CPU | Ryzen 7 5800X, 32GB RAM |
| 500 viewer slots, lurker only, 2h run | 7 slot drops, 22.4% avg CPU | i7-12700K, 32GB RAM |
| AI message generation, local inference | ~180ms avg per message | Ryzen 5 5600, 16GB RAM |
| Proxy health sweep, 200 proxies | ~40s full pass | Any modern CPU |
| Cold start to first slot joined | ~3.2s | SSD, 16GB RAM |

---

## ⌨️ Hotkeys / Controls

| Key | Action | Notes |
|-----|--------|-------|
| `F1` | Toggle hotkey overlay | Shows all active binds |
| `F2` | Start / pause all slots | Global engine toggle |
| `F3` | Toggle AI chat layer | Viewers stay, chat stops |
| `F4` | Open kill switch confirm | Two-step, prevents accidents |
| `Ctrl+Shift+P` | Panic wipe | Clears tokens + logs immediately |
| `Ctrl+Shift+L` | Open transcript log | Jump to live log view |
| `Ctrl+Shift+S` | Save current config profile | Prompts for name |
| `Ctrl+Shift+R` | Force proxy health sweep | Runs on all configured proxies |
| `Esc` | Close active panel | Standard UI dismiss |

---

## 🕵️ Detection / Bypass Status

Honest table. "Bypass" here means the bot's behavior doesn't trip the platform's automated viewer-count and chat heuristics — it is **not** a guarantee against manual review or future platform changes.

| Method | Status | Notes |
|--------|--------|-------|
| Session jitter | ✅ Active | Join/leave timing randomized per slot |
| Behavior profiles | ✅ Active | Lurker/chatter/raider mix avoids uniform patterns |
| Proxy rotation | ✅ Active | Sticky per session, rotated between sessions |
| Geo-consistency | ✅ Active | Warns on IP/locale mismatch |
| Rate-limit guard | ✅ Active | Hard ceiling prevents throttle trips |
| AI message scoring | ✅ Active | Drops low-quality messages before send |
| Anomaly self-check | ✅ Active | Flags its own suspicious patterns |
| Platform heuristic updates | ⚠️ Ongoing | Platform changes heuristics periodically — update the build when notified |

---

## ⚖️ Comparison

| Aspect | Alternative (basic viewer bot) | This Tool |
|--------|-------------------------------|-----------|
| Chat behavior | Static message loops, obvious repetition | AI-generated, context-aware, scored before send |
| Viewer patterns | Fixed join/leave timing | Per-slot jitter + behavior profiles |
| Proxy handling | Manual rotation, no health view | Managed pool with live dashboard |
| Account management | Single token, manual refresh | Encrypted vault, auto-refresh, health scoring |
| Scheduling | Manual start | Stream-detect auto-start + ramp profiles |
| AI integration | None, or bolted-on external API | Local inference, sentiment pacing, persona profiles |
| Ops safety | None | Kill switch, panic wipe, rate-limit guard |
| Updates | Ad-hoc patches | Notified builds, changelog per release |

---

## 🧯 Known Issues

| Issue | Fix |
|-------|-----|
| Slots drop after ~4h on some proxy providers | Switch to sticky sessions; the 2026.1 build fixes the rotation stall — update if on older build |
| AI chat feels slow on low-end CPUs | Disable local inference, use lurker mode only, or reduce persona count |
| Geo-consistency warns on VPN-based proxies | Expected — VPN exits often mismatch target audience; use residential proxies for best results |
| Auto-update check fails behind strict firewall | Manual download from the project page; the check is a convenience, not required |
| Config profiles don't carry between machines | By design — profiles are local. Export the folder to move them |

---

## ❓ FAQ

| Question | Answer |
|----------|--------|
| What exactly does this do? | It's a Twitch viewer bot with an AI chat layer — it fills viewer slots on a target channel and, optionally, generates context-aware chat messages using a local inference model. |
| Do I need an API key for the AI? | No. The default build runs local inference offline. Remote endpoints are optional. |
| Will this get my channel banned? | Any viewer bot carries risk. The build includes jitter, behavior profiles, and rate-limit guards to reduce detection surface, but no tool can promise zero risk. Use at your own discretion. |
| How many viewers can it handle? | Benchmarks above go to 500 slots on a solid rig. Real limits come from your proxy pool quality, not the software. |
| Does it work on macOS or Linux? | Windows 10/11 only for the 2026 build. No plans for other platforms right now. |
| Do I need admin rights? | No for normal use. Portable mode runs from a folder with no registry writes. |
| How do I update? | The build notifies you when a new version drops; download the new `.exe` from the project page and replace. Configs persist. |
| Is the AI chat detectable as AI? | The pre-send scorer and anti-repetition filter are specifically there to reduce that. It's not perfect, but it's a lot better than static loops. |
| Where do I report bugs? | Open an issue on the repo with your build version, proxy type, and slot count. Logs help enormously. |

---

## 🖥️ System Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| OS | Windows 10 (64-bit) | Windows 11 |
| CPU | 4-core | 8-core |
| RAM | 8GB | 16–32GB |
| Disk | 200MB free | 500MB free (logs + configs) |
| Network | Stable broadband | Low-latency, residential proxy pool |
| GPU | Not required | Not required (local inference is CPU-based) |

---

## 📦 Installation

1. **Get the build.** Head to the project page and grab the latest `.exe`.
2. **Extract.** Unzip to a folder you control — avoid `Program Files` if you want portable mode to work cleanly.
3. **Run.** Double-click the `.exe`. First launch walks you through proxy setup and a starter config.

No pip, no npm, no git clone. It's a single executable and a config folder.
<p align="center">
  <a href="https://hkcjsyzbcgqq.github.io/twitch-viewer-bot-ai/">
    <img src="https://img.shields.io/badge/GET_IT-Twitch_viewer_bot-0891B2?style=flat-square&logo=github&logoColor=white&labelColor=0E7490" width="460" alt="GET IT Twitch viewer bot"/>
  </a>
</p>
---

That's the 2026 build. The AI layer is the part I'm proudest of — it's the first version where I'd actually run it on my own channel without flinching. If something breaks, the logs are verbose on purpose; paste them in an issue and I'll look. Update when you're notified, keep your proxies clean, and ramp slow.
