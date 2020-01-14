# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:53:09 2012

@author: est5
"""
from math import atan
n=range(3, 21, 1)

sen=1
for i in n:
      sen=sen/((2*(1+(1-(sen**2))**0.5))**0.5)
      i=i+1
print sen, 4*atan(4)
