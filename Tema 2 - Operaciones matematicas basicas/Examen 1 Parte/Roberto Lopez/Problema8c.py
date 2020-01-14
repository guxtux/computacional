import matplotlib.pyplot as plt
import numpy
from raices import *
from newtonRaphson import *
from math import *
def f(x): return -(x**3)+x+1
def df(x): return -3*(x**2)+1
a,b,dx=(-10.0,20.0,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
    s=(x1+x2)/(2.0)
    raiz,numiter=newtonRaphson(f,df,s,tol=0.0001)
    print 'La raiz esta en el intervalo:(',x1,',',x2,')'
    print 'La raiz en ese intervalo:',raiz
    x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(-10.0,20.0,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
