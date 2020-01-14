#-*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Apr 30 18:40:52 2013
ECUACIONES DE LORENTZ PARA PREDICCIÓN DEL CLIMA
Espacio de configuración y espacio fase
"""
from scipy import integrate
import pylab as p
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3

def dY(Y,t=0.): 
    y1,y2,y3=Y[0],Y[1],Y[2]
    return np.array([a*(y2-y1),(c-y3)*y1-y2,y1*y2-b*y3])

a,b,c=10.,8./3,28.
Y0=[1.,1.,1.]
t=np.linspace(0.,30.,2000)
Y=integrate.odeint(dY,Y0,t)
y1,y2,y3=Y.T     #Y.T devuelve la transpuesta de la matriz Y

#Grafica
f1=p.figure()
p.plot(t,y1,"r-",label="y1")
p.plot(t,y2,"g-",label="y2")
p.plot(t,y3,"b-",label="y3")
p.legend(loc="best")
p.xlabel("Tiempo")
p.ylabel("y1,y2,y3")
p.title(u"Evolución del clima")
p.grid()

f2=p.figure()
ax=p3.Axes3D(f2)
ax.plot3D(Y[:,0],Y[:,1],Y[:,2])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
f2.add_axes(ax)
p.show()
