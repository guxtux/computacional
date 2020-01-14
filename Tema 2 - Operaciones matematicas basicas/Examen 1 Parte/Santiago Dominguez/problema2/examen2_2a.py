# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:52:26 2013

@author: san
"""
#import Gnuplot
from numpy import *
import numpy as np
n=4
x0= np.array([0.3,0.8,1.3])
x= np.array([0.0,0.5,1.0,1.5,2.0,2.5,3.0])
f=np.array([1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727]) 
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