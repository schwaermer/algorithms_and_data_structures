import numpy as np
from numpy.typing import NDArray


class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class list:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addToTail(self, num):
        node = Node(num)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.size += 1

    def addToHead(self, num):
        node = Node(num)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.size += 1

    def _nodeAt(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        
        node = self.head
        for _ in range(index):
            node = node.next

        return node

    def addByIndex(self, num, index):
        if index <= 0:
            self.addToHead(num)
            return
        
        if index >= self.size:
            self.addToTail(num)
            return
        
        right= self._nodeAt(index)
        left = right.prev
        node = Node(num)
        node.prev = left
        node.next = right
        left.next = node
        right.prev = node
        self.size += 1

    def removeByIndex(self, index):
        node = self._nodeAt(index)
        value = node.value
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        self.size -= 1
        return value

    def accessByIndex(self, index):
        return self._nodeAt(index).value
