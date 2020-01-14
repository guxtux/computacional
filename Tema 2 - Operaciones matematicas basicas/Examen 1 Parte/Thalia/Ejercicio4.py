# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 03:25:49 2013

@author: usuario
"""
from numpy import *
import matplotlib.pyplot as plt

ejex=[]
ejey=[]

def evalPoli(a, xDatos, x):
    n=len(xDatos)-1
    p=a[n]    
    for k in range (1, n+1):
        p=a[n-k]+(x-xDatos[n-k])*p
    return p
def coeffts (xDatos, yDatos):
    m=len(xDatos)
    a=yDatos.copy()
    for k in range (1,m):
        a[k:m]=(a[k:m]-a[k-1])/(xDatos[k:m]-xDatos[k-1])
    return a 

xDatos=array([0., 21.1, 37.8, 54.4, 71.1, 87.8, 100])
yDatos=array([1.79e-3, 1.13e-3, 0.696e-3, 0.519e-3, 0.338e-3, 0.321e-3, 0.296e-3])
a=coeffts(xDatos, yDatos)

print 'Temperatura   Viscosidad Cinematica'
for x in array([10, 30, 60, 90]):
    y=evalPoli(a, xDatos, x)
    print '%3.0f            %9.8f' %(x,y)
    ejex.append(x)
    ejey.append(y)

plt.plot ([0., 21.1, 37.8, 54.4, 71.1, 87.8, 100], [1.79e-3, 1.13e-3, 0.696e-3, 0.519e-3, 0.338e-3, 0.321e-3, 0.296e-3], 'co:')
plt.plot(ejex, ejey, 'bs')
plt.grid(True)
plt.xlabel('Temperatura\n [°C]')
plt.ylabel('Viscosidad cinematica del agua\n [m2/s]')
plt.title('Variacion de la viscosidad cinematica\n del agua con la temperatura')
plt.show()
