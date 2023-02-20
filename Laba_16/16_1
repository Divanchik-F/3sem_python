#1)
import random
import numpy as np
v1=np.arange(12, 25, 1)
print("1) ", v1)
#2
v2=np.zeros((1, 12), dtype=np.int64)
v2[0][4]=5
print("2) ", v2)
#3
A1=np.arange(0, 9, 1)
A1=A1.reshape(3, 3)
print("3)\n",  A1)
#4
A2=np.array([1,2,0,0,4,0])
idx=(A2>0)
print("4) ", A2[idx])
#5
B1=np.arange(0, 15, 1)
B1=B1.reshape(5, 3)
B2=np.arange(6, 18, 2)
B2=B2.reshape(3,2)
A3=np.dot(B1, B2)
print("5)\n",  A3)
#6
A4=np.zeros((8, 8))
v=np.ones((8, 1))
A4=np.hstack((v,A4,v))
v=np.ones((1, 10))
A4=np.vstack((v,A4,v))
A4=np.array(A4, dtype=np.int64)
print("6)\n",  A4)




#7 и 11
a=np.floor(60*np.random.random((5,5)))
a=a.reshape(1, 25)
a=np.array(a, dtype=np.int64)
n=random.randint(1,10)
print('7) 11)', " \n Вектор (трансформ матрица): ", a,"\n N=", n)
a=sorted(a)
a=np.array(a, dtype=np.int64)
print('Отсортированный вектор:', a, '\n N наибольших значений:', a[0][:n])
