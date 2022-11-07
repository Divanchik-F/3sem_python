import imp
from random import randint

class BinTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def add(self, elem):
        if elem.value < self.value:
            if self.left is None:
                self.left = elem
            else:
                self.left.add(elem)
        else:
            if self.right is None:
                self.right = elem
            else:
                self.right.add(elem)

    def __iter__(self):
        yield self
        if self.left is not None:
            for elem in self.left:
                yield elem
        if self.right is not None:
            for elem in self.right:
                yield elem

    def __str__(self):
        return str(self.value)


tree = BinTree(3)
for i in range(10):
    elem = BinTree(randint(1, 100))
    tree.add(elem)

for elem in tree:
    print(elem)