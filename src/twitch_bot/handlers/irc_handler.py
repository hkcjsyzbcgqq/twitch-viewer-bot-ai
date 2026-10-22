"""Parses incoming IRC lines from the ws driver (chat, joins, PING)."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class IrcMessage:
    raw: str
    nick: str | None = None
    channel: str | None = None
    body: str | None = None


def parse(line: str) -> IrcMessage:
    if line.startswith("PING"):
        return IrcMessage(raw=line, body="PING")
    prefix, _, rest = line.partition(" ")
    nick = prefix.split("!")[0].lstrip(":") if prefix.startswith(":") else None
    if rest.startswith("PRIVMSG"):
        _, _, channel, _, body = rest.split(" ", 4)
        return IrcMessage(raw=line, nick=nick, channel=channel, body=body.lstrip(":"))
    return IrcMessage(raw=line, nick=nick)


class IrcHandler:
    def __init__(self) -> None:
        self.seen: list[IrcMessage] = []

    def feed(self, line: str) -> IrcMessage:
        msg = parse(line)
        self.seen.append(msg)
        return msg