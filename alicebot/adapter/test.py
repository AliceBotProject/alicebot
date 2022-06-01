"""测试适配器。

这里是一个最简单可以直接使用的适配器示例。
"""
from alicebot.event import Event
from alicebot.adapter import Adapter
from alicebot.utils import Condition


class TestAdapter(Adapter):
    """测试适配器。"""

    name: str = "test"
    _cond: Condition[str]

    async def startup(self):
        self._cond = Condition()

    async def run(self):
        while not self.bot.should_exit.is_set():
            async with self._cond:
                msg = await self._cond.wait()
                await self.handle_event(
                    TestAdapterEvent(adapter=self, type="message", message=msg)
                )

    async def send(self, msg: str):
        """此方法发送的消息会直接使此适配器产生一个事件。"""
        async with self._cond:
            self._cond.notify(msg)


class TestAdapterEvent(Event[TestAdapter]):
    """测试适配器事件。

    Attributes:
        message: 消息内容。
    """

    message: str
