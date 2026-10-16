import numpy as np
from numpy.typing import NDArray


class array:

    def __init__(self, arraySize):
        self.myArray: NDArray[np.int32] = np.empty(arraySize, dtype=np.int32)
        self.capacity: int = arraySize
        self.size: int = 0

    def _grow(self):
        newArray: NDArray[np.int32] = np.empty(self.capacity * 2, dtype=np.int32)
        for i in range(self.size):
            newArray[i] = self.myArray[i]

        self.myArray = newArray
        self.capacity *= 2

    def addToTail(self, num):
        if self.size == self.capacity:
            self._grow()

        self.myArray[self.size] = num
        self.size += 1

    def addByIndex(self, num, index):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        
        if self.size == self.capacity:
            self._grow()

        for i in range(self.size, index, -1):
            self.myArray[i] = self.myArray[i - 1]

        self.myArray[index] = num
        self.size += 1

    def removeByIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        
        value: np.int32 = self.myArray[index]
        for i in range(index, self.size - 1):
            self.myArray[i] = self.myArray[i + 1]

        self.size -= 1

        return value

    def accessByIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        
        return self.myArray[index]

    def setByIndex(self, num, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        
        self.myArray[index] = num
