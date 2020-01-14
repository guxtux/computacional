# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:47:53 2012

@author: est5
"""

#Ajusta xsin(x) en [0,pi/2] con un polinomio de interpolaciòn de Lagrange de
#orden 4, utilizando puntos con igual separaciòn. Calcula el error de cada
#interpolaciòn en cada incremento de pi/16, muestra una grafica


import matplotlib.pyplot as plt
import numpy as np
from math import *

xa = eval(raw_input('da el punto'))
n = 4
f = []
#separacion de 0.125pi
x = np.array([0.,pi/8.,pi/4.,pi*3/8.,pi/2.])
f=np.array([0.,sin(pi/8.)/8.,sin(pi/4.)/4.,sin(pi*3/8.)*3/8.,sin(pi/2.)/2.])

yres = 0

for i in range(0,n+1):
    z = 1.0
    for j in range(0,n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]

print 'El polinomio valuado en P(',xa,')=',yres
#para el error damos de entrada pi/16

c = np.sin(xa)
b = xa*c-yres
print b,c
error=100*abs(b)/c
print 'error relativo a la interpolación del punto:',error,'%'

plt.plot(x,f)
plt.show()   

#obtengo un error de aprox 13.5%, muy grande no se si este mal como tome los puntos
