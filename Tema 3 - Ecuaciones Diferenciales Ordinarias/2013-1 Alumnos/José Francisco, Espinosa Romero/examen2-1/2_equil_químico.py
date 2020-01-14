# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 15:55:02 2012

@author: pako
"""

from math import *

def f(x):
    r=x*((3.-2.*x)**2)-249.2*((1-x)**3)
    return r

def bisecta(f,a,b):
    x1=a; f1=f(a)
    x2=b; f2=f(b)
    x3=(a+b)/2.; f3=f(x3)
    if f1==0.0: return x1
    else:
        while abs(x1-x2)>1e-4:
            if f1*f3<0.0: 
                x2=x3; f2=f(x2)
                x3=(x1+x2)/2.; f3=f(x3)
                #print x1,x2
            elif f2*f3<0.0:
                x1=x3; f1=f(x1)
                x3=(x1+x2)/2.; f3=f(x3)
                #print x1,x2
        return x1
        
raiz=bisecta(f,0,2)

print "El grado de equilibrio de la reacción es:",raiz

"""
Para saber como era la forma de la función
la grafiqué en gnuplot (anexo la gráfica)
y así supe que el intervalo en el que esta la raiz
es [0:2] y con el método de la bisección 
la encuentro, también con la gráfica se observa que solo hay una raiz
"""
