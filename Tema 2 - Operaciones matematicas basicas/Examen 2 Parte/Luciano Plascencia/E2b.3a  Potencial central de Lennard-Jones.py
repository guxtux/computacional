# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 11 14:17:04 2013
POTENCIAL CENTRAL DE LENNARD-JONES PARA EL OXÍGENO: g=150 (aprox.)
Y NIVELES DE CUANTIZACIÓN n=0,1,2
"""
from math import *
from varios import *
from integral import *
from scipy.integrate import *

def F(E): 
    rmin=((-2+2*sqrt(1.+E))/E)**(1/6.)
    rmax=((-2-2*sqrt(1.+E))/E)**(1/6.)
    def R(r): return 4*(1/r**12-1/r**6)
    def G(r): return sqrt(abs(E-R(r)))
#    print E
#    print R(rmin),E-R(rmin)
#    print R(rmax),E-R(rmax)
#    print G(rmin)
#    print romberg(G,rmin,rmax,tol=epsilon)
    return g*romberg(G,rmin,rmax,tol=epsilon)-pi*(n+0.5)

epsilon=1e-2
a0=5.2917720859e-11     #Radio de Bohr en metros
g=150.                  #Constante gamma para el Oxígeno
n=0

E0=-3/8.
E1=-3/4.
y2=2*epsilon
k=0
print F(E0)

while abs(y2)>epsilon:
    y0=F(E0)
    y1=F(E1)
    E2=E1-y1*(E1-E0)/(y1-y0)
    y2=F(E2)
    E0=E1
    E1=E2
    k=k+1
print E2,k
