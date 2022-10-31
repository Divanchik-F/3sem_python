from itertools import permutations

def get_permutations(s, n):
    iterable = permutations(s, n)
    res = []
    while True:
        try:
            res.append("".join(next(iterable)))
        except StopIteration:
            return sorted(res)

print(get_permutations("cat", 2))