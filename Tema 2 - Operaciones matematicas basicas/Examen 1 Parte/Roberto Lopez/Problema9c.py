import matplotlib.pyplot as plt
import numpy
from raices import *
from secante import *
from math import *
def f(x):return x+(1/(x*(x+3)))
a,b,dx=(-4.0,20.0,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
    r=secante(f,x1,x2,epsilon=1.0e-9,N=40)
    if r!=0 and r!=-3 :
        print 'La raiz esta en el intervalo:(',x1,',',x2,')'
        print 'La raiz en ese intervalo es:',secante(f,x1,x2,epsilon=0.001,N=40)
        x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(-4.0,20,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
