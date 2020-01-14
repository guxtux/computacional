# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 20:03:44 2012

@author: pako
"""

from numpy import *

def combinaciones(s,k):
    res = 1.0
    if k!=0:
        for i in range(1,k+1):
            res *= (s-i+1)/i
    return res

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
    for t in range(lrn(xt)):
        sum = f[0]
        for i in range(n):
            sum += combinaciones(s[t],i+1)+deltaF[0,i]
        yt+=[sum]
    return yt
    
x=array([0.4,0.6,0.8,1.0],float)
f=array([0.423,0.684,1.030,1.557],float)
xt=array([0.43,0.49,0.5,0.55,0.73,0.75,0.91,0.95])

ft=NewtonGregory(x[0],x[1]-x[0],f,xt)

print 'xt   ft'
print '-------'
for i in range(len(xt)):
    print '%4.2f    %9.5f' %(xt[i],ft[i])    