class Node:
    def __init__(self, value, nxt=None):
        self.value = value
        self.nxt = nxt

    def get_value(self):
        return self.value

    def get_next(self):
        return self.nxt

class LinkedLiset:
    def __init__(self):
        self.start = None
        self.length = 0
        self.last = None

    def add(self, value):
        elem = Node(value)
        if self.start is None:
            self.start = elem
            self.last = elem
        else:
            self.last.nxt = elem
            self.last = elem
        self.length += 1

    def __len__(self):
        return self.length

    def __getitem__(self, idx):
        if idx >= self.length:
            raise IndexError("Index out of range")
        current = self.start
        for i in range(idx):
            current = current.get_next()
        current.get_value()

    def __iter__(self):
        self.__curr = self.start
        return self

    def __next__(self):
        if self.__curr is None:
            raise StopIteration()
        val = self.__curr.get_value()
        self.__curr = self.__curr.get_next()
        return val


lst = LinkedLiset()
for i in range(10):
    lst.add(i*i)

j = 0
for i in lst:
    print(i)
    if j < 8:
        lst.add(1000)
        j += 1