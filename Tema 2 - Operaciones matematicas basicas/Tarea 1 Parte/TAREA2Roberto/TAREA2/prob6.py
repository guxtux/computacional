import matplotlib.pyplot as plt
from numpy import * 
from raices import *
from biseccion import *
from math import *
def f(x):return (249.2*(1.0-x)**3)-x*((3.0-2.0*x)**2)
a,b,dx=(0.0,20.0,0.2)
x2=0.0
x1, x2 = buscaraiz(f,x2,b,dx)
print 'El grado de equilibrio de la reaccion es:',bisect(f,x1,x2,switch=1,epsilon=1.0e-9)
c=arange(-0.5,20.0,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
