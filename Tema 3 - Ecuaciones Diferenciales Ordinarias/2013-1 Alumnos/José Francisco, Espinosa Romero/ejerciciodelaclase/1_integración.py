# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 19:14:22 2012

@author: pako
"""

from math import *

def integral(f,h):
    i=1
    n=len(f)
    I=f[0]
    while i<n-1:
        I=I+2*f[i]
        i=i+1
    I=(I+f[i])*h/2.0
    return I

b,N=2.0,2
VR=11.7286
print "El valor real del volumen es:",VR,"\n"
while N<=128:   
    a=0.0    
    h=(b-a)/N
    X=[]
    Y=[]
    while a<=b:
        X.append(a)
        y=(1+(a/2.0)**2)**2
        Y.append(y)        
        a=a+h
    V=pi*integral(Y,h)
    e=abs(VR-V)*100/VR
    print "Volumen del sólido con N=",N,"es:",V
    print "El error porcentual para N=",N,"es:",e,"%\n"
    N=N*2
