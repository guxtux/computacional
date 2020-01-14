# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from math import*
r0 = 1.16912
e = 0.967990
tetha = 0
while tetha < 6*pi:
    tetha = tetha + 0.5*pi
    r = r0/(1+e*cos(tetha))
    print r
    
