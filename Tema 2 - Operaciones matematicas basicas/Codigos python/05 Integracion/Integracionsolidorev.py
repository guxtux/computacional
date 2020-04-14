# -*- coding: utf-8 -*-
"""
Created on Thu Apr 04 19:26:04 2013

@author: IIFCES
"""
from numpy import *

def trapecios(f,a,b,n):
   h = (b-a)/float(n)
   x = a
   suma = 0
   for i in range(1,n):
      x = x + h
      suma = suma + funcion(x)
   return (h/2.)*(funcion(a) + funcion(b) + 2*suma)

def funcion(x):
    return pi*(1+(x/2)**2)**2
    
paneles = array([2,4,8,16,32,64,128])

print "  i    Integral     Error"
print "-------------------------------"
for i in paneles:
    print '%3i %2.9f %1.8e' %(i, trapecios(funcion(i),0,2,i),(abs(11.7286-trapecios(funcion(i),0,2,i)))/11.7286)






    
