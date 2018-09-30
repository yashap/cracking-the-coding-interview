from typing import Any, Callable, Dict, Generic, List, Optional, Set, TypeVar, Union

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
        current_node: Optional[Node[T]] = self._head
        while current_node is not None:
            func(current_node.value())
            current_node = current_node.next()

    def to_list(self) -> List[T]:
        out: List[T] = []
        self.for_each(out.append)
        return out

    def is_empty(self) -> bool:
        return self._head is None

    def head(self) -> Optional[T]:
        return None if self._head is None else self._head.value()

    def tail(self) -> "Optional[LinkedList[T]]":
        if self._head is None:
            return None
        else:
            out: Optional[LinkedList[T]] = LinkedList()
            if out is not None:  # make mypy happy, even though this is impossible
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
        if index == 0 and self._head is not None:  # make mypy happy
            self._head = self._head.next()
        elif index > 0 and self._head is not None:  # handle deleting any item from index 1 onwards
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
            raise err
        else:
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

        def append_if_not_seen(item: T) -> None:
            nonlocal out
            if item not in seen:
                out.append(item)
                seen.add(item)

        self.for_each(append_if_not_seen)
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

        def add_to_partition(item: T) -> None:
            nonlocal below, above
            if left_is_smaller(item, value):  # TODO: pass in a function that does this comparison for any T
                below.append(item)
            else:
                above.append(item)

        self.for_each(add_to_partition)

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
        other_items: Set[T] = set(other.to_list())
        current_node: Optional[Node[T]] = self._head
        while current_node is not None:
            current_value = current_node.value()
            if current_value in other_items:
                return current_value
            current_node = current_node.next()
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
        seen: Dict[str, List[Node[T]]] = {}
        while current_node is not None:
            node_address: str = current_node.__repr__()
            seen_nodes: List[Node[T]] = seen.get(node_address, [])  # Almost for sure a list of length 0 or 1
            for node in seen_nodes:
                if node is current_node:
                    return True
            seen_nodes.append(current_node)
            seen[node_address] = seen_nodes
            current_node = current_node.next()
        return False

    def __str__(self) -> str:
        return "LinkedList({})".format(", ".join([str(v) for v in self.to_list()]))

    def __len__(self) -> int:
        out = 0

        def increment(_: T) -> None:
            nonlocal out
            out += 1

        self.for_each(increment)
        return out

    def __eq__(self, other: Any) -> bool:
        return other is not None and type(other) is LinkedList and self.to_list() == other.to_list()
