# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:05:54 2014

@author: Abraham
"""

#problema 8
import matplotlib.pyplot as plt
from imprimeSoln import*
from rk4 import*
import numpy as np

def F(x,y):
    F=np.zeros((2),dtype='float64')
    F[0]=y[1]
    F[1]=-(1.0/x)*y[1]-y[0]
    return F
x=1e-12
xAlto=5.00
y=np.array([1.0,0.0]) 
h=0.001
freq=100
X,Y=integra(F,x,y,xAlto,h)
imprimeSoln(X,Y,freq)

plt.plot(X,Y[:,0], 'r-',label='valores de Jo(x)')
plt.title('ecuacion de bessel')
plt.legend("valores de Jo(x)")
plt.xlabel('X')
plt.ylabel('Jo(X)')
plt.axhline(y=0,c='k')
plt.legend(loc="best")
plt.text(3,0.5,u'$J_{0}=-0.77596756515$',size=18)
plt.grid()
plt.show()
#comparamos e imprimimos el valor de J0(5)
u=len (X)
err=abs(Y[u-1,0]+0.17760)
print ' Jo(5)=', Y[u-1,0],'con error de',err