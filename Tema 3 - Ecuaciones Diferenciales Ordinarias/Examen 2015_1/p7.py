# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:03:56 2014

@author: Abraham
"""

#problema 7
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((4),dtype='float64')
    F[0]=y[1]
    F[1]=-(0.03/0.25)*y[1]*(np.sqrt(y[1]**2+y[3]**2))
    F[2]=y[3]
    F[3]=-(0.03/0.25)*y[3]*(np.sqrt(y[1]**2+y[3]**2))-9.80665
    return F
x=0.0
xAlto=5.090
y=np.array([0.0,25*np.sqrt(3),0.0,25.0]) 
h=0.001
freq=500
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)


#implememtamos una rutina que escanea los datos para encontrar el alcance y el 
#tiempo de vuelo
i=1
t=Y[1,2]
while t>0:
    i=i+1
    t=Y[i,2]
print 'el tiempo de vuelo es %2.5f segundos y el alcance son %3.5f metros'%(X[i],Y[i,0])
plt.figure(1)
plt.plot(Y[:i,0],Y[:i,2], 'r-',label='movimiento con arrastre')
plt.plot(X*25*np.sqrt(3),-0.5*9.80665*X**2+25*X,'k-',label='movimiento libre')
plt.legend(loc='best')
plt.title('movimiento del proyectil')
plt.xlabel('posicion en "X"')
plt.ylabel('posicion en "Y"')
plt.grid()
plt.figure(2)
plt.plot(Y[:i,0],Y[:i,2], 'r-',label='movimiento con arrastre')
#plt.plot(X*25*np.sqrt(3),-0.5*9.80665*X**2+25*X,'k-',label='movimiento libre')
#plt.legend(loc='best')
plt.title('movimiento del proyectil')
plt.xlabel('posicion en "X"')
plt.ylabel('posicion en "Y"')
plt.text(5,1,'Tiempo de vuelo $t=2.018$ s', size=18)
plt.text(5,0.65,'El alcance es $R=18.946$ m', size=18)
plt.grid()

plt.show()
#las curvas presentadas en las grafcas presentan el comportamiento simultánea 
#de los dos movimientos exhibiendo que los resultados obtenidos son razonables 
#dado que aquí el amortiguamiento no sólo viene dado por los factores de arrastre
#si no por  una potencia de la Velocidad. 