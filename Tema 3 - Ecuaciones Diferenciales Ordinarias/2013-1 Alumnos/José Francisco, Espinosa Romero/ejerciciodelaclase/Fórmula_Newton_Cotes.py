# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:42:24 2012

@author: pako
"""

from math import *

f=[1,2,3,4,5,6,7,8,9,10]
h=(f[len(f)-1]-f[0])/8.0
print "h=",h

def integral(f,h):
    i=1
    n=len(f)
    I=f[0]
    while i<n-1:
        I=I+2*f[i]
        i=i+1
    I=(I+f[i])*h/2.0
    return I

print "Integral=",integral(f,h)