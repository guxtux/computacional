# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 14:36:58 2012

@author: jeanhakunamatata
"""

from numpy import *



def f(x): return (4.0+249.2)*x**3 - (3*249.2 + 6)*x**2 + (3*249.2)*x - 249.2

a, b=(0.0, 1000.0)

x1=a; x2=b
while True:
    xmedia=(x1+x2)/2
    if f(xmedia)==0.0:
        break
    if (f(x1)*f(xmedia))<0:
        x2=xmedia
    else:
        x1=xmedia

    error=1.0*10**-4
    
    if abs(x1-x2)<error:
        break

print 'La raiz es:'
print x1