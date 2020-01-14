# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 18:33:06 2012

@author: marisolchavez
"""

from math import*

EXP=0.0

x=eval(raw_input("Elige algun valor para x (0.1,1.0,10.0,100.0,1000.0)"))

for n in range (0,100):
    
    EXP=EXP+((-1.0)**n)*(x**n)/factorial(n)
    
print "para n=100, exp(-x)=", EXP

y=exp(-x)

Error=(abs(EXP-y))/y
print "el error absoluto es:", Error


#Este programa no funciona bien para x=100 y x=1000, pyes van elevados a la n
#Si se reduce n, se reduce el numero de iteraciones y se vuelve poco precisa la estimacion
