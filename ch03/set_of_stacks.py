from ch03.stack import Stack
from typing import Any, Generic, List, TypeVar
from copy import deepcopy

T = TypeVar("T")


class SetOfStacksIterator(Generic[T]):
    def __init__(self, stacks: "SetOfStacks[T]") -> None:
        self._stacks: SetOfStacks[T] = deepcopy(stacks)

    def __iter__(self) -> "SetOfStacksIterator[T]":
        return self

    def __next__(self) -> T:
        try:
            return self._stacks.pop()
        except IndexError:
            raise StopIteration()

# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple. Implement this
# with a set of stacks, where a new stack gets created past some max size. The public API should behave the same as a
# single stack
class SetOfStacks(Generic[T]):
    def __init__(self, max_stack_size: int, items: List[T] = []) -> None:
        if max_stack_size < 1:
            raise ValueError("illegal max_stack_size: {}".format(max_stack_size))
        if items == []:
            items = []  # avoid issues with mutable default args
        self._max_stack_size = max_stack_size
        self._stacks: Stack[Stack[T]] = Stack(Stack())
        self._remaining_space = max_stack_size
        for item in items:
            if self._remaining_space == 0:
                self._stacks.push(Stack())
                self._remaining_space = self._max_stack_size
            self._stacks.peek().push(item)
            self._remaining_space -= 1

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop on empty stack")
        else:
            item: T = self._stacks.peek().pop()
            if self._stacks.peek().is_empty():
                self._stacks.pop()
                if self._stacks.is_empty():
                    self._stacks = Stack(Stack())
            return item

    def peek(self) -> T:
        if self.is_empty() is None:
            raise IndexError("pop on empty stack")
        else:
            return self._stacks.peek().peek()

    def push(self, item: T) -> None:
        if self._remaining_space == 0:
            self._stacks.push(Stack())
            self._remaining_space = self._max_stack_size
        self._stacks.peek().push(item)
        self._remaining_space -= 1
        return

    def is_empty(self) -> bool:
        return self._stacks.peek().is_empty()

    def __str__(self) -> str:
        items = "" if self.is_empty() else ", [{}]".format(", ".join([str(v) for v in list(self)]))
        return "SetOfStacks({}{})".format(self._max_stack_size, items)

    def __len__(self) -> int:
        out = 0
        for _ in self:
            out += 1
        return out

    def __eq__(self, other: Any) -> bool:
        return (
            other is not None and
            type(other) is SetOfStacks and
            self._max_stack_size == other._max_stack_size and
            list(self) == list(other)
        )

    def __iter__(self) -> SetOfStacksIterator[T]:
        return SetOfStacksIterator[T](self)
