# 钩子函数

AliceBot 提供了一些钩子函数，可以以装饰器的形式使用，使用方法如下：

```python
from alicebot import Bot

bot = Bot()


@bot.bot_run_hook
def hook_func(_bot: Bot):
    pass


if __name__ == '__main__':
    bot.run()

```

::: tip 注意
如果你不确定自己在干什么，请不要添加钩子函数。
:::

## Bot 相关钩子

### Bot 启动

```python
@bot.bot_run_hook
async def hook_func(_bot: Bot):
    pass
```

### Bot 退出

```python
@bot.bot_exit_hook
def hook_func(_bot: Bot):
    pass
```

::: warning 注意
只有这个钩子函数非协程！
:::

## 适配器相关钩子

### 适配器初始化

```python
@bot.adapter_startup_hook
async def hook_func(_adapter: 'T_Adapter'):
    pass
```

### 适配器运行

```python
@bot.adapter_run_hook
async def hook_func(_adapter: 'T_Adapter'):
    pass
```

### 适配器关闭

```python
@bot.adapter_shutdown_hook
async def hook_func(_adapter: 'T_Adapter'):
    pass
```

## 事件处理相关钩子

### 事件预处理

```python
@bot.event_preprocessor_hook
async def hook_func(_event: 'T_Event'):
    pass
```

### 事件后处理

```python
@bot.event_postprocessor_hook
async def hook_func(_event: 'T_Event'):
    pass
```