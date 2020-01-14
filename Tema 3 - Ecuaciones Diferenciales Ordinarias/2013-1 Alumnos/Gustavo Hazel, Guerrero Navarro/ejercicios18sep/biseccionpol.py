# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:07:08 2012

@author: est5
"""

from numpy import *



def f(x): return x**3 -10*x**2 +5

a, b=(0.0, 1.5)

x1=a; x2=b

while True:
    xmedia=(x1+x2)/2
    if f(xmedia)==0.0:
        break
    if (f(x1)*f(xmedia))<0:
        x2=xmedia
    else:
        x1=xmedia

print 'La raiz es:'
print x1
