from alicebot import Bot


def test_bot_restart() -> None:
    flag = False

    async def bot_run_hook(bot: Bot) -> None:
        nonlocal flag
        if flag:
            bot.should_exit.set()
            return
        bot.restart()
        flag = True

    bot = Bot()
    bot.bot_run_hook(bot_run_hook)
    bot.run()
    assert flag
