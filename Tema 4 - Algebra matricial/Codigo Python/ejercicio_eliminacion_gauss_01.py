# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:21:17 2020

@author: gusto
"""

import scipy.linalg as sla
import scipy as sc

A = sc.array([[6, -4, 1], [-4, 6, -4], [1, -4, 6]])

b = sc.array([-14, 36, 6])

x = sla.solve(A, b)

print(x)
 