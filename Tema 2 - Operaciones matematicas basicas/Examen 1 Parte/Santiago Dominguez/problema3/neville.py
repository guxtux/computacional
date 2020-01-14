# -*- coding: utf-8 -*-
"""
Created on Thu Mar 07 16:52:35 2013

@author: IIFCES
"""

## module neville
# p = neville(xData,yData,x).
#Evaluates the polynomial interpolant p(x) that passes
#trough the specified data points by Neville’s method.

def neville(xData,yData,x):
    m = len(xData) # number of data points
    y = yData.copy()
    for k in range(1,m):
        y[0:m-k] = ((x - xData[k:m])*y[0:m-k] + \
        (xData[0:m-k] - x)*y[1:m-k+1])/ \
        (xData[0:m-k] - xData[k:m])
    return y[0]