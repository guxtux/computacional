# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:19:20 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
x1=-3.8
x2=-3.1
errordeseado = 0.0001
def f(x):
    return x**3+3*x**2+1/(x**2+3*x)
while True:
    xmed=x2-f(x2)*(x1-x2)/(f(x1)-f(x2))
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