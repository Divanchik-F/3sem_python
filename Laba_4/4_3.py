def swap(func):
    def dec (*args, **kwargs):
        args=args[::-1]
        return func(*args, **kwargs)
    return dec

@swap
def div(x, y, show=False):
    res = x / y
    if show:
        print(res)
    return res

div(2, 4, show=True)
