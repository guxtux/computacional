# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 22:01:59 2012

@author: pako
"""

import numpy as np
pol2=open('polgrado2_ej1.dat','w')
n,l=2,0
h=np.array([0.,3.,6.])
p=np.array([1.225,0.905,0.652])
hi=np.arange(0.,6.,0.5)

l=0
while l<len(hi):
    p2=0.
    for i in range(0,n):
        z=1.0
        for j in range(0,n+1):
            if i!=j:
                z=z*(hi[l]-h[j])/(h[i]-h[j])
        p2=p2+z*p[i]
    print hi[l],",",p2
    pol2.write('%f %f\n' %(hi[l],p2))
    l+=1
