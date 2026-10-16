import numpy as np

from my_avl import avl


def test_add_and_contains():
    t = avl()
    t.add(np.int32(10))
    t.add(np.int32(5))
    t.add(np.int32(15))
    assert t.size == 3
    assert t.contains(np.int32(10))
    assert t.contains(np.int32(5))
    assert t.contains(np.int32(15))
    assert not t.contains(np.int32(99))


def test_duplicate_not_added():
    t = avl()
    t.add(np.int32(5))
    t.add(np.int32(5))
    t.add(np.int32(5))
    assert t.size == 1


def test_balance_right():
    t = avl()
    for v in [1, 2, 3, 4, 5, 6, 7]:
        t.add(np.int32(v))
    assert t.height(t.root) <= 3


def test_balance_left():
    t = avl()
    for v in [7, 6, 5, 4, 3, 2, 1]:
        t.add(np.int32(v))
    assert t.height(t.root) <= 3


def test_left_right_case():
    t = avl()
    t.add(np.int32(30))
    t.add(np.int32(10))
    t.add(np.int32(20))
    assert t.root.value == 20


def test_right_left_case():
    t = avl()
    t.add(np.int32(10))
    t.add(np.int32(30))
    t.add(np.int32(20))
    assert t.root.value == 20


def test_many_values_stay_balanced():
    t = avl()
    for i in range(1000):
        t.add(np.int32(i))
    assert t.size == 1000
    assert t.height(t.root) <= 11


def test_remove_leaf():
    t = avl()
    for v in [10, 5, 15]:
        t.add(np.int32(v))
    t.remove(np.int32(5))
    assert t.size == 2
    assert not t.contains(np.int32(5))


def test_remove_with_two_children():
    t = avl()
    for v in [20, 10, 30, 25, 40]:
        t.add(np.int32(v))
    t.remove(np.int32(30))
    assert not t.contains(np.int32(30))
    assert t.size == 4


def test_remove_root():
    t = avl()
    for v in [10, 5, 15]:
        t.add(np.int32(v))
    t.remove(np.int32(10))
    assert not t.contains(np.int32(10))
    assert t.size == 2


def test_remove_not_found():
    t = avl()
    for v in [10, 5, 15]:
        t.add(np.int32(v))
    t.remove(np.int32(99))
    assert t.size == 3


def test_remove_all():
    t = avl()
    for v in [10, 5, 15, 3, 7, 12, 20]:
        t.add(np.int32(v))
    for v in [10, 5, 15, 3, 7, 12, 20]:
        t.remove(np.int32(v))
    assert t.size == 0
    assert t.root is None


def test_remove_keeps_balance():
    t = avl()
    for i in range(100):
        t.add(np.int32(i))
    for i in range(0, 100, 2):
        t.remove(np.int32(i))
    assert t.size == 50
    assert t.height(t.root) <= 7


tests = [test_add_and_contains, test_duplicate_not_added, test_balance_right, test_balance_left, test_left_right_case,
        test_right_left_case, test_many_values_stay_balanced, test_remove_leaf, test_remove_with_two_children, test_remove_root,
        test_remove_not_found, test_remove_all, test_remove_keeps_balance]

passed = 0
failed = 0

for t in tests:
    try:
        t()
        print("OK: " + t.__name__)
        passed += 1
    except AssertionError as e:
        print("FAIL: " + t.__name__ + ", " + str(e))
        failed += 1
    except Exception as e:
        print("ERR: " + t.__name__ + ", " + type(e).__name__ + ": " + str(e))
        failed += 1

    print("\nИтог: прошло " + str(passed) + ", упало " + str(failed))