# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:03:57 2013

@author: est5
"""
from math import exp
import matplotlib.pyplot as plt
n=10
i=1
er=[]
ejex=[]
while i < 16:
    error = abs(exp(1)-(1+1.0/n)**n)
    print "10^",i,"\t",error
    er.append(error)
    ejex.append(i)
    i+=1
    n*=10
    
plt.plot(ejex, er)
plt.show()