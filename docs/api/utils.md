# alicebot.utils

AliceBot 内部使用的实用工具。

## *class* `ModulePathFinder`(self, /, *args, **kwargs) {#ModulePathFinder}

Bases: `importlib.abc.MetaPathFinder`

用于查找 AliceBot 组件的元路径查找器。

- **Arguments**

  - **args**

  - **kwargs**

- **Attributes**

  - **path** (*List[str]*)

### *method* `find_spec(self, fullname, path = None, target = None)` {#ModulePathFinder.find_spec}

用于查找指定模块的 `spec`。

- **Arguments**

  - **fullname** (*str*)

  - **path** (*Optional[Sequence[str]]*)

  - **target** (*Optional[module]*)

## *function* `is_config_class(config_class)` {#is_config_class}

判断一个对象是否是配置类。

- **Arguments**

  - **config_class** (*Any*) - 待判断的对象。

- **Returns**

  Type: *TypeGuard[Type[alicebot.config.ConfigModel]]*

  返回是否是配置类。

## *function* `get_classes_from_module(module, super_class)` {#get_classes_from_module}

从模块中查找指定类型的类。

- **Arguments**

  - **module** (*module*) - Python 模块。

  - **super_class** (*Type[~_T]*) - 要查找的类的超类。

- **Returns**

  Type: *List[Type[~_T]]*

  返回符合条件的类的列表。

## *function* `get_classes_from_module_name(name, super_class)` {#get_classes_from_module_name}

从指定名称的模块中查找指定类型的类。

- **Arguments**

  - **name** (*str*) - 模块名称，格式和 Python `import` 语句相同。

  - **super_class** (*Type[~_T]*) - 要查找的类的超类。

- **Returns**

  Type: *List[Tuple[Type[~_T], module]]*

  返回由符合条件的类和模块组成的元组的列表。

- **Raises**

  - **ImportError** - 当导入模块过程中出现错误。

## *class* `DataclassEncoder`(self, *, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, sort_keys=False, indent=None, separators=None, default=None) {#DataclassEncoder}

Bases: `json.encoder.JSONEncoder`

用于解析 `MessageSegment` 的 `JSONEncoder` 类。

- **Arguments**

  - **skipkeys**

  - **ensure_ascii**

  - **check_circular**

  - **allow_nan**

  - **sort_keys**

  - **indent**

  - **separators**

  - **default**

### *method* `default(self, o)` {#DataclassEncoder.default}

返回 `o` 的可序列化对象。

- **Arguments**

  - **o** (*Any*)

- **Returns**

  Type: *Any*

## *function* `samefile(path1, path2)` {#samefile}

一个 `os.path.samefile` 的简单包装。

- **Arguments**

  - **path1** (*str*) - 路径1。

  - **path2** (*str*) - 路径2。

- **Returns**

  Type: *bool*

  如果两个路径是否指向相同的文件或目录。

## *function* `sync_func_wrapper(func, *, to_thread = False)` {#sync_func_wrapper}

包装一个同步函数为异步函数。

- **Arguments**

  - **func** (*Callable[~_P, ~_R]*) - 待包装的同步函数。

  - **to_thread** (*bool*) - 是否在独立的线程中运行同步函数。默认为 `False`。

- **Returns**

  Type: *Callable[~_P, Coroutine[NoneType, NoneType, ~_R]]*

  异步函数。

## *function* `sync_ctx_manager_wrapper(cm, *, to_thread = False)` {#sync_ctx_manager_wrapper}

将同步上下文管理器包装为异步上下文管理器。

- **Arguments**

  - **cm** (*ContextManager[~_T]*) - 待包装的同步上下文管理器。

  - **to_thread** (*bool*) - 是否在独立的线程中运行同步函数。默认为 `False`。

- **Returns**

  Type: *AsyncGenerator[~_T, NoneType]*

  异步上下文管理器。

## *function* `wrap_get_func(func)` {#wrap_get_func}

将 `get()` 函数接受的参数包装为一个异步函数。

- **Arguments**

  - **func** (*Optional[Callable[[~T_Event], Union[bool, Awaitable[bool]]]]*) - `get()` 函数接受的参数。

- **Returns**

  Type: *Callable[[~T_Event], Awaitable[bool]]*

  异步函数。

## *function* `get_annotations(obj, *, globals=None, locals=None, eval_str=False)` {#get_annotations}

Compute the annotations dict for an object.

obj may be a callable, class, or module.
Passing in an object of any other type raises TypeError.

Returns a dict.  get_annotations() returns a new dict every time
it's called; calling it twice on the same object will return two
different but equivalent dicts.

This function handles several details for you:

  * If eval_str is true, values of type str will
    be un-stringized using eval().  This is intended
    for use with stringized annotations
    ("from __future__ import annotations").
  * If obj doesn't have an annotations dict, returns an
    empty dict.  (Functions and methods always have an
    annotations dict; classes, modules, and other types of
    callables may not.)
  * Ignores inherited annotations on classes.  If a class
    doesn't have its own annotations dict, returns an empty dict.
  * All accesses to object members and dict values are done
    using getattr() and dict.get() for safety.
  * Always, always, always returns a freshly-created dict.

eval_str controls whether or not values of type str are replaced
with the result of calling eval() on those values:

  * If eval_str is true, eval() is called on values of type str.
  * If eval_str is false (the default), values of type str are unchanged.

globals and locals are passed in to eval(); see the documentation
for eval() for more information.  If either globals or locals is
None, this function may replace that value with a context-specific
default, contingent on type(obj):

  * If obj is a module, globals defaults to obj.__dict__.
  * If obj is a class, globals defaults to
    sys.modules[obj.__module__].__dict__ and locals
    defaults to the obj class namespace.
  * If obj is a callable, globals defaults to obj.__globals__,
    although if obj is a wrapped function (using
    functools.update_wrapper()) it is first unwrapped.

- **Arguments**

  - **obj**

  - **globals**

  - **locals**

  - **eval_str**