# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 12:44:15 2012

@author: pako
"""

import numpy as np

def combinaciones(s,k):
    c=1.0
    if k!=0:
        for i in range(1,k+1):
            c*=(s-i+1)/i
    return c

def NewtonGregory(x1,deltaX,f,xt):
    n=len(f)-1
    deltaF=np.zeros([n+1,n+1])
    deltaF[:,0]=f
    for j in range(1,n+1):
        for i in range(n-j+1):
            deltaF[i,j]=deltaF[i+1,j-1]-deltaF[i,j-1]
    deltaF=deltaF[0:n,1:n+1]
    s=(xt-x1)/deltaX
    yt=[]
    for t in range(len(xt)):
        sum = f[0]
        for i in range(n):
            sum += combinaciones(s[t],i+1)*deltaF[0,i]
        yt+=[sum]
    return yt
    
T=np.array([-100.,100.,300],float)
cp=np.array([0.699,0.941,1.04],float)
Tx=np.array([-250.,200.,300.,400.])
cpx=NewtonGregory(T[0],T[1]-T[0],cp,Tx)

print 'xt   ft'
print '-------'
for i in range(len(Tx)):
    print '%4.2f    %9.5f' %(Tx[i],cpx[i])    
    
T=np.array([-200.,-100.,0.,100.],float)
cp=np.array([0.318,0.699,0.87,0.941],float)
Tx=np.array([-250.,200.,300.,400.])
cpx=NewtonGregory(T[0],T[1]-T[0],cp,Tx)

print '\nxt   ft'
print '-------'
for i in range(len(Tx)):
    print '%4.2f    %9.5f' %(Tx[i],cpx[i])    
    
T=np.array([-100.,100.,300.],float)
cp=np.array([0.699,0.941,1.04],float)
Tx=np.array([-250.,200.,300.,400.])
cpx=NewtonGregory(T[0],T[1]-T[0],cp,Tx)

print '\nxt   ft'
print '-------'
for i in range(len(Tx)):
    print '%4.2f    %9.5f' %(Tx[i],cpx[i])    
