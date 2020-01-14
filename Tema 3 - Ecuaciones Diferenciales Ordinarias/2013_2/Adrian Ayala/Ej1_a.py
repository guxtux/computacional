# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 22:35:53 2013

@author: acesimbrote


Para el método de Euler hacia adelante tenemos Yn+1= Yn + hf(Yn,tn) como
fórmula general, entonces Y1=Y0 + hf(y0,t0); Y2=Y1 + hf(y1,t1)... etc. 
"""

#Para esta función no pude encontrar una solución analítica, sin embargo 
#sí llegué a un resultado con el método de Euler 


from numpy import *
from metodonumerico import *
import matplotlib.pyplot as plt

t=0
y=1.0
h=0.01
n=5
u= linspace(t,n,n/h)

def f(y,t): return 1-t*y



o=Euler_adelante(f,y,t,len(u),h)
print 'El valor aproximado para y(5)= ', o[len(o)-1]





