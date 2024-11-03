# alicebot.utils

AliceBot 内部使用的实用工具。

## _class_ `ModulePathFinder` {#ModulePathFinder}

Bases: `importlib.abc.MetaPathFinder`

用于查找 AliceBot 组件的元路径查找器。

- **Attributes**

  - **path** (_ClassVar\[list\[str\]\]_)

### _method_ `find_spec(self, fullname, path = None, target = None)` {#ModulePathFinder-find-spec}

用于查找指定模块的 `spec`。

- **Arguments**

  - **fullname** (_str_)

  - **path** (_Optional\[collections.abc.Sequence\[str\]\]_)

  - **target** (_Optional\[module\]_)

- **Returns**

  Type: _Optional\[\_frozen\_importlib.ModuleSpec\]_

## _function_ `is_config_class(config_class)` {#is-config-class}

判断一个对象是否是配置类。

- **Arguments**

  - **config\_class** (_Any_) - 待判断的对象。

- **Returns**

  Type: _TypeGuard\[type\[alicebot.config.ConfigModel\]\]_

  返回是否是配置类。

## _function_ `get_classes_from_module(module, super_class)` {#get-classes-from-module}

从模块中查找指定类型的类。

- **Arguments**

  - **module** (_module_) - Python 模块。

  - **super\_class** (_~\_TypeT_) - 要查找的类的超类。

- **Returns**

  Type: _list\[~\_TypeT\]_

  返回符合条件的类的列表。

## _function_ `get_classes_from_module_name(name, super_class, *, reload = False)` {#get-classes-from-module-name}

从指定名称的模块中查找指定类型的类。

- **Arguments**

  - **name** (_str_) - 模块名称，格式和 Python `import` 语句相同。

  - **super\_class** (_~\_TypeT_) - 要查找的类的超类。

  - **reload** (_bool_) - 是否重新加载模块。

- **Returns**

  Type: _list\[tuple\[~\_TypeT, module\]\]_

  返回由符合条件的类和模块组成的元组的列表。

- **Raises**

  - **ImportError** - 当导入模块过程中出现错误。

## _class_ `PydanticEncoder` {#PydanticEncoder}

Bases: `json.encoder.JSONEncoder`

用于解析 `pydantic.BaseModel` 的 `JSONEncoder` 类。

### _method_ `default(self, o)` {#PydanticEncoder-default}

Implement this method in a subclass such that it returns

a serializable object for ``o``, or calls the base implementation
(to raise a ``TypeError``).

For example, to support arbitrary iterators, you could
implement default like this::

    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        # Let the base class default method raise the TypeError
        return super().default(o)

- **Arguments**

  - **o** (_Any_)

- **Returns**

  Type: _Any_

## _function_ `samefile(path1, path2)` {#samefile}

一个 `os.path.samefile` 的简单包装。

- **Arguments**

  - **path1** (_Union\[str, bytes, PathLike\[str\], PathLike\[bytes\]\]_) - 路径1。

  - **path2** (_Union\[str, bytes, PathLike\[str\], PathLike\[bytes\]\]_) - 路径2。

- **Returns**

  Type: _bool_

  如果两个路径是否指向相同的文件或目录。

## _function_ `sync_func_wrapper(func, *, to_thread = False)` {#sync-func-wrapper}

包装一个同步函数为异步函数。

- **Arguments**

  - **func** (_Callable\[~\_P, ~\_R\]_) - 待包装的同步函数。

  - **to\_thread** (_bool_) - 是否在独立的线程中运行同步函数。默认为 `False`。

- **Returns**

  Type: _Callable\[~\_P, collections.abc.Coroutine\[None, None, ~\_R\]\]_

  异步函数。

## _function_ `sync_ctx_manager_wrapper(cm, *, to_thread = False)` {#sync-ctx-manager-wrapper}

将同步上下文管理器包装为异步上下文管理器。

- **Arguments**

  - **cm** (_contextlib.AbstractContextManager\[~\_T\]_) - 待包装的同步上下文管理器。

  - **to\_thread** (_bool_) - 是否在独立的线程中运行同步函数。默认为 `False`。

- **Returns**

  Type: _collections.abc.AsyncGenerator\[~\_T, None\]_

  异步上下文管理器。

## _function_ `wrap_get_func(func, *, event_type = None, adapter_type = None)` {#wrap-get-func}

将 `get()` 函数接受的参数包装为一个异步函数。

- **Arguments**

  - **func** (_Optional\[Callable\[\[~EventT\], Union\[bool, collections.abc.Awaitable\[bool\]\]\]\]_) - `get()` 函数接受的参数。

  - **event\_type** (_Optional\[type\['Event\[Any\]'\]\]_) - 事件类型。

  - **adapter\_type** (_Optional\[type\['Adapter\[Any, Any\]'\]\]_) - 适配器类型。

- **Returns**

  Type: _Callable\[\[~EventT\], collections.abc.Awaitable\[bool\]\]_

  异步函数。
