# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 18:37:44 2013
"""
print "SOLUCIÓN DE EDO CON MÉTODO DE EULER PARA t0=0, tn=5 s, h=0.01"
print "b) dy/dt = exp(-t)-3*y, y(0) = 1"
print "Solución: y(t) = 1/2*exp(-3*t)*(exp(2*t)+1)"
from ecdif import *

def dy(y,t): return exp(-t)-3*y
y0=1.
t0=0.; tn=5.; h=0.01

t=np.arange(t0,tn+h,h)
y=rk(1,dy,y0,t0,tn,h)
yexacta=1/2.*np.exp(-3.*t)*(np.exp(2.*t)+1.)

print "\nt     y(t)  yexacta(t)   Err.abs.   Err.rel."
print "----  ----  ----------   --------   --------"
Ea=[]; Er=[]
for i in range(0,len(t)):
    z=float(yexacta[i])
    print "%.2f  %.2f   %.5f     %.5f    %.4f" %(t[i],y[i],z,Eabs(z,y[i]),Erel(z,y[i]))
    Ea.append(Eabs(z,y[i]))
    Er.append(Erel(z,y[i]))
print 
print "Error absoluto máximo: %.5f" %max(Ea)
print "Error relativo máximo: %.4f" %max(Er)

plt.title(u"Solución de la EDO dy/dt = exp(-t)-3*y, y(0) = 1")
plt.plot(t,y,label=u"Solución calculada y(t)")
plt.plot(t,yexacta,"r",label=u"Solución yexacta(t)")
plt.xlabel(u"t")
plt.ylabel(u"y(t)")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()
