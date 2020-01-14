# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 20:29:02 2012

@author: pako
"""

import numpy as np
from math import *

a=np.array([0,5,10,15,20,25,30])
b=np.array([1.6595,1.5434,1.4186,1.2925,1.1712,1.0585,0.9561])

df=25*(-3*b[0]+4*b[1]-b[2])/(2*5*pi/180)
print "derivada de b en",a[0],"grados =",df
for i in range(1,6):
    df=25*(b[i+1]-b[i-1])/(2*5*pi/180)
    print "derivada de b en",a[i],"grados =",df
    i+=1
df=25*(3*b[6]-4*b[5]+b[4])/(2*5*pi/180)
print "derivada de b en",a[6],"grados =",df