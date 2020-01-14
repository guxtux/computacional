# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 21 20:18:29 2013
INTERPOLACIÓN DE NEVILLE PARA LA DENSIDAD RELATIVA DEL AIRE
"""
from math import *
from interpol import *
import numpy as np
import matplotlib.pyplot as plt

xDatos=np.array([0.,1.525,3.050,4.575,6.1,7.625,9.150])
yDatos=np.array([1.,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741])
x0=10.5

print "INTERPOLACIÓN DE NEVILLE PARA HALLAR LA DENSIDAD RELATIVA DEL AIRE"
print "rho(h), donde [rho]=1 y [h]=Km."
print "\nTenemos las parejas de puntos:"
print "h =", xDatos
print "rho(h) =", yDatos
print "\nInterpolación para h =", x0,":"
y0=neville(xDatos,yDatos,x0)
print "rho(",x0,")= %1.4f" %y0
print "\nN.B.: Usamos el método de Neville pues es el más eficiente para"
print "interpolar un solo punto."

plt.plot(x0,y0,"bo")
plt.plot(xDatos,yDatos,"ro-")
plt.xlabel("h [Km]", fontsize=15)
plt.ylabel(r"$\rho$", fontsize=15)
plt.title("Datos experimentales")
plt.axis([0,10.8,0,1])
plt.text(2,0.2,"La densidad del aire en $10.5$ km es de $0.3177$", fontsize=15)
#plt.axvspan(9, 10.75, facecolor='b', alpha=0.2)
plt.ylim(ymin=0)
plt.grid()
plt.show()
