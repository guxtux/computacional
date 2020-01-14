# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 20:54:39 2012

@author: marisolchavez
"""

from math import*

EXP=0.0
x=eval(raw_input("Elige algun valor para x (0.1,1.0,10.0,100.0,1000.0)"))

y=exp(-x) #Este es el valor calculado real



n=0.0
Error=1.0


while Error > 0.0000001: #esta es la condicion para que calcule la serie, con el error
    
    EXP=EXP+((-1.0)**n)*(x**n)/factorial(n) #Este es el valor aproximado
    
    n=n+1
    Error=(abs(EXP-y))/y
#    print EXP   
#    print Error
    
print "El valor aproximado para x=", x, "de exp(-x)=", EXP
print "El valor real es: exp(-x)", y
print "el error absoluto es:", Error
