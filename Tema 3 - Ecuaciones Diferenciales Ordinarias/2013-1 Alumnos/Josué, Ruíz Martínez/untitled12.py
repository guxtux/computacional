# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 20:43:37 2012

@author: est5
"""


x=eval(raw_input('x='))
a=(1,1,1,1,1,1,1,1,1,1,1)
n=10
b=a[10]
while n>0:
    n=n-1
    b=a[n]+(x/n*(n-1))*b

print 'p(x)=',b
