# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 03:03:40 2013

@author: san
"""

import matplotlib.pyplot as plt
from numpy import *
#la densidad del aire  ro varia con la altura de la siguiente manera
n=2
h0= linspace(0,6,3)
x= linspace(0,20,50)
ro=[1.225,0.905,0.652] 
s=[]
for k in x:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-h0[j])/(h0[i]-h0[j])
        yres=yres+z*ro[i]
    s.append(yres)            
    print 'La densidad Ro evaluada en ho(',k,')=',yres
plt.plot(x,s,'r')
plt.show()