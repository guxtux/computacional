# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/est5/.spyder2/.temp.py
"""
import numpy as np
from math import *

n=eval(raw_input('ingrese el grado del polinomio: '))
#x=arange(0., pi/2 + pi/16, pi/16)


a=[]
b=[]
for k in range(0,9):
    h=(pi/16)*k
    b[k]=b.append[h]
    o=sin(h)
    a[k]=a.append[o]
f=np.array(a)
x=np.array(b)
print x, f

xa=eval(raw_input('ingrese el grado del polinomio: '))

yres=0


for i in range(0, n+1):
    z=1.0
    for j in range (0, n+1):
        if i != j:
            z=z*(xa-x[j])/(x[i]-x[j])
    yres = yres + z*f[i]
print 'P=', yres
