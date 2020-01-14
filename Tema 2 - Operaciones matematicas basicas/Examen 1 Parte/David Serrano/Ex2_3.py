# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:03:14 2013

@author: acesimbrote
"""

import matplotlib.pyplot as plt
from numpy import *
import Neville

n=3
x= linspace(0,3,7)
x0=0.7679
#x0= linspace(1.21,2.42,100)
f=array([1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727]) 


def neville (x, f, x0):
    m=len(x)
    y=f.copy()
    for k in range (1,m-1):
        y[0:m-k]=((x0-x[k:m])*y[0:m-k]+(x[0:m-k]-x0)*y[1:m-k+1])/(x[0:m-k]-x[k:m])
    return y[0]
    


print 'el valor máximo es en:',neville(x,f,x0)
