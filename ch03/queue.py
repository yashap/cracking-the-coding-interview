from ch02.node import Node
from typing import Any, Generic, Optional, TypeVar

T = TypeVar("T")


class QueueIterator(Generic[T]):
    def __init__(self, node: Optional[Node[T]]) -> None:
        self._current_node: Optional[Node[T]] = node

    def __iter__(self) -> "QueueIterator[T]":
        return self

    def __next__(self) -> T:
        if self._current_node is None:
            raise StopIteration()
        else:
            current_value = self._current_node.value()
            self._current_node = self._current_node.next()
            return current_value


class Queue(Generic[T]):
    def __init__(self, *items: T) -> None:
        self._first: Optional[Node[T]] = None
        self._last: Optional[Node[T]] = None
        if len(items) > 0:
            self._first = Node(items[0])
            self._last = self._first
            current_node = self._first
            for item in items[1:]:
                next_node = Node(item)
                current_node.set_next(next_node)
                current_node = next_node
                self._last = current_node

    # Adds to the right side (i.e. last)
    def add(self, item: T) -> None:
        new_last = Node(item)
        if self._last is not None:
            self._last.set_next(new_last)
            self._last = new_last
        else:
            self._first = new_last
            self._last = new_last

    # Removes and returns from the left side (i.e. first)
    def remove(self) -> T:
        if self._first is None:
            raise IndexError("remove from empty queue")
        else:
            value = self._first.value()
            self._first = self._first.next()
            return value

    # Return from left side
    def peek(self) -> T:
        if self._first is None:
            raise IndexError("remove from empty queue")
        else:
            return self._first.value()

    def is_empty(self) -> bool:
        return self._first is None

    def __str__(self) -> str:
        return "Queue({})".format(", ".join([str(v) for v in list(self)]))

    def __len__(self) -> int:
        out = 0
        for _ in self:
            out += 1
        return out

    def __eq__(self, other: Any) -> bool:
        return other is not None and type(other) is Queue and list(self) == list(other)

    def __iter__(self) -> QueueIterator[T]:
        return QueueIterator[T](self._first)
