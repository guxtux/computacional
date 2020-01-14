# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:22:32 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
from math import sinh,cosh,tanh,asinh,acosh,atanh

x1=-6.0
x2=-7.0
errordeseado=0.001 
def f(x):
    return sin(x)-0.3*exp(x) 
while True:
    xmed=(x1+x2)/2
    if f(xmed)==0.0:
        break
    if (f(x1)*f(xmed))<0:
        x2=xmed
    else:
        x1=xmed
    error=abs(x2-x1)
    if error<errordeseado:
        break
print 'La raiz2 es',xmed