# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 09:32:24 2012

@author: pako
"""

import numpy as np
from math import *

x=np.array([0.84,0.92,1.0,1.08,1.16])
f=np.array([0.431711,0.398519,0.367879,0.339596,0.312486])

def d2f(i,j):
    h=(x[i]-x[i-j])
    d2f=(f[i+j]-2*f[i]+f[i-j])/h**2
    return d2f,h

def ERich(h1,h2,f1,f2,p):
    a=(h1/h2)**p
    G=(a*f2-f1)/(a-1)
    return G

d2fh1,h1=d2f(2,2)
d2fh2,h2=d2f(2,1)
d2fh4=ERich(h1,h2,d2fh1,d2fh2,2)

print "f''(",x[2],", h=",h1,")=",d2fh1,"\n"
print "f''(",x[2],", h=",h2,")=",d2fh2,"\n"
print "f''(",x[2],", E=E(h**4) )=",d2fh4,"\n"