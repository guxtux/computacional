# -*- coding: utf-8 -*-
"""
Autor: Luciano Plascencia Valle
Fecha de creación: Tue Feb 26 19:35:00 2013
Examen 1, Ejercicio 5
SUCESIÓN DE FIBONACCI MEDIANTE DOS MÉTODOS
"""
from math import *

def Eabs(x,x_): return abs(x-x_)
    
def Erel(x,x_): return abs((x-x_)/x)

def Fib1(N):        #Usando relación de recurrencia
    L2=0
    L1=1
    fibonacci=[]
    for n in range(1,N+1):
        fibonacci.append(L1)
        L2,L1=L1,L1+L2
    return fibonacci

def Fib2(N):        #Usando la razón dorada
    fibonacci=[]
    for n in range(1,N+1):
        Ln=(((1+sqrt(5))/2)**n-((1-sqrt(5))/2)**n)/sqrt(5)
        fibonacci.append(Ln)
    return fibonacci

a=Fib1(50)
b=Fib2(50)
print "CÁLCULO DE LA SUCESIÓN DE FIBONACCI MEDIANTE DOS MÉTODOS:"
print "LA RELACIÓN DE RECURRENCIA Y LA RAZÓN DORADA \n"
print " n, Recurrencia,     Razón dorada,       Err.Relativo"
for n in range(0,50):
    print "%2d" %(n+1), "%12d" %a[n],"  %20.15f" %b[n], "  %.2e" %Erel(a[n],b[n])

print "\nComo era de esperarse, la sucesión calculada con la relación"
print "de recurrencia Fib1 proporciona valores enteros.\n"
print "En cambio, la sucesión  calculada usando la razón dorada"
print "proporciona valores de punto flotante, y el error va creciendo"
print "conforme aumenta n."
"""    
    Ln_2=1
    Ln_1=0
    fib=[]
    for n in range(1,N):
        fib.append(Ln_2)
        Ln_1=Ln_2
        Ln_2=Ln_2+Ln_1
        print n,Ln_2
    return fib
"""

