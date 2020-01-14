from numpy import *
from nevilleinter import *


x=linspace(0,3,7)
y=[1.8241,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727]
x0=0.7679
n=4
puntos=[]

i=0
while x0>=x[i]: #cierra el ciclo cuando i esta en la posicion del primer numero mayor que x0
    i=i+1 

j=0
while len(puntos)<n:
    puntos.insert(0,y[i-j-1])
    puntos.append(y[i+j])
    j=j+1
print("los puntos y en los que se evaluara el metodo son:")
print(puntos)
print("")


xpuntos=linspace(x[i-j],x[i+j-1],len(puntos))
maximo=neville(xpuntos,puntos,x0)
print("el valor del maximo es:%3.8f"%maximo)

import matplotlib.pyplot as plt
plt.plot(x,y,x0,maximo,"s")
plt.grid()
plt.show()

