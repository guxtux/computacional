# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:05:16 2013

@author: san
"""

import matplotlib.pyplot as plt
from numpy import *
#El calor especifico del aluminio Cp depende de la temperatura Tcomo sigue:
n=5
T= array([-250.,-200.,-100.,0.,100.,300.])
x= linspace(-250.,450,15)
Cp=[0.0163,0.318,0.699,0.870,0.941,1.04] 
s=[]
for k in x:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-T[j])/(T[i]-T[j])
        yres=yres+z*Cp[i]
    s.append(yres)            
    print 'el calor especifico evaluado en(',k,')=',yres
               

plt.plot(x,s,'r')
plt.show()