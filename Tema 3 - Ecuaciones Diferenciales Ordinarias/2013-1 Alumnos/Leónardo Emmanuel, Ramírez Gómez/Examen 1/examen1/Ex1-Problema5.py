# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 12:22:23 2012

@author: dell
"""

from math import*

print 'Fibonacci 1'
x=2
l=1
m=1
o=[]
while x<50:
    k=l+m
    l=m
    m=k
    x=x+1
    o.append(k)
print o

print '-----------------------------------------'

i=3
p=[]
print 'Fibonacci 2'
while i<=50:
    a=(0.5)*(1+sqrt(5.))
    b=(0.5)*(1-sqrt(5.))
    f=((a**i)-(b**i))*((sqrt(5.))**-1.)
    p.append(f)    
    i=i+1
print p

# la diferencia principal esta en que en la formula los resultados se arrojan
#con decimales, esto posiblemente por error de las funciones usadas, pero sin
#embargo los valores no decimales coinciden con los obtenidos en la de recurrencia