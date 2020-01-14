# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 08:17:45 2013

@author: est5
"""
import matplotlib.pyplot as plt
from math import sin, cos, pi
def f(xf):
    return sin(2*pi*xf)

def fp(xf):
    return 2*pi*cos(2*pi*xf)
    
h = 0.1
i = 1
x = 0.45
er=[]
ejex=[]
while i < 16:
    v = (f(x+h)-f(x))/h
    error=abs((fp(x)-v)/fp(x))
    #print f(x+h), f(x)
    print "10^-",i,"\t", v, "\t", error
    er.append(error)
    ejex.append(i)
    h/=10
    i+=1
plt.plot(ejex, er)
plt.show()