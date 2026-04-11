from typing import Any, override

from alicebot import MessageEvent, Plugin
from alicebot.exceptions import GetEventTimeout


class Weather(Plugin[MessageEvent[Any]]):
    @override
    async def handle(self) -> None:
        args = self.event.get_plain_text().split(" ")

        if len(args) > 1:
            await self.event.reply(await self.get_weather(args[1]))
            return

        try:
            city_event = await self.event.ask("请输入想要查询天气的城市：", timeout=10)
        except GetEventTimeout:
            return
        else:
            await self.event.reply(await self.get_weather(city_event.get_plain_text()))

    @override
    async def rule(self) -> bool:
        if not isinstance(self.event, MessageEvent):
            return False
        message = self.event.get_plain_text()
        return message.startswith(("天气", "weather"))

    @staticmethod
    async def get_weather(city: str) -> str:
        if city not in ["北京", "上海"]:
            return "你想查询的城市暂不支持！"
        return f"{city}的天气是..."
