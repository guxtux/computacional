# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:05:38 2012

@author: pako
"""
import numpy as np
from math import*
import matplotlib.pyplot as plt

f=-0.93*1.2*0.5/250
v0=67.0
g=9.81
w=1*10**-10
t=[]
i,h=0,0
while i<75:
    t.append(h)
    h=h+0.2
    i=i+1
print t
while w<=pi/2.0:
    a=f*cos(w)
    b=f*sin(w)
    n,x,y=0,0.0,0.0
    print "ángulo =",w*180/pi,"rad\n"
    while y>=0:
        x=(v0/f)*(exp(a*t[n])-1)
        y=(((v0/f)-g/(b**2))*(exp(b*t[n])-1))+(g*t[n])/b
        print "t=",t[n],"x=",x,"y=",y
        n=n+1
    w=w+(pi/100.0)
    print "\n"
    
def x(w,t):
    f=-0.93*1.2*0.5/250
    v0=67.0
    a=f*cos(w)
    x=(v0/f)*(exp(a*t)-1)
    return x 
    
def y(w,t):
    f=-0.93*1.2*0.5/250
    v0=67.0
    g=9.81
    b=f*sin(w)
    y=(((v0/f)-g/(b**2))*(exp(b*t)-1))+g*t/b
    return y
    
c1=np.arange(0.0,15,0.1)
c=c1
while w<=pi/2.0:
    j=0
    plt.figure(1)
    while j<len(c):
        plt.plot(x(pi/4,c[j]),y(pi/4,c[j]),'b.')
        j=j+1
    w=w+(pi/100.0)
plt.show()