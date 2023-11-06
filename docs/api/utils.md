# alicebot.utils

AliceBot 内部使用的实用工具。

## _class_ `ModulePathFinder` {#ModulePathFinder}

Bases: `importlib.abc.MetaPathFinder`

用于查找 AliceBot 组件的元路径查找器。

- **Attributes**

  - **path** (_ClassVar\[List\[str\]\]_)

### _method_ `__init__(self, /, *args, **kwargs)` {#object.\_\_init\_\_}

Initialize self.  See help(type(self)) for accurate signature.

- **Arguments**

  - **args**

  - **kwargs**

### _method_ `find_spec(self, fullname, path = None, target = None)` {#ModulePathFinder.find\_spec}

用于查找指定模块的 `spec`。

- **Arguments**

  - **fullname** (_str_)

  - **path** (_Optional\[Sequence\[str\]\]_)

  - **target** (_Optional\[module\]_)

- **Returns**

  Type: _Optional\[\_frozen\_importlib.ModuleSpec\]_

## _function_ `is_config_class(config_class)` {#is\_config\_class}

判断一个对象是否是配置类。

- **Arguments**

  - **config\_class** (_Any_) - 待判断的对象。

- **Returns**

  Type: _typing\_extensions.TypeGuard\[typing.Type\[alicebot.config.ConfigModel\]\]_

  返回是否是配置类。

## _function_ `get_classes_from_module(module, super_class)` {#get\_classes\_from\_module}

从模块中查找指定类型的类。

- **Arguments**

  - **module** (_module_) - Python 模块。

  - **super\_class** (_~\_TypeT_) - 要查找的类的超类。

- **Returns**

  Type: _List\[~\_TypeT\]_

  返回符合条件的类的列表。

## _function_ `get_classes_from_module_name(name, super_class, *, reload = False)` {#get\_classes\_from\_module\_name}

从指定名称的模块中查找指定类型的类。

- **Arguments**

  - **name** (_str_) - 模块名称，格式和 Python `import` 语句相同。

  - **super\_class** (_~\_TypeT_) - 要查找的类的超类。

  - **reload** (_bool_) - 是否重新加载模块。

- **Returns**

  Type: _List\[Tuple\[~\_TypeT, module\]\]_

  返回由符合条件的类和模块组成的元组的列表。

- **Raises**

  - **ImportError** - 当导入模块过程中出现错误。

## _class_ `PydanticEncoder` {#PydanticEncoder}

Bases: `json.encoder.JSONEncoder`

用于解析 `pydantic.BaseModel` 的 `JSONEncoder` 类。

### _method_ `__init__(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None)` {#JSONEncoder.\_\_init\_\_}

Constructor for JSONEncoder, with sensible defaults.

If skipkeys is false, then it is a TypeError to attempt
encoding of keys that are not str, int, float or None.  If
skipkeys is True, such items are simply skipped.

If ensure_ascii is true, the output is guaranteed to be str
objects with all incoming non-ASCII characters escaped.  If
ensure_ascii is false, the output can contain non-ASCII characters.

If check_circular is true, then lists, dicts, and custom encoded
objects will be checked for circular references during encoding to
prevent an infinite recursion (which would cause an RecursionError).
Otherwise, no such check takes place.

If allow_nan is true, then NaN, Infinity, and -Infinity will be
encoded as such.  This behavior is not JSON specification compliant,
but is consistent with most JavaScript based encoders and decoders.
Otherwise, it will be a ValueError to encode such floats.

If sort_keys is true, then the output of dictionaries will be
sorted by key; this is useful for regression tests to ensure
that JSON serializations can be compared on a day-to-day basis.

If indent is a non-negative integer, then JSON array
elements and object members will be pretty-printed with that
indent level.  An indent level of 0 will only insert newlines.
None is the most compact representation.

If specified, separators should be an (item_separator, key_separator)
tuple.  The default is (', ', ': ') if *indent* is ``None`` and
(',', ': ') otherwise.  To get the most compact JSON representation,
you should specify (',', ':') to eliminate whitespace.

If specified, default is a function that gets called for objects
that can't otherwise be serialized.  It should return a JSON encodable
version of the object or raise a ``TypeError``.

- **Arguments**

  - **skipkeys**

  - **ensure\_ascii**

  - **check\_circular**

  - **allow\_nan**

  - **sort\_keys**

  - **indent**

  - **separators**

  - **default**

### _method_ `default(self, o)` {#PydanticEncoder.default}

返回 `o` 的可序列化对象。

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

## _function_ `sync_func_wrapper(func, *, to_thread = False)` {#sync\_func\_wrapper}

包装一个同步函数为异步函数。

- **Arguments**

  - **func** (_Callable\[\[~\_P\], ~\_R\]_) - 待包装的同步函数。

  - **to\_thread** (_bool_) - 是否在独立的线程中运行同步函数。默认为 `False`。

- **Returns**

  Type: _Callable\[\[~\_P\], Coroutine\[NoneType, NoneType, ~\_R\]\]_

  异步函数。

## _function_ `sync_ctx_manager_wrapper(cm, *, to_thread = False)` {#sync\_ctx\_manager\_wrapper}

将同步上下文管理器包装为异步上下文管理器。

- **Arguments**

  - **cm** (_ContextManager\[~\_T\]_) - 待包装的同步上下文管理器。

  - **to\_thread** (_bool_) - 是否在独立的线程中运行同步函数。默认为 `False`。

- **Returns**

  Type: _AsyncGenerator\[~\_T, NoneType\]_

  异步上下文管理器。

## _function_ `wrap_get_func(func)` {#wrap\_get\_func}

将 `get()` 函数接受的参数包装为一个异步函数。

- **Arguments**

  - **func** (_Optional\[Callable\[\[~EventT\], Union\[bool, Awaitable\[bool\]\]\]\]_) - `get()` 函数接受的参数。

- **Returns**

  Type: _Callable\[\[~EventT\], Awaitable\[bool\]\]_

  异步函数。

## _function_ `get_annotations(obj)` {#get\_annotations}

计算一个对象的标注字典。

- **Arguments**

  - **obj** (_Union\[Callable\[..., object\], Type\[Any\], module\]_) - 一个可调用对象、类或模块。

- **Returns**

  Type: _Dict\[str, Any\]_

  对象的标注字典。

- **Raises**

  - **TypeError** - `obj` 不是一个可调用对象、类或模块。

  - **ValueError** - 对象的 `__annotations__` 不是一个字典或 `None`。
