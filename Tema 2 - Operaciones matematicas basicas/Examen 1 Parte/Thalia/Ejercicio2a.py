# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:06:11 2013

@author: usuario
"""
from numpy import *
import matplotlib.pyplot as plt

ejex=[]
ejey=[]

n=2
x0=array([0.0])

#El problema pide que calcules la raíz, pero debes de usar los
#puntos más cecanos a la misma, tu elegiste los primeros tres de la
#tabla que están alejados de la raíz y=0
x=array([1.8421, 1.9047, -1.5727])
f=array([0., 1.5, 3.])

for k in x0:
    yres=0
    for i in range (0, n+1):
        z=1.0
        for j in range (0, n+1):
            if i != j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]
    ejex.append(k)
    ejey.append(yres)
    print 'El polinomio evaluado en P(',k,')= ',yres
    
plt.plot([1.8421, 1.9047, -1.5727], [0., 1.5, 3.], 'ro-')
plt.grid(True)
plt.title('Polinomio de grado 2 para aproximar una funcion')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
