# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 19:37:53 2013

@author: est5
"""

import math as mt
import matplotlib.pyplot as plt
import numpy as np

x=[0.1,1.0,10,100,1000]
#e a la -1000 se sale del epsilon de la maquina y no me lo da

n=-1.0
e=0.0
#def f(t):
#    f=mt.sin(2*mt.pi*t)
 #   return f
while n<3:
    n=n+1
    e=((-1.0)**n)*((x[3]**n)/mt.factorial(n))+e
exp=mt.e**-x[3]
h=abs((exp-e)/exp)
print e,exp,h
#para valores de 100 y 1000 el error crece muchisimo, por error de redondeo

    
    