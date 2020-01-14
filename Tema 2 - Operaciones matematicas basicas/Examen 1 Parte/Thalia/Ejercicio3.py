# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 02:35:50 2013

@author: usuario
"""
from numpy import *
import matplotlib.pyplot as plt

ejex=[]
ejey=[]

def neville (xDatos, yDatos, x):
    m=len(xDatos)
    y=yDatos.copy()
    for k in range (1,m):
        for i in range (m-k):        
            y[i]=((x-xDatos[i+k]*y[i])+(xDatos[i]-x)*y[i+1])/(xDatos[i]-xDatos[i+k])
    return y[0]

#Esta es la funcion que usamos en la clase
#def neville(xDatos, yDatos, x):
#    m=len(xDatos)
#    y=yDatos.copy()
#    for k in range (1,m):
#        y[0:m-k] = ((x - xDatos[k:m])*y[0:m-k] + \
#        (xDatos[0:m-k] - x)*y[1:m-k+1])/ \
#        (xDatos[0:m-k] - xDatos[k:m])
#    return y[0]

#1. Hay que usar toda la lista de datos.
#2. Tomar en cuenta la informacion que se te da, sobre en donde esta el maximo

xDatos=array([1., 1.5, 2., 2.5])
yDatos=array([2.4921, 1.9047, 0.8509, -0.4112])

#xDatos=array([0,0.5,1., 1.5, 2., 2.5])
#yDatos=array([1.8421,2.4694,2.4921, 1.9047, 0.8509, -0.4112])

r=neville (xDatos, yDatos, 5)
#No me queda claro el por que usaste el valor x=5??
#r=neville(xDatos[0:3], yDatos[0:3], 0.7679)

ejex.append(0.5)
ejey.append(r)

plt.plot(xDatos, yDatos, 'bo--')
plt.plot(0.7679, r, 'ms')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Maximo de y(x)')
plt.show()

print u'La función y(x) alcanza su maximo en' 
print neville(xDatos[0:3], yDatos[0:3], 5)
#si cambias la funcion, veras que se obtiene el valor del maximo
