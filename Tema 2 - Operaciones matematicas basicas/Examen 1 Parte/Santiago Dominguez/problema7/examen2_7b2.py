# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:33:58 2013

@author: san
"""

from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi

x1=0.6
x2=0.8
errordeseado = 0.00001
def f(x):
    return log(1+x)-x**2
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