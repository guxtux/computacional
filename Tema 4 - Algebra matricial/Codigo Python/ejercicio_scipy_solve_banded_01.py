# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:12:25 2020

@author: gusto
"""

import scipy.linalg as sla
import numpy as np

g = [0. ,0, 3, 5, 9, 4, -2, -6]
c = [0., -5, -3, 5, 5, -3, 1, 7]
d = [1., 2, 1, -1, 2, 0, 2, 1]
e = [3., -2, 9, 0, 2, -3, 9, 0]

b = np.array([5., 3, -3, 2, 0, 7, 8, 1])

cm = np.array([g, c, d, e])

x = sla.solve_banded((1,2), cm, b)

print('xi \t Solución')
print('-'*20)

for i in range(len(x)):
    print('x{0:1d} \t {1:1.6f}'.format(i, x[i]))