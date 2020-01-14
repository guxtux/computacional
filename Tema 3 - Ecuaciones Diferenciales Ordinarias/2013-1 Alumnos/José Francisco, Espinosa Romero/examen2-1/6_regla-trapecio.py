# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 19:58:13 2012

@author: pako
"""
from numpy import *

def f(t):
    I=1./(3*(t**(4./3.)+1))
    return I

def integral(f,h):
    i=1
    n=len(f)
    I=f[0]
    while i<n-1:
        I=I+2*f[i]
        i=i+1
    I=(I+f[i])*h/2.0
    return I

a,b,n=0.,1.,5
h=(b-a)/n
t=arange(0,1+h,h)
fx=[]

for i in range (n+1):
    fx.append(f(t[i]))

Ir=0.24375
Ic=integral(fx,h)
print "La integral calculada es: %3.5f" %(Ic)
print "La integral exacta es:",Ir
print "El error es:",abs((Ir-Ic)*100/Ir),"%" 

"""
DEspues de hacer el cambio de variable propuesto, 
se llega a un intervalo definido de 0 a 1 
en vez de 1 a infinito, 
ya con eso se puede usar el método del trapecio extendido
para 5 bloques y obtener una mejor aproximación de la integral
Al comparar el resultado con el valor teórico de la integral
se obtiene un error de 0.02% lo cual es muy buena aproximación
"""