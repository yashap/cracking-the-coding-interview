from ch02.node import Node
from util.comparable import Comparable
from typing import Any, Generic, Optional, TypeVar
from copy import deepcopy

T = TypeVar("T", bound=Comparable)


class StackIterator(Generic[T]):
    def __init__(self, node: Optional[Node[T]]) -> None:
        self._current_node: Optional[Node[T]] = node

    def __iter__(self) -> "StackIterator[T]":
        return self

    def __next__(self) -> T:
        if self._current_node is None:
            raise StopIteration()
        else:
            current_value = self._current_node.value()
            self._current_node = self._current_node.next()
            return current_value


class Stack(Generic[T]):
    def __init__(self, *items: T) -> None:
        self._top: Optional[Node[T]] = None
        if len(items) > 0:
            current_top = Node(items[0])
            for item in items[1:]:
                next_top = Node[T](item)
                next_top.set_next(current_top)
                current_top = next_top
            self._top = current_top

    def pop(self) -> T:
        if self._top is None:
            raise IndexError("pop on empty stack")
        else:
            value = self._top.value()
            self._top = self._top.next()
            return value

    def peek(self) -> T:
        if self._top is None:
            raise IndexError("pop on empty stack")
        else:
            return self._top.value()

    def push(self, item: T) -> None:
        new_top = Node[T](item)
        new_top.set_next(self._top)
        self._top = new_top
        return

    def is_empty(self) -> bool:
        return self._top is None

    def sorted(self) -> "Stack[T]":
        stack = deepcopy(self)
        sorted_stack = Stack[T]()
        while not stack.is_empty():
            item = stack.pop()
            number_popped = 0
            while not sorted_stack.is_empty() and sorted_stack.peek() > item:
                stack.push(sorted_stack.pop())
                number_popped += 1
            sorted_stack.push(item)
            while number_popped > 0:
                sorted_stack.push(stack.pop())  # These items came from sorted_stack, so they're also sorted
                number_popped -= 1
        return sorted_stack

    def __str__(self) -> str:
        return "Stack({})".format(", ".join([str(v) for v in list(self)]))

    def __len__(self) -> int:
        out = 0
        for _ in self:
            out += 1
        return out

    def __eq__(self, other: Any) -> bool:
        return other is not None and type(other) is Stack and list(self) == list(other)

    def __iter__(self) -> StackIterator[T]:
        return StackIterator[T](self._top)
