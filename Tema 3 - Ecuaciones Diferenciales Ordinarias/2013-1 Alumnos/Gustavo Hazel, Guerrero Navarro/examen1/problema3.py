# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 19:53:09 2012

@author: est5
"""
from math import exp
t=eval(raw_input('ingrese el valor para el tiempo, t:'))
c=eval(raw_input('ingrese el valor de la constante, c:'))
m=eval(raw_input('ingrese el valor para la masa, m:'))
k=eval(raw_input('ingrese el valor de la constante de fricción, k:'))
g=9.8

a=m/k

x=range(0, a+1, 0.1)
i=0

for i in x:
      y=g*(t - a) + c*exp(-t/a)
      i=i+1
      print x, y

