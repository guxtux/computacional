import matplotlib.pyplot as plt
import numpy
from raices import *
from newtonRaphson import *
from math import *
def f(x): return tan(x)-x+1
def df(x): return 1.0/((cos(x))**2)
a,b,dx=(0.0,3*pi,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
     s=(x1+x2)/(2.0)
     if abs(tan(s))<10:
         raiz,numiter=newtonRaphson(f,df,s,tol=0.0001)
         print 'La raiz esta en el intervalo:(',x1,',',x2,')'
         print 'La raiz en ese intervalo:',raiz
     x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(0.0,3*pi,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()

