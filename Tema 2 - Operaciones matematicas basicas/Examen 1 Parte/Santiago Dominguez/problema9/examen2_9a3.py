# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:30:48 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi
x1=0.5
x2=1.5
errordeseado = 0.00001
def f(x):
    return 0.1*x**3-5*x**2-x+4+exp(-x)
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