# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 19:15:10 2013

@author: est5
"""

##module biseccion
import numpy as np
from math import *
def bisect(f,x1,x2,switch=0,epsilon=1.0e-9):
    f1=f(x1)
    if f1==0.0: return x1
    f2=f(x2)
    if f2 ==0.0: return x2
    if f1*f2 >0.0: print 'La raiz no se ha identificado en un intervalo'
    n=ceil(log(abs(x2-x1)/epsilon)/log(2.0))
    for i in np.arange(n):
        x3=0.5*(x1+x2); f3=f(x3)
        if (switch==0) and (abs(f3)>abs(f1)) and (abs(f3)<abs(f2)):
            return None
        if f3 == 0.0: return x3
        if f2*f3 < 0.0:
            x1=x3; f1=f3
        else:
            x2=x3; f2=f3
    return(x1+x2)/2.0