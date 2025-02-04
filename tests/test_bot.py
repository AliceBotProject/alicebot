from pytest_mock import MockerFixture

from alicebot import Bot


def test_bot_restart(mocker: MockerFixture) -> None:
    mock = mocker.AsyncMock()

    async def bot_run_hook(bot: Bot) -> None:
        if mock.called:
            bot.exit()
            return
        await mock()
        bot.restart()

    bot = Bot()
    spy = mocker.spy(bot, "restart")
    bot.bot_run_hook(bot_run_hook)
    bot.run()
    spy.assert_called_once()
