# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:53:12 2012

@author: est5
"""

#Ajusta sin(x) en [0,2pi] con el polinomio de interpolacion de Lagrange de orden
#4 y 8, utilizando puntos con igual separacion (5 y 9 puntos respectivamente).
#Grafica los polinomios de interpolaciòn junto con sin(x) y las distribuciones.

import matplotlib.pyplot as plt
import numpy as np
from math import *
n = 5
x = np.array([0,.4*pi,.8*pi,1.2*pi,1.6*pi,2.*pi])
f = np.array([sin(0.),sin(.4*pi),sin(pi*.8),sin(1.2*pi),sin(1.6*pi),sin(2.*pi)])
xa = eval(raw_input('Da el valor de x'))
yres = 0
for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
print 'aproximacion 5'
print 'El polinomio valuado en P(',xa,')=',yres

plt.figure(1)
plt.subplot(211)
plt.plot(x,f,'b')

#---------------------------------------------------------------------
n = 9
x=np.array([0,.22*pi,.44*pi,.66*pi,.88*pi,1.11*pi,1.33*pi,1.55*pi,1.77*pi,2*pi])
f = np.array([0.,.6428,.9848,.866,.342,-.342,-.866,-.9848,-.6427,0])

yres = 0
for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i != j:
            z = z * (xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
print 'aproximacion 9'
print 'El polinomio valuado en P(',xa,')=',yres

def g(t):
    return np.sin(t)
t1=np.arange(0.0,2.*pi,2.*pi/5.)
t2=np.arange(0.0,2.*pi,2.*pi/9.)


plt.subplot(211)
plt.plot(x,f,'r')

plt.subplot(211)
plt.plot(t1,g(t1),'bs')
plt.plot(t2,g(t2),'gs')
plt.show()


#me parece muy mala la aproximacion a orden 8, no se cual sea el error en el codigo?