"""Convenience launcher: `python scripts/run_bot.py <channel> --viewers 100`."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from twitch_bot.bootstrap import main  # noqa: E402

if __name__ == "__main__":
    main()