# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 21 20:18:29 2013
INTERPOLACIÓN DE NEVILLE Y DE LAGRANGE
"""
from math import *
from interpol import *
import numpy as np
import matplotlib.pyplot as plt

xDatos=np.array([-1.2,0.3,1.1])
yDatos=np.array([-5.76,-5.61,-3.69])

print u"INTERPOLACIÓN DE NEVILLE Y DE LAGRANGE EN x=0."
print "Tenemos las parejas de puntos:"
print "x =", xDatos
print "y =", yDatos
print u"Método de Neville:         y(0) =",neville(xDatos,yDatos,0.0)
print u"Método de Lagrange:        y(0) =",lagrange(xDatos,yDatos,0.0)
print u"Extra: Método de Newton:   y(0) =",newton(xDatos,yDatos,0.0)

print u"\nCONCLUSIÓN: para estas parejas de puntos, los tres métodos"
print u"dan el mismo resultado numérico en Python."

plt.plot(xDatos,yDatos)
plt.grid(True)
plt.show()