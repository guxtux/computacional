# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:18:40 2012

@author: jeanhakunamatata
"""

from math import *

h1=1.0
h2=1.0

def f(t): return (1+t**(4./3))**(-1)

I3=(h1/3)*(f(1.0) + 4*(2.0) + f(3.0))
I8=(3*h2/8)