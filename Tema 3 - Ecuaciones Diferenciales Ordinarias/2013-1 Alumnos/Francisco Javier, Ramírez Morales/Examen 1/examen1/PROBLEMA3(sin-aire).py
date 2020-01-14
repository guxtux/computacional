#RAMIREZ MORALES FRANCISCO JAVIER
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 09 11:05:37 2012

@author: vaio
"""

import numpy as np
import matplotlib.pyplot as plt 
g=-9.8#m/s gravedad
#las formulas usadas aqui estan justificadas en el correspondiente archivo de texto
#

def v(t):
    return -g*t
    
t1=np.arange(0.0,5.0,0.1)

def y(t):
    return -(.5*g)*(t**2)

t2=np.arange(0.0,5.0,0.1)
plt.plot(t1,v(t1),'bo',t2,y(t2),'r*')
plt.xlabel('tiempo')
plt.ylabel('velocidad( o ) , altura ( *) ')
plt.title('caida gota de agua sin resistencia' )
plt.grid()
plt.show()

