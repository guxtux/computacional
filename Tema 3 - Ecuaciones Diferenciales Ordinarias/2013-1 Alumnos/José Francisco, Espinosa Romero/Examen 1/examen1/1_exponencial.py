# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 18:30:33 2012

@author: pako
"""

from math import*

def fact(N):
    i=0
    f=1
    while i<N:
        i=i+1
        f=f*i
    return f

print "Este programa calcula el inverso de la exponencial de un número cualquiera"
X=[0.1,1,10,100,1000]
j=0
while j<=4:
    e,i,e2=0.0,0,1
    x=-1.0*X[j]
    ex=exp(x)
    print "El valor de exp(",x,") es: ", ex
    while e2>(10**-8):
        e = e+(x**i)/(fact(i)) 
        i = i+1
        e2 = abs(ex-e)/ex
    print "El valor calculado para exp(",x,") es: ",e
    print "El error absoluto de exp(",x,") es: ", e2
    j=j+1