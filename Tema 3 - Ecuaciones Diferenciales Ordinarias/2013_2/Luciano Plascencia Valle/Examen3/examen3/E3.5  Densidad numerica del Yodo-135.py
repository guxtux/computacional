# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "CÁLCULO DE LA DENSIDAD NUMÉRICA DEL YODO-135"
print "USANDO EL MÉTODO DE EULER (=RK1) DESPUÉS DE tn=1 hora:"
from ecdif import *

def dNi(Ni,t=0.): return -Li*Ni
Li=0.1044               #Constante de decaimiento [hr**(-1)]
t0=0.; tn=20.; h=0.05    #Extremos de t y paso h [horas]
Ni0=1e5                 #Condiciones iniciales [átomos/cm**3]

Ni=rk(1,dNi,Ni0,t0,tn,h)
print "Ni(tn) = %.2f " %Ni[-1]
print "Valor exacto = Ni0*exp(-Li*tn) = %.2f" %(Ni0*exp(-Li*tn))
print "Error abs. = %.2f " %Eabs((Ni0*exp(-Li*tn)),Ni[-1])
print "Error rel. = %.5f " %Erel((Ni0*exp(-Li*tn)),Ni[-1])
rk(1,dNi,Ni0,t0,tn,h,0,1,"Tiempo t [horas]",u"Número de átomos Ni(t)","Decaimiento del Yodo")
