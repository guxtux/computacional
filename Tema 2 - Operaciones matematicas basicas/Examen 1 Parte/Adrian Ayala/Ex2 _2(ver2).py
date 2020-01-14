# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 20:22:45 2013

@author: Deivid
"""

from numpy import *

import matplotlib.pyplot as plt
from numpy import *

n=2
l=6
e=pi
y0=3
x0=linspace(0,3,7)
x= linspace(1.2,2.5,1000)
f=[1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727] 
s=[]
s2=[]
sabs=[]
s2abs=[]
for k in x:
    yres =0
    for i in range (0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i !=j:
                z=z*(k-x0[j])/(x0[i]-x0[j])
        yres=yres+z*f[i]
    s.append(yres)
    sabs.append(abs(yres))
    #print'el polinomio en P(',k,')=',yres
for k in x:
    yres2 =0
    for i in range (n+1,l+1):
        z=1.0
        for j in range(n+1,l+1):
            if i !=j:
                z=z*(k-x0[j])/(x0[i]-x0[j])
        yres2=yres2+z*f[i]
    s2.append(yres2)            
    s2abs.append(abs(yres2))
    #print 'el polinomio evaluado en P(',k,')=',yres2



mi=min(sabs)
mi2=min(s2abs)
p2=s2abs.index(mi2)
p=sabs.index(mi) 


print 'la funcion con tres puntos tiene un minimo en P(',x[p],')=',abs(s[p])
print 'la uncion con cuatro puntos tiene un minimo en :',x[p2],')=',abs(s2[p2])
plt.plot(x,s2,'r')
plt.show()
