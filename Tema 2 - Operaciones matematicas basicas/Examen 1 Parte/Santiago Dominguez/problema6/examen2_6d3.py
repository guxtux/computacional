# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 16:10:20 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
from math import sinh,cosh,tanh,asinh,acosh,atanh

x1=0.8
x2=1.0
errordeseado=0.001 
def f(x):
    return 16*x**5-20*x**3+x**2+5*x-0.5 
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
print 'La raiz3 es',xmed