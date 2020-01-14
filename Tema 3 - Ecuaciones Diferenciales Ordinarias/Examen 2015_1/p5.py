# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:58:40 2014

@author: Abraham
"""

#problema5
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=(-9.80665/1.0)*np.sin(y[0])+((2.5**2)*0.25)*(np.cos(y[0]))*np.sin(2.5*x)
    return F
x=0.0
xAlto=10.0
y=np.array([0.0,0.0]) #dado que parte del equilibrio ponemos un valor cercano a cero
h=0.001
freq=100
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(X,Y[:,0], 'r-')
plt.title('tetha v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('desplazamiento')
plt.axhline(y=0, c='k')

plt.subplot(212)
plt.title('diagrama fase')
plt.plot(Y[:,0],Y[:,1], 'c-')
plt.xlabel('posicion')
plt.ylabel('momento')

plt.figure(2)
#plt.subplot(2,1,1)
plt.plot(X,Y[:,0], 'r-')
plt.title('tetha v/s tiempo')
plt.xlabel('tiempo')
plt.ylabel('desplazamiento')
plt.text(5,0.9,r'$\theta_{max}=0.81547$ radianes', size=18)
plt.axhline(y=0, c='k')
plt.show()
#analizando los datos podemos ver que el perido es 2.77seg y la amplitud maxima   
#de desplazamiento es  4.9175e-01 metros
#opservamos que el sistema es conservativo y no disipa dado qe el plano fase que se obtiene da una orbita cerrada
#semejante a la de un oscilador armónico solo que los movimientos del collar lo hacen desplazarce introducir una energía 
#cinética extra produciendo que las elipses se muevan de sus centros originales 
# se hace el prodcto l=0*r pero r=1
print ' la amplitud maxima es',np.max(abs(Y[:,0])),' radianes'