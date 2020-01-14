# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:32:44 2013

@author: Deivid
"""

from math import *
def f(x):return exp(x)-5*x**2
x0 = .4
x1 = 1
y0=4.5
y1=5

f0 = f(x0)
f1 = f(x1)
fy0= f(y0)
fy1= f(y1)
tol = 0.0001
if f0 * f1 < 0.0:
    while abs((x1 - x0) / x1) > tol:
        R = x1 - (f1 * (x0 - x1)) / (f0 - f1)
        fR = f(R)
        if f0 * fR < 0.0:
            x1 = R
            f1 = fR
            f0=f(x0)/2
        if fR * f1 < 0.0:
            x0 = R
            f0 = fR
            f1=f(x1)/2
         
if fy0 * fy1 < 0.0:
    while abs((y1 - y0) / y1) > tol:
        s = y1 - (fy1 * (y0 - y1)) / (fy0 - fy1)
        fys = f(s)
        if fy0 * fys < 0.0:
            y1 = s
            fy1 = fys
            fy0=f(y0)/2
        if fys * fy1 < 0.0:
            y0 = s
            fy0 = fys
            fy1=f(y1)/2         
    
if fy0 * fy1 < 0.0:
    print "La raiz es:", s
else:
    print "Valores iniciales malos"    
if f0 * f1 < 0.0:
    print "La raiz es:", R
else:
    print "Valores iniciales malos"