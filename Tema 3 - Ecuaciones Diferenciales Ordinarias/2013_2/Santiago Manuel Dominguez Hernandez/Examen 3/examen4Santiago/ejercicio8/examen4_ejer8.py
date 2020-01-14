# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:54:34 2013

@author: san
"""

from matplotlib.pylab import*    
from math import*
import  numpy as np
h=0.01
b1=0.5
b2=0.005
b3=pi*2
b4=3.0
b5=3./8.
t=np.linspace(0,300,50)
y=np.linspace(0,300,50)
z=np.linspace(0,300,50)
k1=np.zeros(50)
k2=np.zeros(50)
l1=np.zeros(50)
l2=np.zeros(50)
yn=np.zeros(50)
zn=np.zeros(50)
xV=np.zeros(50)
yV=np.zeros(50)
def f1(y,z,t):
    return -b2*sqrt(y**2+z**2)*y
def f2(y,z,t):
    return -b3*-b2*sqrt(y**2+z**2)*z
    


for i in range(49):

    zn[0]=150.
    yn[0]=150.
    k1[i]=h*f1(yn[i],zn[i],t[i])
    l1[i]=h*f2(yn[i],zn[i],t[i])    
    k2[i]=h*f1(yn[i]+k1[i],zn[i]+l1[i],t[i+1])
    l2[i]=h*f2(yn[i]+k1[i],zn[i]+l1[i],t[i+1])
    zn[i+1]=zn[i]+b1*(k1[i]+k2[i])
    yn[i+1]=yn[i]+b1*(l1[i]+l2[i])
print zn
#print yn
#X=[]
#Y=[]
#n=50
#for i in range(46):
#    X.append(yn[i])
#    Y.append(zn[i])
#for i in range(50):
#    xV[i+1]=Y[i-1]
#    xV[0]=0.
#    yV[0]=0.
#    xV[i]=(X[i]+b1*X[i+1]+b1*X[i+2]+X[i+3])*(b5*h)
#    yV[i]=(Y[i]+b1*Y[i+1]+b1*Y[i+2]+Y[i+3])*(b5*h)
#    xV[i]=xV[i]+(yn[i]+yn[i+1]+b1*yn[i+2]+yn[i+3])*(b5*h)
#    yV[i]=yV[i]+(zn[i]+zn[i+1]+b1*zn[i+2]+zn[i+3])*(b5*h)    
    
#print X
#print Y
#print xV
#print yV

plot(t,zn)
show()   