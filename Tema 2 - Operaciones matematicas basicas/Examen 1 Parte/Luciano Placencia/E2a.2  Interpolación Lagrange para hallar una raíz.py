# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 21 20:18:29 2013
INTERPOLACIÓN INVERSA DE LAGRANGE PARA HALLAR LA RAÍZ DE y(x)
"""
from math import *
from interpol import *
import numpy as np
import matplotlib.pyplot as plt

xDatos=np.arange(0,3.5,.5)
yDatos=np.array([1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727])

print u"INTERPOLACIÓN INVERSA DE LAGRANGE PARA HALLAR LA RAÍZ DE y(x)"
print "Tenemos las parejas de puntos:"
print "x =", xDatos
print "y =", yDatos
print u"\nDado que el punto de la raíz debe estar entre los puntos 5 y 6,"
print "es decir, entre (2,0.8509) y (2.5,-0.4112), escogeremos los puntos"
print u"más cercanos a ellos:"
print "a) Usando 3 puntos (3 al 5):         x(y=0) = %1.4f" %lagrange(yDatos[3:5],xDatos[3:5],0)
print "a) Usando 3 puntos (4 al 6):         x(y=0) = %1.4f" %lagrange(yDatos[4:6],xDatos[4:6],0)
print "b) Usando 4 puntos vecinos (3 al 6): x(y=0) = %1.4f" %lagrange(yDatos[3:7],xDatos[3:7],0)
print "b) Usando los 7 puntos:              x(y=0) = %1.4f" %lagrange(yDatos,xDatos,0)
print u"\nCONCLUSIÓN: la mejor aproximación parece ser la que toma 4 puntos."
print u"En cambio, si tomamos los 7 puntos, la aproximación empeora mucho,"
print u"como podemos ver, comparando con la gráfica."

plt.plot(xDatos,yDatos,"ro-")
plt.plot(lagrange(yDatos[3:7],xDatos[3:7],0),0,"b*",markersize=15)
plt.axis([0.0,3.0,-1.7,3.0])
plt.axhline(y=0, color ='k')
plt.text(0.5, -0.5, u"El valor de la raíz es: $2.3397$", fontsize=18)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title(u"Gráfica de los datos del problema")
plt.grid()
plt.show()
