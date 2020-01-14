# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Apr 30 18:40:52 2013
SISTEMA DEPREDADOR-PRESA (LOTKA-VOLTERRA)
Espacio de configuración y espacio fase
"""
from scipy import integrate
import pylab as p
import numpy as np

def dY(Y,t=0.):
    return np.array([a*Y[0]-b*Y[0]*Y[1],-c*Y[1]+d*b*Y[0]*Y[1]])

a,b,c,d=1.,0.1,1.5,0.75
Y0=np.array([10.,5.])
t=np.linspace(0.,15.,1000)
Y=integrate.odeint(dY,Y0,t)
conejos,zorros=Y.T     #X.T devuelve la transpuesta de la matriz X

#Grafica conejos vs. zorros
f1=p.figure()
p.plot(t,conejos,"r-",label="Conejos")
p.plot(t,zorros,"b-",label="Zorros")
p.legend(loc="best")
p.xlabel("Tiempo")
p.ylabel(u"Población de conejos y zorros")
p.title(u"Evolución de la población de conejos y zorros")
p.grid()

#Condiciones de equilibrio
X_f0=np.array([0.,0.])
X_f1=np.array([c/d/b,a/b])

values=np.linspace(0.3,0.9,5)
vcolors=p.cm.autumn_r(np.linspace(0.3,1.,len(values))) #p.cm=Color Master
f2=p.figure()

#Calcula las trayectorias
for v,col in zip(values,vcolors):
    Y0=v*X_f1
    Y=integrate.odeint(dY,Y0,t)
    p.plot(Y[:,0],Y[:,1],lw=3.5*v,color=col,label="Y0=(%.f, %.f)" %(Y0[0],Y0[1]))

#Define una malla y calcula la dirección
xmax=p.xlim(xmin=0)[1]
ymax=p.ylim(ymin=0)[1]
nb_points=20

x=p.linspace(0,xmax,nb_points)
y=p.linspace(0,ymax,nb_points)

X1,Y1=p.meshgrid(x,y)
DX1,DY1=dY([X1,Y1])
M=(p.hypot(DX1,DY1))
M[M==0]=1.
DX1/=M
DY1/=M

#Dibuja las direcciones usando quiver
p.title(u"Trayectorias y campo de dirección")
Q=p.quiver(X1,Y1,DX1,DY1,M,pivot="mid",cmap=p.cm.jet)
p.xlabel(u"Número de conejos")
p.ylabel(u"Número de zorros")
p.legend()
p.grid()
p.xlim(0,xmax)
p.ylim(0,ymax)
p.show()
