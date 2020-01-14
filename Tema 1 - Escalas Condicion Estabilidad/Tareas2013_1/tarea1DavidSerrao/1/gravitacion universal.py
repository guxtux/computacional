# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:26:13 2013

@author: Deivid
"""
import matplotlib.pyplot as plt
import math as mt
ex=[]
ey=[]
g=6.67*10**11
m0=1
m=1.99*10.0**30.0
af=5.28*10.0**12.0
vay=-9.12*10.0**2.0
vax=0.0
ay=0.0
vx=0.0
vy=0.0
t=0.0
x=5.28*10**12
y=0

while t<23328000000:
    
    t=t+23328000
    
    r=mt.hypot(x,y)
    
    f=g*m0*m/r*r      
    
    ax=-(f/m0)*x/r
    ay=-(f/m0)*y/r
    
    vx=vax+ax
    vy=vay+ay
    
    y=vy*t+y
    x=vx*t+x
    
    ex.append(x)
    ey.append(y)
    vax=vx
    vay=vy
    print f
    
    
    

