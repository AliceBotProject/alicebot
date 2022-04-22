from alicebot.plugin import Plugin


class GlobalStateTest1(Plugin):
    async def handle(self) -> None:
        if self.bot.global_state.get('count', None) is None:
            self.bot.global_state['count'] = 0
        self.bot.global_state['count'] += 1
        await self.event.reply(f'add: {self.bot.global_state["count"]}')

    async def rule(self) -> bool:
        return self.adapter.name == 'cqhttp' and self.event.type == 'message' and self.event.message.startswith('add')
