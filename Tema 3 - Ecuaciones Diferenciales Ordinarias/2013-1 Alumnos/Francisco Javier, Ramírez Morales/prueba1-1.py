# -*- coding: utf-8 -*-
"""
Created on Wed Sep 05 19:34:26 2012

@author: vaio
"""

 
import numpy as np
t0=np.linspace(0.0,(np.pi)*(1/2),100)
v0=67.0#velocidad inicial
v0x=np.cos(t0)*v0
print v0x