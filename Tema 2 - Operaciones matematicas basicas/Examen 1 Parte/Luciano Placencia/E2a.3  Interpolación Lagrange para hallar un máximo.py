# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 21 20:18:29 2013
INTERPOLACIÓN DE NEVILLE PARA HALLAR EL MÁXIMO EN x=0.7679
"""
from math import *
from interpol import *
import numpy as np
import matplotlib.pyplot as plt

xDatos=np.arange(0,3.5,.5)
yDatos=np.array([1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727])

print u"INTERPOLACIÓN DE NEVILLE PARA HALLAR EL MÁXIMO EN x=0.7679"
print "Tenemos las parejas de puntos:"
print "x =", xDatos
print "y =", yDatos
print u"\nDado que el punto de la raíz debe estar entre los puntos 1 y 2,"
print "es decir, entre (0.5,2.4694) y (1,2.4921), escogeremos los 4 puntos"
print u"más cercanos a ellos (puntos del 0 al 3):"
print "yMAX = y(0.7679) = %1.4f" %neville(xDatos[0:3],yDatos[0:3],0.7679)

print yDatos[0:3]
plt.plot(xDatos,yDatos,"ro-")
plt.plot(0.7679,neville(xDatos[0:3],yDatos[0:3],0.7679),"b*", markersize=15)
plt.xlabel("x")
plt.ylabel("y(x)")
plt.title(u"Representación de los datos")
plt.text(0.5, -1.0, u"El valor máximo de la \n función es: $2.5568$", fontsize=18)
l =plt.axhline(y=0.0 ,color='k', linestyle ='-')
plt.axis([0,3.2,-2,2.8])
plt.grid(1)
plt.show()
