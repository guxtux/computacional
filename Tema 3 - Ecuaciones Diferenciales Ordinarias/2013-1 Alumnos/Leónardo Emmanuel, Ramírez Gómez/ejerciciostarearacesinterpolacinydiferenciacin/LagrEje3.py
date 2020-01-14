# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 00:59:03 2012

@author: emmanuel
"""

import numpy as np
n = 5
x = np.array([-250.,-200.,-100.,0.,100.,300.])
f = np.array([0.0163,0.318,0.699,0.870,0.941,1.04])
g=0.

while g<=1:
    xa = 200.+g*200.
    yres = 0.

    for i in range(0,n+1):
        z=1.0
        for j in range(0,n+1):
            if i != j:
                z = z * (xa-x[j])/(x[i]-x[j])
        yres = yres + z*f[i]
                
    print 'El calor específico a T=',xa,'°C  es:',yres
    g=g+1.
    ax=400.