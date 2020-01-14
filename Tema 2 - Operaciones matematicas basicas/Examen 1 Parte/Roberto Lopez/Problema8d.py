import matplotlib.pyplot as plt
import numpy
from raices import *
from newtonRaphson import *
from math import *
def f(x): return 16*(x**5)-20*(x**3)+(x**2)+5*x-0.5
def df(x): return 80*(x**4)-60*(x**2)+2*x+5
a,b,dx=(0.0,20.0,0.2)
x1, x2 = buscaraiz(f,a,b,dx)
while x2 !=None:
    s=(x1+x2)/(2.0)
    raiz,numiter=newtonRaphson(f,df,s,tol=0.0001)
    print 'La raiz esta en el intervalo:(',x1,',',x2,')'
    print 'La raiz en ese intervalo:',raiz
    x1, x2 = buscaraiz(f,x2,b,dx)
c=numpy.arange(0.0,20.0,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
