# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/est5/.spyder2/.temp.py
"""
from numpy import *

a=[48, 100, 70, -20, 2]
n=4
b=a[4]

misdatos=open('datos.dat', 'w')
x=arange(-4, -0.5, 0.5)
while n>0:
     n=n-1
     b=a[n] + x*b
print x , b
misdatos.write(x, b)
misdatos.close()
