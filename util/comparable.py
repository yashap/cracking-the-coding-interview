from typing import Any, TypeVar
from typing_extensions import Protocol
from abc import abstractmethod

T = TypeVar("T", bound="Comparable")


class Comparable(Protocol):
    @abstractmethod
    def __eq__(self, other: Any) -> bool:
        pass

    @abstractmethod
    def __lt__(self: T, other: T) -> bool:
        pass

    def __gt__(self: T, other: T) -> bool:
        return (not self < other) and self != other

    def __le__(self: T, other: T) -> bool:
        return self < other or self == other

    def __ge__(self: T, other: T) -> bool:
        return (not self < other)
