from itertools import product

def get_cartesian_product(a, b):
    return list(product(a, b))

print(get_cartesian_product([1, 2], [3, 4]))