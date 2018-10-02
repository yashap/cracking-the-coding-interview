from ch03.queue import Queue
import pytest


def test_iter():
    ll_iter = Queue(10, 11, 12).__iter__()
    assert ll_iter.__next__() == 10
    assert ll_iter.__next__() == 11
    assert ll_iter.__next__() == 12
    with pytest.raises(StopIteration):
        ll_iter.__next__()
    with pytest.raises(StopIteration):
        ll_iter.__next__()


def test_to_list():
    assert list(Queue(10, 11, 12)) == [10, 11, 12]


def test_to_str():
    assert str(Queue()) == "Queue()"
    assert str(Queue(10)) == "Queue(10)"
    assert str(Queue(10, 11)) == "Queue(10, 11)"


def test_len():
    assert len(Queue(10, 11, 12, 13)) == 4


def test_eq():
    assert Queue(10, 11, 12, 13) == Queue(10, 11, 12, 13)
    assert Queue() == Queue()
    assert Queue() != Queue(10)
    assert Queue(10, 11, 12, 13) != Queue(10, 11, 12)
    assert Queue(10, 11, 12, 13) != Queue(11, 12, 13)
    assert Queue() != []
    assert Queue() is not None


def test_is_empty():
    assert Queue(10, 11, 12).is_empty() is False
    assert Queue(10).is_empty() is False
    assert Queue().is_empty() is True


def test_add():
    queue = Queue[int]()
    queue.add(10)
    queue.add(11)
    queue.add(12)
    assert queue == Queue(10, 11, 12)


def test_remove():
    queue = Queue[int]()
    with pytest.raises(IndexError):
        queue.remove()
    queue.add(10)
    queue.add(11)
    queue.add(12)
    assert queue.remove() == 10
    assert queue.remove() == 11
    assert queue.remove() == 12
    with pytest.raises(IndexError):
        queue.remove()
    with pytest.raises(IndexError):
        queue.remove()


def test_peek():
    queue = Queue[int]()
    with pytest.raises(IndexError):
        queue.peek()
    queue.add(10)
    queue.add(11)
    queue.add(12)
    assert queue.peek() == 10
    assert queue.peek() == 10
