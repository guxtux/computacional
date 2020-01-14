import matplotlib.pyplot as plt
from numpy import * 
from raices import *
from biseccion import *
from math import *
def f(x):return 335.0+9.81*x-2510*log(2.8E6/((2.8E6)-(13.3E3)*x))
a,b,dx=(0.0,100.0,0.2)
x2=0.0
x1, x2 = buscaraiz(f,x2,b,dx)
print 'El tiempo que tarda en alcanzar la velocidad del sonido es:',bisect(f,x1,x2,switch=1,epsilon=1.0e-9),'segundos'
c=arange(0,100,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
     
