# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 18:32:24 2013

@author: acesimbrote
"""

import math as mt
from numpy import *

#x= [0.1,1,10,100]
x = eval(raw_input('x = '))
n = eval(raw_input('n = '))
i=0
e=0.0
j=0.0
r=[]

while j < n:
    
    e = ((-x)**j) / (mt.factorial(j)) + e
    j=j+1
        
#     r.append(e)

print e

s = mt.exp(-x)

print s
Error=abs((s-e)/s)
print Error
