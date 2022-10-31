def my_zip(*arrays):
    iterators = [iter(i) for i in arrays]
    while True:
        try:
            val = tuple([next(i) for i in iterators])
            yield val
        except StopIteration:
            return

def my_map(func, lst):
    iterable = iter(lst)
    while True:
        try:
            yield func(next(iterable))
        except StopIteration:
            break

def my_enumerate(lst, start = 0):
    iterable = iter(lst)
    while True:
        try:
            yield tuple([start, next(iterable)])
            start+=1
        except StopIteration:
            break

a = [1,2,3]
b = ['a','b','c']
c = ["first", "second", "third"]

def mul(x):
    return x*x

for i in my_zip(a, b, c):
    print(i)

for i in my_map(mul, a):
    print(i)

for i in my_enumerate(c, 5):
    print(i)