# calor especifico en 200 y 400 grados
"""
@author: Calderon Apolinar Marco A
"""

import numpy as np
n=3
x=np.array([-250.,-200.,-100.,0.,100.,300.])
f=np.array([0.0163,0.318,0.699,0.870,0.941,1.04])

def g(xa):
 yres=0
 for i in range(0,n+1):
    z=1.0
    for j in range(0,n+1):
        if i!=j:
            z=z*(xa-x[j])/(x[i]-x[j])
    yres=yres+z*f[i]

 return yres

y=[200,400]
for c in y:
    print 'el calor especifico en',c,'grados es:', g(c)