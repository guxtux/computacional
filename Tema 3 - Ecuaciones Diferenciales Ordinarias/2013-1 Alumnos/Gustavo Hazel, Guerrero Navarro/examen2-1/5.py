# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/jeanhakunamatata/.spyder2/.temp.py
"""

from math import *

def f(x): return cos(2*acos(x))

h2=1.0
h4=0.5
h6=1.0/3

I2=(h2/3)*(f(-1.0) + 4.0*(f(0.0)) + f(1.0))
I4=(h4/3)*(f(-1.0) + 4*(f(-0.5)) +2*f(0.0) + 4*f(0.5) + f(1.0))
I6=(h6/3)*( f(-1.0) + 4*f(-2./3) + 2*f(-1./3) + 2*f(0.) + 2*f(1./3) + 4*f(2./3) + f(1.0))

print I2, I4, I6