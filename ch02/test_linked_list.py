from ch02.linked_list import LinkedList
import pytest


def test_iter():
    ll_iter = LinkedList(10, 11, 12).__iter__()
    assert ll_iter.__next__() == 10
    assert ll_iter.__next__() == 11
    assert ll_iter.__next__() == 12
    with pytest.raises(StopIteration):
        ll_iter.__next__()
    with pytest.raises(StopIteration):
        ll_iter.__next__()


def test_to_list():
    assert list(LinkedList(10, 11, 12)) == [10, 11, 12]


def test_to_str():
    assert str(LinkedList()) == "LinkedList()"
    assert str(LinkedList(10)) == "LinkedList(10)"
    assert str(LinkedList(10, 11)) == "LinkedList(10, 11)"


def test_len():
    assert len(LinkedList(10, 11, 12, 13)) == 4


def test_eq():
    assert LinkedList(10, 11, 12, 13) == LinkedList(10, 11, 12, 13)
    assert LinkedList() == LinkedList()
    assert LinkedList() != LinkedList(10)
    assert LinkedList(10, 11, 12, 13) != LinkedList(10, 11, 12)
    assert LinkedList(10, 11, 12, 13) != LinkedList(11, 12, 13)
    assert LinkedList() != []
    assert LinkedList() is not None


def test_head():
    assert LinkedList(10, 11, 12).head() == 10
    assert LinkedList(10).head() == 10
    assert LinkedList().head() is None


def test_tail():
    assert LinkedList(10, 11, 12).tail() == LinkedList(11, 12)
    assert LinkedList(10).tail() == LinkedList()
    assert LinkedList().tail() is None


def test_is_empty():
    assert LinkedList(10, 11, 12).is_empty() is False
    assert LinkedList(10).is_empty() is False
    assert LinkedList().is_empty() is True


def test_append():
    ll = LinkedList()
    assert ll.append(3) == LinkedList(3)
    assert ll.append(4) == LinkedList(3, 4)
    assert ll.append(5) == LinkedList(3, 4, 5)
    ll.append(6)
    assert ll == LinkedList(3, 4, 5, 6)


def test_prepend():
    ll = LinkedList()
    assert ll.prepend(3) == LinkedList(3)
    assert ll.prepend(4) == LinkedList(4, 3)
    assert ll.prepend(5) == LinkedList(5, 4, 3)
    ll.prepend(6)
    assert ll == LinkedList(6, 5, 4, 3)


def test_get():
    assert LinkedList(10, 11, 12, 13, 14, 15).get(0) == 10
    assert LinkedList(10, 11, 12, 13, 14, 15).get(1) == 11
    assert LinkedList(10, 11, 12, 13, 14, 15).get(2) == 12
    assert LinkedList(10, 11, 12, 13, 14, 15).get(5) == 15
    assert LinkedList(10, 11, 12, 13, 14, 15).get(6) is None
    assert LinkedList(10, 11, 12, 13, 14, 15).get(7) is None
    assert LinkedList().get(0) is None
    assert LinkedList().get(1) is None
    assert LinkedList(10).get(0) == 10
    assert LinkedList(10).get(1) is None


def test_get_kth_to_last():
    assert LinkedList(10, 11, 12, 13, 14, 15).get_kth_to_last(0) == 15
    assert LinkedList(10, 11, 12, 13, 14, 15).get_kth_to_last(1) == 14
    assert LinkedList(10, 11, 12, 13, 14, 15).get_kth_to_last(2) == 13
    assert LinkedList(10, 11, 12, 13, 14, 15).get_kth_to_last(5) == 10
    assert LinkedList(10, 11, 12, 13, 14, 15).get_kth_to_last(6) is None
    assert LinkedList(10, 11, 12, 13, 14, 15).get_kth_to_last(7) is None
    assert LinkedList().get_kth_to_last(0) is None
    assert LinkedList().get_kth_to_last(1) is None
    assert LinkedList(10).get_kth_to_last(0) == 10
    assert LinkedList(10).get_kth_to_last(1) is None


