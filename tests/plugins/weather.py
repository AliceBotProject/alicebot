from alicebot.plugin import Plugin
from alicebot.exception import AdapterTimeout


class Weather(Plugin):
    async def handle(self) -> None:
        args = self.event.get_plain_text().split(' ')
        if len(args) >= 2:
            await self.event.replay(await self.get_weather(args[1]))
        else:
            await self.event.replay('请输入想要查询天气的城市：')
            try:
                city_event = await self.get(lambda x: x.type == 'message', timeout=10)
            except AdapterTimeout:
                return
            else:
                await self.event.replay(await self.get_weather(city_event.get_plain_text()))

    async def rule(self) -> bool:
        if self.adapter.name != 'cqhttp':
            return False
        if self.event.type != 'message':
            return False
        return self.event.message.startswith('天气') or self.event.message.startswith('weather')

    @staticmethod
    async def get_weather(city):
        if city not in ['北京', '上海']:
            return '你想查询的城市暂不支持！'
        return f'{city}的天气是...'
