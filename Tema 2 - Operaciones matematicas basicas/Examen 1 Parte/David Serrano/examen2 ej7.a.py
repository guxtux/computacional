# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:55:02 2013

@author: Deivid
"""
from fpm import *
from numpy import *
def f(x):return (0.5*e**(x/3))-sin(x)
x0 = 0.1
x1 = 1
 
##Metodo
f0 = f(x0)
f1 = f(x1)
tol = 0.0001

a=fpm(x1,x0,f1,f0,tol)
     
    
        
##Salidas
if f0 * f1 < 0.0:
    print "La raiz es:", R
else:
    print "Valores iniciales malos"