from random import randint

class GetAverage(Exception):
    pass

class GetDispers(Exception):
    pass

class GetCount(Exception):
    pass

def receive_coroutine():
    data=[]
    try:
        while True:
            try:
                x=yield
                data.append(x)
            except GetAverage:
                yield f"Среднее: {sum(data)/len(data)}"
            except GetDispers:
                avg=sum(data)/len(data)
                yield f"Дисперсия: {sum((i-avg)**2 for i in data)/(len(data)-1)}"
            except GetCount:
                yield f"Количество: {len(data)}"
    finally:
        return


coroutine=receive_coroutine()
next(coroutine)
for i in range(100000):
    coroutine.send(randint(1, 200))

print(coroutine.throw(GetAverage))
next(coroutine)
print(coroutine.throw(GetDispers))
next(coroutine)
print(coroutine.throw(GetCount))
next(coroutine)
coroutine.close()