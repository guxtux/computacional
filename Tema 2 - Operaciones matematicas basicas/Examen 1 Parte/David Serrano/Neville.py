# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 19:33:40 2013

@author: usuario
"""
##module neville
def neville (x, f, x0):
    m=len(x)
    y=f.copy()
    for k in range (1,m+1):
        y[0:m-k]=((x0-x[k:m])*y[0:m-k]+(x[0:m-k]-x0)*y[1:m-k+1])/(x[0:m-k]-x[k:m])
        return y[0]
