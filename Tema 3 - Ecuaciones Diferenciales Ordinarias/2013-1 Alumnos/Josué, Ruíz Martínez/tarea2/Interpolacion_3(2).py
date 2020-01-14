# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 21:23:01 2012

@author: pako
"""

import numpy as np

def coeficientes(xDatos, yDatos):
    m=len(xDatos)
    a=yDatos.copy()
    for k in range(1,m):
        a[k:m]=(a[k:m]-a[k-1])/(xDatos[k:m]-xDatos[k-1])
    return a

def evalPol(a,xDatos,x):
    n=len(xDatos)-1
    p=a[n]
    for k in range(1,n+1):
        p=a[n-k]+(x-xDatos[n-k])*p
    return p

T=np.array([-100.,0.,100.,300.],float)
cp=np.array([0.699,0.870,0.941,1.04],float)
Tx=np.array([200.,400.])
a=coeficientes(T,cp)
cpx=evalPol(a,T,Tx)

print 'xt   ft'
print '-------'
for i in range(len(Tx)):
    print '%4.2f    %9.5f' %(Tx[i],cpx[i])

T=np.array([-250.,-200.,-100.,0.,100.,300.],float)
cp=np.array([0.0163,0.318,0.699,0.870,0.941,1.04],float)
Tx=np.array([200.,400.])
a=coeficientes(T,cp)
cpx=evalPol(a,T,Tx)

print '\nxt   ft'
print '-------'
for i in range(len(Tx)):
    print '%4.2f    %9.5f' %(Tx[i],cpx[i])    