def test_delete():
    ll = LinkedList(10, 11, 12, 13, 14, 15)
    ll.delete(0)
    assert ll == LinkedList(11, 12, 13, 14, 15)
    ll.delete(4)
    assert ll == LinkedList(11, 12, 13, 14)
    ll.delete(2)
    assert ll == LinkedList(11, 12, 14)
    ll.delete(1)
    assert ll == LinkedList(11, 14)
    ll.delete(1)
    assert ll == LinkedList(11)
    ll.delete(0)
    assert ll == LinkedList()


def test_delete_out_of_bounds():
    with pytest.raises(IndexError):
        LinkedList().delete(0)
    with pytest.raises(IndexError):
        LinkedList(10).delete(-1)
    with pytest.raises(IndexError):
        LinkedList().delete(1)
    with pytest.raises(IndexError):
        LinkedList(10).delete(1)
    with pytest.raises(IndexError):
        LinkedList(10, 11).delete(2)


def test_distinct():
    assert LinkedList(10, 11, 12, 13, 12, 15).distinct() == LinkedList(10, 11, 12, 13, 15)
    assert LinkedList().distinct() == LinkedList()
    assert LinkedList(10).distinct() == LinkedList(10)
    assert LinkedList(10, 11).distinct() == LinkedList(10, 11)
    assert LinkedList(10, 10).distinct() == LinkedList(10)
    assert LinkedList(10, 10, 11, 10, 10, 10).distinct() == LinkedList(10, 11)


def test_partition():
    assert LinkedList(10, 8, 6, 7, 11, 5).partition(10, lambda l, r: l < r) == LinkedList(8, 6, 7, 5, 10, 11)
    assert LinkedList[int]().partition(10, lambda l, r: l < r) == LinkedList[int]()
    assert LinkedList(10).partition(10, lambda l, r: l < r) == LinkedList(10)
    assert LinkedList(5, 10, 15).partition(5, lambda l, r: l < r) == LinkedList(5, 10, 15)
    assert LinkedList(5, 10, 15).partition(10, lambda l, r: l < r) == LinkedList(5, 10, 15)
    assert LinkedList(5, 10, 15).partition(15, lambda l, r: l < r) == LinkedList(5, 10, 15)
    assert LinkedList(15, 10, 5).partition(11, lambda l, r: l < r) == LinkedList(10, 5, 15)


def test_is_palindrome():
    assert LinkedList().is_palindrome() is True
    assert LinkedList(10).is_palindrome() is True
    assert LinkedList(10, 10).is_palindrome() is True
    assert LinkedList(10, 11).is_palindrome() is False
    assert LinkedList(10, 11, 10).is_palindrome() is True
    assert LinkedList(10, 11, 11, 10).is_palindrome() is True
    assert LinkedList(10, 11, 0, 11, 10).is_palindrome() is True


def test_intersects_with():
    assert LinkedList(10, 11, 12).intersects_with(LinkedList(8, 11)) == 11
    assert LinkedList(10, 11, 12).intersects_with(LinkedList(8, 9)) is None
    assert LinkedList(10, 11, 12).intersects_with(LinkedList(11)) == 11
    assert LinkedList(10, 11, 12).intersects_with(LinkedList()) is None
    assert LinkedList().intersects_with(LinkedList()) is None
    assert LinkedList().intersects_with(LinkedList(10, 11)) is None


def test_has_loop():
    assert LinkedList().has_loop() is False
    assert LinkedList(10).has_loop() is False
    assert LinkedList(10, 11, 10).has_loop() is False

    ll = LinkedList(10, 11, 12)
    first_node = ll._get_node(0)
    last_node = ll._get_node(2)
    last_node.set_next(first_node)
    assert ll.has_loop() is True

    ll = LinkedList(10, 11, 12, 13, 14)
    second_node = ll._get_node(1)
    second_last_node = ll._get_node(3)
    second_last_node.set_next(second_node)
    assert ll.has_loop() is True
