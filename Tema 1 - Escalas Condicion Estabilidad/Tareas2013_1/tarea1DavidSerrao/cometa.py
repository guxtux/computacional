# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:49:31 2013

@author: acesimbrote
"""

import matplotlib.pyplot as plt
import math as mt

ex=[]
ey=[]

g=6.67e11
m=1
M=1.99e30
af=5.28e12
vay=9.12e2
vax=0.0
ay=0.0
vx=0.0
vy=0.0
t=0.0
x=5.28*10**12
y=0

while t<2332800000:
    
    t=t+233280000
    
    r=mt.hypot(x,y)
    
    f=g*M/r*r      
    
    ax=-f*x/r
    ay=-f*y/r
    
    vx=vx+vax+ax*t
    vy=vy+vay+ay*t
    
    y=vy*t+y
    x=vx*t+x
    
    ex.append(x)
    ey.append(y)
    
    print r
    
    
plt.plot (ex,ey)
plt.show()
