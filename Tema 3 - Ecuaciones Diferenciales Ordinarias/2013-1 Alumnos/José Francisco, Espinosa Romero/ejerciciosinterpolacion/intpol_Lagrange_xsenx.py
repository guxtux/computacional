# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:51:04 2012

@author: pako
"""

import numpy as np
from math import *
xsenx=open('xsenx.dat','w')
ip=open('interpolacionxsenx.dat','w')
error=open('errorxsenx.dat','w')

n,i,h=4,0,0
w=np.arange(0,pi/2,pi/16)
x=np.linspace(0,pi/2,5)
y=[]

while i<len(x):
    y.append(x[i]*np.sin(x[i]))
    xsenx.write('%f %f\n' %(x[i],y[i]))
    i+=1
f=np.array(y)

while h<len(w):
    p=0
    for k in range(0,n):
        z=1.0
        for j in range(0,n+1):
            if k!=j:
                z=z*(w[h]-x[j])/(x[k]-x[j])
        p=p+z*f[k]
        vr=(w[h]*np.sin(w[h]))
        e=abs(vr-p)/vr
    print "El valor calculado de P(",w[h],") es:",p
    ip.write('%f %f\n' %(w[h],p))     
    print "El error entre la interpolación y el valor real es:",e,"\n"
    error.write('%f %f\n' %(w[h],e))  
    h+=1