import matplotlib.pyplot as plt
import numpy
from raices import *
from metposfalse import *
from math import *
def f(x):return 0.5*exp(x/3)-sin(x)
a,b,dx=(0.0,20.0,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
     print 'La raiz esta en el intervalo:(',x1,',',x2,')'
     print 'La raiz en ese intervalo',metposfalse(f,x1,x2,epsilon=1.0e-9,N=40)
     x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(0.0,20,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
