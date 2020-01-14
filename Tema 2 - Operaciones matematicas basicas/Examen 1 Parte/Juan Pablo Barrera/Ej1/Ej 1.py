from lagrange import *
from nevilleinter import *
from numpy import *
from grafica import *



x=[-1.2, 0.3, 1.1]
y=[-5.76, -5.61, -3.69]

x0=0 #puntos que quiero encontrar


n=2   #orden del polinomio de lagrange
yres=intlagrange(n,x0,x,y) #llamado de metodo de lagrange
a=neville(x,y,x0) #llamado de metodo de neville

print("El valor del punto x=0 es:")
print("%3.4f"%yres[0],"usando el metodo de lagrange")
print("%3.4f"%a,"usando el metodo de neville")

#grafica
import matplotlib.pyplot as plt
plt.plot(x,y,0,a,"s")
plt.grid()
plt.show()
