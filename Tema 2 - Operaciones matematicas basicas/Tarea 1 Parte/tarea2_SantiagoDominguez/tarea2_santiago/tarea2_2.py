# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 03:19:16 2013

@author: san
"""

from numpy import *
from newtonPoly import *
import matplotlib.pyplot as plt
#usando el metodo de newton, encontrar el polinomio que se ajuste a los 
#los siguientes puntos
xDatos=array([-3., -1., 1., 2., 3.])
yDatos=array([0.,-4 , 0., -5., 12.])
a=coeffi(xDatos, yDatos)
print 'x,     yInterp'
print '________________'
for x in arange (-5.0, 10.1, 0.2):
    y=evalPoly(a, xDatos, x)
    print '%3.1f %9.5f' %(x,y)
    
plt.plot(x,y,'b+-')
plt.axis('auto')
plt.show()