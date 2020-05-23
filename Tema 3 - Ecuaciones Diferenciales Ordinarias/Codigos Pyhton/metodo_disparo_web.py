# -*- coding: utf-8 -*-
"""
Created on Sun May 17 21:07:22 2020

@author: gusto
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
c=0.65
g=9.81
# gravitational force on earth angle=50 # angle at which projectile is launched
m=0.1
#returning dx/dt, dy/dt, dv/dt as an array 
def model(yaf,t):
    x=yaf[0] # x position is first element of yaf 
    y=yaf[1] # y position is second element of yaf 
    v=yaf[2] # velocity is third element of yaf 
    return np.array([dx/dt, dy/dt, dv/dt])

t0=0 # initial condition for time 
tmax=20 # max time 
steps=20 # numer of steps # time points 
t = np.linspace(0,tmax, steps) #initial conditions for x position, y position and velocity 
initial=[0,0,10] # solve ODE 

y = odeint(model,initial,t)
print(y)

# plot results 
plt.plot(t,y)
plt.show()
