# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:27:54 2013

@author: san
"""
import Gnuplot
import numpy as np
n=1
x0= np.array([0.0])
x= np.array([-1.2,0.3,1.1])
f=np.array([-5.76,-5.61,-3.69]) 
for k in x0:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x[j])/(x[i]-x[j])
        yres=yres+z*f[i]            
    print 'el polinomio evaluado en P(',k,')=',yres
n=yres
x= np.array([-1.2,0.0,0.3,1.1])
f=np.array([-5.76,n,-5.61,-3.69])
g=Gnuplot.Gnuplot(persist=1)
d=Gnuplot.Data(x,f,with_="lines",title="examen2_1b")
g.plot(d)