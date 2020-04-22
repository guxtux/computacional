# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 19:26:04 2013

@author: IIFCES
"""
from numpy import pi, array

def trapecios(f, a, b, n):
   h = (b - a)/float(n)
   x = a
   suma = 0
   for i in range(1, n):
      x = x + h
      suma = suma + funcion(x)
   return (h/2.)*(funcion(a) + funcion(b) + 2*suma)

def funcion(x):
    return pi*(1 + (x/2)**2)**2

def error_relativo(aprox):
    valor = abs(11.7286 - aprox)/11.7286 
    return valor*100

#============================================================================
def qTrapecio(Func, a, b, n):
#----------------------------------------------------------------------------
#  Integrates function Func on interval [a,b] using the trapezoidal rule
#  with n integration points
#----------------------------------------------------------------------------
   h = (b-a)/(float(n)-1)
   s = 0.5*(Func(a) + Func(b))
   for i in range(1, n-1): s += Func(a+i*h)

   return h*s

# main

#a = 0e0; b = 1e0; n = 100
#print("I = ",qTrapz(funcion, 0, 2,n))

paneles = array([2, 4, 8, 16, 32, 64, 128])

print("i \t Integral \t Error")
print("--"*20)
for i in paneles:
    integral = qTrapecio(funcion, 0., 2., i)
    print('{0:} \t {1:2.9f} \t {2:1.8e}'.format(i, integral, \
          error_relativo(integral)))
          