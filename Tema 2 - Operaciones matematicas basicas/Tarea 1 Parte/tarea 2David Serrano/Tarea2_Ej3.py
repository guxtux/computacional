# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 21:20:22 2013

@author: acesimbrote
"""
from numpy import *

import matplotlib.pyplot as plt
from numpy import *

n=5
e=pi
x0= array([-250.,-200.,-100.,0.,100.,300.])
x= linspace(-250.,450,15)
f=[0.0163,0.318,0.699,0.870,0.941,1.04] 
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
    
print'el calor específico del aluminio a 200 C es:', s[9]               
print'el calor específico del aluminio a 400 C es:', s[13]
#plt.plot(x,s,'r')
#plt.show()
