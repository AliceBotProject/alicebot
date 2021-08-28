"""
==================
APScheduler 配置
==================
"""
from typing import Any, Dict

from pydantic import BaseModel


class Config(BaseModel):
    """
    APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。
    """
    __config_name__ = 'apscheduler'
    """
    配置名称。
    """
    scheduler_config: Dict[str, Any] = {}
    """
    调度器配置
    """
