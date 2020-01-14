# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 04:25:08 2012

@author: emmanuel
"""

from math import *

n=3
s=1.0
p=0.0
while n<=20:
    t=(2*pi)/(2**n)
    s=s/((2*(1+(1-(s**2))**0.5))**0.5)
    p=(2**(n-1))*s
    q=(2**(n-1))*sin(t)
    n=n+1
h=4.0*(atan(1.0))
error1=(abs(h-p))/h
error2=(abs(h-q))/h

print 'pi-recurrencia','-','pi formula','-','pi real'
print p,',',q,',',h
print 'error recurrencia','-','error formula'
print error1,',',error2