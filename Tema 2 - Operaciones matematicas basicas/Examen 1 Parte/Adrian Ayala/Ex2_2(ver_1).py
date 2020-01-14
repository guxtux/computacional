# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 11:51:47 2013

@author: acesimbrote
"""

import matplotlib.pyplot as plt
from numpy import *
#2.33866666667,2.33933333333
n=6
x= linspace(0,3,7)
x0= linspace(1.21,2.42,100)
f=[1.8421,2.4694,2.4921,1.9047,0.8509,-0.4112,-1.5727] 
s=[]
t=[]
p=[]
r=[]
z=len(x)


for k in x0:
    if k<3:
        yres =0
        for i in range (0,n+1):
            z=1.0
            for j in range(0,n+1):
                if i !=j:
                    z=z*(k-x[j])/(x[i]-x[j])
                yres=yres+z*f[i]
            s.append(abs(yres))
            r.append(yres)
              
            print 'el polinomio evaluado en P(',k,')=',yres
    elif k>3:
        yrez =0
        for u in range (0,n+1):
            v=1.0
            for h in range(0,n+1):
                if u !=h:
                    v=v*(k-x[h])/(x[u]-x[h])
                yrez=yrez+v*f[u]
            t.append(abs(yrez))
            p.append(yrez)

            print 'el polinomio evaluado en P(',k,')=',yres


#x02=min(t)           
#x01=min(s)
#y01=t.index(x01)
#y0=s.index(x01)
#print 'La función se hace cero en: ',x0[y0]
#print 'La función se hace cero en: ',x0[y01]
#
#plt.plot(x0,r,'b')
#plt.show()



