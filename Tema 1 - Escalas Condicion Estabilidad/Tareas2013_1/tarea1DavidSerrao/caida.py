# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:57:55 2013

@author: acesimbrote
"""

import math

m = eval(raw_input('m/k = '))
t = eval(raw_input('t = '))
j = 0 
yo = eval(raw_input('h = '))
g = 9.81


while j < t:
    v = (g*m) - (g*m*math.exp(-j))
    y = (-g*m*j) + (-g*m*math.exp(-j)) + yo + (g*m)
    j = j+1
 #   for y = 0:
  #      brake
    print y,v
#print v, h

