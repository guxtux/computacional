# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 16:58:41 2012

@author: pako
"""
from math import *
import numpy as np

def iS(f,a,b,h):
    I=(f[a]+4*f[(a+b)/2]+f[b])*h/3
    return I

def f(x):
    s=cos(2*acos(x))
    return s

a,b,k=-1.,1.,0
n=[2,4,6]
while k<len(n): 
    h=(b-a)/n[k]
    x=np.arange(-1,1+h,h)
    fx=[]
    for i in range (n[k]+1):
        fx.append(f(x[i]))
    
    I,j=0.,0
    
    while j+2<=n[k]:
        I=I+iS(fx,j,j+2,h)
        j=j+2
    print "El número de bloques es:",n[k]
    print "El valor de la integral es:",I,"\n"
    k=k+1
    
""" 
Había hecho una modalidad en la que el programa pedía al usuario
el número de bloques que deseaba, y así calculaba la integral,
pero lo cambie para tener definidos el número de bloques,
si se desea solo se debe cambiar el valor de n
en vez de ser una lista, que pida el valor al usuario con
n=eval(raw_input()), y quitar el ciclo de k
y donde dice n[k] poner la variable n
Los valores de la integral no cambiaron con el número de bloques
eso nos da una idea de que la aproximación es buena
"""