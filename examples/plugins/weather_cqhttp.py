from alicebot import Plugin
from alicebot.exceptions import GetEventTimeout


class Weather(Plugin):
    async def handle(self) -> None:
        args = self.event.get_plain_text().split(" ")

        if len(args) >= 2:  # noqa: PLR2004
            await self.event.reply(await self.get_weather(args[1]))
            return

        try:
            city_event = await self.event.ask("请输入想要查询天气的城市：", timeout=10)
        except GetEventTimeout:
            return
        else:
            await self.event.reply(await self.get_weather(city_event.get_plain_text()))

    async def rule(self) -> bool:
        if self.event.adapter.name != "cqhttp":
            return False
        if self.event.type != "message":
            return False
        return self.event.message.startswith("天气") or self.event.message.startswith(
            "weather"
        )

    @staticmethod
    async def get_weather(city):
        if city not in ["北京", "上海"]:
            return "你想查询的城市暂不支持！"
        return f"{city}的天气是..."
