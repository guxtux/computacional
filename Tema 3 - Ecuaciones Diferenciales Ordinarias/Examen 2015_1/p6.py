# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:01:14 2014

@author: Abraham
"""

#problema 6
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=(((np.pi**2)/12.0)**2)*y[0]*((np.sin((np.pi)*x))**2)-9.80665*(np.sin((np.pi/12.0)*(np.cos(x*np.pi))))
    return F
x=0.0
xAlto=3.95
y=np.array([0.75,0.0]) #suponemos que la velocidad al inicio es cero pero su posición es 0.75m
h=0.001
freq=100
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

plt.plot(X,Y[:,0], 'g-',label='posicion de la masa')
plt.title('posicion v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('posicion')
plt.text(1,2.5,'El tiempo para alcanzar el extremo es 3.557 s')
plt.axhline(y=2,c='k')
plt.axvline(x=3.557, c='k')
plt.legend(loc="best")
plt.show()

#de la grafica es posible bscar el límite superio en el cual r=2
i=0
while Y[i,0]<2:
    i=i+1
#asi escaneamos los daos para ver el tiempo en el cual la posición llega a 2mts
print 'el tiempo paa alcanzar el extremo es', X[i],'segundos'
