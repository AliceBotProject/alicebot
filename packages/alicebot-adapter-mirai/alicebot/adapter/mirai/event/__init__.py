"""Mirai 适配器事件。"""
import inspect
from typing import Type

from .mate import *
from .notice import *
from .message import *
from .request import *
from .base import T_MiraiEvent

_mirai_events = {
    name: model
    for name, model in globals().items()
    if inspect.isclass(model) and issubclass(model, MiraiEvent)
}


def get_event_class(event_type: str) -> Type[T_MiraiEvent]:
    """根据接收到的消息类型返回对应的事件类。

    Args:
        event_type: 事件类型。

    Returns:
        对应的事件类。
    """
    return _mirai_events.get(event_type)


__all__ = list(_mirai_events.keys()) + ["get_event_class"]
