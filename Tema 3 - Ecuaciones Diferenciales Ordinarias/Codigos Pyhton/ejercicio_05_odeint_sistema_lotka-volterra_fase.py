# -*- coding: utf-8 -*-

from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

a = 1.
b = 0.1
c = 1.5
d = 0.75

def dX_dt(X, t=0):
    return np.array([a*X[0] - b*X[0]*X[1] , -c*X[1] + d*b*X[0]*X[1]])

#condiciones de equilibrio
X_f0 = np.array([0., 0.])
X_f1 = np.array([c/(d*b), a/b])

t = np.linspace(0.0, 15.0,  500) 

values  = np.linspace(0.3, 0.9, 5)                         
vcolors = plt.cm.autumn_r(np.linspace(0.3, 1., len(values)))  
f2 = plt.figure()
#-------------------------------------------------------
#dibuja las trayectorias
for v, col in zip(values, vcolors):
    X0 = v * X_f1
    X = odeint(dX_dt, X0, t)
    plt.plot( X[:,0], X[:,1], lw=3.5*v, color=col, label='X0=(%.f, %.f)' % (X0[0],X0[1]))
    
#Define una malla y calcula la direccion
ymax = plt.ylim(ymin=0)[1]                        
xmax = plt.xlim(xmin=0)[1]
nb_points   = 20
 
x = np.linspace(0, xmax, nb_points)
y = np.linspace(0, ymax, nb_points)
 
X1 , Y1  = np.meshgrid(x, y)                       
DX1, DY1 = dX_dt([X1, Y1])                      
M = (np.hypot(DX1, DY1))                           
M[ M == 0] = 1.                                 
DX1 /= M                                        
DY1 /= M
 
#-------------------------------------------------------
#Dibuja las direcciones usando quiver
plt.title('Trayectorias y campo de dirección')
#plt.title('Espacio fase del sistema poblacional con diferentes condiciones iniciales', wrap=True)
Q = plt.quiver(X1, Y1, DX1, DY1, M, pivot='mid', cmap=plt.cm.jet)
plt.xlabel('Número de conejos')
plt.ylabel('Número de zorros')
plt.legend()
plt.grid()
plt.xlim(0, xmax)
plt.ylim(0, ymax)
plt.show()