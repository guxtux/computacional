# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "CÁLCULO DE LA DENSIDAD NUMÉRICA DEL YODO-135 Y DEL XENÓN-135"
print "USANDO EL MÉTODO DE EULER MODIFICADO (=RK2)"
print "DESPUÉS DE tn=50 horas:"
from ecdif import *

def dN(N,t=0.): 
    Ni,Nx=N
    dNi=-Li*Ni
    dNx=-Lx*Nx+Li*Ni
    return np.array([dNi,dNx])
Li=0.1044; Lx=0.0753    #Constantes de decaimiento [hr**(-1)]
t0=0.; tn=50.; h=0.1    #Extremos de t y paso h [horas]
Ni0=1e5;Nx0=0.          #Condiciones iniciales [átomos/cm**3]
N0=[Ni0,Nx0]

Ni,Nx=rk(2,dN,N0,t0,tn,h).T
print "Tiempo (t) [hr.]  Atomos de Yodo (Ni)  Atomos de Xenón (Nx)"
print "----------------  -------------------  --------------------"
for t in np.arange(t0,tn+h,2):
    j=int(round(t/h))
    print "%2i" %t,"               %9.2f" %Ni[j],"+ O(0.01)  %9.2f" %Nx[j]," + O(0.01)"

t=np.arange(t0,tn+h,h)
plt.title(u"Decaimiento del Yodo-135 y del Xenón-135")
plt.plot(t,Ni,label="Atomos de Yodo-135 Ni(t)")
plt.plot(t,Nx,label=u"Atomos de Xenón-135 Nx(t)")
plt.plot(t,Ni+Nx,label=u"Total de átomos Ni(t)+Nx(t)")
plt.xlabel("Tiempo t [horas]")
plt.ylabel(u"Número de átomos N(t)")
plt.axhline(color="k"); plt.axvline(color="k"); 
plt.legend(loc="best")
plt.grid()
plt.show()
