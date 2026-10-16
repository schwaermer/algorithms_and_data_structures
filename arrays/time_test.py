import time
import numpy as np

from my_array import array
from my_list import list as my_list
from my_deque import deque

N = 10000

def measure(name, func):
    start = time.time()
    func()
    end = time.time()
    print(f"{name:<35} {end - start:.4f} сек")


def test_speed():
    def arr_append():
        a = array(arraySize=4)
        for i in range(N):
            a.addToTail(num=np.int32(i))

    def lst_append():
        l = my_list()
        for i in range(N):
            l.addToTail(num=np.int32(i))

    def deq_append():
        d = deque(arraySize=8)
        for i in range(N):
            d.addToTail(num=np.int32(i))

    def arr_prepend():
        a = array(arraySize=4)
        for i in range(N):
            a.addByIndex(num=np.int32(i), index=np.int32(0))

    def lst_prepend():
        l = my_list()
        for i in range(N):
            l.addToHead(num=np.int32(i))

    def deq_prepend():
        d = deque(arraySize=8)
        for i in range(N):
            d.addToHead(num=np.int32(i))


    print("Append в конец")
    measure("array.addToTail", arr_append)
    measure("list.addToTail", lst_append)
    measure("deque.addToTail", deq_append)

    print("\nBставка в начало")
    measure("array.addByIndex(0)", arr_prepend)
    measure("list.addToHead", lst_prepend)
    measure("deque.addToHead", deq_prepend)

test_speed()
