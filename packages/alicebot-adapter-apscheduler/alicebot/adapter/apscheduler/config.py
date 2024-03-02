"""APScheduler 适配器配置。"""

from typing import Any, Dict

from pydantic import Field

from alicebot.config import ConfigModel

__all__ = ["Config"]


class Config(ConfigModel):
    """APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

    Attributes:
        scheduler_config: 调度器配置。
    """

    __config_name__ = "apscheduler"
    scheduler_config: Dict[str, Any] = Field(default_factory=dict)
