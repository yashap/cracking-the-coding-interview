from ch03.stack import Stack
import pytest


def test_iter():
    ll_iter = Stack(10, 11, 12).__iter__()
    assert ll_iter.__next__() == 12
    assert ll_iter.__next__() == 11
    assert ll_iter.__next__() == 10
    with pytest.raises(StopIteration):
        ll_iter.__next__()
    with pytest.raises(StopIteration):
        ll_iter.__next__()


def test_to_list():
    assert list(Stack(10, 11, 12)) == [12, 11, 10]


def test_to_str():
    assert str(Stack()) == "Stack()"
    assert str(Stack(10)) == "Stack(10)"
    assert str(Stack(10, 11)) == "Stack(11, 10)"


def test_len():
    assert len(Stack(10, 11, 12, 13)) == 4


def test_eq():
    assert Stack(10, 11, 12, 13) == Stack(10, 11, 12, 13)
    assert Stack() == Stack()
    assert Stack() != Stack(10)
    assert Stack(10, 11, 12, 13) != Stack(10, 11, 12)
    assert Stack(10, 11, 12, 13) != Stack(11, 12, 13)
    assert Stack() != []
    assert Stack() is not None


def test_is_empty():
    assert Stack(10, 11, 12).is_empty() is False
    assert Stack(10).is_empty() is False
    assert Stack().is_empty() is True


def test_push():
    stack = Stack[int]()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    assert stack == Stack(10, 11, 12)


def test_pop():
    stack = Stack[int]()
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
    stack = Stack[int]()
    with pytest.raises(IndexError):
        stack.peek()
    stack.push(10)
    stack.push(11)
    stack.push(12)
    assert stack.peek() == 12
    assert stack.peek() == 12


def test_sorted():
    assert Stack(10, 1, 5, 7).sorted() == Stack(1, 5, 7, 10)
    assert Stack(10, 1, 7, 5, 7).sorted() == Stack(1, 5, 7, 7, 10)
    assert Stack().sorted() == Stack()
    assert Stack(5).sorted() == Stack(5)
    assert Stack(5, 6).sorted() == Stack(5, 6)
    assert Stack(6, 5).sorted() == Stack(5, 6)


def test_sorted_does_not_mutate():
    stack = Stack(10, 1, 5, 7)
    stack.sorted()
    assert stack == Stack(10, 1, 5, 7)
