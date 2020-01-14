# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "CÁLCULO DE LA CONCENTRACIÓN DE SAL"
print "EN LOS TANQUES DE AGUA 1 (50 gal) Y 2 (20 gal)"
print "USANDO EL MÉTODO RK2.\n"
from ecdif import *

def dY(Y,t):        #Sistema de 2 EDO dy1/dt,dy2/dt (y1,y2,t)
    y1,y2=Y
    dy1=-y1/25.
    dy2=-3/20.*y2+y1/10.
    return np.array([dy1,dy2])

def dt_dy1(t,y1): return -25./y1    #EDO dt/dy1 (y1,t)

t0=0.; tn=100.; h=1        #Extremos de t y paso h [horas]
y10=10.; y20=0.            #Condiciones iniciales [onzas/galón]
Y0=np.array([y10,y20])
y1,y2=rk(2,dY,Y0,t0,tn,h).T

print "a) En el tanque 1, la concentración de sal y1 se redujo "
print "   de y1(0)=10 oz/gal a y1(0)/10=1 oz/gal"
print "   en un tiempo t(y1(0)/10)=t(1) de valor:"
t=np.arange(t0,tn+h,h)
i=0
while y1[i]>y10/10.: 
    i=i+1
print "     1) Resolviendo para dy1/dt, h=1 min:"
print "          %i min. < t(1) < %i min." %(t[i-1],t[i])
tmejor=rk(2,dt_dy1,t0,y10,y10/10.,-.001)
print "     2) Resolviendo para dt/dy1, h=.001 oz/gal:"
print "          t(1) = %.6f + O(.000001) min." %tmejor[-1]
print
print "b) En el tanque 2, la concentración de sal alcanza su"
print "   máximo y2max(t) = %i oz/gal en t = %i min." %(y2.max(),t[y2.argmax()])

plt.title(u"Concentración de sal en los tanques 1 y 2")
plt.plot(t,y1,"b",label=u"Concentración de sal (y1) en el tanque 1 (50 gal)")
plt.plot(t,y2,"g",label=u"Concentración de sal (y2) en el tanque 2 (20 gal)")
plt.plot(tmejor[-1],y10/10.,"b*")
plt.plot(t[y2.argmax()],y2.max(),"g*")
plt.xlabel(u"Tiempo t [min.]")
plt.ylabel(u"Concentración de sal y(t) [oz/gal]")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()
