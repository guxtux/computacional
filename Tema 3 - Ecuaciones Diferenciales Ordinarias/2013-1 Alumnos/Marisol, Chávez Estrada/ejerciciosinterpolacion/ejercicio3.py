# -*- coding: utf-8 -*-
"""
EJERCICIO 3.

EL CALOR ESPECIFICO DEL ALUMINIO Cp DEPENDE DE LA TEMPERATURA T COMO SIGUE
T, Cp
CALCULA Cp EN T=200 Y T=400

@author: marisolchavez

"""

import numpy as np
from math import *

#Usando el metodo de Newton:

TDatos = np.array([-250.0,-200.0,-100.0,0.0,100.0,300.0])
CDatos = np.array([0.0163,0.318,0.699,0.870,0.941,1.040])

def coeficientes(TDatos, CDatos):
    m = len(TDatos)
    a = CDatos.copy()
    
    for k in range(1,m):
        a[k:m] = (a[k:m]-a[k-1])/(TDatos[k:m]-TDatos[k-1])
        
    return a
    

def evaluaPoli(a,TDatos,T):
    n = len(TDatos)-1
    p=a[n]
    
    for k in range(1,n+1):
        p = a[n-k]+(T - TDatos[n-k])*p
        
    return p
    



a=coeficientes(TDatos, CDatos)

print "T         Cp "
print "_______________"


for T in np.arange (200.0, 600.0, 200.0):
    C= evaluaPoli(a,TDatos,T)
    
	
    print "%3.1f %9.5f "  %(T,C)


