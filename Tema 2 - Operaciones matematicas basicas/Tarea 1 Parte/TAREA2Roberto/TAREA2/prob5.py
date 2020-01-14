import matplotlib.pyplot as plt
from numpy import * 
from raices import *
from biseccion import *
from math import *
def f(x):return -1E5+8.311441*x*log((x/4.44418)**(5/2))
a,b,dx=(1000.0,1500.0,0.2)
x2=1000
x1, x2 = buscaraiz(f,x2,b,dx)
print 'La temperatura para la cual G=-10E5j es:',bisect(f,x1,x2,switch=1,epsilon=1.0e-9),'K'
c=arange(1000,1500,0.2)
y=[]
for k in c:
     y.append(f(k))
plt.plot(c,y)
plt.grid(True)
plt.show()
