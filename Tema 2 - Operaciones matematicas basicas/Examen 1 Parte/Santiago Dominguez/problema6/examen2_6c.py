# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 15:50:51 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
from math import sinh,cosh,tanh,asinh,acosh,atanh

x1=1.
x2=2.
errordeseado=0.001 
def f(x):
    return -x**3+x+1 
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
print 'La raiz es',xmed