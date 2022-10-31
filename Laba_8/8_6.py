from itertools import starmap
from operator import ne

def maximize(lists, m):
    iterable = starmap(max, lists)
    sum = 0
    while True:
        try:
            num = next(iterable)
            sum += num*num
        except StopIteration:
            return sum

lists = [
    [5, 4],
    [7, 8, 9],
    [5, 7, 8, 9, 10]
]
print(maximize(lists, m=1000))