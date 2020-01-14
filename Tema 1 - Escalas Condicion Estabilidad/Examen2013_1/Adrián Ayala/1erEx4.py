# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:01:24 2013

@author: acesimbrote
"""

from math import *
from numpy import *
import math as mt


n=arange(3,21,1)
sen2=1
sen=[]
p=[]
i=0

for i in range(3,22):
    i = i+1
    a= sen2
#    a = mt.sin(i-1)
    b=mt.sqrt(2 - 2 * sen2**2)
#    b = mt.sqrt(2 - 2 * mt.sin(i-1)**2)
    senn = a/ mt.sqrt(2+b)
    pn= (2 ** i-1) * senn


    print senn, pn


