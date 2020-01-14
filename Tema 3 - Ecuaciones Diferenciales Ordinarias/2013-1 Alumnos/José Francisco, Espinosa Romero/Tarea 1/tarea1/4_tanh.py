# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: pako
"""
x = eval(raw_input("Ingrese el valor inicial de x: ")) 

from math import*
z=1.0
n=1.2*10**-7

while z>n:
   z = 1.0-tanh(x)
   x = x+(1.2*10**-7)
print "Se indetermina en:",x-1.2*10**-7
x=x-2*(1.2*10**-7)
z=1.0-tanh(x)
print "El valor máximo de x=",x
print "1-tanh(x)=",z
p=1/z
print "El valor de f(x)=1/(1-tanh(x)) es:",p