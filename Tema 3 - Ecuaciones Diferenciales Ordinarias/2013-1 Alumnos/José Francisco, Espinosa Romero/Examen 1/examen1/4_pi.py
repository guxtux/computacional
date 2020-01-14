# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:26:18 2012

@author: pako
"""

from math import *

n,sen,pn=3.0,1.0,0.0

while n<=20:
    On=(2*pi)/(2**n)
    sen=sen/((2*(1+(1-(sen**2))**0.5))**0.5)
    pn=(2**(n-1))*sen
    p2=(2**(n-1))*sin(On)
    n=n+1
print "El valor calculado para PI con recurrencia es:",pn
pi=4.0*(atan(1.0))
e=(abs(pi-pn))/pi
e2=(abs(pi-p2))/pi
print "El valor calculado para PI con fórmula es:",p2
print "El valor real de PI es:",pi
print "El error absoluto con recurrencia es:",e
print "El error absoluto con fórmula es:",e2
