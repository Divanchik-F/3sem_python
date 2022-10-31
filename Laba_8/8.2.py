def fib(quant):
    first, second = 0, 1
    for i in range(quant):
        yield first
        first, second = second, first + second

for i in fib(13):
    print(i)