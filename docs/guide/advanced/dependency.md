# 依赖注入

AliceBot 提供了一套简单易用的依赖注入系统。

## 什么是依赖注入？

简单来说，依赖注入 (Dependency Injection，DI) 是实现控制反转 (Inversion of Control，IoC) 的一种方法。这意味着你只需要在使用依赖注入的类上声明所需要的依赖项即可直接使用，而不需要手动处理依赖项的初始化、子依赖嵌套等问题，这些将由 AliceBot 自动处理。

这听起来可能有些抽象，让我们从一个例子开始。

想象这样一个场景，我们需要实现一个权限管理功能，很显然这是一个许多插件都需要使用的功能。最显而易见的解决方案是创建一个名为 `PermissionPlugin` 的插件公用基类，里面定义了类似 `is_admin()` 这样的方法，就像这样。

```python
from abc import ABC

from alicebot import Plugin


class PermissionPlugin(Plugin, ABC):
    def is_admin(self):
        ...


class TestPlugin(PermissionPlugin):
    ...

```

AliceBot 对这种解决方案提供了支持，对于**显式**继承自 `abc.ABC` 的插件类，无论它实际上是否是抽象的，AliceBot 都将不会把它作为一个插件加载。

但是，这是一个比较简单的例子，当项目的规模变大，实际上我们的插件很可能会依赖许多通用的功能。这时候，即使 Python 支持多继承，继承似乎也并不是一个优雅的解决方案了。或许你想到了设计模式中的一个说法：“组合优于继承”。于是，我们可以改造一下之前的设计，提供一个单独 `Permission` 类。

```python
from alicebot import Event, Plugin


class Permission:
    def __init__(self, event: Event):
        self.event = event

    def is_admin(self) -> bool:
        ...


class TestPlugin(Plugin):
    def __init__(self) -> None:
        self.permission = Permission(self.event)

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

这里也有几个细节值得注意，首先，对于插件类的 `__init__()` 方法无需添加 `super().__init__()`。其次，你可能注意到了，我们直接在 `__init__()` 方法中使用了 `self.event`。等一下，`__init__()` 中居然就可以使用，插件类的 `event` 属性是什么时候被设置的呢？这个问题涉及 AliceBot 依赖注入机制的具体实现，这里暂时先不展开了。你只需要知道，`Plugin` 类的 `event` 属性就是使用依赖注入设置的，依赖注入的属性会在 `__init__()` 方法之前就被设置。

现在我们的实现还没有用到依赖注入。那么，现在的解决方案还有什么问题呢？让我们继续扩展刚才的例子。连接数据库的功能也是插件很常用的一个功能，而不仅我们的插件需要连接数据库，权限管理功能也需要连接数据库来进行权限认证。

现在，我们的例子就会变成这样。

```python
from alicebot import Event, Plugin


class Database:
    def __init__(self) -> None:
        ...

    def connect(self) -> DBSession:
        ...

    def close(self):
        ...


class Permission:
    def __init__(self, event: Event, database: Database):
        self.event = event
        self.database = database

    def is_admin(self) -> bool:
        ...


class TestPlugin(Plugin):
    def __init__(self) -> None:
        self.database = Database()
        self.permission = Permission(self.event, self.database)

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

这样写当然没什么问题，不过似乎略显麻烦，`__init__()` 方法中充斥了重复的对象初始化和设置。这还只是两个的情况，如果依赖项的数量变得更多或者子依赖关系变得更加复杂，那么编写 `__init__()` 方法会变得十分麻烦。并且一旦修改一个依赖，就需要修改所有涉及它的对象初始化部分。

除此之外，对于我们现在的例子来说，数据库会话 (session) 也很难进行有效的共享。在 `Permission` 和 `TestPlugin` 中需要分别产生新的会话，使用完再分别关闭，这显然是低效的。如果需要共享会话，那又需要添加新的代码，还要手动保证会话在任何情况下都被关闭了，防止出现资源泄露。

