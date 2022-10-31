from itertools import combinations

def get_combinations(s, n):
    res = []
    for i in range(1, n + 1):
        iterable = combinations(s, i)
        while True:
            try:
                res.append("".join(next(iterable)))
            except StopIteration:
                break
    return res

print(get_combinations("cat", 2))