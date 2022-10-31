from itertools import combinations_with_replacement

def get_combinations_with_r(s, n):
    iterable = combinations_with_replacement(s, n)
    res = []
    while True:
        try:
            res.append("".join(next(iterable)))
        except StopIteration:
            return sorted(res)

print(get_combinations_with_r("cat", 2))