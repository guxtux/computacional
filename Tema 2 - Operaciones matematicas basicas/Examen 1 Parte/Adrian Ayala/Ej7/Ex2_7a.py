# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:55:02 2013

@author: Acesimbrote
"""
from fpm import *
from numpy import *
from raices import *

x0 = 0.1
x1 = 1
 
##Metodo
f0 = g1(x0)
f1 = g1(x1)
tol = 0.0001

a=fpm(x1,x0,f1,f0,tol)
     
    
        
##Salidas
if f0 * f1 < 0.0:
    print "La raiz es:", R
else:
    print "Valores iniciales malos"
