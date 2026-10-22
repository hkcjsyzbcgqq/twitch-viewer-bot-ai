"""Stub: writes proxies.txt from stdin, one per line."""
import sys
from pathlib import Path

out = Path("proxies.txt")
lines = [l.strip() for l in sys.stdin if l.strip()]
out.write_text("\n".join(lines), encoding="utf-8")
print(f"wrote {len(lines)} proxies to {out}")