# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 12:02:21 2012

@author: gabriela
"""

from math import*
h1 = 1.
igralch1 = (cos(2*acos(-1.)) + 4*cos(2*acos(0.)) + cos(2*acos(1.)))*((h1)/(3))
h2 = 0.5
igralch2 = (cos(2*acos(-1.)) + 4*cos(2*acos(-0.5)) + cos(2*acos(0.)))*((h2)/(3))
igralch3 = (cos(2*acos(0.)) + 4*cos(2*acos(0.5)) + cos(2*acos(1.)))*((h2)/(3))
igral2 = igralch2 + igralch3
h3 = 1./3.
igralch4 = (cos(2*acos(-1.)) + 4*cos(2*acos(-2./3.)) + cos(2*acos(-1./3.)))*((h3)/(3))
igralch5 = (cos(2*acos(-1./3.)) + 4*cos(2*acos(0.)) + cos(2*acos(1./3.)))*((h3)/(3))
igralch6 = (cos(2*acos(1./3.)) + 4*cos(2*acos(2./3.)) + cos(2*acos(1.)))*((h3)/(3))
igral3 = igralch4 + igralch5 + igralch6
print "El valor de la integral por medio de la regla 1/3 de Simpson con 2 bloques es:", igralch1
print "El valor de la integral por medio de la regla 1/3 de Simpson con 4 bloques es:", igral2
print "El valor de la integral por medio de la regla 1/3 de Simpson con 6 bloques es:", igral3