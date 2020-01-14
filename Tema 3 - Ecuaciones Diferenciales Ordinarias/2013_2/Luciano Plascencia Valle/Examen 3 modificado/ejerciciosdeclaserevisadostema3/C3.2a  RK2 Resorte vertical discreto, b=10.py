# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Thu Apr 18 19:08:16 2013
"""
print "MOVIMIENTO VERTICAL y(t) DE UN RESORTE DADO POR"
print "m*d2y/dt + b*dy/dt + k*y = 0 (unidades MKS)"
print "CALCULADO USANDO RUNGE-KUTTA RK2\n"

from math import *
from ecdif import *

def d2y(dy,y,t): return -a*dy - w2*y
b=10; k=100; m=0.5
a=b/m; w2=k/m
dy0=0; y0=1; t0=0.; tn=0.05
h=0.025
yDatos=rk_d2f(2,d2y,dy0,y0,t0,tn,h,1,2,"t [s]","y(t) [m]","Resorte con resistencia b=10")
