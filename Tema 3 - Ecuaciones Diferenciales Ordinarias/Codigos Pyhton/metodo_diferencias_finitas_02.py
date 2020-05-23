# -*- coding: utf-8 -*-
"""
Created on Wed May 20 21:30:44 2020

@author: gusto
"""
import numpy as np
from scipy.linalg import solve_banded, solve

#c = [0., 1.6667, 1.6667, 1.6667, 1.6667]
#d = [-0.2222, -0.2222, -0.2222, -0.2222, -0.2222]
#e = [0.3333, 0.3333, 0.3333, 0.3333, 0.]
#
#b = np.array([-0.1111, 0., 0., 0., -0.0117])


c = [0, 1.8, 1.8, 1.8]
d = [0.56, 0.56, 0.56, 0.56]
e = [0.2, 0.2, 0.2, 0.]

b = np.array([-0.0667, 0., 0., -0.0126])

cm = np.array([c, d, e])
print(cm)

solucion = solve_banded((1,1), cm, b)
print(solucion)

