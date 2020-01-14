# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 07:13:19 2012

@author: pako
"""

import numpy as np
from math import *
g4=open('polgrado4.dat','w')
g8=open('polgrado8.dat','w')
errorg4=open('errorg4.dat','w')
errorg8=open('errorg8.dat','w')

y1,y2=[],[]
h,i,l,m,n=0,0,0,4,8
x=np.arange(0,2*pi,pi/6)
x1=np.linspace(0,2*pi,5)
x2=np.linspace(0,2*pi,9)

while i<len(x1):
    y1.append(np.sin(x1[i]))
    i+=1
f1=np.array(y1)

while h<len(x2):
    y2.append(np.sin(x2[h]))
    h+=1
f2=np.array(y2)

while l<len(x):
    p=0
    for k in range (0,m):
        z=1.0
        for j in range(0,m+1):
            if k!=j:
                z=z*(x[l]-x1[j])/(x1[k]-x1[j])
        p=p+z*f1[k]
        vr=np.sin(x[l])
        e=abs(vr-p)/abs(vr)
    g4.write('%f %f\n' %(x[l],p))
    errorg4.write('%f %f\n' %(x[l],e))
    l+=1

l=0
while l<len(x):
    p=0
    for k in range (0,n):
        z=1.0
        for j in range(0,n+1):
            if k!=j:
                z=z*(x[l]-x2[j])/(x2[k]-x2[j])
        p=p+z*f2[k]
        vr=np.sin(x[l])
        e=abs(vr-p)/abs(vr)
    g8.write('%f %f\n' %(x[l],p))
    errorg8.write('%f %f\n' %(x[l],e))
    l+=1
