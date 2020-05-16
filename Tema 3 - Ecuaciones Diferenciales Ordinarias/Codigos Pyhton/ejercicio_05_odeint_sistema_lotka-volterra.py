# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:48:35 2020

@author: gusto
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 1.
b = 0.1
c = 1.5
d = 0.75

def dXdt(X, t = 0):
     return  np.array([a*X[0] - b*X[0]*X[1], -c*X[1] + d*b*X[0]*X[1]])
 
Xf0 = np.array([0., 0.])
Xf1 = np.array([ c/(d*b), a/b])

print(Xf0)
print(Xf1)

all(dXdt(Xf0) == np.zeros(2) ) and all(dXdt(Xf1) == np.zeros(2))

t = np.linspace(0.0, 15.0, 500)
              
X0 = np.array([10.0, 5.0])
            
X = odeint(dXdt, X0, t)
conejos, zorros = X.T

f1 = plt.figure()
plt.plot(t, conejos, 'r-', label='Conejos')
plt.plot(t, zorros  , 'b-', label='Zorros')
plt.grid()
plt.legend(loc='best')
plt.xlabel('tiempo')
plt.ylabel('poblacion')
plt.xlim([0, 15])
plt.title('Evolución de la población de conejos y zorros')
plt.show()