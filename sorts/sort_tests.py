import numpy as np

from my_sorts import bubbleSort, insertionSort


# bubble

def test_bubble_reverse():
    assert bubbleSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_bubble_random():
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert bubbleSort(a) == sorted(a)


def test_bubble_duplicates():
    assert bubbleSort([2, 2, 1, 1, 3, 3]) == [1, 1, 2, 2, 3, 3]


# insertion

def test_insertion_reverse():
    assert insertionSort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_insertion_random():
    a = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    assert insertionSort(a) == sorted(a)


def test_insertion_duplicates():
    assert insertionSort([2, 2, 1, 1, 3, 3]) == [1, 1, 2, 2, 3, 3]


tests = [test_bubble_reverse, test_bubble_random, test_bubble_duplicates,
        test_insertion_reverse, test_insertion_random, test_insertion_duplicates]

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

print("Итог: прошло " + str(passed) + ", упало " + str(failed))


# тесты на время

def benchmark():
    import time
    import random

    for n in [100, 500, 1000]:
        print("N = ", n)

        data = [random.randint(0, 10000) for _ in range(n)]

        start = time.time()
        bubbleSort(data[:])
        t_bubble = time.time() - start

        start = time.time()
        insertionSort(data[:])
        t_insert = time.time() - start

        reverse_data = list(range(n, 0, -1))

        start = time.time()
        bubbleSort(reverse_data[:])
        t_bubble_rev = time.time() - start

        start = time.time()
        insertionSort(reverse_data[:])
        t_insert_rev = time.time() - start

        print("random: Bubble sort " + str(round(t_bubble, 4)) +
              " Insertion " + str(round(t_insert, 4)))
        print("reverse: Bubble sort " + str(round(t_bubble_rev, 4)) +
              " Insertion " + str(round(t_insert_rev, 4)))
        
benchmark()
