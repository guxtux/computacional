# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:15:06 2013

@author: est5
"""
import math
import numpy
n=numpy.arange(3,20)  
for k in n:
    pn=4    
    theta=2*(math.pi)/2**n[k]
    seno=math.sin(theta)
    seno=seno/math.sqrt(2(1+math.sqrt((1-seno**2))))
    pn=(2**(n-1))*seno
    print pn