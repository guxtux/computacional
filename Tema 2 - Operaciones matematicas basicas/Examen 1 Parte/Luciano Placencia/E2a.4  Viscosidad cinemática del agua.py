# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Mar 21 20:18:29 2013
INTERPOLACIÓN DE NEWTON PARA HALLAR LA VISCOSIDAD CINEMÁTICA DEL AGUA
"""
from math import *
from interpol import *
import numpy as np
import matplotlib.pyplot as plt


xDatos=np.array([0.,21.1,37.8,54.4,71.1,87.8,100.])
yDatos=np.array([1.79,1.13,0.696,0.519,0.338,0.321,0.296])
x0=[10,30,60,90]
y0=[]

print u"INTERPOLACIÓN DE NEWTON PARA HALLAR LA VISCOSIDAD CINEMÁTICA"
print u"DEL AGUA mu_k(T), donde [muk]=1e-3 m^2/s y [K]=ºC."
print u"\nTenemos las parejas de puntos:"
print "T =", xDatos
print "muk(T) =", yDatos
print "\nLos datos interpolados para T =", x0, "son:"
for i in range(4):
    y0.append(newton(xDatos,yDatos,x0[i]))
    print "muk(",x0[i],")=%1.3f" %y0[i]
    plt.plot(x0[i],y0[i],"bo")
print u"\nN.B.: Usamos el método de Newton pues es el idóneo para interpolar"
print u"varios puntos."

plt.plot(xDatos,yDatos,"ro-")
plt.title("Datos experimentales")
plt.xlabel("T [$^{\circ}C$]", fontsize=15)
plt.ylabel("$\mu_{k}$", fontsize=25)
plt.text(50,1.6, "Temperatura", fontsize=15)
plt.text(80,1.6, "$\mu_{k}$", fontsize=20)
plt.text(60,1.5, "$10$", fontsize=15)
plt.text(80,1.5, "$1.621$", fontsize=15)
plt.text(60,1.4, "$30$", fontsize=15)
plt.text(80,1.4, "$0.842$", fontsize=15)
plt.text(60,1.3, "$60$", fontsize=15)
plt.text(80,1.3, "$0.457$", fontsize=15)
plt.text(60,1.2, "$90$", fontsize=15)
plt.text(80,1.2, "$0.333$", fontsize=15)
plt.grid()
plt.show()
