import asyncio
import collections
from typing import Generic, Iterable, TypeVar, Optional

T_Node = TypeVar('T_Node', bound='LinkedQueueNode')


class LinkedQueue(Generic[T_Node]):
    """
    限定长度的链队列基类。
    """

    def __init__(self, max_len: Optional[int] = None,
                 next_alias: str = 'next'):
        self.max_len: Optional[int] = max_len
        self._next_alias: str = next_alias

        self._head: Optional[T_Node] = None
        self._rear: Optional[T_Node] = None
        self._len: int = 0

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterable[T_Node]:
        point = self._head
        while self._get_next(point) is not None:
            yield point
            point = self._get_next(point)
        yield point

    def _get_next(self, node: T_Node) -> Optional[T_Node]:
        return getattr(node, self._next_alias, None)

    def _set_next(self, node: T_Node, new_value: Optional[T_Node]):
        setattr(node, self._next_alias, new_value)

    def push(self, node: T_Node):
        if self._head is None:
            self._head = node
            self._rear = node
            self._len = 1
            return
        self._set_next(self._rear, node)
        self._rear = node
        self._len += 1
        while self._len > self.max_len:
            self.pop()

    def pop(self) -> T_Node:
        if self._head is None:
            raise ValueError('LinkedQueue is empty.')
        temp = self._head
        self._head = self._get_next(self._head)
        self._set_next(temp, None)
        if self._head is None:
            self._rear = None
        self._len -= 1
        return temp

    def top(self) -> Optional[T_Node]:
        return self._head

    def end(self) -> Optional[T_Node]:
        return self._rear

    def append(self, obj: T_Node):
        self.push(obj)

    def clear(self):
        self._head = None
        self._rear = None
        self._len = None


class Condition:
    """类似于 asyncio.Condition ，但允许在 notify() 时传递值，并由 wait() 返回。"""

    def __init__(self):
        self._loop = asyncio.get_event_loop()
        lock = asyncio.Lock(loop=self._loop)
        self._lock = lock
        # Export the lock's locked(), acquire() and release() methods.
        self.locked = lock.locked
        self.acquire = lock.acquire
        self.release = lock.release

        self._waiters = collections.deque()

    async def __aenter__(self):
        await self.acquire()
        # We have no use for the "as ..."  clause in the with
        # statement for locks.
        return None

    async def __aexit__(self, exc_type, exc, tb):
        self.release()

    def __repr__(self):
        res = super().__repr__()
        extra = 'locked' if self.locked() else 'unlocked'
        if self._waiters:
            extra = f'{extra}, waiters:{len(self._waiters)}'
        return f'<{res[1:-1]} [{extra}]>'

    async def wait(self):
        if not self.locked():
            raise RuntimeError('cannot wait on un-acquired lock')

        self.release()
        try:
            fut = self._loop.create_future()
            self._waiters.append(fut)
            try:
                return await fut
            finally:
                self._waiters.remove(fut)

        finally:
            # Must reacquire lock even if wait is cancelled
            cancelled = False
            while True:
                try:
                    await self.acquire()
                    break
                except asyncio.CancelledError:
                    cancelled = True

            if cancelled:
                raise asyncio.CancelledError

    async def wait_for(self, predicate):
        result = predicate()
        while not result:
            await self.wait()
            result = predicate()
        return result

    def notify(self, value=None, n=1):
        if not self.locked():
            raise RuntimeError('cannot notify on un-acquired lock')

        idx = 0
        for fut in self._waiters:
            if idx >= n:
                break

            if not fut.done():
                idx += 1
                fut.set_result(value)

    def notify_all(self, value=None):
        self.notify(value, len(self._waiters))
