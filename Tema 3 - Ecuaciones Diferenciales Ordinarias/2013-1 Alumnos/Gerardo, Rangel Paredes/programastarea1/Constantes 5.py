# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 20:26:58 2012

@author: est5
"""

from math import*

print "El valor de pi es: "
p = 4.0
n = 1.0
while n <= 1000:
    p +=4.0*((-1)**n/(2*n + 1))
    n += 1
    print p
a = abs(pi - 3.14259165434)
b = a/pi
e1 = b*100
print "El valor del error relativo verdadero de pi es :" ,e1 #con respecto al ultimo elemento de la aproximación
              
   
print "El valor de e es: "
e = 1
i = 1.0
while i < 20:
    e += (1.0)/(factorial(i)) 
    i += 1.0
    print e
c = abs(e - 2.71828182846)
d = c/e
e2 = d*100
print "El valor del error relativo verdadero de e es: ", e2


print "El valor de la constante de Euler es: "
E = 0.0
k = 1.0
while k < 1000:
    E += ((1.0/k) - log (1 + (1.0/k)))
    k += 1.0
    print E
f = abs(0.5772156649 - 0.576715581568)
g = f/0.5772156649
e3 = g*100
print "El valor del error relativo verdadero de la constante de Euler es: ", e3


