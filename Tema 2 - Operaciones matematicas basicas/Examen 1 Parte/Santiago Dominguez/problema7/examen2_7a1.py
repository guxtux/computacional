# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 01:31:19 2013

@author: san
"""
from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp,pi

x1=0.
x2=1.
errordeseado = 0.00001
def f(x):
    return 0.5*exp(x/3)-sin(x)
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
 
