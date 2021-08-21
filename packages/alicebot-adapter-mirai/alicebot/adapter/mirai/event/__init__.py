"""
============
Mirai 事件
============
"""
import inspect
from typing import Type

from .base import T_MiraiEvent
from .mate import *
from .message import *
from .notice import *
from .request import *

_mirai_events = {name: model
                 for name, model in globals().items()
                 if inspect.isclass(model) and issubclass(model, MiraiEvent)}


def get_event_class(event_type: str) -> Type[T_MiraiEvent]:
    """
    根据接收到的消息类型返回对应的事件类。

    :param event_type: 事件类型。
    :return: 对应的事件类。
    :rtype: Type[T_MiraiEvent]
    """
    return _mirai_events.get(event_type)


__all__ = list(_mirai_events.keys()) + ['get_event_class']
