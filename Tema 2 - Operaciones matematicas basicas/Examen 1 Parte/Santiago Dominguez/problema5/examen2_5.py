# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:51:30 2013

@author: san
"""
#import Gnuplot
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
n=2
x0= np.array([10.5])
x= np.array([0.0,1.525,3.050,4.575,6.10,7.625,9.150])
f=np.array([1.0,0.8617,0.7385,0.6292,0.5328,0.4481,0.3741]) 

for k in x0:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]
                
    print 'el polinomio evaluado en P(',k,')=',yres
#n=np.array([yres])
#g=Gnuplot.Gnuplot(persist=1)
#d=Gnuplot.Data(x,f,with_="lines",title="examen2_2a")

#g.plot(d,n)
    