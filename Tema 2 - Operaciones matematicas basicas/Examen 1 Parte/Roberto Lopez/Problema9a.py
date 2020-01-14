import matplotlib.pyplot as plt
import numpy
from raices import *
from secante import *
from math import *
def f(x):return 0.1*(x**3)-5*(x**2)-x+4+exp(-x)
a,b,dx=(-2.0,20.0,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
     print 'La raiz esta en el intervalo:(',x1,',',x2,')'
     print 'La raiz en ese intervalo es:',secante(f,x1,x2,epsilon=0.001,N=40)
     x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(-10,20,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
