# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:58:44 2013

@author: est5
"""

import matplotlib.pyplot as plt
import numpy
l=[2,-20,70,100,48]
x=numpy.arange(-4,-1,0.5)  
y=[]
k=0
while k<len(x):
    i=0
    b=l[i]  
    while i<4:
        i=i+1    
        b=l[i]+x[k]*b
    y.append(b)
    k=k+1
plt.plot(x,y)
plt.show()
