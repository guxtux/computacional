# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 19:07:08 2012

@author: est5
"""

from numpy import *
from math import tan



def f(x): return x-tan(x)

a, b=(0.0, 8)

x1=a; x2=b

while True:
    xmedia=(x1+x2)/2
    if f(xmedia)==0.0:
        break
    if (f(x1)*f(xmedia))<0:
        x2=xmedia
    else:
        x1=xmedia
    
    error=1.0*10**-4
    
    if abs(x1-x2)<error:
        break
  #  d=1/f(xmedia)
   # if d<error:
    #    break

print 'La raiz es:'
print x1
