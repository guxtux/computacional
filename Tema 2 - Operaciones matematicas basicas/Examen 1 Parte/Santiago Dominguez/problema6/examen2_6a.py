# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:32:15 2013

@author: san
"""
from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
from math import sinh,cosh,tanh,asinh,acosh,atanh

x1=0
x2=3*pi
errordeseado=0.001 
def f(x):

    return tan(x)-x+1 
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