def print_map(function, iterable):
    iterator = iter(iterable)
    while (True):
        try:
            print(function(next(iterator)))
        except StopIteration:
            break

def retstr(str):
    return f"Object is: {str}"

arr = [1,2,3,4]
print_map(retstr, arr)