# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:40:56 2014

@author: Abraham
"""

#problema 1
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=-1.0*y[0]
    return F
x=0.0
xAlto=9.0
y=np.array([1.0,0.0]) #la posiscion es de un radian en un inicio pero es un punto
#de retorno de manera que la velocidad es cero en ese punto 
h=0.001
freq=300
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)
#incorporamos los elementos necesarios para poder obserbar el espacio fase
plt.figure(1)
plt.subplot(2,1,1)
plt.plot(X,Y[:,0], 'r-')
plt.title('posicion v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('posicion')
plt.subplot(212)
plt.title('diagrama fase')
plt.plot(Y[:,0],Y[:,1], 'c-')
plt.xlabel('posicion')
plt.ylabel('mometo')

plt.show()
#de la grafica observamos dos cosas la primera de ellas es que tenemos un sistema conservativo que no 
#disipa energía pero también  que el periodo es de 2pi podemos analizar el periodo de la sigueiente manera 
#de la grafica podemos ver que en la primera mitad del periodo se tien una velocidad negativa
#aspi podemos encontrar el elemento de la lista en la cual la derivada la derivada cambia 
#de signo y el valor del periodo será dos veves el termino en el cual se presento el cambio
t=Y[1,1]
i=1
while t<0:
    i=i+1
    t=Y[i,1]
err=abs(2*np.pi-X[2*(i+1)]) #asignamos 2pi como el periodo real
print 'el periodo es %7.5f radianes con un error de %7.5e '%(X[2*(i+1)],err)
#ponemos i+1 por sel el termino sobre el que esta montado el contador 