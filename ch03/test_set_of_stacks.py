from ch03.set_of_stacks import SetOfStacks
import pytest


def test_iter():
    ll_iter = SetOfStacks(2, [10, 11, 12]).__iter__()
    assert ll_iter.__next__() == 12
    assert ll_iter.__next__() == 11
    assert ll_iter.__next__() == 10
    with pytest.raises(StopIteration):
        ll_iter.__next__()
    with pytest.raises(StopIteration):
        ll_iter.__next__()


def test_to_list():
    assert list(SetOfStacks(2, [10, 11, 12])) == [12, 11, 10]


def test_to_str():
    assert str(SetOfStacks(2)) == "SetOfStacks(2)"
    assert str(SetOfStacks(2, [10])) == "SetOfStacks(2, [10])"
    assert str(SetOfStacks(2, [10, 11])) == "SetOfStacks(2, [11, 10])"


def test_len():
    assert len(SetOfStacks(5, [10, 11, 12, 13])) == 4


def test_eq():
    assert SetOfStacks(3, [10, 11, 12, 13]) == SetOfStacks(3, [10, 11, 12, 13])
    assert SetOfStacks(10) == SetOfStacks(10)
    # TODO: the rest
    assert SetOfStacks(2) != SetOfStacks(2, [10])
    assert SetOfStacks(2, [10, 11, 12, 13]) != SetOfStacks(2, [10, 11, 12])
    assert SetOfStacks(2, [10, 11, 12, 13]) != SetOfStacks(2, [11, 12, 13])
    assert SetOfStacks(2) != []
    assert SetOfStacks(2) is not None


def test_is_empty():
    assert SetOfStacks(2, [10, 11, 12]).is_empty() is False
    assert SetOfStacks(2, [10]).is_empty() is False
    assert SetOfStacks(2).is_empty() is True


def test_push():
    stack = SetOfStacks[int](2)
    stack.push(10)
    stack.push(11)
    stack.push(12)
    assert stack == SetOfStacks(2, [10, 11, 12])


def test_pop():
    stack = SetOfStacks[int](2)
    with pytest.raises(IndexError):
        stack.pop()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    assert stack.pop() == 12
    assert stack.pop() == 11
    assert stack.pop() == 10
    with pytest.raises(IndexError):
        stack.pop()
    with pytest.raises(IndexError):
        stack.pop()


def test_peek():
    stack = SetOfStacks[int](2)
    with pytest.raises(IndexError):
        stack.peek()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    assert stack.peek() == 12
    assert stack.peek() == 12
