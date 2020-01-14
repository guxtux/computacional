# -*- coding: utf-8 -*-
"""
Created on Mon Nov 03 21:40:50 2014

@author: Master Chief
"""

from numpy import pi,sqrt, sin, radians
from scipy.integrate import quad

def f(x):
    return 1./sqrt(1-(sin(radians(x/2.))**2)*sin(radians(x))**2)

print quad(f,0.0,2*pi)
