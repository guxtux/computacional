# -*- coding: utf-8 -*-
"""
Created on Thu May 28 19:55:05 2020

@author: gusto
"""

import numpy as np
import numpy.linalg as nla

a = np.array([[ 3, -5, 8], [-1, 2, 3], [-5, -6, 2]])

print(nla.det(a))
print(nla.trace(a))