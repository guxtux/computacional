# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 21:29:34 2012

@author: est5
"""
from math import *
def f(x):return (1+(x/2)**2)**2
N=2.
while N<=128:
    I=0.
    i=1
    a=0.
    b=2.
    h=(b-a)/N
    #print h
    while i<=N:
        b=a+h
        I=I+(f(a)+f(b))*h/2.
        a=a+h
        i=i+1
    I=I*pi
    Error=abs(I-11.72860000)/11.72860000*100
    print 'para N=',N,'I=',I
    print 'Error',Error,'%'
    print '-----'
    N=N*2.
    
    