import matplotlib.pyplot as plt
import numpy
from raices import *
from biseccion import *
from math import *
def f(x):return sin(x)-0.3*exp(x)
a,b,dx=(0.0,20.0,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
    print 'La raiz esta en el intervalo:(',x1,',',x2,')'
    print 'La raiz en ese intervalo:',bisect(f,x1,x2,switch=1,epsilon=0.001)
    x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(0.0,20.0,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
