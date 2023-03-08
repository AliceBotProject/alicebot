"""Mirai 适配器事件。"""
import inspect
from typing import Type

from .mate import *
from .notice import *
from .message import *
from .request import *

_mirai_events = {
    name: model
    for name, model in globals().items()
    if inspect.isclass(model) and issubclass(model, MiraiEvent)
}


def get_event_class(event_type: str) -> Type[MiraiEvent]:
    """根据接收到的消息类型返回对应的事件类。

    Args:
        event_type: 事件类型。

    Returns:
        对应的事件类。
    """
    return _mirai_events[event_type]
