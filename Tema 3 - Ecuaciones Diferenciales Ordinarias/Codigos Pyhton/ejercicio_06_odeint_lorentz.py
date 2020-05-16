# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:41:03 2020

@author: gusto
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3


def lorentz(X, t0):
    a, b, c = 10., 28, 6./3
    x, y, z = X
    return [a*(y - x),
            x*(b - z) - y,
            x*y - c*z]

x0 = [1., 1, 1]
t = np.linspace(0, 30, 2000)
x_t = integrate.odeint(lorentz, x0, t)

fig = plt.figure()
ax = p3.Axes3D(fig)


ax.plot3D(x_t[:,0], x_t[:,1], x_t[:,2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
fig.add_axes(ax)
plt.show()