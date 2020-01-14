# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:47:38 2013

@author: san
"""
import Gnuplot
import numpy as np
import matplotlib.pyplot as plt
from numpy import *
n=5
x0= np.array([10.0,30.0,60.0,90.0])
x= np.array([0.0,21.1,37.8,54.4,71.1,87.8,100.0])
f=np.array([1.79,1.13,0.696,0.519,0.338,0.321]) 
for k in x0:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]            
    print 'el polinomio evaluado en P(',k,')=',yres
n=np.array([yres])
g=Gnuplot.Gnuplot(persist=1)
d=Gnuplot.Data(x,f,with_="lines",title="examen2_4")
g.plot(d)   