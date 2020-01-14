import matplotlib.pyplot as plt
from numpy import * 
from raices import *
from biseccion import *
from math import *
def f(x):return (1100.0/1000)*x -sinh(x)
a,b,dx=(0.1,2.0,0.2)
x2=0.1
x1, x2 = buscaraiz(f,x2,b,dx)
r=bisect(f,x1,x2,switch=1,epsilon=1.0e-9)
s=(77E3)*(1000)/(2.0*r)
sm=s*cosh(r)
print "La tension maxima que se produce es:",sm
c=arange(0.1,2.0,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
