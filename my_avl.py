import numpy as np


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class avl:
    def __init__(self):
        self.root = None
        self.size = 0

    def height(self, node):
        if node is None:
            return 0
        
        return node.height

    def updateHeight(self, node):
        h_left = self.height(node.left)
        h_right = self.height(node.right)
        if h_left > h_right:
            node.height = h_left + 1
        else:
            node.height = h_right + 1

    def rotateRight(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        self.updateHeight(y)
        self.updateHeight(x)
        return x

    def rotateLeft(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        self.updateHeight(x)
        self.updateHeight(y)
        return y

    def balance(self, node):
        self.updateHeight(node)
        bf = self.height(node.left) - self.height(node.right)

        if bf > 1:
            if self.height(node.left.left) < self.height(node.left.right):
                node.left = self.rotateLeft(node.left)
            return self.rotateRight(node)

        if bf < -1:
            if self.height(node.right.right) < self.height(node.right.left):
                node.right = self.rotateRight(node.right)
            return self.rotateLeft(node)

        return node

    def insert(self, node, value):
        if node is None:
            self.size += 1
            return Node(value)

        if value < node.value:
            node.left = self.insert(node.left, value)
        elif value > node.value:
            node.right = self.insert(node.right, value)
        else:
            return node

        return self.balance(node)

    def add(self, value):
        self.root = self.insert(self.root, value)

    def contains(self, value):
        node = self.root
        while node is not None:
            if value == node.value:
                return True
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    def minNode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self.delete(node.left, value)
        elif value > node.value:
            node.right = self.delete(node.right, value)
        else:
            if node.left is None:
                self.size -= 1
                return node.right
            if node.right is None:
                self.size -= 1
                return node.left
            successor = self.minNode(node.right)
            node.value = successor.value
            node.right = self.delete(node.right, successor.value)

        return self.balance(node)

    def remove(self, value):
        self.root = self.delete(self.root, value)