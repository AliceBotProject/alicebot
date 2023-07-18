"""测试适配器。

这里是一个最简单可以直接使用的适配器示例。
"""
from asyncio import Condition

from alicebot.adapter import Adapter
from alicebot.event import Event


class TestAdapterEvent(Event["TestAdapter"]):
    """测试适配器事件。

    Attributes:
        message: 消息内容。
    """

    message: str


class TestAdapter(Adapter[TestAdapterEvent, None]):
    """测试适配器。"""

    name: str = "test"
    _msg: str = ""
    _cond: Condition

    async def startup(self):
        """初始化适配器。"""
        self._cond = Condition()

    async def run(self):
        """运行适配器。"""
        while not self.bot.should_exit.is_set():
            async with self._cond:
                await self._cond.wait()
                await self.handle_event(
                    TestAdapterEvent(adapter=self, type="message", message=self._msg)
                )

    async def send(self, msg: str):
        """此方法发送的消息会直接使此适配器产生一个事件。"""
        async with self._cond:
            self._msg = msg
            self._cond.notify()
