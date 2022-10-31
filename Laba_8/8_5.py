from itertools import groupby

def compress_string(s):
    iterable = groupby(s)
    res = []
    while True:
        try:
            item, quant = next(iterable)
            res.append(tuple([len(list(quant)), int(item)]))
        except StopIteration:
            break
    return res

print(compress_string('1222311'))