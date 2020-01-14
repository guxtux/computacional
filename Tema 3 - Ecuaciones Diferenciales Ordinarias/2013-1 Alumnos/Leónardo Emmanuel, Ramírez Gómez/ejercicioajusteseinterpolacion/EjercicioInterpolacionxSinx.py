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
f=[]
x = np.array([0.,0.125*pi,0.250*pi,0.375*pi,0.5*pi])
f=np.array([0.,.125*sin(.125*pi),.25*sin(.25*pi),.375*sin(.375*pi),.5*sin(.5*pi)])

yres=0

for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]

plt.plot(x,f)
plt.show()   
print 'El polinomio valuado en P(',xa,')=',yres

z=factorial(n+1)
L=(xa-0)*(xa-.125)*(xa-.25)*(xa-.375)*(xa-.5)/z
