# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:54:19 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi

x1=-0.6
x2=0.9
errordeseado = 0.0001
def f(x):
    return x**3+2*x-1
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