# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 11:40:26 2013

@author: Deivid
"""
#con este metodo no me ue posible encontrar la raiz deido a que no es función y para cada x tiene dos valores en f(x)
from math import *
def f(x):return sqrt(x+2)
x0 = -2.5
x1 = -1.5

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
         

       
if f0 * f1 < 0.0:
    print "La raiz es:", R
else:
    print "Valores iniciales malos"