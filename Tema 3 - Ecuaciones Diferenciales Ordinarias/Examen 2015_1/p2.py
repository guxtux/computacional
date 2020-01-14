# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:46:40 2014

@author: Abraham
"""

#problema2
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=9.80665-(0.2028/80.0)*(y[1]**2)
    return F
x=0.0
xAlto=13.0
y=np.array([1.0,0.0])
h=0.001
freq=2000
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)
#se incorporán los elementos que permiten verificar la comparación con caída libre
#plt.figure(1)
#plt.subplot(2,1,1)
plt.plot(X,Y[:,0], 'r-',label='movimiento con arrastre')
plt.axhline(y=500, c='k')
plt.axvline(x=12.28,c='k')
plt.text(1,600,'El tiempo para una distancia de 500 metros, es t=12.28 s')
plt.plot(X,+4.9*X**2, 'c-', label='caida libre')
plt.legend(loc="best")
plt.title('posicion v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('posicion')
#plt.subplot(212)
#plt.title('velocidad v/s tiempo')
#plt.plot(X,Y[:,1], 'r-', label='velocidad con arrastre')
#plt.xlabel('tiempo')
#plt.ylabel('velocidad')
#plt.plot(X,9.80665*X,'c-',label='caida libre')
plt.legend(loc="best")
plt.show()
if Y[-1,0]>500:
    i,t=0,Y[0,0]
#ahora incorporamos un forma de escanear los datos  para que se identifique 
#el tiempo necesario para recorrer los 500 metros  
    while t<=500:
        i=i+1
        t=Y[i,0]
    print 'el tiempo para recorrer %3.0f, es %3.5f segundos' %(Y[i,0],X[i])
else : print'pon un tiempo mayor'