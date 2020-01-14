# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:44:09 2013

@author: acesimbrote
"""

from numpy import arange

x=arange(-4,-0.5,0.5)
#x=eval(raw_input('x'))
a=(2,-20,70,100,48)
n=4
b=a[n]

while n>0:
    n = n-1
    b = a[n] + b*x
    
print b

