# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:18:21 2013

@author: acesimbrote
"""

import matplotlib.pyplot as plt
from numpy import *

n=2
e=pi
x0= linspace(0,6,3)
x= linspace(0,20,50)
f=[1.225,0.905,0.652] 
s=[]
for k in x:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x0[j])/(x0[i]-x0[j])
        yres=yres+z*f[i]
    s.append(yres)            
    print 'el polinomio evaluado en P(',k,')=',yres
#er=abs(g(x)-s)

#print er                

plt.plot(x,s,'r')
plt.show()
