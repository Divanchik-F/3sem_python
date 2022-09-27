from random import randint

def decorator(func):

    def mm(t):
        f=func(t)
        if f==0:
            return("Нет(")
        elif f>10:
            return("Очень много")
        else:
            return(f)

    return mm
    

A=[randint(0,300) for i in range(randint(0,40))]
print(A)

@decorator
def qw(A:list):
    k=0
    for i in range (len(A)):
        if A[i]%2==0:
            k+=1
    return(k)

if __name__ == "__main__":
    print(qw(A))
