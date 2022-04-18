# alicebot.adapter.apscheduler.config

APScheduler 适配器配置。

## *class* `Config`(__pydantic_self__, **data) {#Config}

Bases: `pydantic.main.BaseModel`

APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **scheduler_config** (*Dict[str, Any]*) - 调度器配置。

  - **__config_name__** - 配置名称。