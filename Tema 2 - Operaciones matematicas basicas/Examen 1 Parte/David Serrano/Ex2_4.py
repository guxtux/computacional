# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:48:59 2013

@author: acesimbrote
"""


import matplotlib.pyplot as plt
from numpy import *
n=6
e=pi
x= array([0.,21.1,37.8,54.4,71.1,87.8,100.])
x0= array([10.,30.,60.,90])
f=[1.79,1.13,0.696,0.519,0.338,0.321,0.296] 
ss=[]


for k in x0:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]
    ss.append(yres) 
           
    print 'el polinomio evaluado en P(',k,')=',yres
               
plt.plot(x0,ss,'r')
plt.show()
