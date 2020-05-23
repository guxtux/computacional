# -*- coding: utf-8 -*-
"""
Created on Wed May 20 15:06:09 2020

@author: gusto
"""

import numpy as np
#from scipy.linalg import solve_triangular
from scipy.interpolate import interp1d

import matplotlib.pyplot as plt

def TRDG(a,b,c,d):
    nf = len(a)     # numero de ecuaciones
    ac, bc, cc, dc = map(np.array, (a, b, c, d))     
    for it in range(1, nf):
        mc = ac[it]/bc[it-1]
        bc[it] = bc[it] - mc*cc[it-1] 
        dc[it] = dc[it] - mc*dc[it-1]

    xc = ac
    xc[-1] = dc[-1]/bc[-1]
    
    for il in range(nf-2, -1, -1):
        xc[il] = (dc[il]-cc[il]*xc[il+1])/bc[il]

    del bc, cc, dc 

    return xc

def exacta(t):
    valor = ((2*np.sqrt(3))/9)*np.exp(-4*t)*np.sin(4*np.sqrt(3)*t+(np.pi/3))
    return valor

#coeficientes = np.array([[0.56, 1.8, 0., 0.],
#                        [0.2, 0.56, 1.8, 0],
#                        [0., 0.2, 0.56, 1.8],
#                        [0., 0., 0.2, 0.56]])
#
#a = np.array([1.8, 1.8, 1.8, 1.8])
#b = np.array([0.56, 0.56, 0.56, 0.56])
#c = np.array([0.2, 0.2, 0.2, 0.2])
#
#    
#d = np.array([-0.0667, 0., 0., -0.0126])
#
t = np.linspace(0.0, 1.0, 200)

def espacio_n(N):
    tn = np.arange(0., 1.1, 1/N)   
    return tn
#
#solucion = TRDG(a, b, c, d)
#print(solucion)


#N=5
y1 = [0.3333, 0.1126, -0.0487, -0.0308, 0.0047, 0.0070]
y1c = [0.3333, -0.8000, 0.2120, 0.0229, 0.0307, 0.0070]

y2 = [0.3333, 0.1595, -0.0216, -0.0510, 0.0155, 0.0070, 0.0070]
y2c = [0.3333, 0.6361, 0.0181, -0.1247, -0.0201, 0.0222, 0.0070]


def ajuste(tn, t, y, colorforma='b'):
    f = interp1d(tn, y, kind='quadratic')
    y_smooth=f(t)
    plt.plot (t,y_smooth, colorforma)
    #plt.scatter (tn, y1c, colorforma)
 

def grafica_n(tn, fy, aprox, n):
    ajuste(tn, t, aprox)
    ajuste(tn, t, fy, 'r')
    plt.plot(tn, aprox, 'bs', label='aproximación')
    plt.plot(tn, fy, 'ro', label='función')
    plt.title('Solución al problema mediante diferencias finitas con $N= ' + str(n) + '$')
    plt.legend(loc='best')
    plt.xlim([0,1])


#n10 = exacta(espacio_n(20))
#plt.plot(espacio_n(20), n10, 'ro')
#plt.plot(t, exacta(t))
    
    
plt.figure(1)
grafica_n(espacio_n(5), y1, y1c, 5)

plt.figure(2)
grafica_n(espacio_n(6), y2, y2c, 6)


plt.show()



