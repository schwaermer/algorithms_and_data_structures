class Node:

    def __init__(self, key):
        self.key = key
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:

    def __init__(self):
        self.root = None

    def height(self, node):
        if node is not None:
            return node.height
        else:
            return -1

    def update_height(self, node):
        node.height = max(self.height(node.left), self.height(node.right)) + 1

    def balance_factor(self, node):
        return self.height(node.left) - self.height(node.right)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            return node

        self.update_height(node)
        bf = self.balance_factor(node)

        # повороты

        if bf > 1 and key < node.left.key:
            return self.rotate_right(node)

        if bf < -1 and key > node.right.key:
            return self.rotate_left(node)

        if bf > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if bf < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node  # если баланс в норме

    def rotate_left(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def rotate_right(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        self.update_height(node)
        self.update_height(new_root)
        return new_root

    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = self._min(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        self.update_height(node)
        bf = self.balance_factor(node)

        if bf > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)

        if bf < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)

        if bf > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if bf < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)
        