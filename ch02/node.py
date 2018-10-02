from typing import Generic, Optional, TypeVar

T = TypeVar("T")


class Node(Generic[T]):
    def __init__(self, value: T) -> None:
        self._next: Optional[Node[T]] = None
        self._value: T = value

    def value(self) -> T:
        return self._value

    def next(self) -> "Optional[Node[T]]":
        return self._next

    def set_next(self, next_node: "Optional[Node[T]]") -> None:
        self._next = next_node
