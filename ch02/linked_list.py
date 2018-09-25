from typing import Callable, Generic, List, Optional, TypeVar

T = TypeVar("T")


class LinkedList(Generic[T]):
    def __init__(self, *items: T) -> None:
        self._next: Optional[LinkedList[T]] = None
        self._value: Optional[T] = None
        if len(items) > 0:
            current = self
            current._value = items[0]
            for item in items[1:]:
                next_node = LinkedList[T](item)
                current._next = next_node
                current = next_node

    def for_each(self, func: Callable[[T], None]) -> None:
        current = self
        while current is not None:
            func(current._value)
            current = current._next

    def to_list(self) -> List[T]:
        out: List[T] = []
        self.for_each(out.append)
        return out

    def prepend(self, item: T): # -> LinkedList[T]: <= why doesn't this work?
        out = LinkedList[T](item)
        out._next = self
        return out

    def append(self, item: T): # -> LinkedList[T]: <= why doesn't this work?
        current = self
        while current._next is not None:
            current = current._next
        current._next = LinkedList[T](item)
        return self

    def tail(self): # -> Optional[LinkedList[T]]: <= why doesn't this work?
        return self._next

    def __str__(self):
        return str(self.to_list())

    def __len__(self):
        out = 0

        def increment(_: T) -> None:
            nonlocal out
            out += 1

        self.for_each(increment)
        return out
