# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:46:36 2012

@author: guest-sYRpal
"""

print 'programa motociclista en fluido'
import numpy as np
from math import*
import matplotlib.pyplot as plt
m=250
b=0.93*1.2*1*0.5
v=67
a=0.
print 'distancia maxima','fraccion de pi'
while a<=(0.5):
    c=a*pi
    xm=(m/b)*v*cos(c)
    print xm,'--',a,'--'
    a=a+0.05
def f(c):
    return (m/b)*v*np.cos(c)
c1=np.arange(0.0,1.6,0.05)
c2=np.arange(0.0,90,1000)

plt.figure(1)
plt.subplot(211)
plt.plot(c1,f(c1),'bo',c2,f(c2),'g')




plt.show()