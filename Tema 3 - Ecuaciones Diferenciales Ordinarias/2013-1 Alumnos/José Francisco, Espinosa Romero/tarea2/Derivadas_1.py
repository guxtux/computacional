# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:24:49 2012

@author: pako
"""

import numpy as np
from math import *

x=np.array([2.36,2.37,2.38,2.39])
f=np.array([0.85866,0.86289,0.86710,0.87129])

df=(-3*f[0]+4*f[1]-f[2])/(2*0.01)
print "f'(",x[0],")=",df

d2f=(2*f[0]-5*f[1]+4*f[2]-f[3])/(0.01)**2
print "f''(",x[0],")=",d2f
