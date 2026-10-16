import numpy as np
import pytest

from my_deque import deque
from my_array import array
from my_list import list as my_list


# array

def array_addToTail():
    a = array(arraySize=4)
    a.addToTail(num=np.int32(1))
    a.addToTail(num=np.int32(2))
    a.addToTail(num=np.int32(3))
    assert a.accessByIndex(index=np.int32(0)) == 1
    assert a.accessByIndex(index=np.int32(1)) == 2
    assert a.accessByIndex(index=np.int32(2)) == 3
    assert a.size == 3


def array_grow():
    a = array(arraySize=2)
    for i in range(10):
        a.addToTail(num=np.int32(i))

    assert a.size == 10
    assert a.capacity == 16
    assert a.accessByIndex(index=np.int32(9)) == 9


def array_addByIndex():
    a = array(arraySize=4)
    a.addToTail(num=np.int32(1))
    a.addToTail(num=np.int32(3))
    a.addByIndex(num=np.int32(2), index=np.int32(1))
    assert a.accessByIndex(index=np.int32(0)) == 1
    assert a.accessByIndex(index=np.int32(1)) == 2
    assert a.accessByIndex(index=np.int32(2)) == 3


def array_removeByIndex():
    a = array(arraySize=4)
    for i in range(3):
        a.addToTail(num=np.int32(i))

    v = a.removeByIndex(index=np.int32(1))
    assert v == 1
    assert a.size == 2
    assert a.accessByIndex(index=np.int32(1)) == 2


def array_accessOutOfRange():
    a = array(arraySize=4)
    with pytest.raises(IndexError):
        a.accessByIndex(index=np.int32(0))


# list

def list_addToTail_and_access():
    l = my_list()
    for i in range(5):
        l.addToTail(num=np.int32(i))

    assert l.size == 5
    assert l.accessByIndex(index=np.int32(0)) == 0
    assert l.accessByIndex(index=np.int32(4)) == 4


def list_addToHead():
    l = my_list()
    l.addToTail(num=np.int32(2))
    l.addToHead(num=np.int32(1))
    assert l.accessByIndex(index=np.int32(0)) == 1
    assert l.accessByIndex(index=np.int32(1)) == 2


def list_addByIndex():
    l = my_list()
    l.addToTail(num=np.int32(1))
    l.addToTail(num=np.int32(3))
    l.addByIndex(num=np.int32(2), index=np.int32(1))
    assert l.accessByIndex(index=np.int32(0)) == 1
    assert l.accessByIndex(index=np.int32(1)) == 2
    assert l.accessByIndex(index=np.int32(2)) == 3


def list_removeByIndex():
    l = my_list()
    for i in range(4):
        l.addToTail(num=np.int32(i))

    v = l.removeByIndex(index=np.int32(0))
    assert v == 0
    assert l.size == 3
    assert l.accessByIndex(index=np.int32(0)) == 1


def list_bad_index():
    l = my_list()
    with pytest.raises(IndexError):
        l.accessByIndex(index=np.int32(0))


# deque

def deque_addToHead():
    d = deque(arraySize=10)
    d.addToHead(num=np.int32(1))
    d.addToHead(num=np.int32(2))
    assert d.accessByIndex(index=np.int32(0)) == 2
    assert d.accessByIndex(index=np.int32(1)) == 1


def deque_addToTail():
    d = deque(arraySize=10)
    d.addToTail(num=np.int32(3))
    d.addToTail(num=np.int32(4))
    assert d.accessByIndex(index=np.int32(0)) == 3
    assert d.accessByIndex(index=np.int32(1)) == 4


def deque_both_ends():
    d = deque(arraySize=10)
    d.addToHead(num=np.int32(2))
    d.addToTail(num=np.int32(3))
    d.addToHead(num=np.int32(1))
    d.addToTail(num=np.int32(4))
    assert d.accessByIndex(index=np.int32(0)) == 1
    assert d.accessByIndex(index=np.int32(3)) == 4
    assert d.size == 4


def deque_remove():
    d = deque(arraySize=4)
    for i in range(4):
        d.addToTail(num=np.int32(i))

    assert d.removeFromHead() == 0
    assert d.removeFromTail() == 3
    assert d.size == 2


def deque_circular():
    d = deque(arraySize=3)
    d.addToTail(num=np.int32(1))
    d.addToTail(num=np.int32(2))
    d.addToTail(num=np.int32(3))
    d.removeFromHead()
    d.addToTail(num=np.int32(4))
    assert d.accessByIndex(index=np.int32(0)) == 2
    assert d.accessByIndex(index=np.int32(2)) == 4

tests = [array_addToTail, array_grow, array_addByIndex, array_removeByIndex, array_accessOutOfRange,
        list_addToTail_and_access, list_addToHead, list_addByIndex, list_removeByIndex, list_bad_index,
        deque_addToHead, deque_addToTail, deque_both_ends, deque_remove, deque_circular]

passed = 0
failed = 0

for t in tests:
    try:
        t()
        print(f"OK: {t.__name__}")
        passed += 1

    except AssertionError as e:
        print(f"FAIL: {t.__name__},  {e}")
        failed += 1

    except Exception as e:
        print(f"ERR: {t.__name__}, {type(e).__name__}: {e}")
        failed += 1

print(f"\nИтог: прошло {passed}, упало {failed}")