好麻烦啊！不过不用担心，是时候让 AliceBot 提供的依赖注入系统派上用场了。

## 依赖项

还是让我们从一个例子开始。

```python {13-16}
from alicebot import Plugin, Depends


class DepA:
    ...


class DepB:
    ...


class TestPlugin(Plugin):
    a: DepA = Depends()
    b: DepB = Depends()
    # a = Depends(DepA)
    # b = Depends(DepB)

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

现在，魔法发生了。你可以像这样直接在类上定义一个子依赖项，之后 AliceBot 就会自动完成它们的初始化工作，你会得到 `DepA` 类和 `DepB` 类的对象。

下面被注释的代码的效果也是完全一样的，只是写法不一样罢了。

不过现在的这个例子还太过简单，无法体现出依赖注入的方便之处。

## 子依赖项

```python {9,13-14,17}
from alicebot import Plugin, Depends


class DepA:
    ...


class DepB:
    a: DepA = Depends()


class TestPlugin(Plugin):
    a: DepA = Depends()
    b: DepB = Depends()

    async def handle(self) -> None:
        assert self.a is self.b.a

    async def rule(self) -> bool:
        ...

```

现在，`DepB` 和 `TestPlugin` 都依赖了 `DepA`，AliceBot 将自动处理它们之间的依赖关系。

AliceBot 支持创建含子依赖项的依赖项，并且支持任意深度的嵌套层级。

此外，AliceBot 会对处理过的依赖项进行“缓存”，在不同的依赖项中使用相同的子依赖项并不会创建多次实例，就像上面的两个 `DepA` 的实例是相同的。

如果确实有需要重复实例化多个相同子依赖的话，`Depends()` 有一个 `use_cache` 参数，你可以把它设为 `False`，就像这样：`Depends(use_cache=False)`。

## 特殊的依赖注入

除了支持对用户自己创建的依赖项进行依赖注入，AliceBot 特别支持了一些内置对象的依赖注入。分别是 `Event` 和 `Bot`，它们分别代表当前正在处理的事件和当前的机器人对象。对于 `Plugin` 来说 `Event` 是被默认注入的。

```python {5-6}
from alicebot import Plugin, Depends


class DepA:
    event: Event = Depends()
    bot: Bot = Depends()


class TestPlugin(Plugin):
    a: DepA = Depends()

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

现在我们就可以将开头的例子改造为使用依赖注入的版本了。

```python {16-17,24-25}
from alicebot import Event, Plugin, Depends


class Database:
    def __init__(self) -> None:
        ...

    def connect(self) -> DBSession:
        ...

    def close(self):
        ...


class Permission:
    event: Event = Depends()
    database: Database = Depends()

    def is_admin(self) -> bool:
        ...


class TestPlugin(Plugin):
    database: Database = Depends()
    permission: Permission = Depends()

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

变得简单了，如果依赖项更多的话会更明显。然而我们目前还没有处理一个问题，那就是会话的共享和上下文管理。会话的共享确实可以通过子依赖的缓存机制处理，但上下文管理，或者说会话的关闭该怎么办呢？

## 上下文管理

AliceBot 的依赖注入支持上下文管理。

上下文管理你应该不陌生，它对应着 Python 的 `with` 和 `async with` 语法，如果你不熟悉这个语法，建议先了解一下，可以参考 [contextlib](https://docs.python.org/zh-cn/3/library/contextlib.html)、[with 语句上下文管理器](https://docs.python.org/zh-cn/3/reference/datamodel.html#context-managers)、[异步上下文管理器](https://docs.python.org/zh-cn/3/reference/datamodel.html#asynchronous-context-managers)或者其他教程。

如果一个子依赖项是一个“上下文管理器类型”，那么 AliceBot 将自动管理这个依赖项的的上下文，即在实例化后自动执行 `__enter__()` 并在结束后自动执行 `__exit__()`。

```python
from alicebot import Event, Plugin, Depends


