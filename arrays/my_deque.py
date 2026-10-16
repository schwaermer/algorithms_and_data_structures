import numpy as np
from numpy.typing import NDArray


class deque:

    def __init__(self, arraySize):
        self.myArray: NDArray[np.int32] = np.empty(arraySize, dtype=np.int32)
        self.capacity = arraySize
        self.size = 0
        self.head = 0
        self.tail = 0

    def _grow(self):
        newArray: NDArray[np.int32] = np.empty(self.capacity * 2, dtype=np.int32)
        for i in range(self.size):
            newArray[i] = self.myArray[(self.head + i) % self.capacity]

        self.myArray = newArray
        self.capacity *= 2
        self.head = 0
        self.tail = self.size

    def addToTail(self, num):
        if self.size == self.capacity:
            self._grow()

        self.myArray[self.tail] = num
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def addToHead(self, num) -> None:
        if self.size == self.capacity:
            self._grow()

        self.head = (self.head - 1) % self.capacity
        self.myArray[self.head] = num
        self.size += 1

    def removeFromTail(self):
        if self.size == 0:
            raise IndexError("deque is empty")
        
        self.tail = (self.tail - 1) % self.capacity
        value: np.int32 = self.myArray[self.tail]
        self.size -= 1
        return value

    def removeFromHead(self):
        if self.size == 0:
            raise IndexError("deque is empty")
        
        value: np.int32 = self.myArray[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return value

    def accessByIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("bad index")
        
        return self.myArray[(self.head + index) % self.capacity]
