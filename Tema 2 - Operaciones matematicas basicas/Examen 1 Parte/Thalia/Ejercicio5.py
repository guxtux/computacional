# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 03:53:58 2013

@author: usuario
"""
from numpy import *
import matplotlib.pyplot as plt

n=6
x0=array([10.5])
x=array([0., 1.525, 3.050, 4.575, 6.10, 7.625, 9.150])
f=array([1., 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741])
ejex=[]
ejey=[]

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
    print 'La densidad relativa del aire a ',k,' km es ',yres

plt.plot (ejex, ejey, 'ms', [0., 1.525, 3.050, 4.575, 6.10, 7.625, 9.150], [1., 0.8617, 0.7385, 0.6292, 0.5328, 0.4481, 0.3741],  'bo-')
plt.grid(True)
plt.xlabel('h[Km]')
plt.ylabel('p(h)')
plt.title('Densidad relativa del aire\n como funcion de la altitud')
plt.show()
