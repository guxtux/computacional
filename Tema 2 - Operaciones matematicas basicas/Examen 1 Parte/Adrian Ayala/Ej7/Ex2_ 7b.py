# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 01:03:17 2013

@author: Acesimbrote
"""
#from raices import *
from math import *

x0 = 0.1
x1 = 0.5
y0=0.2
y1=0.5

f0 = g2(x0)
f1 = g2(x1)
fy0= g2(y0)
fy1= g2(y1)
tol = 0.0001
if f0 * f1 < 0.0:
    while abs((x1 - x0) / x1) > tol:
        R = x1 - (f1 * (x0 - x1)) / (f0 - f1)
        fR = f(R)
        if f0 * fR < 0.0:
            x1 = R
            f1 = fR
            f0=g2(x0)/2
        if fR * f1 < 0.0:
            x0 = R
            f0 = fR
            f1=f(x1)/2
         
if fy0 * fy1 < 0.0:
    while abs((y1 - y0) / y1) > tol:
        s = y1 - (fy1 * (y0 - y1)) / (fy0 - fy1)
        fys = g2(s)
        if fy0 * fys < 0.0:
            y1 = s
            fy1 = fys
            fy0=g2(y0)/2
        if fys * fy1 < 0.0:
            y0 = s
            fy0 = fys
            fy1=g2(y1)/2         
    
if fy0 * fy1 < 0.0:
    print "La raiz es:", s
else:
    print "Valores iniciales malos"    
if f0 * f1 < 0.0:
    print "La raiz es:", R
else:
    print "Valores iniciales malos"
