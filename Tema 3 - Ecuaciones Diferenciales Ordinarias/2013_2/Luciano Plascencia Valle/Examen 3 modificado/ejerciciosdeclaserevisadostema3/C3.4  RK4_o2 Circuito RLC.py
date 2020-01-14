# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "CIRCUITO RLC DADO POR"
print "L*d2q + R*dq + q/C = E(t), t>0 (unidades MKS)"
print "CALCULADO USANDO RK4"

from math import *
from ecdif import *

#Constantes en unidades MKS (Henry, Farad, Volt, Ohm)
L=200.; C=.001; E=1.
Rdatos=[0.,50.,100.,300.]   #Valores de resistencias
dq0=0.; q0=0.; t0=0.; tn=5.
h=0.01

def d2q(dq,q,t): return -R/L*dq - q/(L*C) + E/L

for R in Rdatos:
    print "\nResistencia R = %i ohms:" %R
    rk_d2f(4,d2q,dq0,q0,t0,tn,h,1,2,"t [s]","q(t) [m]","Resistencia R="+str(int(R)))
