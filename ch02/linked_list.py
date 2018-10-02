from ch02.node import Node
from typing import Any, Callable, Generic, Optional, Set, TypeVar

T = TypeVar("T")


class LinkedListIterator(Generic[T]):
    def __init__(self, node: Optional[Node[T]]) -> None:
        self._current_node: Optional[Node[T]] = node

    def __iter__(self) -> "LinkedListIterator[T]":
        return self

    def __next__(self) -> T:
        if self._current_node is None:
            raise StopIteration()
        else:
            current_value = self._current_node.value()
            self._current_node = self._current_node.next()
            return current_value


class LinkedList(Generic[T]):
    def __init__(self, *items: T) -> None:
        self._head: Optional[Node[T]] = None
        if len(items) > 0:
            self._head = Node(items[0])
            current_node = self._head
            for item in items[1:]:
                next_node = Node(item)
                current_node.set_next(next_node)
                current_node = next_node

    def for_each(self, func: Callable[[T], None]) -> None:
        for node_value in self:
            func(node_value)

    def is_empty(self) -> bool:
        return self._head is None

    def head(self) -> Optional[T]:
        return None if self._head is None else self._head.value()

    def tail(self) -> "Optional[LinkedList[T]]":
        if self._head is None:
            return None
        else:
            out = LinkedList[T]()
            out._head = self._head.next()
            return out

    def prepend(self, item: T) -> "LinkedList[T]":
        current_head: Optional[Node[T]] = self._head
        if current_head is None:
            self._head = Node(item)
        else:
            new_head = Node(item)
            new_head.set_next(current_head)
            self._head = new_head
        return self

    def append(self, item: T) -> "LinkedList[T]":
        if self.is_empty():
            self._head = Node(item)
        else:
            last_node: Optional[Node[T]] = self._get_node(len(self) - 1)
            if last_node is not None:
                last_node.set_next(Node(item))
        return self

    def delete(self, index: int) -> None:
        err = IndexError("index out of bounds")
        if index == 0 and self._head is not None:  # delete first item, if there is one
            self._head = self._head.next()
        elif index > 0 and self._head is not None:  # delete any item from index 1 onwards
            current_index = 1
            prev_node: Node[T] = self._head
            current_node: Optional[Node[T]] = self._head.next()
            while current_node is not None:
                if current_index == index:
                    prev_node.set_next(current_node.next())
                    return
                prev_node = current_node
                current_node = current_node.next()
                current_index += 1
            raise err  # tried to delete index higher than exists
        else:  # tried to delete from empty list, or tried to delete negative index
            raise err

    def _get_node(self, index: int) -> Optional[Node[T]]:
        current_node: Optional[Node[T]] = self._head
        current_index = 0
        while current_node is not None:
            if index == current_index:
                return current_node
            current_node = current_node.next()
            current_index += 1
        return None

    def get(self, index: int) -> Optional[T]:
        node: Optional[Node[T]] = self._get_node(index)
        return None if node is None else node.value()

    # Write code to remove duplicates from an unsorted linked list.
    def distinct(self) -> "LinkedList[T]":
        seen: Set[T] = set()
        out: LinkedList[T] = LinkedList()
        for node_value in self:
            if node_value not in seen:
                out.append(node_value)
                seen.add(node_value)
        return out

    # Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.
    def get_kth_to_last(self, k: int) -> Optional[T]:
        return self.get(len(self) - 1 - k)

    # Partition: Write code to partition a linked list around a value x, such that all nodes less than x come before all
    # nodes greater than or equal to x. If x is contained within the list, the values of x only need to be after the
    # elements less than x (see below). The partition element x can appear anywhere in the "right partition"; it does
    # not need to appear between the left and right partitions.
    def partition(self, value: T, left_is_smaller: Callable[[T, T], bool]) -> "LinkedList[T]":
        below: LinkedList[T] = LinkedList()
        above: LinkedList[T] = LinkedList()
        for node_value in self:
            if left_is_smaller(node_value, value):
                below.append(node_value)
            else:
                above.append(node_value)
        final_below_node: Optional[Node[T]] = below._get_node(len(below) - 1)
        first_above_node: Optional[Node[T]] = above._get_node(0)
        if final_below_node is not None and first_above_node is not None:
            final_below_node.set_next(first_above_node)
            self._head = below._head
        return self

    # Palindrome: Implement a function to check if a linked list is a palindrome
    def is_palindrome(self) -> bool:
        left = 0
        right = len(self) - 1
        while left < right:
            if self.get(left) != self.get(right):
                return False
            left += 1
            right -= 1
        return True

    # Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting node.
    def intersects_with(self, other: "LinkedList[T]") -> Optional[T]:
        other_node_values: Set[T] = set(other)
        for node_value in self:
            if node_value in other_node_values:
                return node_value
        return None

    # Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the beginning of the
    # loop.
    #
    # DEFINITION
    # Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so as to
    # make a loop in the linked list.
    #
    # EXAMPLE
    # Input: A -> B -> C -> D -> E -> C [the same C as earlier]
    # Output: C
    def has_loop(self) -> bool:
        current_node: Optional[Node[T]] = self._head
        seen: Set[Node[T]] = set()
        while current_node is not None:
            if current_node in seen:
                return True
            else:
                seen.add(current_node)
                current_node = current_node.next()
        return False

    def __str__(self) -> str:
        return "LinkedList({})".format(", ".join([str(v) for v in list(self)]))

    def __len__(self) -> int:
        out = 0
        for _ in self:
            out += 1
        return out

    def __eq__(self, other: Any) -> bool:
        return other is not None and type(other) is LinkedList and list(self) == list(other)

    def __iter__(self) -> LinkedListIterator[T]:
        return LinkedListIterator[T](self._head)
