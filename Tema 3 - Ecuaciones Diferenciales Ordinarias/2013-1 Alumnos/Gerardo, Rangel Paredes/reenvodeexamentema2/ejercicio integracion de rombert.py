# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 19:40:06 2012

@author: est5
"""
from scipy import*
from math import*
from scipy.integrate import romberg

def f(x): return 2/(sqrt(1-x**4))
resultado = romberg (f, 0, sqrt(sin(pi/4)), show = True)



   



