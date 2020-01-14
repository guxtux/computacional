# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 18:40:15 2013

@author: acesimbrote
"""

from numpy import *
from newtonPoli import *
import matplotlib.pyplot as plt

xDatos=array([-3., -1., 1., 2., 3.])
yDatos=array([0.,-4 , 0., -5., 12.])
a=coeffts(xDatos, yDatos)
print 'x,     yInterp'
print '________________'
for x in arange (-5., 10.1, 0.2):
    y=evalPoli(a, xDatos, x)
    print '%3.1f %9.5f' %(x,y)
    
plt.plot(x,y,'b+-')
plt.axis('auto')
plt.show()


    
    
    
