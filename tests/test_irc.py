from twitch_bot.handlers.irc_handler import parse


def test_parse_privmsg():
    msg = parse(":user123!user123@user123.tmi.twitch.tv PRIVMSG #demo :hello chat")
    assert msg.nick == "user123"
    assert msg.channel == "#demo"
    assert msg.body == "