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
