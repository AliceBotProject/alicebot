# alicebot.adapter.apscheduler.config

APScheduler 适配器配置。

## _class_ `Config` {#Config}

Bases: `alicebot.config.ConfigModel`

APScheduler 配置类，将在适配器被加载时被混入到机器人主配置中。

- **Attributes**

  - **scheduler\_config** (_dict\[str, typing.Any\]_) - 调度器配置。
