# -*- coding: utf-8 -*-
"""
EJERCICIO 4.
DADOS LOS PUNTOS DE LA TABLA X,Y CALCULA EL VALOR DE LA RAIZ Y(X)=0
@author: marisolchavez
"""

import numpy as np
from math import *
import matplotlib.pyplot as plt
xt =np.array([0.0]) 
print "Dame el valor evaluado (y(x)):"
xt[0]= raw_input()

def NewtonGregory(x1,deltaX,f,xt):
    n = len(x)-1
    deltaF = np.zeros([n+1,n+1])
    deltaF [:,0] = x 
    
    for j in range(1,n+1):
        for i in range(n-j+1):
            deltaF[i,j] = deltaF[i+1,j-1]-deltaF[i,j-1]
    deltaF = deltaF[0:n,1:n+1]
    
    s = (xt-x1)/deltaX
    
    yt = []
    
    for t in range (len(xt)):
        sum = f[0]
        for i in range(n):
            sum+=combinaciones(s[t],i+1)*deltaF[0,i]
        yt += [sum]
    return yt
    
def combinaciones(s,k):
    res = 1.0
    if k!=0:
        for i in range(1,k+1):
            res*=(s-i+1)/i
    return res
    
f = np.array ([-0.06604, -0.02724, 0.01282, 0.05383])#el valor de el arreglo corresponde a la tabla de y se invirtieron las variables
x = np.array ([4.0, 3.9, 3.8, 3.7]) #corresponde a los valores de las x


ft = NewtonGregory(f[0], f[1]-f[0], x,xt)# cambiamos las x por f y las f por x

print "ft      xt"
print "_________________"

for i in range(len(xt)):
    print "%4.2f %9.5f" %(xt[i], ft[i])

    

    
    