class Database:
    async def __aenter__(self) -> Database:
        self.session = DBSession()
        return self

    async def __aexit__(self, __exc_type, __exc_value, __traceback) -> bool:
        self.session.close()
        return False


class Permission:
    event: Event = Depends()
    database: Database = Depends()

    def is_admin(self) -> bool:
        ...


class TestPlugin(Plugin):
    database: Database = Depends()
    permission: Permission = Depends()

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

现在，`Database` 依赖项自动进行上下文管理，它将在 `Permission` 和 `TestPlugin` 之间共享会话，并且会在这个插件的生命周期结束后自动结束会话。

你可能注意到，这里我们用的是 `__aenter__()` 和 `__aexit__()` 而不是 `__enter__()` 和 `__exit__()`，其实，AliceBot 同时同步和异步的上下文管理器，你可以根据需要任意选用。

此外，你也可以直接让 `__aenter__()` 返回 `DBSession` 对象，不过这种情况下，使用依赖的时候就不能用类型注解的形式了，虽然运行起来没有区别，但是这样的类型注解是不正确的。

```python {5,7,15}
from alicebot import Plugin, Depends


class Database:
    async def __aenter__(self) -> DBSession:
        self.session = DBSession()
        return self.session

    async def __aexit__(self, __exc_type, __exc_value, __traceback) -> bool:
        self.session.close()
        return False


class TestPlugin(Plugin):
    session = Depends(Database)
    # 这里也可以显式标注 session 的类型为 DBSession
    # 不过即使不标注，类型检查工具也能推断出 session 的类型

    # session: Database = Depends()
    # 类型注解的形式
    # 虽然和上面的运行起来是等效的，但是这里的类型注解是错误的！

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

## 使用生成器的的上下文管理

除了上面提到的将依赖项设置为上下文管理器之外，AliceBot 还支持一种更加简单的上下文管理方法。

你可以直接把一个生成器 (generator) 或者异步生成器 (async generator) 作为依赖项。

其实就是写一个普通的函数 (函数或者协程都可以)，但是要把 `return` 换成 `yield`，并把额外的步骤 (比如关闭会话) 写在 `yield` 后面。

```python
from typing import AsyncGenerator


async def get_db() -> AsyncGenerator[DBSession, None]:
    session = DBSession()
    try:
        yield session
    finally:
        session.close()
```

使用依赖时只需要像普通依赖一样就可以，类型推断会自动推断出 `session` 属性的类型是 `DBSession`。

```python
from alicebot import Plugin, Depends

class TestPlugin(Plugin):
    session = Depends(get_db)

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```

如果你想要使用的数据本身已经支持上下文管理了，比如 `aiohttp` 的 `ClientSession`，也可以像下面这样写，实现在不同依赖项中共享一个 `ClientSession`。

```python
from typing import AsyncGenerator

import aiohttp


async def get_client() -> AsyncGenerator[aiohttp.ClientSession, None]:
    try:
        async with aiohttp.ClientSession() as session:
            yield session
    finally:
        # 在这里进行其他额外工作
        # 如果没有额外工作的话这里的 try...finally 是不需要的
        ...

```

要注意生成器只能有一次 `yield`！这是由于对生成器上下文管理的支持本质上是用 [asynccontextmanager](https://docs.python.org/zh-cn/3/library/contextlib.html#contextlib.asynccontextmanager) 实现的，你可以参阅它的文档获取更多信息。

最后，让我们完成开始的示例吧！

```python
from alicebot import Event, Plugin, Depends


async def get_db():
    session = DBSession()
    try:
        yield session
    finally:
        session.close()


class Permission:
    event: Event = Depends()
    session = Depends(get_db)

    def is_admin(self) -> bool:
        ...


class TestPlugin(Plugin):
    session = Depends(get_db)
    permission: Permission = Depends()

    async def handle(self) -> None:
        ...

    async def rule(self) -> bool:
        ...

```
