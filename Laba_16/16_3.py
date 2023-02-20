import matplotlib.pyplot as plt
import numpy as np

def f(t):
    return np.sin(t/5)*np.exp(t/10)+5*np.exp(-t/2) 

x=np.linspace(0, 16, 100)
y=f(x)

#1
A=np.array(
        [[1, 1],
         [1, 15,]])
af=np.array([f(1),f(15)])

q0,q1=np.linalg.solve(A,af)
Fa=q0+q1*x
print(q0, q1)

#2
B=np.array(
        [[1, 1, 1],
         [1, 8, 8**2],
         [1, 15, 15**2]])
bf=np.array([f(1), f(8),f(15)])

q0,q1,q2=np.linalg.solve(B,bf)
Fb=q0+q1*x+q2*x**2
print(q0, q1, q2)


#3
C=np.array(
        [[1, 1, 1, 1],
         [1, 4, 4**2, 4**3 ],
         [1, 10, 100, 1000 ],
         [1, 15, 15**2, 15**3]])
cf=np.array([f(1), f(4), f(10), f(15)])

q0,q1,q2,q3=np.linalg.solve(C,cf)
Fc=q0+q1*x+q2*x**2+q3*x**3
print(q0, q1, q2, q3)


graph=plt.figure()
plt.plot(x, y, "r")
plt.plot(x, Fa, "g")
plt.plot(x, Fb, "b")
plt.plot(x, Fc, "y")
plt.legend(['Given function', 'Linear approximation', 'Quadratic approximation', '3-rd order approximation'])
plt.savefig("3_plot.png")
